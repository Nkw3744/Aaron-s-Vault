# Final Project LaserSimContract

> [!info] Course material
> [[Final Project Overview|Back]] · Source: `LaserSimContract.cs`

```csharp
namespace FinalProject
{
    /// <summary>
    /// Shared protocol and classification constants for Laser Simulator data.
    /// Keep this in sync with the MCU firmware command handlers.
    /// </summary>
    internal static class LaserSimContract
    {
        // Baseline instructions
        public const byte TxCheck   = 0x00;
        public const byte ReadPina  = 0x01;
        public const byte ReadPot1  = 0x02;
        public const byte ReadPot2  = 0x03;
        public const byte ReadTemp  = 0x04;
        public const byte ReadLight = 0x05;
        public const byte SetPortc  = 0x0A;
        public const byte SetHeater = 0x0B;
        public const byte SetLight  = 0x0C;
        public const byte SetMotor  = 0x0D;

        // Piece 7 read extensions
        public const byte ReadSimMargin  = 0x10;
        public const byte ReadSimStatus  = 0x11;
        public const byte ReadSimDewpt   = 0x13;
        public const byte ReadSimPower   = 0x14;
        public const byte ReadSimFan     = 0x15;
        public const byte ReadAlarmFlags = 0x16;
        public const byte SetSimDewpt    = 0xF0;
        public const byte ClearSimDewpt  = 0xF1;

        // Classification thresholds in degree C.
        public const double SafeMarginC = 3.0;
        public const double MarginalMarginC = 0.0;

        // Alarm bits from ReadAlarmFlags
        public const int AlarmDoorFault = 1 << 0;
        public const int AlarmAxisAlarm = 1 << 1;
        public const int AlarmOvertemp = 1 << 2;

        // Wire encoding constants
        private const int MarginByteOffset = 100;

        public static double DecodeMargin(byte raw)
        {
            return (raw - MarginByteOffset) / 10.0;
        }

        public static byte EncodeMargin(double marginC)
        {
            int encoded = (int)System.Math.Round(marginC * 10.0) + MarginByteOffset;
            if (encoded < 0) encoded = 0;
            if (encoded > 255) encoded = 255;
            return (byte)encoded;
        }

        public static double DecodeDewPoint(byte raw)
        {
            return raw / 2.0;
        }

        public static byte EncodeDewPoint(double dewPointC)
        {
            int encoded = (int)System.Math.Round(dewPointC * 2.0);
            if (encoded < 0) encoded = 0;
            if (encoded > 255) encoded = 255;
            return (byte)encoded;
        }

        public static int ClassifyStatus(double marginC)
        {
            if (marginC >= SafeMarginC) return 0;
            if (marginC >= MarginalMarginC) return 1;
            return 2;
        }
    }
}
```
