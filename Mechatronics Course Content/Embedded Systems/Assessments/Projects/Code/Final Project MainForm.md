# Final Project MainForm

> [!info] Course material
> [[Final Project Overview|Back]] · Source: `MainForm.cs` · [[GUI and Event-Driven Programming]]

```csharp
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using Bulb;
using DmitryBrant.CustomControls;
using AquaControls;

namespace FinalProject
{
    public partial class MainForm : Form
    {
        private IAppBoard _board;
        private DatabaseLogger _db;
        private Timer _updateTimer;

        private bool _dataLoggingEnabled;

        // Chart data
        private readonly List<float> _tempHistory    = new List<float>();
        private readonly List<float> _setpointHistory = new List<float>();
        private const int MaxChartPoints = 100;

        // PI controller state
        private double   _intError   = 0.0;
        private double   _lastError  = 0.0;
        private DateTime _lastPiTime = DateTime.MinValue;
        private bool     _isClosing  = false;
        private int      _tickCounter = 0;

        // Cached board samples to avoid duplicate serial reads in one UI cycle.
        private byte _lastPina;
        private byte _lastPot1;
        private byte _lastPot2;
        private byte _lastTemp;
        private byte _lastLight;
        private double _lastMargin;
        private double _lastDewPoint;
        private int _lastStatus;
        private int _lastAlarms;
        private bool _dewWriteSupported = true;
        private double _lastSentDewPoint = double.NaN;
        private double _lastMotorCmdPct = 0.0;
        private double _lastHeaterCmdPct = 0.0;
        private bool _syncingSwitchIndicators = false;
        private bool _dewOverrideWasOn = false;
        private readonly LedBulb[] _laserPowerLeds = new LedBulb[6];

        // ── Laser head / axis position ──────────────────────────────────────────
        private enum MoveDir { None, Up, Down, Left, Right }
        private MoveDir  _heldDir       = MoveDir.None;
        private double   _laserX        = 150.0;   // mm
        private double   _laserY        = 150.0;   // mm
        private const double MaxPos     = 300.0;
        private const double MinPos     = 0.0;
        private const double StepMm     = 3.0;     // mm per 80 ms tick
        private const double RetractMm  = 20.0;
        private bool     _limitAlarm    = false;
        private string   _limitAxis     = "";
        private int      _holdTicks     = 0;
        private const int HoldAlarmTicks = 25;     // 25 × 80 ms ≈ 2 seconds
        private Timer    _dirTimer;

        public MainForm()
        {
            InitializeComponent();
            InitializeCustom();
        }

        private void InitializeCustom()
        {
            if (lblPiTuning != null) lblPiTuning.Text = "PI tuning (stabilizes head temp)";
            if (lblWorkflowIntro != null) lblWorkflowIntro.Text = "Connect COM when machine and chiller are powered. Then verify condensation safety before enabling laser.";
            if (grpConnection != null) grpConnection.Text = "1) Machine startup";
            if (grpCondRisk != null) grpCondRisk.Text = "2) Dewpoint safety check";
            if (grpLabSwitches != null) grpLabSwitches.Text = "3) Door and track-limit warnings";
            if (grpTempControl != null) grpTempControl.Text = "4) Laser thermal control";
            if (grpChart != null) grpChart.Text = "Laser run trend";
            if (grpPots != null) grpPots.Text = "Safety inputs";
            if (grpDigitalIO != null) grpDigitalIO.Text = "Board diagnostics (read-only)";
            if (grpLaserHead != null) grpLaserHead.Visible = false;
            if (grpLabSwitches != null) grpLabSwitches.Visible = true;
            if (grpLampLight != null) grpLampLight.Visible = false;
            if (grpLampLight != null && grpDigitalIO != null)
            {
                grpDigitalIO.Location = grpLampLight.Location;
                grpDigitalIO.Size = new Size(grpDigitalIO.Size.Width, 496);
            }
            if (chkVbSW0 != null) chkVbSW0.Enabled = false;
            if (chkVbSW1 != null) chkVbSW1.Enabled = false;
            if (chkVbSW0 != null) chkVbSW0.Text = "Laser enable switch (SW0 / PA0)";
            if (chkVbSW1 != null) chkVbSW1.Text = "Door interlock switch (SW1 / PA1)";
            if (lblVbAutoNote != null) lblVbAutoNote.Text = "Track limit warning comes from TSWB alarm bit.";

            if (lblPot1Name != null) lblPot1Name.Text = "Laser Heat Request % (Pot1 / ADC2)";
            if (lblPot2Name != null) lblPot2Name.Text = "Humidity Input % (Pot2 / ADC1)";
            if (lblLampName != null) lblLampName.Text = "Laser status lamp (PB6 / OC1B)";
            if (lblLightName != null) lblLightName.Text = "Reflected light sensor (ADC0 / PF0)";
            if (scrollLamp != null) { scrollLamp.Visible = false; scrollLamp.Enabled = false; }
            if (lblLampPercent != null) lblLampPercent.Text = "OFF";
            if (seg7Tens != null) seg7Tens.Visible = false;
            if (seg7Ones != null) seg7Ones.Visible = false;

            if (chkPc0 != null) { chkPc0.Visible = false; chkPc0.Enabled = false; }
            if (chkPc1 != null) { chkPc1.Visible = false; chkPc1.Enabled = false; }
            if (chkPc2 != null) chkPc2.Visible = false;
            if (chkPc3 != null) chkPc3.Visible = false;
            if (chkPc4 != null) chkPc4.Visible = false;
            if (chkPc5 != null) chkPc5.Visible = false;
            if (chkPc6 != null) chkPc6.Visible = false;
            if (chkPc7 != null) chkPc7.Visible = false;
            EnsureLaserPowerLedRow();

            if (lblMotorSpeed != null)
            {
                lblMotorSpeed.Location = new Point(12, 142);
                lblMotorSpeed.AutoSize = false;
                lblMotorSpeed.Size = new Size(255, 40);
            }

            // Move the dew-override controls into the side "Safety inputs" panel,
            // below the humidity input where they belong.
            if (grpPots != null)
            {
                grpPots.Size = new Size(grpPots.Size.Width, 210);

                if (chkVbTempOverride != null)
                {
                    grpTempControl?.Controls.Remove(chkVbTempOverride);
                    grpPots.Controls.Add(chkVbTempOverride);
                    chkVbTempOverride.Location = new Point(10, 126);
                }
                if (numVbTemp != null)
                {
                    grpTempControl?.Controls.Remove(numVbTemp);
                    grpPots.Controls.Add(numVbTemp);
                    numVbTemp.Location = new Point(150, 124);
                }
                if (lblVbTempUnit != null)
                {
                    grpTempControl?.Controls.Remove(lblVbTempUnit);
                    grpPots.Controls.Add(lblVbTempUnit);
                    lblVbTempUnit.Location = new Point(216, 128);
                }
                if (lblVbTempLive != null)
                {
                    grpTempControl?.Controls.Remove(lblVbTempLive);
                    grpPots.Controls.Add(lblVbTempLive);
                    lblVbTempLive.Location = new Point(10, 152);
                }
            }

            // Compact dewpoint panel layout to remove dead space.
            if (lblSimRH != null) lblSimRH.Location = new Point(12, 116);
            if (lblSimSurfaceTemp != null) lblSimSurfaceTemp.Location = new Point(12, 142);
            if (lblSimDewPoint != null) lblSimDewPoint.Location = new Point(12, 168);
            if (lblSimMargin != null) lblSimMargin.Location = new Point(12, 194);
            if (lblSimHeadHint != null) lblSimHeadHint.Visible = false;
            if (lblSimNote != null) lblSimNote.Visible = false;
            if (lblSimLaserState != null) lblSimLaserState.Location = new Point(330, 116);
            if (lblSimPower != null) lblSimPower.Location = new Point(330, 150);
            if (lblSimFan != null) lblSimFan.Location = new Point(330, 178);
            if (lblSimPhase != null) lblSimPhase.Location = new Point(330, 206);
            if (lblSimAmbientModel != null) lblSimAmbientModel.Visible = false;
            if (lblBoardRiskCaption != null) lblBoardRiskCaption.Location = new Point(12, 256);
            if (ledSimSafe != null) ledSimSafe.Location = new Point(12, 280);
            if (lblSimStatusSafe != null) lblSimStatusSafe.Location = new Point(36, 280);
            if (ledSimMarginal != null) ledSimMarginal.Location = new Point(220, 280);
            if (lblSimStatusMarginal != null) lblSimStatusMarginal.Location = new Point(244, 280);
            if (ledSimHighRisk != null) ledSimHighRisk.Location = new Point(430, 280);
            if (lblSimStatusHighRisk != null) lblSimStatusHighRisk.Location = new Point(454, 280);
            if (ledSimDoorFault != null) ledSimDoorFault.Location = new Point(12, 308);
            if (lblSimDoorFault != null) lblSimDoorFault.Location = new Point(32, 307);
            if (ledSimAxisAlarm != null) ledSimAxisAlarm.Location = new Point(240, 308);
            if (lblSimAxisAlarm != null) lblSimAxisAlarm.Location = new Point(260, 307);

            if (chkVbTempOverride != null) chkVbTempOverride.Visible = false;
            if (numVbTemp != null)
            {
                numVbTemp.Enabled = false;
                numVbTemp.Minimum = 0;
                numVbTemp.Maximum = 60;
                numVbTemp.DecimalPlaces = 1;
                numVbTemp.Value = 15;
            }
            if (chkVbTempOverride != null)
            {
                chkVbTempOverride.Visible = true;
                chkVbTempOverride.Text = "Dew override ON";
                chkVbTempOverride.Checked = false;
            }
            if (lblVbTempUnit != null) lblVbTempUnit.Text = "°C dew";
            if (lblVbTempLive != null) lblVbTempLive.Text = "Dew point override";

            _updateTimer = new Timer { Interval = 200 };
            _updateTimer.Tick += UpdateTimerOnTick;

            _dirTimer = new Timer { Interval = 80 };
            _dirTimer.Tick += DirTimer_Tick;

            // Populate COM ports
            try
            {
                string[] ports = AppBoard.GetAvailablePorts();
                if (comboComPorts != null)
                {
                    comboComPorts.Items.Clear();
                    comboComPorts.Items.AddRange(ports);
                    if (comboComPorts.Items.Count > 0)
                    {
                        comboComPorts.SelectedIndex = 0;
                    }
                }
            }
            catch { }

            SetupTooltips();

            if (numSetpoint != null) numSetpoint.ValueChanged += (_, __) => ResetPiController();
            if (numKp != null) numKp.ValueChanged += (_, __) => ResetPiController();
            if (numKi != null) numKi.ValueChanged += (_, __) => ResetPiController();
        }

        private void ResetPiController()
        {
            _intError = 0.0;
            _lastError = 0.0;
            _lastPiTime = DateTime.MinValue;
        }

        private void EnsureLaserPowerLedRow()
        {
            if (grpDigitalIO == null || _laserPowerLeds[0] != null) return;

            int startX = 12;
            int ledY = 96;
            int stepX = 24;
            var powerTitle = new Label
            {
                Name = "lblPowerOutputTitle",
                Text = "Power output",
                Location = new Point(startX, ledY + 24),
                AutoSize = true,
                ForeColor = Color.FromArgb(20, 20, 20),
                Font = new Font("Segoe UI", 8.5F, FontStyle.Bold)
            };
            grpDigitalIO.Controls.Add(powerTitle);
            for (int i = 0; i < _laserPowerLeds.Length; i++)
            {
                var led = new LedBulb
                {
                    Name = $"ledPc{i + 2}",
                    Location = new Point(startX + i * stepX, ledY),
                    Size = new Size(18, 18),
                    On = false,
                    Color = Color.Lime
                };

                var caption = new Label
                {
                    Name = $"lblLedPc{i + 2}",
                    Text = "",
                    Location = new Point(startX + i * stepX - 3, ledY + 40),
                    AutoSize = true,
                    ForeColor = Color.FromArgb(20, 20, 20),
                    Font = new Font("Segoe UI", 8F, FontStyle.Regular)
                };

                grpDigitalIO.Controls.Add(led);
                grpDigitalIO.Controls.Add(caption);
                _laserPowerLeds[i] = led;
            }
        }

        private void SetupTooltips()
        {
            var tt = new ToolTip { AutoPopDelay = 8000, InitialDelay = 400, ShowAlways = true };

            // Connection
            tt.SetToolTip(comboComPorts,         "Select the board COM port.");
            tt.SetToolTip(comboBaudRate,          "Board firmware expects 38400 baud 8N1.");
            tt.SetToolTip(btnConnect,             "Open the serial link and send a TXCHECK ping. LED turns green on success.");
            tt.SetToolTip(btnDisconnect,          "Close the serial link and stop all updates.");
            tt.SetToolTip(btnDatabaseConnect,     "Connect to MySQL for temperature logging.");
            tt.SetToolTip(btnDatabaseDisconnect,  "Disconnect from the database.");

            // Laser head D-pad
            tt.SetToolTip(btnDirUp,     "Move laser head Y− (up). Hold for continuous movement.");
            tt.SetToolTip(btnDirDown,   "Move laser head Y+ (down). Hold for continuous movement.");
            tt.SetToolTip(btnDirLeft,   "Move laser head X− (left). Hold for continuous movement.");
            tt.SetToolTip(btnDirRight,  "Move laser head X+ (right). Hold for continuous movement.");
            tt.SetToolTip(btnDirCentre, "Clear table-limit alarm and retract 20 mm from the triggered edge.");
            tt.SetToolTip(panelPositionMap, "Live map of laser head position. Red dot + red border = limit alarm active.");

            tt.SetToolTip(chkVbSW0, "Live state of physical SW0 (laser enable).");
            tt.SetToolTip(chkVbSW1, "Live state of physical SW1 (door interlock).");
            tt.SetToolTip(grpLabSwitches, "Door warning and track-limit warning come from board inputs/alarms.");

            // Temperature control
            tt.SetToolTip(numSetpoint,       "Target surface temperature for the PI controller (°C).");
            tt.SetToolTip(numKp,             "Proportional gain — faster response, more overshoot.");
            tt.SetToolTip(numKi,             "Integral gain — eliminates steady-state error; too high = oscillation.");
            tt.SetToolTip(chkVbTempOverride, "Enable/disable manual dewpoint override.");
            tt.SetToolTip(numVbTemp,         "Override dewpoint (°C) when Dew override is ON.");

            tt.SetToolTip(scrollPot1, "Pot 1 / PF2 / ADC2 — heater command on hardware.");
            tt.SetToolTip(scrollPot2, "Pot 2 / PF1 / ADC1 — ambient RH.");
            tt.SetToolTip(grpPots, "Pot1 = laser heat request. Pot2 = humidity input.");

            // Lamp / light
            tt.SetToolTip(scrollLamp, "Unused in this build; lamp follows laser-enable state.");
            tt.SetToolTip(gaugeLight, "Light sensor voltage (0–5 V) read back from the ADC.");

            // Digital I/O
            tt.SetToolTip(btnRefresh, "Refresh board indicator readouts.");
            tt.SetToolTip(chkPc0, "Unused in this panel.");
            tt.SetToolTip(chkPc1, "Unused in this panel.");
            tt.SetToolTip(chkPc2, "Laser power bar step 1/6 (~17%).");
            tt.SetToolTip(chkPc3, "Laser power bar step 2/6 (~33%).");
            tt.SetToolTip(chkPc4, "Laser power bar step 3/6 (~50%).");
            tt.SetToolTip(chkPc5, "Laser power bar step 4/6 (~67%).");
            tt.SetToolTip(chkPc6, "Laser power bar step 5/6 (~83%).");
            tt.SetToolTip(chkPc7, "Laser power bar step 6/6 (100%).");
            tt.SetToolTip(grpDigitalIO, "Read-only diagnostics from board state.");
            for (int i = 0; i < _laserPowerLeds.Length; i++)
            {
                if (_laserPowerLeds[i] != null)
                {
                    tt.SetToolTip(_laserPowerLeds[i], $"Laser power LED step {i + 1}/6.");
                }
            }

            // Logging
            tt.SetToolTip(numManualLogging, "Number of rows to insert in one manual snapshot.");
            tt.SetToolTip(btnInsertData,    "Insert current temperature into the database (manual).");
            tt.SetToolTip(btnEnableLogging, "Begin auto-inserting a row on every update tick (~100 ms).");
            tt.SetToolTip(btnStopLogging,   "Stop auto-logging.");
        }

        // ── Connection ───────────────────────────────────────────────────────────

        private void btnConnect_Click(object sender, EventArgs e)
        {
            if (_board != null && _board.IsConnected) return;

            string portName = comboComPorts?.SelectedItem as string;
            if (string.IsNullOrEmpty(portName)) { MessageBox.Show("Select a COM port first."); return; }

            int baud = 38400;
            if (comboBaudRate?.SelectedItem != null && int.TryParse(comboBaudRate.SelectedItem.ToString(), out int b))
                baud = b;

            _board = new AppBoard(portName, baud);

            try
            {
                _board.Connect();
                bool ok = _board.Ping();
                if (ledSerialStatus  != null) ledSerialStatus.On  = ok;
                if (btnDisconnect    != null) btnDisconnect.Enabled = ok;
                if (btnConnect       != null) btnConnect.Enabled   = !ok;
                SyncVirtualControls();
                if (ok)
                {
                    ResetPiController();
                    _dewWriteSupported = true;
                    _lastSentDewPoint = double.NaN;
                    _dewOverrideWasOn = false;
                    SyncDewOverrideState();
                    _updateTimer.Start();
                }
                else MessageBox.Show("Board did not respond to TXCHECK.");
            }
            catch (Exception ex)
            {
                if (ledSerialStatus != null) ledSerialStatus.On = false;
                if (btnDisconnect   != null) btnDisconnect.Enabled = false;
                MessageBox.Show("Failed to connect: " + ex.Message);
            }
        }

        private void btnDisconnect_Click(object sender, EventArgs e)
        {
            _updateTimer.Stop();
            ResetPiController();
            if (ledSerialStatus != null) ledSerialStatus.On = false;
            if (btnDisconnect   != null) btnDisconnect.Enabled = false;
            if (btnConnect      != null) btnConnect.Enabled = true;
            if (_board != null)
            {
                try
                {
                    // Best-effort safe shutdown before dropping the serial link.
                    _board.WriteHeaterPercent(0.0);
                    _board.WriteMotorPercent(0.0);
                    _board.WriteLampPercent(0.0);
                }
                catch { /* ignore disconnect-path errors */ }
                _board.Disconnect();
                if (_board is IDisposable d) d.Dispose();
                _board = null;
            }
            SyncVirtualControls();
        }

        private void btnDatabaseConnect_Click(object sender, EventArgs e)
        {
            try
            {
                string connStr = $"Server={txtDbServer?.Text ?? "127.0.0.1"};Port=3306;" +
                                 $"Database={txtDbDatabase?.Text ?? "enel712_final"};" +
                                 $"Uid={txtDbUsername?.Text ?? "root"};Pwd={txtDbPassword?.Text ?? ""};";
                _db = new DatabaseLogger(connStr);
                _db.Open();
                if (ledDatabaseStatus != null) ledDatabaseStatus.On = true;
                if (btnDatabaseDisconnect != null) btnDatabaseDisconnect.Enabled = true;
                if (btnDatabaseConnect    != null) btnDatabaseConnect.Enabled    = false;
            }
            catch (Exception ex)
            {
                if (ledDatabaseStatus != null) ledDatabaseStatus.On = false;
                MessageBox.Show("Database connect failed: " + ex.Message);
            }
        }

        private void btnDatabaseDisconnect_Click(object sender, EventArgs e)
        {
            _db?.Close(); _db = null;
            if (ledDatabaseStatus    != null) ledDatabaseStatus.On = false;
            if (btnDatabaseDisconnect != null) btnDatabaseDisconnect.Enabled = false;
            if (btnDatabaseConnect    != null) btnDatabaseConnect.Enabled    = true;
            if (lblLoggingStatus      != null) lblLoggingStatus.Text = "";
            _dataLoggingEnabled = false;
        }

        // ── Update loop (100 ms, updates all sections simultaneously) ────────────

        private void UpdateTimerOnTick(object sender, EventArgs e)
        {
            if (_isClosing || IsDisposed || Disposing) return;
            if (_board == null || !_board.IsConnected) return;
            try
            {
                _tickCounter++;

                // Baseline values are read often; light sensor is slower.
                PollBaseSensors();
                // Extension values are polled at 2 Hz.
                if ((_tickCounter % 2) == 0)
                {
                    PollSimExtension();
                }

                UpdateDigitalIoSection();
                UpdatePotsLightSection();
                UpdateTempControlSection();
                UpdateCondRiskSection();
                UpdateVirtualBoardLiveReadouts();
            }
            catch (Exception ex)
            {
                // Stop runaway timer activity if the form is shutting down or controls are gone.
                _updateTimer?.Stop();
                Console.WriteLine("Update error: " + ex.Message);
            }
        }

        private void PollBaseSensors()
        {
            _lastPina  = _board.ReadPINA();
            _lastPot1  = _board.ReadPot1();
            _lastPot2  = _board.ReadPot2();
            _lastTemp  = _board.ReadTemp();
            if ((_tickCounter % 3) == 0)
            {
                _lastLight = _board.ReadLight();
            }
        }

        private void PollSimExtension()
        {
            _lastMargin  = _board.ReadSimMargin();
            _lastDewPoint = _board.ReadSimDewPoint();
            _lastStatus  = _board.ReadSimStatus();
            _lastAlarms  = _board.ReadAlarmFlags();
        }

        // ── Digital I/O ─────────────────────────────────────────────────────────

        private void UpdateDigitalIoSection()
        {
            byte portc = 0;
            bool laserOn = (_lastPina & 1) != 0;
            int lampSegments = laserOn ? Math.Max(0, Math.Min(6, (int)Math.Ceiling((_lastPot1 / 255.0) * 6.0))) : 0;
            if (lampSegments >= 1) portc |= 4;
            if (lampSegments >= 2) portc |= 8;
            if (lampSegments >= 3) portc |= 16;
            if (lampSegments >= 4) portc |= 32;
            if (lampSegments >= 5) portc |= 64;
            if (lampSegments >= 6) portc |= 128;

            if (_lastStatus == 0)
            {
                if (seg7Tens != null) seg7Tens.Value = "G";
                if (seg7Ones != null) seg7Ones.Value = "O";
            }
            else if (_lastStatus == 1)
            {
                if (seg7Tens != null) seg7Tens.Value = "E";
                if (seg7Ones != null) seg7Ones.Value = "H";
            }
            else
            {
                if (seg7Tens != null) seg7Tens.Value = "n";
                if (seg7Ones != null) seg7Ones.Value = "O";
            }

            if (_laserPowerLeds[0] != null) _laserPowerLeds[0].On = (portc & 4) != 0;
            if (_laserPowerLeds[1] != null) _laserPowerLeds[1].On = (portc & 8) != 0;
            if (_laserPowerLeds[2] != null) _laserPowerLeds[2].On = (portc & 16) != 0;
            if (_laserPowerLeds[3] != null) _laserPowerLeds[3].On = (portc & 32) != 0;
            if (_laserPowerLeds[4] != null) _laserPowerLeds[4].On = (portc & 64) != 0;
            if (_laserPowerLeds[5] != null) _laserPowerLeds[5].On = (portc & 128) != 0;

            if (ledPa0 != null) ledPa0.On = (_lastPina &   1) != 0;
            if (ledPa1 != null) ledPa1.On = (_lastPina &   2) != 0;
            if (ledPa2 != null) ledPa2.On = (_lastPina &   4) != 0;
            if (ledPa3 != null) ledPa3.On = (_lastPina &   8) != 0;
            if (ledPa4 != null) ledPa4.On = (_lastPina &  16) != 0;
            if (ledPa5 != null) ledPa5.On = (_lastPina &  32) != 0;
            if (ledPa6 != null) ledPa6.On = (_lastPina &  64) != 0;
            if (ledPa7 != null) ledPa7.On = (_lastPina & 128) != 0;

            _syncingSwitchIndicators = true;
            try
            {
                if (chkVbSW0 != null) chkVbSW0.Checked = (_lastPina & 1) != 0;
                if (chkVbSW1 != null) chkVbSW1.Checked = (_lastPina & 2) != 0;
            }
            finally
            {
                _syncingSwitchIndicators = false;
            }
        }

        private void btnRefresh_Click(object sender, EventArgs e)
        {
            if (_board != null && _board.IsConnected) UpdateDigitalIoSection();
        }

        // ── Potentiometers, lamp, light ──────────────────────────────────────────

        private void UpdatePotsLightSection()
        {
            // Real hardware: board is the source of truth → update scrollbars from ADC.
            int pct1  = (int)Math.Round(_lastPot1 / 255.0 * 100.0);
            int pct2  = (int)Math.Round(_lastPot2 / 255.0 * 100.0);
            if (scrollPot1 != null) scrollPot1.Value = Math.Min(100, pct1);
            if (scrollPot2 != null) scrollPot2.Value = Math.Min(100, pct2);
            UpdatePotLabels();

            bool laserOn = (_lastPina & 1) != 0;
            if (lblLampPercent != null) lblLampPercent.Text = laserOn ? "ON" : "OFF";

            float lightV = 5.0f * _lastLight / 255f;
            if (gaugeLight != null) gaugeLight.Value = lightV;
        }

        private void UpdatePotLabels()
        {
            int p1 = scrollPot1?.Value ?? 50;
            int p2 = scrollPot2?.Value ?? 90;
            if (lblPot1Val != null) lblPot1Val.Text = $"{p1}%  ({p1 * 5.0 / 100.0:F2} V)";
            if (lblPot2Val != null) lblPot2Val.Text = $"{p2}%  ({p2 * 5.0 / 100.0:F2} V)";
        }

        private void scrollPot1_ValueChanged(object sender, EventArgs e)
        {
            int pct = scrollPot1?.Value ?? 50;
            if (lblPot1Val != null) lblPot1Val.Text = $"{pct}%  ({pct * 5.0 / 100.0:F2} V)";
        }

        private void scrollPot2_ValueChanged(object sender, EventArgs e)
        {
            int pct = scrollPot2?.Value ?? 90;
            if (lblPot2Val != null) lblPot2Val.Text = $"{pct}%  ({pct * 5.0 / 100.0:F2} V)";
        }

        private void scrollLamp_ValueChanged(object sender, EventArgs e)
        {
            // Lamp slider is hidden in current hardware-focused UI.
        }

        // ── Temperature Control ──────────────────────────────────────────────────

        private void UpdateTempControlSection()
        {
            double tempV       = 5.0 * _lastTemp / 255.0;
            double tempC       = tempV / 0.05;
            double setpointC   = (double)(numSetpoint?.Value ?? 40);
            double heaterPct   = _lastPot1 / 255.0 * 100.0; // Heater directly tied to Pot1.

            if (lblActualTemp != null)
                lblActualTemp.Text = $"Temp:   {tempC:F2} °C  /  {setpointC:F2} °C";

            double kp = (double)(numKp?.Value ?? 5);
            double ki = (double)(numKi?.Value ?? 1);
            DateTime now = DateTime.UtcNow;
            double dt    = (_lastPiTime != DateTime.MinValue) ? (now - _lastPiTime).TotalSeconds : 0.10;
            _lastPiTime  = now;
            if (dt <= 0.0) dt = 0.10;
            if (dt > 0.50) dt = 0.50;

            double error  = setpointC - tempC;
            bool errorSignChanged = (Math.Sign(error) != Math.Sign(_lastError)) && (Math.Abs(error) > 0.2);
            if (errorSignChanged)
            {
                // Prevent stale integral from driving the wrong actuator after crossing setpoint.
                _intError = 0.0;
            }
            _lastError = error;

            // Integrate only in a narrow unsaturated region to reduce windup.
            if (Math.Abs(error) < 15.0)
            {
                _intError += error * dt;
            }
            _intError = Math.Max(-40.0, Math.Min(40.0, _intError));

            /* Positive controller output applies heat; negative applies cooling. */
            double output    = kp * error + ki * _intError;
            double motorPct  = Math.Max(0, Math.Min(100, -output));

            // Guarantee some active cooling when significantly above setpoint.
            if (tempC > (setpointC + 1.0))
            {
                motorPct = Math.Max(motorPct, 20.0);
            }

            _board.WriteHeaterPercent(heaterPct);
            _board.WriteMotorPercent(motorPct);
            _lastHeaterCmdPct = heaterPct;
            _lastMotorCmdPct = motorPct;
            SendDewPointOverride();

            if (lblMotorSpeed != null)
            {
                lblMotorSpeed.Text =
                    $"Water Chiller Power % (Fan): {motorPct:F1}%{Environment.NewLine}" +
                    $"Laser Heat % (Heater): {heaterPct:F1}%";
            }

            if (_db != null && _db.IsConnected && _dataLoggingEnabled)
                _db.InsertTemperature(DateTime.Now, tempC, setpointC, kp, ki, null);

            _tempHistory.Add((float)tempC);
            _setpointHistory.Add((float)setpointC);
            if (_tempHistory.Count > MaxChartPoints)
            {
                _tempHistory.RemoveAt(0);
                _setpointHistory.RemoveAt(0);
            }
            DrawChart();
        }

        // ── Condensation / workflow (centre column) ─────────────────────────────

        private void UpdateCondRiskSection()
        {
            bool sw0 = (_lastPina & 1) != 0;
            bool sw1 = (_lastPina & 2) != 0;
            string phase;
            Color phaseColor;
            if      (!sw0 && !sw1) { phase = "IDLE";       phaseColor = Color.FromArgb(180, 210, 255); }
            else if (!sw0)          { phase = "DOOR OPEN";  phaseColor = Color.FromArgb(255, 220, 100); }
            else if (!sw1)          { phase = "LASER ON";   phaseColor = Color.FromArgb(120, 255, 120); }
            else                    { phase = "FAULT";      phaseColor = Color.FromArgb(255, 100, 100); }

            double surfaceC = 5.0 * _lastTemp / 255.0 / 0.05;
            int    rh       = (int)Math.Round(_lastPot2 / 255.0 * 100.0);

            double margin   = _lastMargin;
            double dewPoint = _lastDewPoint;
            int    power    = (int)Math.Round(_lastHeaterCmdPct);
            int    fan      = (int)Math.Round(_lastMotorCmdPct);
            int    status   = _lastStatus;
            int    alarms   = _lastAlarms;

            bool laserSourceOn = sw0;
            bool laserBeamOk   = sw0 && !sw1;

            if (lblSimRH != null)
                lblSimRH.Text = $"Humidity: {rh}%";
            if (lblSimSurfaceTemp != null)
                lblSimSurfaceTemp.Text = $"Head temp: {surfaceC:F1} °C";
            if (lblSimDewPoint != null)
                lblSimDewPoint.Text = $"Dew point: {dewPoint:F1} °C";

            Color marginColor = status switch
            {
                0 => Color.FromArgb(120, 255, 120),
                1 => Color.FromArgb(255, 220, 80),
                _ => Color.FromArgb(255, 100, 100)
            };
            if (lblSimMargin != null)
            {
                lblSimMargin.Text = $"Margin (head temp - dew point): {margin:F1} °C";
                lblSimMargin.ForeColor = marginColor;
            }

            if (lblSimLaserState != null)
                lblSimLaserState.Text = $"Laser state: {(laserSourceOn ? "ON" : "OFF")}";
            if (lblSimPhase != null)
            {
                lblSimPhase.Text = $"Door/laser phase: {phase}";
                lblSimPhase.ForeColor = phaseColor;
            }
            if (lblSimPower != null)
                lblSimPower.Text = $"Laser heat request: {power}%";
            if (lblSimFan != null)
                lblSimFan.Text = $"Water chiller power: {fan}%";

            if (lblSimAmbientModel != null) lblSimAmbientModel.Visible = false;

            // Startup suitability: green / orange / red (overall)
            bool interlockFault = sw0 && sw1;
            bool axisAlarm      = (alarms & LaserSimContract.AlarmAxisAlarm) != 0;
            bool doorInterlock  = (alarms & LaserSimContract.AlarmDoorFault) != 0;
            bool redStartup     = status == 2 || interlockFault || axisAlarm || doorInterlock;
            bool doorOpenOnly   = !sw0 && sw1;
            bool orangeStartup  = !redStartup && (status == 1 || doorOpenOnly);
            bool greenStartup   = !redStartup && !orangeStartup;

            if (ledStartupGreen  != null) ledStartupGreen.On  = greenStartup;
            if (ledStartupOrange != null) ledStartupOrange.On = orangeStartup;
            if (ledStartupRed    != null) ledStartupRed.On    = redStartup;

            if (lblStartupSummaryLine != null)
            {
                if (redStartup)
                {
                    if (status == 2) lblStartupSummaryLine.Text = "Summary: High condensation risk or active fault — do not enable laser.";
                    else if (axisAlarm) lblStartupSummaryLine.Text = "Summary: Axis limit active.";
                    else lblStartupSummaryLine.Text = "Summary: Door interlock fault.";
                }
                else if (orangeStartup)
                {
                    if (doorOpenOnly)
                        lblStartupSummaryLine.Text = "Summary: Door open.";
                    else
                        lblStartupSummaryLine.Text = "Summary: Condensation margin is marginal.";
                }
                else
                    lblStartupSummaryLine.Text = "Summary: Safe to proceed.";
            }

            if (ledSimSafe     != null) ledSimSafe.On     = status == 0;
            if (ledSimMarginal != null) ledSimMarginal.On = status == 1;
            if (ledSimHighRisk != null) ledSimHighRisk.On = status == 2;

            if (ledSimDoorFault != null) ledSimDoorFault.On = (alarms & LaserSimContract.AlarmDoorFault) != 0;
            if (ledSimAxisAlarm != null) ledSimAxisAlarm.On = (alarms & LaserSimContract.AlarmAxisAlarm) != 0;
        }

        // ── Chart ────────────────────────────────────────────────────────────────

        private void DrawChart() => panelChart?.Invalidate();

        private void PanelChart_Paint(object sender, PaintEventArgs e)
        {
            var g   = e.Graphics;
            var bg  = Color.White;
            var fg  = Brushes.Black;
            var gridPen = new Pen(Color.LightGray);
            g.Clear(bg);

            int w = panelChart.Width - 50, h = panelChart.Height - 50;
            if (w <= 0 || h <= 0) { gridPen.Dispose(); return; }
            int ox = 40, oy = 22;

            g.DrawString("Temp (°C)", SystemFonts.DefaultFont, fg, 2, oy + h / 2 - 20);
            g.DrawString("Sample",   SystemFonts.DefaultFont, fg, ox + w / 2 - 20, oy + h + 8);
            g.DrawRectangle(gridPen, ox, oy, w, h);
            gridPen.Dispose();

            if (_tempHistory.Count < 2) return;

            float minT = float.MaxValue, maxT = float.MinValue;
            foreach (var v in _tempHistory)     { minT = Math.Min(minT, v); maxT = Math.Max(maxT, v); }
            foreach (var v in _setpointHistory) { minT = Math.Min(minT, v); maxT = Math.Max(maxT, v); }
            float range = Math.Max(maxT - minT, 1f);
            minT -= range * 0.1f; maxT += range * 0.1f; range = maxT - minT;

            var pts = new List<PointF>();
            for (int i = 0; i < _tempHistory.Count; i++)
            {
                float x = ox + (float)i / Math.Max(_tempHistory.Count - 1, 1) * w;
                float y = oy + h - (_tempHistory[i] - minT) / range * h;
                pts.Add(new PointF(x, y));
            }
            if (pts.Count >= 2)
                g.DrawLines(new Pen(Color.DeepSkyBlue, 2), pts.ToArray());

            float spY = oy + h - (_setpointHistory.Count > 0
                ? (_setpointHistory[_setpointHistory.Count - 1] - minT) / range * h : 0);
            g.DrawLine(new Pen(Color.Orange, 2), ox, spY, ox + w, spY);
        }

        // ── Position map (laser head dot on grid) ────────────────────────────────

        private void PanelPositionMap_Paint(object sender, PaintEventArgs e)
        {
            var g = e.Graphics;
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            g.Clear(Color.FromArgb(22, 22, 28));

            int w = panelPositionMap.Width, h = panelPositionMap.Height;

            // Grid lines
            using var gridPen = new Pen(Color.FromArgb(40, 40, 55));
            for (int i = 1; i < 6; i++)
            {
                g.DrawLine(gridPen, i * w / 6, 0, i * w / 6, h);
                g.DrawLine(gridPen, 0, i * h / 6, w, i * h / 6);
            }

            // Border (red when alarm)
            using var borderPen = new Pen(_limitAlarm ? Color.FromArgb(220, 60, 60) : Color.FromArgb(70, 70, 100), 2);
            g.DrawRectangle(borderPen, 1, 1, w - 3, h - 3);

            // Laser head dot
            float dotX = (float)((_laserX - MinPos) / (MaxPos - MinPos) * (w - 16)) + 8;
            float dotY = (float)((_laserY - MinPos) / (MaxPos - MinPos) * (h - 16)) + 8;
            var   dotC = _limitAlarm ? Color.FromArgb(255, 80, 80) : Color.FromArgb(100, 200, 255);
            using var dotBrush = new SolidBrush(dotC);
            g.FillEllipse(dotBrush, dotX - 6, dotY - 6, 12, 12);
            using var xhPen = new Pen(Color.White);
            g.DrawLine(xhPen, dotX - 9, dotY, dotX + 9, dotY);
            g.DrawLine(xhPen, dotX, dotY - 9, dotX, dotY + 9);

            // Corner labels
            using var labelBrush = new SolidBrush(Color.FromArgb(90, 90, 110));
            using var sf         = new Font("Segoe UI", 7);
            g.DrawString("0,0",     sf, labelBrush, 3,     3);
            g.DrawString("300,300", sf, labelBrush, w - 36, h - 13);
        }

        // ── D-pad direction control ───────────────────────────────────────────────

        private void StartMove(MoveDir dir)
        {
            if (_limitAlarm) return;
            _heldDir   = dir;
            _holdTicks = 0;
            _dirTimer.Start();
        }

        private void StopMove()
        {
            _heldDir = MoveDir.None;
            _dirTimer.Stop();
        }

        private void DirTimer_Tick(object sender, EventArgs e)
        {
            if (_limitAlarm) { _dirTimer.Stop(); return; }

            _holdTicks++;
            switch (_heldDir)
            {
                case MoveDir.Up:    _laserY = Math.Max(MinPos, _laserY - StepMm); break;
                case MoveDir.Down:  _laserY = Math.Min(MaxPos, _laserY + StepMm); break;
                case MoveDir.Left:  _laserX = Math.Max(MinPos, _laserX - StepMm); break;
                case MoveDir.Right: _laserX = Math.Min(MaxPos, _laserX + StepMm); break;
            }

            bool atEdge = _laserX <= MinPos || _laserX >= MaxPos ||
                          _laserY <= MinPos || _laserY >= MaxPos;
            if (atEdge || _holdTicks >= HoldAlarmTicks)
            {
                _limitAlarm = true;
                if      (_laserX <= MinPos) _limitAxis = "X-MIN";
                else if (_laserX >= MaxPos) _limitAxis = "X-MAX";
                else if (_laserY <= MinPos) _limitAxis = "Y-MIN";
                else if (_laserY >= MaxPos) _limitAxis = "Y-MAX";
                else                        _limitAxis = "OVERTRAVEL";
                _dirTimer.Stop();

                // Hardware alarm indication comes from board firmware.
            }

            UpdatePositionDisplay();
        }

        private void btnDirCentre_Click(object sender, EventArgs e)
        {
            if (!_limitAlarm) return;

            // Retract 20 mm away from the triggered limit
            if      (_limitAxis == "X-MIN") _laserX = MinPos + RetractMm;
            else if (_limitAxis == "X-MAX") _laserX = MaxPos - RetractMm;
            else if (_limitAxis == "Y-MIN") _laserY = MinPos + RetractMm;
            else if (_limitAxis == "Y-MAX") _laserY = MaxPos - RetractMm;
            else { _laserX = 150.0; _laserY = 150.0; }

            _limitAlarm = false;
            _limitAxis  = "";

            UpdatePositionDisplay();
        }

        private void UpdatePositionDisplay()
        {
            if (lblPosX      != null) lblPosX.Text     = $"X:  {_laserX:F1} mm";
            if (lblPosY      != null) lblPosY.Text     = $"Y:  {_laserY:F1} mm";
            if (lblLimitAlarm != null)
            {
                lblLimitAlarm.Text    = _limitAlarm
                    ? $"⚠  LIMIT: {_limitAxis}   —   press ● to retract {RetractMm} mm"
                    : "";
                lblLimitAlarm.Visible = _limitAlarm;
            }
            panelPositionMap?.Invalidate();
        }

        // ── Virtual / simulator controls ─────────────────────────────────────────

        /// <summary>Sync controls for hardware-only mode.</summary>
        private void SyncVirtualControls()
        {
            if (grpLabSwitches != null) grpLabSwitches.Visible = false;
            if (scrollPot1 != null) scrollPot1.Enabled = true;
            if (scrollPot2 != null) scrollPot2.Enabled = true;
            if (lblVbAutoNote != null) lblVbAutoNote.Text = "";
            UpdatePotLabels();
        }

        private void UpdateVirtualBoardLiveReadouts()
        {
            if (lblVbTempLive != null)
            {
                bool overrideOn = chkVbTempOverride?.Checked ?? false;
                lblVbTempLive.Text = overrideOn
                    ? $"Dew set: {(double)(numVbTemp?.Value ?? 15M):F1} °C"
                    : "Dew set: AUTO (from humidity)";
            }
            if (lblVbAutoNote != null)
            {
                bool axis = (_lastAlarms & LaserSimContract.AlarmAxisAlarm) != 0;
                lblVbAutoNote.Text = axis ? "Track limit warning: ACTIVE (press TSWB centre)." : "Track limit warning: clear.";
            }
        }

        private void chkVbSW_CheckedChanged(object sender, EventArgs e)
        {
            if (_syncingSwitchIndicators) return;
        }

        private void chkVbTempOverride_CheckedChanged(object sender, EventArgs e)
        {
            SyncDewOverrideState();
        }

        private void numVbTemp_ValueChanged(object sender, EventArgs e)
        {
            if ((_board != null) && _board.IsConnected && (chkVbTempOverride?.Checked ?? false))
            {
                SendDewPointOverride();
            }
        }

        private void SyncDewOverrideState()
        {
            bool useOverride = chkVbTempOverride?.Checked ?? false;
            if (numVbTemp != null) numVbTemp.Enabled = useOverride;
            if (_board == null || !_board.IsConnected) { _dewOverrideWasOn = useOverride; return; }

            if (useOverride)
            {
                SendDewPointOverride();
            }
            else
            {
                try
                {
                    _board.ClearSimDewPointOverride();
                    _lastSentDewPoint = double.NaN;
                    PollSimExtension();
                }
                catch
                {
                    // Ignore transient link issues on clear.
                }
            }

            _dewOverrideWasOn = useOverride;
        }

        private void SendDewPointOverride()
        {
            if (_board == null || !_board.IsConnected || !_dewWriteSupported) return;
            if (!(chkVbTempOverride?.Checked ?? false)) return;
            double dew = (double)(numVbTemp?.Value ?? 15M);
            if (Math.Abs(dew - _lastSentDewPoint) < 0.05) return;
            try
            {
                bool ack = _board.WriteSimDewPoint(dew);
                if (ack)
                {
                    _lastSentDewPoint = dew;
                    PollSimExtension();
                }
            }
            catch
            {
                // Allow retry on transient failures.
            }
        }

        // ── Logging ──────────────────────────────────────────────────────────────

        private void btnInsertData_Click(object sender, EventArgs e)
        {
            if (_db == null || !_db.IsConnected)   { MessageBox.Show("Connect to database first."); return; }
            if (_board == null || !_board.IsConnected) { MessageBox.Show("Connect to board first.");    return; }
            byte t   = _board.ReadTemp();
            double c = 5.0 * t / 255.0 / 0.05;
            int count = (int)(numManualLogging?.Value ?? 1);
            for (int i = 0; i < count; i++)
                _db.InsertTemperature(DateTime.Now, c, (double?)numSetpoint?.Value,
                    (double?)numKp?.Value, (double?)numKi?.Value, null);
        }

        private void btnEnableLogging_Click(object sender, EventArgs e)
        {
            _dataLoggingEnabled = true;
            if (lblLoggingStatus != null) lblLoggingStatus.Text = "Logging in progress…";
        }

        private void btnStopLogging_Click(object sender, EventArgs e)
        {
            _dataLoggingEnabled = false;
            if (lblLoggingStatus != null) lblLoggingStatus.Text = "";
        }

        // ── Cleanup ──────────────────────────────────────────────────────────────

        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            _isClosing = true;
            _dataLoggingEnabled = false;
            _updateTimer?.Stop();
            _dirTimer?.Stop();
            if (_updateTimer != null) _updateTimer.Tick -= UpdateTimerOnTick;
            if (_dirTimer != null) _dirTimer.Tick -= DirTimer_Tick;
            if (_board != null)
            {
                try
                {
                    _board.WriteHeaterPercent(0.0);
                    _board.WriteMotorPercent(0.0);
                    _board.WriteLampPercent(0.0);
                }
                catch { }
                _board.Disconnect();
                if (_board is IDisposable d) d.Dispose();
                _board = null;
            }
            _db?.Close();
        }
    }
}
```
