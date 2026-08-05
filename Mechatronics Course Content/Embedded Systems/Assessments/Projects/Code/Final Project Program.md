# Final Project Program

> [!info] Course material
> [[Final Project Overview|Back]] · Source: `Program.cs`

```csharp
using System;
using System.Windows.Forms;

namespace FinalProject
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
