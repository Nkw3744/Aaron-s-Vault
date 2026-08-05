# Lab 7 Scoring

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Scoring.cs`

```csharp
using System.Collections.Generic;

namespace AaronYatzeeSimpleScoring
{
    public static class Scoring
    {
        // Simple scoring rule: a turn scores the sum of all five dice.
        public static int SumDice(List<Die> dice)
        {
            int total = 0;
            foreach (Die die in dice)
            {
                total += die.Value;
            }

            return total;
        }
    }
}
```
