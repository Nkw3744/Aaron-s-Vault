# Lab 8 Die

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Die.cs` · [[File Handling and Serial Ports]] · [[GUI and Event-Driven Programming]]

```csharp
using System;

namespace ExampleDieRollerGUI
{
    public sealed class Die
    {
        public int Value { get; private set; }
        public bool AllowRoll { get; set; } = true;

        private readonly Random _rng;

        public Die(Random rng)
        {
            _rng = rng;
            Roll();
        }

        public void Roll()
        {
            if (!AllowRoll)
            {
                return;
            }

            Value = _rng.Next(1, 7);
        }
    }
}
```
