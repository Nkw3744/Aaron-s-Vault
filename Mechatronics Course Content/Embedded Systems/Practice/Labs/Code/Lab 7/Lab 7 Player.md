# Lab 7 Player

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Player.cs`

```csharp
namespace AaronYatzeeSimpleScoring
{
    public class Player
    {
        public string Name { get; }
        public int TotalScore { get; private set; }

        public Player(string name)
        {
            Name = name;
        }

        public void AddScore(int points)
        {
            TotalScore += points;
        }
    }
}
```
