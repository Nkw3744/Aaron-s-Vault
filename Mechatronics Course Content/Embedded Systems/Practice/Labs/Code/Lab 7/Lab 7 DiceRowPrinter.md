# Lab 7 DiceRowPrinter

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `DiceRowPrinter.cs`

```csharp
using System;
using System.Collections.Generic;

namespace AaronYatzeeSimpleScoring
{
    public static class DiceRowPrinter
    {
        public static void PrintDiceRow(List<Die> dice)
        {
            const int LinesPerDie = 5;
            const string Gap = "   ";

            for (int line = 0; line < LinesPerDie; line++)
            {
                for (int i = 0; i < dice.Count; i++)
                {
                    string[] face = DieFace.GetLines(dice[i].Value);
                    Console.Write(face[line]);

                    if (i < dice.Count - 1)
                    {
                        Console.Write(Gap);
                    }
                }

                Console.WriteLine();
            }
        }
    }
}
```
