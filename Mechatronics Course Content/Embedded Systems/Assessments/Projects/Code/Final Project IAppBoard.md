# Final Project IAppBoard

> [!info] Course material
> [[Final Project Overview|Back]] · Source: `IAppBoard.cs` · [[Virtual Override Abstract and Sealed]]

```csharp
namespace FinalProject
{
    /// <summary>
    /// Interface for the application board (real hardware or simulator).
    /// </summary>
    public interface IAppBoard
    {
        bool IsConnected { get; }
        void Connect();
        void Disconnect();
        void Dispose();
        bool Ping();

        byte ReadPINA();
        byte ReadPot1();
        byte ReadPot2();
        byte ReadTemp();
        byte ReadLight();

        bool WritePORTC(byte value);
        bool WriteMotorOCR(ushort ocrValue);
        bool WriteMotorPercent(double percent);
        bool WriteLampOCR(ushort ocrValue);
        bool WriteLampPercent(double percent);
        bool WriteHeaterOCR(ushort ocrValue);
        bool WriteHeaterPercent(double percent);

        // Laser simulator extension opcodes (0x10–0x16, requires Piece 7 firmware)
        double ReadSimMargin();     // condensation margin °C (positive = safe headroom)
        int    ReadSimStatus();     // 0 = Safe (>=3 C), 1 = Marginal (>=0 C), 2 = High Risk (<0 C)
        double ReadSimDewPoint();   // dew point °C
        int    ReadSimPower();      // laser power setpoint 0–100 %
        int    ReadSimFan();        // fan duty cycle 0–100 %
        int    ReadAlarmFlags();    // bit 0 = door_fault, bit 1 = axis_alarm
        bool   WriteSimDewPoint(double dewPointC); // host override, half-degree steps
        bool   ClearSimDewPointOverride();
    }
}
```
