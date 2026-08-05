# Lab 7 Die

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Die.cs`

```csharp
using System;

namespace AaronYatzeeSimpleScoring
{
    public class Die
    {
        public int Value { get; private set; }

        public void Roll(Random rng)
        {
            Value = rng.Next(1, 7);
        }
    }
}
```
