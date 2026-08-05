# Lab 8 Player

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Player.cs` · [[File Handling and Serial Ports]] · [[GUI and Event-Driven Programming]]

```csharp
namespace ExampleDieRollerGUI
{
    public class Player
    {
        public string Name { get; set; }
        public int TotalScore { get; private set; }
        public int RollsRemaining { get; set; }

        public Player(string name)
        {
            Name = name;
            TotalScore = 0;
            RollsRemaining = 3;
        }

        public void AddScore(int points)
        {
            TotalScore += points;
        }

        public void ResetRolls()
        {
            RollsRemaining = 3;
        }

        public override string ToString()
        {
            return $"{Name}: {TotalScore} pts";
        }
    }
}
```
