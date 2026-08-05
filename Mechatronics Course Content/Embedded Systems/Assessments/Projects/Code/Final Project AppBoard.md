# Final Project AppBoard

> [!info] Course material
> [[Final Project Overview|Back]] · Source: `AppBoard.cs` · [[File Handling and Serial Ports]]

```csharp
using System;
using System.IO.Ports;
using System.Threading;

namespace FinalProject
{
    /// <summary>
    /// Encapsulates the UART protocol to the AT90USB1287 applications board.
    /// Responsible for framing, timeouts, and high-level convenience methods.
    /// </summary>
    public class AppBoard : IAppBoard, IDisposable
    {
        private const byte START_BYTE = 0x53;
        private const byte STOP_BYTE  = 0xAA;

        private readonly SerialPort _port;

        public bool IsConnected => _port != null && _port.IsOpen;

        public AppBoard(string portName, int baudRate = 38400)
        {
            _port = new SerialPort
            {
                PortName = portName,
                BaudRate = baudRate,
                Parity = Parity.None,
                DataBits = 8,
                StopBits = StopBits.One,
                Handshake = Handshake.None,
                ReadTimeout = 200,   // ms
                WriteTimeout = 200   // ms
            };
        }

        public static string[] GetAvailablePorts()
        {
            return SerialPort.GetPortNames();
        }

        public void Connect()
        {
            if (!_port.IsOpen)
            {
                _port.Open();
                // Small delay to let the virtual COM port settle
                Thread.Sleep(100);
            }
        }

        public void Disconnect()
        {
            if (_port.IsOpen)
            {
                _port.Close();
            }
        }

        public void Dispose()
        {
            if (_port != null)
            {
                if (_port.IsOpen)
                {
                    _port.Close();
                }

                _port.Dispose();
            }
        }

        private void WritePacket(byte[] packet)
        {
            if (!_port.IsOpen)
                throw new InvalidOperationException("Serial port is not open.");

            _port.DiscardInBuffer();
            _port.Write(packet, 0, packet.Length);
        }

        private byte ReadByteWithTimeout()
        {
            int value = _port.ReadByte();
            if (value < 0)
            {
                throw new TimeoutException("No data received from board.");
            }

            return (byte)value;
        }

        /// <summary>
        /// Send TXCHECK and verify that the board responds with 0x0F.
        /// </summary>
        public bool Ping()
        {
            byte[] packet = { START_BYTE, LaserSimContract.TxCheck, STOP_BYTE };
            WritePacket(packet);

            try
            {
                byte reply = ReadByteWithTimeout();
                return reply == 0x0F;
            }
            catch (TimeoutException)
            {
                return false;
            }
        }

        /// <summary>
        /// Generic 8-bit read (READ_* instructions).
        /// </summary>
        private byte ReadUInt8(byte instr)
        {
            byte[] packet = { START_BYTE, instr, STOP_BYTE };
            WritePacket(packet);
            return ReadByteWithTimeout();
        }

        /// <summary>
        /// Generic 16-bit write (SET_* instructions). Returns true if ACK matches.
        /// </summary>
        private bool WriteUInt16(byte instr, ushort value)
        {
            byte lsb = (byte)(value & 0xFF);
            byte msb = (byte)((value >> 8) & 0xFF);
            byte[] packet = { START_BYTE, instr, lsb, msb, STOP_BYTE };

            WritePacket(packet);
            byte ack = ReadByteWithTimeout();
            return ack == instr;
        }

        // High-level methods matching proposal

        public byte ReadPINA()
        {
            return ReadUInt8(LaserSimContract.ReadPina);
        }

        public byte ReadPot1()
        {
            return ReadUInt8(LaserSimContract.ReadPot1);
        }

        public byte ReadPot2()
        {
            return ReadUInt8(LaserSimContract.ReadPot2);
        }

        public byte ReadTemp()
        {
            return ReadUInt8(LaserSimContract.ReadTemp);
        }

        public byte ReadLight()
        {
            return ReadUInt8(LaserSimContract.ReadLight);
        }

        public bool WritePORTC(byte value)
        {
            return WriteUInt16(LaserSimContract.SetPortc, value);
        }

        /// <summary>
        /// Write motor PWM in raw OCR units (0..399).
        /// </summary>
        public bool WriteMotorOCR(ushort ocrValue)
        {
            if (ocrValue > 399)
                ocrValue = 399;
            return WriteUInt16(LaserSimContract.SetMotor, ocrValue);
        }

        /// <summary>
        /// Write motor PWM as percentage (0..100).
        /// </summary>
        public bool WriteMotorPercent(double percent)
        {
            if (percent < 0.0) percent = 0.0;
            if (percent > 100.0) percent = 100.0;
            ushort ocr = (ushort)Math.Round(percent * 399.0 / 100.0);
            return WriteMotorOCR(ocr);
        }

        public bool WriteLampOCR(ushort ocrValue)
        {
            if (ocrValue > 399)
                ocrValue = 399;
            return WriteUInt16(LaserSimContract.SetLight, ocrValue);
        }

        public bool WriteLampPercent(double percent)
        {
            if (percent < 0.0) percent = 0.0;
            if (percent > 100.0) percent = 100.0;
            ushort ocr = (ushort)Math.Round(percent * 399.0 / 100.0);
            return WriteLampOCR(ocr);
        }

        public bool WriteHeaterOCR(ushort ocrValue)
        {
            if (ocrValue > 399)
                ocrValue = 399;
            return WriteUInt16(LaserSimContract.SetHeater, ocrValue);
        }

        public bool WriteHeaterPercent(double percent)
        {
            if (percent < 0.0) percent = 0.0;
            if (percent > 100.0) percent = 100.0;
            ushort ocr = (ushort)Math.Round(percent * 399.0 / 100.0);
            return WriteHeaterOCR(ocr);
        }

        // Laser simulator extension reads (requires Piece 7 firmware on the MCU)

        /// <summary>
        /// Condensation margin in °C. Raw byte is offset: margin = (raw − 100) / 10.
        /// Positive values mean the surface is above the dew point by that amount.
        /// </summary>
        public double ReadSimMargin()
        {
            byte raw = ReadUInt8(LaserSimContract.ReadSimMargin);
            return LaserSimContract.DecodeMargin(raw);
        }

        /// <summary>Returns 0 = Safe, 1 = Marginal, 2 = High Risk.</summary>
        public int ReadSimStatus() => ReadUInt8(LaserSimContract.ReadSimStatus);

        /// <summary>Returns dew point in °C. Raw byte = dewPoint × 2.</summary>
        public double ReadSimDewPoint() => LaserSimContract.DecodeDewPoint(ReadUInt8(LaserSimContract.ReadSimDewpt));

        /// <summary>Returns laser power setpoint 0–100 %.</summary>
        public int ReadSimPower() => ReadUInt8(LaserSimContract.ReadSimPower);

        /// <summary>Returns fan duty cycle 0–100 %.</summary>
        public int ReadSimFan() => ReadUInt8(LaserSimContract.ReadSimFan);

        /// <summary>Returns alarm flags: bit 0 = door_fault, bit 1 = axis_alarm.</summary>
        public int ReadAlarmFlags() => ReadUInt8(LaserSimContract.ReadAlarmFlags);

        /// <summary>
        /// Override dew point in 0.5 °C steps for tuning / test workflows.
        /// </summary>
        public bool WriteSimDewPoint(double dewPointC)
        {
            byte raw = LaserSimContract.EncodeDewPoint(dewPointC);
            return WriteUInt16(LaserSimContract.SetSimDewpt, raw);
        }

        public bool ClearSimDewPointOverride()
        {
            return WriteUInt16(LaserSimContract.ClearSimDewpt, 0);
        }
    }
}
```
