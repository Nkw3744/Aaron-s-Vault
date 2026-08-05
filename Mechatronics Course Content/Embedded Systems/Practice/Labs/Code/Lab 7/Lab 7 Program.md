# Lab 7 Program

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Program.cs`

```csharp
using System;
using System.Collections.Generic;

namespace AaronYatzeeSimpleScoring
{
    class Program
    {
        private const int DiceCount = 5;
        private const int RollsPerTurn = 3;
        private const int MaxPlayers = 5;

        static void Main(string[] args)
        {
            Random rng = new Random();

            Console.WriteLine("=== Yatzee ===");
            Console.WriteLine("Each turn rolls 5 dice. Score = sum of dice.");
            Console.WriteLine();

            List<Player> players = ReadPlayers();
            int rounds = ReadPositiveInt("How many rounds? ", min: 1);

            for (int round = 1; round <= rounds; round++)
            {
                foreach (Player player in players)
                {
                    PlayOneTurn(player, rng, round, rounds);
                }
            }

            PrintFinalScoreboard(players);
        }

        private static void PlayOneTurn(Player player, Random rng, int round, int totalRounds)
        {
            Console.WriteLine();
            Console.WriteLine($"--- Round {round}/{totalRounds}, {player.Name}'s turn ---");

            List<Die> dice = NewDiceSet();

            // Roll 1: roll all dice.
            RollAll(dice, rng);
            DiceRowPrinter.PrintDiceRow(dice);

            // Rolls 2 and 3: re-roll only the dice the player chooses.
            for (int rollNumber = 2; rollNumber <= RollsPerTurn; rollNumber++)
            {
                Console.WriteLine();
                List<int> indices = ReadRerollIndices();
                ReRoll(dice, rng, indices);
                DiceRowPrinter.PrintDiceRow(dice);
            }

            int turnScore = Scoring.SumDice(dice);
            player.AddScore(turnScore);

            Console.WriteLine();
            Console.WriteLine($"{player.Name} scored {turnScore} this turn. Total: {player.TotalScore}");
            Console.WriteLine("Press Enter for next turn...");
            Console.ReadLine();
        }

        private static List<Die> NewDiceSet()
        {
            List<Die> dice = new List<Die>();
            for (int i = 0; i < DiceCount; i++)
            {
                dice.Add(new Die());
            }

            return dice;
        }

        private static void RollAll(List<Die> dice, Random rng)
        {
            foreach (Die die in dice)
            {
                die.Roll(rng);
            }
        }

        private static void ReRoll(List<Die> dice, Random rng, List<int> indices)
        {
            foreach (int index in indices)
            {
                dice[index].Roll(rng);
            }
        }

        private static void PrintFinalScoreboard(List<Player> players)
        {
            Console.WriteLine();
            Console.WriteLine("=== Final scoreboard ===");
            foreach (Player p in players)
            {
                Console.WriteLine($"  {p.Name,-20} {p.TotalScore,5}");
            }

            Console.WriteLine();
            Console.WriteLine("Thanks for playing!");
        }

        private static List<Player> ReadPlayers()
        {
            while (true)
            {
                Console.Write($"Number of players (1-{MaxPlayers})? ");
                string? line = Console.ReadLine();

                if (int.TryParse(line, out int count) && count >= 1 && count <= MaxPlayers)
                {
                    List<Player> players = new List<Player>();
                    for (int i = 1; i <= count; i++)
                    {
                        Console.Write($"Name for player {i}? ");
                        string? name = Console.ReadLine();

                        if (string.IsNullOrWhiteSpace(name))
                        {
                            name = $"Player {i}";
                        }

                        players.Add(new Player(name.Trim()));
                    }

                    return players;
                }

                Console.WriteLine($"Please enter a number from 1 to {MaxPlayers}.");
            }
        }

        private static int ReadPositiveInt(string prompt, int min)
        {
            while (true)
            {
                Console.Write(prompt);
                string? line = Console.ReadLine();

                if (int.TryParse(line, out int value) && value >= min)
                {
                    return value;
                }

                Console.WriteLine($"Please enter a whole number >= {min}.");
            }
        }

        // Reads digits 1-5 to choose which dice to re-roll. Empty line keeps all.
        private static List<int> ReadRerollIndices()
        {
            while (true)
            {
                Console.Write("Dice to re-roll (e.g. 135), or Enter to keep all: ");
                string? line = Console.ReadLine();

                if (string.IsNullOrWhiteSpace(line))
                {
                    return new List<int>();
                }

                List<int> indices = new List<int>();
                bool valid = true;

                foreach (char c in line.Trim())
                {
                    if (c >= '1' && c <= '5')
                    {
                        int index = c - '1';
                        if (!indices.Contains(index))
                        {
                            indices.Add(index);
                        }
                    }
                    else
                    {
                        valid = false;
                        break;
                    }
                }

                if (valid)
                {
                    return indices;
                }

                Console.WriteLine("Please use only digits 1-5 (e.g. 24 or 135).");
            }
        }
    }
}
```
