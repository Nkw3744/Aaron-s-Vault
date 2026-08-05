# Final Project HelpForm

> [!info] Course material
> [[Final Project Overview|Back]] · Source: `HelpForm.cs`

```csharp
using System;
using System.Drawing;
using System.Windows.Forms;

namespace FinalProject
{
    /// <summary>
    /// Scrollable help dialog explaining how to use the GUI in simulator and hardware modes.
    /// </summary>
    public class HelpForm : Form
    {
        public HelpForm()
        {
            Text            = "Laser Cutter Safety Panel — Help";
            Size            = new Size(680, 700);
            MinimumSize     = new Size(520, 400);
            StartPosition   = FormStartPosition.CenterParent;
            BackColor       = Color.White;
            ForeColor       = Color.Black;
            FormBorderStyle = FormBorderStyle.Sizable;

            var rtb = new RichTextBox
            {
                Dock        = DockStyle.Fill,
                ReadOnly    = true,
                BackColor   = Color.White,
                ForeColor   = Color.Black,
                Font        = new Font("Segoe UI", 10),
                BorderStyle = BorderStyle.None,
                ScrollBars  = RichTextBoxScrollBars.Vertical,
                Padding     = new Padding(8)
            };

            var closeBtn = new Button
            {
                Text      = "Close",
                Dock      = DockStyle.Bottom,
                Height    = 34,
                BackColor = SystemColors.Control,
                ForeColor = SystemColors.ControlText,
                FlatStyle = FlatStyle.Flat
            };
            closeBtn.Click += (s, e) => Close();

            Controls.Add(rtb);
            Controls.Add(closeBtn);

            BuildContent(rtb);
            rtb.SelectionStart = 0;
            rtb.ScrollToCaret();
        }

        private static void H(RichTextBox r, string text)
        {
            r.SelectionStart  = r.TextLength;
            r.SelectionLength = 0;
            r.SelectionFont   = new Font("Segoe UI", 12, FontStyle.Bold);
            r.SelectionColor  = Color.FromArgb(20, 95, 160);
            r.AppendText("\n" + text + "\n");
        }

        private static void Sub(RichTextBox r, string text)
        {
            r.SelectionStart  = r.TextLength;
            r.SelectionLength = 0;
            r.SelectionFont   = new Font("Segoe UI", 10, FontStyle.Bold);
            r.SelectionColor  = Color.FromArgb(0, 120, 0);
            r.AppendText(text + "\n");
        }

        private static void P(RichTextBox r, string text)
        {
            r.SelectionStart  = r.TextLength;
            r.SelectionLength = 0;
            r.SelectionFont   = new Font("Segoe UI", 10);
            r.SelectionColor  = Color.Black;
            r.AppendText(text + "\n");
        }

        private static void Row(RichTextBox r, string label, string desc)
        {
            r.SelectionStart  = r.TextLength;
            r.SelectionLength = 0;
            r.SelectionFont   = new Font("Segoe UI", 10, FontStyle.Bold);
            r.SelectionColor  = Color.Black;
            r.AppendText("  " + label.PadRight(28));

            r.SelectionStart  = r.TextLength;
            r.SelectionLength = 0;
            r.SelectionFont   = new Font("Segoe UI", 10);
            r.SelectionColor  = Color.Black;
            r.AppendText(desc + "\n");
        }

        private static void Warn(RichTextBox r, string text)
        {
            r.SelectionStart  = r.TextLength;
            r.SelectionLength = 0;
            r.SelectionFont   = new Font("Segoe UI", 10, FontStyle.Italic);
            r.SelectionColor  = Color.FromArgb(170, 90, 0);
            r.AppendText(text + "\n");
        }

        private void BuildContent(RichTextBox r)
        {
            H(r, "Purpose");
            P(r, "This panel is for real-hardware operation of the lab-board laser safety simulator.");
            P(r, "Workflow: connect board -> confirm dewpoint safety -> check door/track alarms -> run thermal control.");

            H(r, "Quick Start (Current Setup)");
            P(r, "1. Power the lab board and connect the board COM port.");
            P(r, "2. Set baud to 38400 and click Connect. Serial LED must turn green.");
            P(r, "3. Check Dewpoint Safety: watch Humidity, Head Temp, Dew Point, Margin, and status LEDs.");
            P(r, "4. Confirm door and track warnings are clear before laser run.");
            P(r, "5. Use setpoint + PI tuning while heater follows Pot1 and chiller power follows PI output.");

            H(r, "1) Machine Startup");
            Row(r, "COM Port", "Select the physical board COM port.");
            Row(r, "Baud", "Use 38400 unless firmware was changed.");
            Row(r, "Connect", "Opens UART and sends TXCHECK.");
            Row(r, "Disconnect", "Stops updates and sends safe output shutdown.");
            Row(r, "DB Connect", "Optional MySQL connection for logging.");

            H(r, "2) Dewpoint Safety Check");
            Row(r, "Humidity Input % (Pot2/ADC1)", "Live humidity source from board Pot2.");
            Row(r, "Dew point override", "Manual dewpoint test value sent to firmware.");
            Row(r, "Margin", "Head temp - dew point (core safety metric).");
            Row(r, "Status LEDs", "Safe / Caution / High Risk states.");
            Warn(r, "Do not enable laser when High Risk is active.");

            H(r, "3) Door and Track-Limit Warnings");
            Row(r, "Laser enable switch", "Live state of SW0 / PA0.");
            Row(r, "Door interlock switch", "Live state of SW1 / PA1.");
            Row(r, "Track limit warning", "From TSWB alarm flag; clear using TSWB centre on board.");
            P(r, "You are using physical board switches, not software simulator buttons.");

            H(r, "4) Laser Thermal Control");
            Row(r, "Setpoint", "Target head temperature.");
            Row(r, "Kp, Ki", "PI fan tuning.");
            Row(r, "Laser Heat Request % (Pot1/ADC2)", "Heater demand from Pot1.");
            Row(r, "Water Chiller Power % (Fan Power%)", "Cooling command from PI loop.");
            Row(r, "Laser run trend", "Chart of actual temperature versus setpoint.");

            H(r, "Board Diagnostics (Read-only)");
            Row(r, "PC2 Laser source power", "Indicator tied to laser-enable state.");
            Row(r, "PC3-PC7 Lamp bar", "Firmware-driven lamp/power bar segments.");
            Row(r, "PINA LEDs", "Raw PA0-PA7 input states.");
            Row(r, "7-segment safety code", "GO = safe, EH = caution, nO = unsafe.");
            Row(r, "Refresh", "Manual readout refresh.");

            H(r, "Data Logging");
            Row(r, "Rows + Insert", "Manual insert count and one-shot insert.");
            Row(r, "Enable / Stop", "Continuous logging toggle.");
            Warn(r, "Logging requires successful DB connection.");

            H(r, "Current Hardware Mapping Summary");
            P(r, "Inputs: PA0/PA1 switches, Pot1/Pot2, ADC temp/light.");
            P(r, "Outputs: fan/heater PWM, lamp output, risk LEDs, lamp bar LEDs, 7-seg safety code, LCD safety text.");
        }
    }
}
```
