# Lab 8 Prompt

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Prompt.cs`

```csharp
namespace ExampleDieRollerGUI
{
    /// <summary>
    /// Tiny modal input dialog used for player setup.
    /// Keeps things WinForms-only (no extra packages).
    /// </summary>
    public static class Prompt
    {
        public static string? Ask(string title, string message, string defaultValue = "")
        {
            using var form = new Form
            {
                Width = 380,
                Height = 170,
                Text = title,
                FormBorderStyle = FormBorderStyle.FixedDialog,
                StartPosition = FormStartPosition.CenterParent,
                MaximizeBox = false,
                MinimizeBox = false,
            };

            var lbl = new Label
            {
                Left = 12,
                Top = 12,
                AutoSize = true,
                Text = message,
            };

            var tb = new TextBox
            {
                Left = 12,
                Top = 40,
                Width = 340,
                Text = defaultValue,
            };

            var ok = new Button
            {
                Text = "OK",
                Left = 200,
                Top = 80,
                Width = 70,
                DialogResult = DialogResult.OK,
            };

            var cancel = new Button
            {
                Text = "Cancel",
                Left = 280,
                Top = 80,
                Width = 70,
                DialogResult = DialogResult.Cancel,
            };

            form.Controls.Add(lbl);
            form.Controls.Add(tb);
            form.Controls.Add(ok);
            form.Controls.Add(cancel);
            form.AcceptButton = ok;
            form.CancelButton = cancel;
            tb.SelectAll();

            DialogResult result = form.ShowDialog();
            return result == DialogResult.OK ? tb.Text : null;
        }

        public static int AskInt(string title, string message, int min, int max, int defaultValue)
        {
            while (true)
            {
                string? answer = Ask(title, $"{message} ({min}-{max})", defaultValue.ToString());

                // Treat Cancel as "use default" so the user is never stuck.
                if (answer == null)
                {
                    return defaultValue;
                }

                if (int.TryParse(answer.Trim(), out int n) && n >= min && n <= max)
                {
                    return n;
                }

                MessageBox.Show(
                    $"Please enter an integer between {min} and {max}.",
                    title,
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Warning);
            }
        }
    }
}
```
