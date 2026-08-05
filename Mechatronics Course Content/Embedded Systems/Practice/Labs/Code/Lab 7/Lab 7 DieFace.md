# Lab 7 DieFace

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `DieFace.cs`

```csharp
namespace AaronYatzeeSimpleScoring
{
    public static class DieFace
    {
        public static string[] GetLines(int value)
        {
            switch (value)
            {
                case 1: return new[] { "+---+", "|   |", "| o |", "|   |", "+---+" };
                case 2: return new[] { "+---+", "|o  |", "|   |", "|  o|", "+---+" };
                case 3: return new[] { "+---+", "|o  |", "| o |", "|  o|", "+---+" };
                case 4: return new[] { "+---+", "|o o|", "|   |", "|o o|", "+---+" };
                case 5: return new[] { "+---+", "|o o|", "| o |", "|o o|", "+---+" };
                case 6: return new[] { "+---+", "|o o|", "|o o|", "|o o|", "+---+" };
                default: return new[] { "?????", "?????", "?????", "?????", "?????" };
            }
        }
    }
}
```
