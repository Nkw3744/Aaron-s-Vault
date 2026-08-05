# Lab 8 Program

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Program.cs` · [[File Handling and Serial Ports]] · [[GUI and Event-Driven Programming]]

```csharp
using System;
using System.Windows.Forms;

namespace ExampleDieRollerGUI
{
    internal static class Program
    {
        [STAThread]
        private static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }
}
```
