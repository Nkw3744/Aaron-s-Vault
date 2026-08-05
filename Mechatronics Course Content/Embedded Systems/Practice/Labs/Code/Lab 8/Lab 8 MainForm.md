# Lab 8 MainForm

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `MainForm.cs` · [[File Handling and Serial Ports]] · [[GUI and Event-Driven Programming]]

```csharp
using System.IO.Ports;
namespace ExampleDieRollerGUI
{
    public sealed class MainForm : Form
    {
        private readonly SplitContainer _root = new SplitContainer();
        private readonly GroupBox _gbGame = new GroupBox();
        private readonly Panel _pbDie = new Panel();
        private readonly TextBox _tbName = new TextBox();
        private readonly Button _btnRoll = new Button();
        private readonly Button _btnEndTurn = new Button();
        private readonly Button _btnNewGame = new Button();
        private readonly Label _lblGameStatus = new Label();
        private readonly Label _lblScoreboard = new Label();
        private readonly Label _lblRollsLeft = new Label();
        private const int DiceCount = 5;
        private readonly FlowLayoutPanel _pnlDiceStrip = new FlowLayoutPanel();
        private readonly PictureBox[] _dicePbs = new PictureBox[DiceCount];
        private readonly CheckBox[] _diceChecks = new CheckBox[DiceCount];
        private readonly Random _rng = new Random();
        private readonly List<Die> _dice;
        private readonly GroupBox _gbCom = new GroupBox();
        private readonly ComboBox _cbPorts = new ComboBox();
        private readonly ComboBox _cbBaud = new ComboBox();
        private readonly ComboBox _cbDataBits = new ComboBox();
        private readonly ComboBox _cbParity = new ComboBox();
        private readonly ComboBox _cbStopBits = new ComboBox();
        private readonly ComboBox _cbHandshake = new ComboBox();
        private readonly Button _btnOpenClose = new Button();
        private readonly Label _lblComStatus = new Label();
        private SerialPort? _serialPort = null;
        private bool _comConnected = false;
        private GameSession? _session = null;
        private bool _gameStarted = false;
        public MainForm()
        {
            Text = "Yahtzee - Five Dice";
            StartPosition = FormStartPosition.CenterScreen;
            ClientSize = new Size(760, 460);
            MinimumSize = new Size(720, 440);
            _rng = new Random();
            _dice = new List<Die>();
            for (int i = 0; i < DiceCount; i++)
            {
                _dice.Add(new Die(_rng));
            }
            BuildLayout();
            SetupInitialUiState();
            PopulateSerialSettingsCombos();
            PopulateComPorts();
            FormClosing += OnFormClosing;
        }
        private void BuildLayout()
        {
            _root.Dock = DockStyle.Fill;
            _root.Orientation = Orientation.Vertical;
            _root.SplitterWidth = 6;
            _root.Panel1MinSize = 400;
            _root.Panel2MinSize = 100;
            Controls.Add(_root);
            _gbGame.Dock = DockStyle.Fill;
            _gbGame.Text = "Game";
            _gbGame.Padding = new Padding(12);
            _gbCom.Dock = DockStyle.Fill;
            _gbCom.Text = "COM Port";
            _gbCom.Padding = new Padding(12);
            _root.Panel1.Controls.Add(_gbGame);
            _root.Panel2.Controls.Add(_gbCom);
            BuildGamePanel(_gbGame);
            BuildComPanel(_gbCom);
        }
        protected override void OnShown(EventArgs e)
        {
            base.OnShown(e);
            SetSplitterDistanceSafe(_root, desired: 420);
        }
        private static void SetSplitterDistanceSafe(SplitContainer sc, int desired)
        {
            int min = 0;
            int max = Math.Max(0, sc.Width - sc.SplitterWidth);
            sc.SplitterDistance = Math.Clamp(desired, min, max);
        }
        private void BuildGamePanel(Control parent)
        {
            int _gamePanelOriginX = 20;
            int _gamePanelOriginY = 30;
            int _dieSize = 50;
            int _diePadding = 5;
            _pbDie.BorderStyle = BorderStyle.FixedSingle;
            _pbDie.BackColor = Color.LightGray;
            _pbDie.Location = new Point(_gamePanelOriginX, _gamePanelOriginY);
            _pbDie.Size = new Size(
                8 * _diePadding + 6 * _dieSize + 5 * _diePadding,
                1 * _dieSize + 4 * _diePadding + 30);
            _pnlDiceStrip.Location = new Point(_diePadding, _diePadding);
            _pnlDiceStrip.Size = new Size(
                4 * _diePadding + 6 * _dieSize + 5 * _diePadding,
                1 * _dieSize + 1 * _diePadding + 30);
            _pnlDiceStrip.WrapContents = false;
            _pnlDiceStrip.AutoScroll = false;
            _pnlDiceStrip.FlowDirection = FlowDirection.LeftToRight;
            _pnlDiceStrip.BackColor = Color.LightGray;
            for (int i = 0; i < DiceCount; i++)
            {
                int dieIndex = i;
                var pb = new PictureBox
                {
                    Size = new Size(_dieSize, _dieSize),
                    Margin = new Padding(_diePadding),
                    BorderStyle = BorderStyle.FixedSingle,
                    BackColor = Color.LightGray,
                    SizeMode = PictureBoxSizeMode.Zoom
                };
                var cb = new CheckBox
                {
                    Text = "Roll",
                    Checked = true,
                    AutoSize = true,
                    TextAlign = ContentAlignment.MiddleCenter
                };
                cb.CheckedChanged += (s, e) =>
                {
                    _dice[dieIndex].AllowRoll = cb.Checked;
                    SendLedCommand();
                };
                _dicePbs[dieIndex] = pb;
                _diceChecks[dieIndex] = cb;
                var diePanel = new FlowLayoutPanel
                {
                    FlowDirection = FlowDirection.TopDown,
                    WrapContents = false,
                    AutoSize = true,
                    Margin = new Padding(_diePadding)
                };
                diePanel.Controls.Add(pb);
                diePanel.Controls.Add(cb);
                _pnlDiceStrip.Controls.Add(diePanel);
            }
            _pbDie.Controls.Add(_pnlDiceStrip);
            parent.Controls.Add(_pbDie);
            _lblRollsLeft.AutoSize = true;
            _lblRollsLeft.Font = new Font("Segoe UI", 9f, FontStyle.Bold);
            _lblRollsLeft.ForeColor = Color.DarkBlue;
            _lblRollsLeft.Location = new Point(_gamePanelOriginX,
                _gamePanelOriginY + _dieSize + 4 * _diePadding + 34);
            var lblName = MakeLabel("Player Name:", _gamePanelOriginX,
                _gamePanelOriginY + _dieSize + 4 * _diePadding + 55);
            _tbName.Location = new Point(_gamePanelOriginX,
                _gamePanelOriginY + _dieSize + 4 * _diePadding + 73);
            _tbName.Width = 200;
            _tbName.TextChanged += OnNameTextChanged;
            _btnRoll.Text = "Roll";
            _btnRoll.Location = new Point(_gamePanelOriginX,
                _gamePanelOriginY + _dieSize + 4 * _diePadding + 108);
            _btnRoll.Width = 100;
            _btnRoll.Height = 30;
            _btnRoll.Click += OnRollClicked;
            _btnEndTurn.Text = "End Turn";
            _btnEndTurn.Location = new Point(_gamePanelOriginX + 110,
                _gamePanelOriginY + _dieSize + 4 * _diePadding + 108);
            _btnEndTurn.Width = 100;
            _btnEndTurn.Height = 30;
            _btnEndTurn.Click += OnEndTurnClicked;
            _btnNewGame.Text = "New Game";
            _btnNewGame.Location = new Point(_gamePanelOriginX + 220,
                _gamePanelOriginY + _dieSize + 4 * _diePadding + 108);
            _btnNewGame.Width = 100;
            _btnNewGame.Height = 30;
            _btnNewGame.Click += OnNewGameClicked;
            _lblGameStatus.AutoSize = true;
            _lblGameStatus.Location = new Point(_gamePanelOriginX,
                _gamePanelOriginY + _dieSize + 4 * _diePadding + 150);
            _lblGameStatus.ForeColor = Color.DimGray;
            _lblScoreboard.AutoSize = true;
            _lblScoreboard.Font = new Font("Courier New", 8.5f);
            _lblScoreboard.Location = new Point(_gamePanelOriginX,
                _gamePanelOriginY + _dieSize + 4 * _diePadding + 175);
            _lblScoreboard.ForeColor = Color.DarkSlateGray;
            parent.Controls.Add(_lblRollsLeft);
            parent.Controls.Add(lblName);
            parent.Controls.Add(_tbName);
            parent.Controls.Add(_btnRoll);
            parent.Controls.Add(_btnEndTurn);
            parent.Controls.Add(_btnNewGame);
            parent.Controls.Add(_lblGameStatus);
            parent.Controls.Add(_lblScoreboard);
        }
        private void BuildComPanel(Control parent)
        {
            int xLabel = 20;
            int xCtrl = 100;
            int y = 30;
            int dy = 34;
            int w = 160;
            parent.Controls.Add(MakeLabel("Port:", xLabel, y));
            SetupCombo(_cbPorts, xCtrl, y, w);
            parent.Controls.Add(_cbPorts);
            y += dy;
            parent.Controls.Add(MakeLabel("Baud:", xLabel, y));
            SetupCombo(_cbBaud, xCtrl, y, w);
            parent.Controls.Add(_cbBaud);
            y += dy;
            parent.Controls.Add(MakeLabel("Data bits:", xLabel, y));
            SetupCombo(_cbDataBits, xCtrl, y, w);
            parent.Controls.Add(_cbDataBits);
            y += dy;
            parent.Controls.Add(MakeLabel("Parity:", xLabel, y));
            SetupCombo(_cbParity, xCtrl, y, w);
            parent.Controls.Add(_cbParity);
            y += dy;
            parent.Controls.Add(MakeLabel("Stop bits:", xLabel, y));
            SetupCombo(_cbStopBits, xCtrl, y, w);
            parent.Controls.Add(_cbStopBits);
            y += dy;
            parent.Controls.Add(MakeLabel("Handshake:", xLabel, y));
            SetupCombo(_cbHandshake, xCtrl, y, w);
            parent.Controls.Add(_cbHandshake);
            y += dy + 8;
            _btnOpenClose.Text = "Open";
            _btnOpenClose.Location = new Point(xCtrl, y);
            _btnOpenClose.Width = 140;
            _btnOpenClose.Click += OnOpenCloseClicked;
            parent.Controls.Add(_btnOpenClose);
            y += dy;
            _lblComStatus.AutoSize = true;
            _lblComStatus.Location = new Point(xLabel, y + 6);
            _lblComStatus.ForeColor = Color.DarkGreen;
            parent.Controls.Add(_lblComStatus);
        }
        private static void SetupCombo(ComboBox cb, int x, int y, int width)
        {
            cb.Location = new Point(x, y - 3);
            cb.Width = width;
            cb.DropDownStyle = ComboBoxStyle.DropDownList;
        }
        private static Label MakeLabel(string text, int x, int y)
        {
            return new System.Windows.Forms.Label
            {
                Text = text,
                AutoSize = true,
                Location = new Point(x, y)
            };
        }
        private void SetupInitialUiState()
        {
            _tbName.Enabled = false;
            _btnRoll.Enabled = false;
            _btnEndTurn.Enabled = false;
            _btnNewGame.Enabled = false;
            _pbDie.Enabled = false;
            _lblGameStatus.Text = "Game locked: connect to board first.";
            _lblComStatus.Text = "Status: Closed";
            _lblRollsLeft.Text = "";
            for (int i = 0; i < DiceCount; i++)
            {
                _dicePbs[i].Image = DieFace.GetPlaceholder();
            }
        }
        private void PopulateSerialSettingsCombos()
        {
            _cbBaud.Items.AddRange(new object[]
            {
                "9600", "19200", "38400", "57600", "115200"
            });
            _cbBaud.SelectedItem = "9600";
            _cbDataBits.Items.AddRange(new object[] { "7", "8" });
            _cbDataBits.SelectedItem = "8";
            _cbParity.Items.AddRange(new object[]
            {
                "None", "Odd", "Even", "Mark", "Space"
            });
            _cbParity.SelectedItem = "None";
            _cbStopBits.Items.AddRange(new object[]
            {
                "One", "Two", "OnePointFive", "None"
            });
            _cbStopBits.SelectedItem = "One";
            _cbHandshake.Items.AddRange(new object[]
            {
                "None", "XOnXOff", "RequestToSend", "RequestToSendXOnXOff"
            });
            _cbHandshake.SelectedItem = "None";
        }
        private void PopulateComPorts()
        {
            _cbPorts.Items.Clear();
            string[] ports = SerialPort.GetPortNames()
                .OrderBy(p => p)
                .ToArray();
            if (ports.Length == 0)
            {
                _cbPorts.Enabled = false;
                _btnOpenClose.Enabled = false;
                _lblComStatus.ForeColor = Color.DarkRed;
                _lblComStatus.Text = "Status: No COM ports detected";
                return;
            }
            _cbPorts.Items.AddRange(ports);
            _cbPorts.SelectedIndex = 0;
            _cbPorts.Enabled = true;
            _btnOpenClose.Enabled = true;
        }
        private void OnOpenCloseClicked(object? sender, EventArgs e)
        {
            if (_comConnected)
            {
                CloseSerialPort();
                return;
            }
            if (_cbPorts.SelectedItem == null)
            {
                MessageBox.Show("Please select a COM port.", "COM Port",
                    MessageBoxButtons.OK, MessageBoxIcon.Information);
                return;
            }
            string portName = _cbPorts.SelectedItem.ToString()!;
            int baud = 9600;
            int dataBits = 8;
            Parity parity = Parity.None;
            StopBits stopBits = StopBits.One;
            Handshake handshake = Handshake.None;
            try
            {
                if (_cbBaud.SelectedItem != null)
                    baud = int.Parse(_cbBaud.SelectedItem.ToString()!);
                if (_cbDataBits.SelectedItem != null)
                    dataBits = int.Parse(_cbDataBits.SelectedItem.ToString()!);
                if (_cbParity.SelectedItem != null)
                    parity = (Parity)Enum.Parse(typeof(Parity),
                        _cbParity.SelectedItem.ToString()!);
                if (_cbStopBits.SelectedItem != null)
                    stopBits = (StopBits)Enum.Parse(typeof(StopBits),
                        _cbStopBits.SelectedItem.ToString()!);
                if (_cbHandshake.SelectedItem != null)
                    handshake = (Handshake)Enum.Parse(typeof(Handshake),
                        _cbHandshake.SelectedItem.ToString()!);
            }
            catch
            {
                baud = 9600; dataBits = 8; parity = Parity.None;
                stopBits = StopBits.One; handshake = Handshake.None;
            }
            const int EchoTimeoutMs = 600;
            var sp = new SerialPort(portName, baud, parity, dataBits, stopBits)
            {
                Handshake = handshake,
                ReadTimeout = EchoTimeoutMs,
                WriteTimeout = EchoTimeoutMs,
                NewLine = "\n"
            };
            try
            {
                sp.Open();
                sp.DiscardInBuffer();
                sp.DiscardOutBuffer();
                sp.WriteLine("HELLO");
                string echo = sp.ReadLine().Trim();
                if (string.Equals(echo, "HELLO", StringComparison.Ordinal))
                {
                    _serialPort = sp;
                    _comConnected = true;
                    _lblComStatus.ForeColor = Color.DarkGreen;
                    _lblComStatus.Text = $"Status: Open ({portName}), online";
                    _btnOpenClose.Text = "Disconnect";
                    _cbPorts.Enabled = false;
                    _cbBaud.Enabled = false;
                    _cbDataBits.Enabled = false;
                    _cbParity.Enabled = false;
                    _cbStopBits.Enabled = false;
                    _cbHandshake.Enabled = false;
                    _tbName.Enabled = true;
                    _pbDie.Enabled = true;
                    _btnNewGame.Enabled = true;
                    _lblGameStatus.Text = "Connected! Enter name and press New Game.";
                    for (int i = 0; i < DiceCount; i++)
                        _dicePbs[i].Image = DieFace.GetImage(_dice[i].Value);
                    SendLedCommand();
                    MessageBox.Show($"Connected to {portName} and handshake succeeded.",
                        "COM Port", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
                else
                {
                    sp.Close();
                    sp.Dispose();
                    _lblComStatus.ForeColor = Color.DarkRed;
                    _lblComStatus.Text = "Status: Handshake failed (unexpected reply)";
                    MessageBox.Show("Handshake failed: unexpected reply from device.",
                        "COM Port", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }
            catch (Exception ex)
            {
                try { sp.Close(); sp.Dispose(); } catch { }
                _lblComStatus.ForeColor = Color.DarkRed;
                _lblComStatus.Text = $"Status: Error opening {portName}";
                MessageBox.Show(
                    $"Failed to open/handshake on {portName}.\n\nDetails: {ex.Message}",
                    "COM Port", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
        private void CloseSerialPort()
        {
            if (_serialPort != null)
            {
                try
                {
                    if (_serialPort.IsOpen) _serialPort.Close();
                    _serialPort.Dispose();
                }
                catch { }
                _serialPort = null;
            }
            _comConnected = false;
            _btnOpenClose.Text = "Open";
            _lblComStatus.ForeColor = Color.DimGray;
            _lblComStatus.Text = "Status: Closed";
            _cbPorts.Enabled = true; _cbBaud.Enabled = true;
            _cbDataBits.Enabled = true; _cbParity.Enabled = true;
            _cbStopBits.Enabled = true; _cbHandshake.Enabled = true;
            _tbName.Enabled = false;
            _btnRoll.Enabled = false;
            _btnEndTurn.Enabled = false;
            _btnNewGame.Enabled = false;
            _pbDie.Enabled = false;
            _gameStarted = false;
            _session = null;
            _lblGameStatus.Text = "Game locked: connect to board first.";
            _lblRollsLeft.Text = "";
            _lblScoreboard.Text = "";
            for (int i = 0; i < DiceCount; i++)
                _dicePbs[i].Image = DieFace.GetPlaceholder();
        }
        private void SendLedCommand()
        {
            if (_serialPort == null || !_serialPort.IsOpen) return;
            byte ledByte = Scoring.GetLedByte(_dice, _diceChecks);
            try
            {
                _serialPort.WriteLine($"LED:{ledByte:X2}");
            }
            catch { }
        }
        private void OnNameTextChanged(object? sender, EventArgs e)
        {
            _btnNewGame.Enabled = _tbName.Enabled &&
                                  _tbName.Text.Trim().Length > 0;
        }
        private void OnNewGameClicked(object? sender, EventArgs e)
        {
            string input = ShowInputDialog("How many players? (1-5)",
                "New Game", "1") ?? "";
            if (!int.TryParse(input, out int numPlayers)
                || numPlayers < 1 || numPlayers > 5)
            {
                MessageBox.Show("Please enter a number between 1 and 5.",
                    "Invalid Input", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            var players = new List<Player>();
            for (int i = 0; i < numPlayers; i++)
            {
                string defaultName = (i == 0 && _tbName.Text.Trim().Length > 0)
                    ? _tbName.Text.Trim() : $"Player {i + 1}";
                string name = ShowInputDialog(
                    $"Enter name for Player {i + 1}:",
                    "Player Name", defaultName) ?? defaultName;
                if (string.IsNullOrWhiteSpace(name)) name = defaultName;
                players.Add(new Player(name.Trim()));
            }
            string rInput = ShowInputDialog(
                "How many rounds? (1-13)", "Rounds", "3") ?? "3";
            if (!int.TryParse(rInput, out int totalRounds)
                || totalRounds < 1 || totalRounds > 13)
                totalRounds = 3;
            _session = new GameSession(players, totalRounds);
            _gameStarted = true;
            ResetForNewTurn();
            UpdateGameStatus();
            UpdateScoreboard();
        }
        private void ResetForNewTurn()
        {
            _session!.CurrentPlayer.ResetRolls();
            for (int i = 0; i < DiceCount; i++)
            {
                _diceChecks[i].Checked = true;
                _dice[i].AllowRoll = true;
            }
            foreach (var die in _dice)
                die.Roll();
            for (int i = 0; i < DiceCount; i++)
                _dicePbs[i].Image = DieFace.GetImage(_dice[i].Value);
            _session.CurrentPlayer.RollsRemaining = 2;
            _btnRoll.Enabled = true;
            _btnEndTurn.Enabled = true;
            SendLedCommand();
            UpdateRollsLabel();
        }
        private void OnRollClicked(object? sender, EventArgs e)
        {
            if (!_gameStarted || !_tbName.Enabled || !_pbDie.Enabled) return;
            Player current = _session!.CurrentPlayer;
            if (current.RollsRemaining <= 0) return;
            for (int i = 0; i < DiceCount; i++)
            {
                if (!_dice[i].AllowRoll) continue;
                _dice[i].Roll();
                _dicePbs[i].Image = DieFace.GetImage(_dice[i].Value);
            }
            current.RollsRemaining--;
            if (current.RollsRemaining <= 0)
                _btnRoll.Enabled = false;
            UpdateRollsLabel();
            UpdateGameStatus();
            SendLedCommand();
        }
        private void OnEndTurnClicked(object? sender, EventArgs e)
        {
            if (!_gameStarted || _session == null) return;
            Player current = _session.CurrentPlayer;
            int turnScore = Scoring.SumAll(_dice);
            current.AddScore(turnScore);
            string diceStr = string.Join(", ", _dice.Select(d => d.Value));
            MessageBox.Show(
                $"{current.Name} scored {turnScore} points!\n" +
                $"(Dice: {diceStr})\nTotal: {current.TotalScore}",
                "Turn Score", MessageBoxButtons.OK, MessageBoxIcon.Information);
            for (int i = 0; i < DiceCount; i++)
            {
                _diceChecks[i].Checked = true;
                _dice[i].AllowRoll = true;
            }
            SendLedCommand();
            _session.AdvanceTurn();
            if (_session.GameOver)
            {
                EndGame();
                return;
            }
            ResetForNewTurn();
            UpdateGameStatus();
            UpdateScoreboard();
        }
        private void EndGame()
        {
            _gameStarted = false;
            _btnRoll.Enabled = false;
            _btnEndTurn.Enabled = false;
            for (int i = 0; i < DiceCount; i++)
            {
                _diceChecks[i].Checked = true;
                _dice[i].AllowRoll = true;
            }
            SendLedCommand();
            MessageBox.Show(_session!.GetEndGameSummary(), "Game Over!",
                MessageBoxButtons.OK, MessageBoxIcon.Information);
            _lblGameStatus.Text = "Game over! Press New Game to play again.";
            UpdateScoreboard();
        }
        private void UpdateGameStatus()
        {
            if (!_gameStarted || _session == null) return;
            string diceStr = string.Join("  ", _dice.Select(d => $"[{d.Value}]"));
            _lblGameStatus.Text = _session.GetTurnStatus() + $"\nDice: {diceStr}";
        }
        private void UpdateRollsLabel()
        {
            if (!_gameStarted || _session == null)
            {
                _lblRollsLeft.Text = "";
                return;
            }
            int r = _session.CurrentPlayer.RollsRemaining;
            _lblRollsLeft.Text = $"Rolls remaining: {r}";
        }
        private void UpdateScoreboard()
        {
            if (_session == null) { _lblScoreboard.Text = ""; return; }
            _lblScoreboard.Text = _session.GetScoreboard();
        }
        private static string? ShowInputDialog(
            string prompt, string title, string defaultValue)
        {
            using var form = new Form
            {
                Text = title,
                StartPosition = FormStartPosition.CenterParent,
                ClientSize = new Size(320, 110),
                FormBorderStyle = FormBorderStyle.FixedDialog,
                MaximizeBox = false,
                MinimizeBox = false
            };
            var lbl = new Label
            {
                Text = prompt, Left = 12, Top = 12,
                Width = 296, AutoSize = false
            };
            var tb = new TextBox
            {
                Text = defaultValue, Left = 12, Top = 38, Width = 296
            };
            tb.SelectAll();
            var btnOk = new Button
            {
                Text = "OK", DialogResult = DialogResult.OK,
                Left = 148, Top = 70, Width = 76
            };
            var btnCancel = new Button
            {
                Text = "Cancel", DialogResult = DialogResult.Cancel,
                Left = 232, Top = 70, Width = 76
            };
            form.Controls.AddRange(new Control[] { lbl, tb, btnOk, btnCancel });
            form.AcceptButton = btnOk;
            form.CancelButton = btnCancel;
            return form.ShowDialog() == DialogResult.OK
                ? tb.Text.Trim() : null;
        }
        private void OnFormClosing(object? sender, FormClosingEventArgs e)
        {
            if (_serialPort != null && _serialPort.IsOpen)
            {
                try { _serialPort.WriteLine("LED:00"); } catch { }
            }
            CloseSerialPort();
            DieFace.ClearCache();
        }
    }
}
```
