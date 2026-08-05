# Final Project SimulatorBoard

> [!info] Course material
> [[Final Project Overview|Back]] · Source: `SimulatorBoard.cs`

```csharp
using System;

namespace FinalProject
{
    /// <summary>
    /// Simulates the AT90USB1287 board for testing the GUI without hardware.
    /// The Virtual Lab Board panel can override any input via the Set* methods.
    /// </summary>
    public class SimulatorBoard : IAppBoard, IDisposable
    {
        private bool _connected;
        private readonly Random _rnd = new Random();

        // Core simulated state
        private byte _portc;
        private double _lampPercent;
        private double _heaterPercent;
        private double _motorPercent;
        private double _simTemp = 25.0;      // °C  — laser head surface temperature
        private double _simPot1 = 2.5;       // 0–5 V  (laser power setpoint, ~50 %)
        private double _simPot2 = 4.5;       // 0–5 V  (ambient RH ~90 % — starts near Safe/Marginal boundary)
        private double _simPhaseTime = 0.0;  // seconds — drives the auto-cycle phase state machine
        private DateTime _lastUpdate = DateTime.UtcNow;

        // Virtual Lab Board overrides — set from the side panel
        private bool? _manualSW0 = null;     // null = auto-cycle; non-null = user override
        private bool? _manualSW1 = null;
        private bool _pot1Manual = false;    // when true, skip random drift for Pot1
        private bool _pot2Manual = false;    // when true, skip random drift for Pot2
        private double? _tempOverride = null; // when set, locks _simTemp to this value
        private bool _axisAlarm = false;     // forced axis-alarm flag from virtual panel

        // Auto-cycle phase sequence — each slot lasts 5 s.
        // Demonstrates IDLE → LASER_ON (×3) → FAULT (brief) → LASER_ON → IDLE.
        private static readonly (bool sw0, bool sw1)[] _phaseSequence =
        {
            (false, false), // IDLE       (0 – 5 s)
            (true,  false), // LASER_ON   (5 – 10 s)
            (true,  false), // LASER_ON   (10 – 15 s)
            (true,  false), // LASER_ON   (15 – 20 s)
            (true,  true),  // FAULT      (20 – 25 s)
            (true,  false), // LASER_ON   (25 – 30 s)
            (false, false), // IDLE       (30 – 35 s)
        };

        public bool IsConnected => _connected;

        // ── Virtual Lab Board public setters ────────────────────────────────────

        /// <summary>Set Pot1 voltage (0–5 V) directly; disables random drift.</summary>
        public void SetPot1Voltage(double v)
        {
            _simPot1 = Math.Max(0, Math.Min(5, v));
            _pot1Manual = true;
        }

        /// <summary>Set Pot2 voltage (0–5 V) directly; disables random drift.</summary>
        public void SetPot2Voltage(double v)
        {
            _simPot2 = Math.Max(0, Math.Min(5, v));
            _pot2Manual = true;
        }

        /// <summary>Manually set SW0 (LASER ON) and SW1 (DOOR OPEN); overrides auto-cycle.</summary>
        public void SetSwitches(bool sw0, bool sw1)
        {
            _manualSW0 = sw0;
            _manualSW1 = sw1;
        }

        /// <summary>Return to the auto-cycle phase state machine.</summary>
        public void SetSwitchAutoMode()
        {
            _manualSW0 = null;
            _manualSW1 = null;
        }

        /// <summary>Override surface temperature. Pass null to re-enable the thermal model.</summary>
        public void SetTempOverride(double? tempC) => _tempOverride = tempC;

        /// <summary>Force-set the axis alarm flag for testing the Laser Sim alarm display.</summary>
        public void SetAxisAlarm(bool active) => _axisAlarm = active;

        /// <summary>Expose current simulated surface temperature for syncing the virtual panel display.</summary>
        public double SimTemp => _simTemp;

        /// <summary>
        /// Effective “room air” temperature (°C) used in dew-point and thermal equilibrium.
        /// In simulator mode, PC3–PC7 on PORTC nudge this value (see GUI labels).
        /// </summary>
        public double SimAmbientRoomC => AmbientFromPortc(_portc);

        // ── IAppBoard connection ─────────────────────────────────────────────────

        public static string[] GetAvailablePorts()
        {
            var ports = AppBoard.GetAvailablePorts();
            var list = new string[ports.Length + 1];
            list[0] = "Simulator";
            Array.Copy(ports, 0, list, 1, ports.Length);
            return list;
        }

        public void Connect()
        {
            _connected = true;
            _lastUpdate = DateTime.UtcNow;
        }

        public void Disconnect() => _connected = false;

        public void Dispose() => _connected = false;

        public bool Ping() => _connected;

        // ── Sensor reads ─────────────────────────────────────────────────────────

        public byte ReadPINA()
        {
            // Bits 0 and 1: SW0 (PA0 = LASER ON) and SW1 (PA1 = DOOR OPEN).
            var (sw0, sw1) = GetCurrentSwitches();
            byte result = (byte)((sw0 ? 1 : 0) | (sw1 ? 2 : 0));
            // Upper 6 bits: random noise simulating unconnected PORTA pins.
            result |= (byte)(_rnd.Next(0, 64) << 2);
            return result;
        }

        public byte ReadPot1()
        {
            AdvanceSimulation();
            return VoltageToByte(_simPot1);
        }

        public byte ReadPot2()
        {
            AdvanceSimulation();
            return VoltageToByte(_simPot2);
        }

        public byte ReadTemp()
        {
            AdvanceSimulation();
            double v = Math.Max(0, Math.Min(5, _simTemp * 0.05));
            return VoltageToByte(v);
        }

        public byte ReadLight()
        {
            AdvanceSimulation();
            double v = _lampPercent / 100.0 * 5.0 + (_rnd.NextDouble() - 0.5) * 0.2;
            return VoltageToByte(Math.Max(0, Math.Min(5, v)));
        }

        // ── Actuator writes ──────────────────────────────────────────────────────

        public bool WritePORTC(byte value) { _portc = value; return true; }

        public bool WriteMotorOCR(ushort ocrValue)
        {
            _motorPercent = Math.Min(100.0, ocrValue * 100.0 / 399.0);
            return true;
        }

        public bool WriteMotorPercent(double percent)
        {
            _motorPercent = Math.Max(0, Math.Min(100, percent));
            return true;
        }

        public bool WriteLampOCR(ushort ocrValue)
        {
            _lampPercent = Math.Min(100.0, ocrValue * 100.0 / 399.0);
            return true;
        }

        public bool WriteLampPercent(double percent)
        {
            _lampPercent = Math.Max(0, Math.Min(100, percent));
            return true;
        }

        public bool WriteHeaterOCR(ushort ocrValue)
        {
            _heaterPercent = Math.Min(100.0, ocrValue * 100.0 / 399.0);
            return true;
        }

        public bool WriteHeaterPercent(double percent)
        {
            _heaterPercent = Math.Max(0, Math.Min(100, percent));
            return true;
        }

        // ── Laser simulator extension reads (opcodes 0x10–0x16) ──────────────────

        public double ReadSimMargin()
        {
            AdvanceSimulation();
            double margin = _simTemp - ComputeDewPoint();
            byte wire = LaserSimContract.EncodeMargin(margin);
            return LaserSimContract.DecodeMargin(wire);
        }

        public int ReadSimStatus()
        {
            AdvanceSimulation();
            double margin = _simTemp - ComputeDewPoint();
            return LaserSimContract.ClassifyStatus(margin);
        }

        public double ReadSimDewPoint()
        {
            AdvanceSimulation();
            byte wire = LaserSimContract.EncodeDewPoint(ComputeDewPoint());
            return LaserSimContract.DecodeDewPoint(wire);
        }

        public int ReadSimPower()
        {
            AdvanceSimulation();
            return (int)Math.Round(_simPot1 / 5.0 * 100.0);
        }

        public int ReadSimFan() => (int)Math.Round(_motorPercent);

        public int ReadAlarmFlags()
        {
            var (sw0, sw1) = GetCurrentSwitches();
            int flags = (sw0 && sw1) ? LaserSimContract.AlarmDoorFault : 0;
            if (_axisAlarm) flags |= LaserSimContract.AlarmAxisAlarm;
            return flags;
        }

        public bool WriteSimDewPoint(double dewPointC)
        {
            // Keep simulator interface-compatible; adjust Pot2 so modeled RH tracks dew intent loosely.
            double clamped = Math.Max(0.0, Math.Min(50.0, dewPointC));
            _simPot2 = Math.Max(0.0, Math.Min(5.0, clamped / 10.0));
            _pot2Manual = true;
            return true;
        }

        public bool ClearSimDewPointOverride()
        {
            _pot2Manual = false;
            return true;
        }

        // ── Private helpers ──────────────────────────────────────────────────────

        /// <summary>Returns current switch state: manual override if set, otherwise auto-cycle.</summary>
        private (bool sw0, bool sw1) GetCurrentSwitches()
        {
            if (_manualSW0.HasValue || _manualSW1.HasValue)
                return (_manualSW0 ?? false, _manualSW1 ?? false);
            int slot = (int)(_simPhaseTime / 5.0) % _phaseSequence.Length;
            return _phaseSequence[slot];
        }

        /// <summary>Linear Magnus approximation: Tdew ≈ Tambient − (100 − RH) / 5.</summary>
        private double ComputeDewPoint()
        {
            double rh      = _simPot2 / 5.0 * 100.0;
            double ambient = AmbientFromPortc(_portc);
            return ambient - (100.0 - rh) / 5.0;
        }

        /// <summary>
        /// PORTC bits PC3–PC7 (simulator only) shift the model room-air temperature used for
        /// dew point and passive cooling toward ambient. PC0–PC2 are the lab risk LEDs on hardware;
        /// they do not affect this helper.
        /// </summary>
        private static double AmbientFromPortc(byte portc)
        {
            double t = 22.0;
            if ((portc & (1 << 3)) != 0) t -= 2.0;  // PC3 — extra ventilation / cooler air
            if ((portc & (1 << 4)) != 0) t += 1.5;  // PC4 — warmer enclosure / heat soak
            if ((portc & (1 << 7)) != 0) t -= 1.0;  // PC7 — cold purge assist
            return t;
        }

        private static byte VoltageToByte(double v)
        {
            int b = (int)Math.Round(v * 255.0 / 5.0);
            return (byte)Math.Max(0, Math.Min(255, b));
        }

        private void AdvanceSimulation()
        {
            var now = DateTime.UtcNow;
            double dt = Math.Min((now - _lastUpdate).TotalSeconds, 0.5);
            _lastUpdate = now;

            // Thermal model — skipped when temperature is locked from virtual panel
            if (!_tempOverride.HasValue)
            {
                double ambientEq = AmbientFromPortc(_portc);
                double heaterEffect = _heaterPercent / 100.0 * 8.0 * dt;
                if ((_portc & (1 << 6)) != 0) heaterEffect *= 0.55; // PC6 — laser/heater derate (sim)

                double fanMul = 1.0;
                if ((_portc & (1 << 5)) != 0) fanMul = 1.35;       // PC5 — auxiliary fan assist (sim)
                if ((_portc & (1 << 3)) != 0) fanMul += 0.15;       // PC3 — stacks slightly with PC5

                double fanEffect = _motorPercent / 100.0 * 6.0 * dt * fanMul;
                double cooling   = (_simTemp - ambientEq) * 0.02 * dt;
                if ((_portc & (1 << 7)) != 0) cooling += 0.35 * dt; // PC7 — extra passive purge

                _simTemp += heaterEffect - fanEffect - cooling;
                _simTemp = Math.Max(15, Math.Min(80, _simTemp));
            }
            else
            {
                _simTemp = _tempOverride.Value;
            }

            // Potentiometer random drift — skipped when set manually from virtual panel
            if (!_pot1Manual)
            {
                _simPot1 += (_rnd.NextDouble() - 0.5) * 0.3 * dt;
                _simPot1 = Math.Max(0, Math.Min(5, _simPot1));
            }
            if (!_pot2Manual)
            {
                _simPot2 += (_rnd.NextDouble() - 0.5) * 0.2 * dt;
                _simPot2 = Math.Max(3.5, Math.Min(5.0, _simPot2)); // stay in 70–100 % RH range
            }

            _simPhaseTime += dt;
        }
    }
}
```
