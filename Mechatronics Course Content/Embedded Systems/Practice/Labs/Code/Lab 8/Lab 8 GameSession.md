# Lab 8 GameSession

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `GameSession.cs` · [[File Handling and Serial Ports]] · [[GUI and Event-Driven Programming]]

```csharp
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace ExampleDieRollerGUI
{
    public class GameSession
    {
        public List<Player> Players { get; private set; } = new List<Player>();
        public int CurrentPlayerIndex { get; private set; } = 0;
        public int CurrentRound { get; private set; } = 1;
        public int TotalRounds { get; private set; } = 3;
        public bool GameOver { get; private set; } = false;

        public Player CurrentPlayer => Players[CurrentPlayerIndex];

        public GameSession(List<Player> players, int totalRounds)
        {
            Players = players;
            TotalRounds = totalRounds;
            CurrentPlayerIndex = 0;
            CurrentRound = 1;
            GameOver = false;
        }

        public void AdvanceTurn()
        {
            CurrentPlayerIndex++;

            if (CurrentPlayerIndex >= Players.Count)
            {
                CurrentPlayerIndex = 0;
                CurrentRound++;
            }

            if (CurrentRound > TotalRounds)
            {
                GameOver = true;
            }
        }

        public string GetScoreboard()
        {
            var lines = Players
                .OrderByDescending(p => p.TotalScore)
                .Select(p => $"{p.Name,-14} {p.TotalScore,5} pts");

            return "--- Scoreboard ---\n" + string.Join("\n", lines);
        }

        public List<Player> GetWinners()
        {
            int maxScore = Players.Max(p => p.TotalScore);
            return Players.Where(p => p.TotalScore == maxScore).ToList();
        }

        public string GetEndGameSummary()
        {
            string results = "=== FINAL SCORES ===\n\n";

            foreach (var p in Players.OrderByDescending(p => p.TotalScore))
                results += $"  {p.Name,-14} {p.TotalScore,5} pts\n";

            results += "\n";

            var winners = GetWinners();
            if (winners.Count == 1)
                results += $"Winner: {winners[0].Name}!";
            else
                results += $"Tie: {string.Join(", ", winners.Select(w => w.Name))}";

            return results;
        }

        public string GetTurnStatus()
        {
            if (GameOver) return "Game over!";
            return $"Round {CurrentRound}/{TotalRounds} — {CurrentPlayer.Name}'s turn";
        }
    }
}
```
