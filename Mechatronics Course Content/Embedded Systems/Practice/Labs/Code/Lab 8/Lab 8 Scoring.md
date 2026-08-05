# Lab 8 Scoring

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Scoring.cs` · [[File Handling and Serial Ports]] · [[GUI and Event-Driven Programming]]

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace ExampleDieRollerGUI
{
    public static class Scoring
    {
        public static int SumAll(List<Die> dice)
        {
            return dice.Sum(d => d.Value);
        }

        public static byte GetLedByte(List<Die> dice, CheckBox[] checks)
        {
            byte result = 0;
            for (int i = 0; i < checks.Length && i < 5; i++)
            {
                if (!checks[i].Checked)
                    result |= (byte)(1 << i);
            }
            return result;
        }
    }
}
```
