# Final Project DatabaseLogger

> [!info] Course material
> [[Final Project Overview|Back]] · Source: `DatabaseLogger.cs`

```csharp
using System;
using System.Data;
using MySql.Data.MySqlClient;

namespace FinalProject
{
    /// <summary>
    /// Minimal helper for logging temperature data to MySQL.
    /// </summary>
    public class DatabaseLogger : IDisposable
    {
        private readonly MySqlConnection _connection;

        public bool IsConnected => _connection?.State == ConnectionState.Open;

        public DatabaseLogger(string connectionString)
        {
            _connection = new MySqlConnection(connectionString);
        }

        public void Open()
        {
            if (_connection.State != ConnectionState.Open)
            {
                _connection.Open();
            }
        }

        public void Close()
        {
            if (_connection.State != ConnectionState.Closed)
            {
                _connection.Close();
            }
        }

        public void Dispose()
        {
            Close();
            _connection.Dispose();
        }

        /// <summary>
        /// Insert a single temperature record.
        /// </summary>
        public void InsertTemperature(
            DateTime timestamp,
            double temperatureC,
            double? setpointC,
            double? kp,
            double? ki,
            string remark = null)
        {
            const string sql = @"
INSERT INTO temperature_record
    (ts, temperature_c, setpoint_c, kp, ki, remark)
VALUES
    (@ts, @temp, @setpoint, @kp, @ki, @remark);";

            using (var cmd = new MySqlCommand(sql, _connection))
            {
                cmd.Parameters.AddWithValue("@ts", timestamp);
                cmd.Parameters.AddWithValue("@temp", temperatureC);
                cmd.Parameters.AddWithValue("@setpoint", (object)setpointC ?? DBNull.Value);
                cmd.Parameters.AddWithValue("@kp",       (object)kp       ?? DBNull.Value);
                cmd.Parameters.AddWithValue("@ki",       (object)ki       ?? DBNull.Value);
                cmd.Parameters.AddWithValue("@remark",   (object)remark   ?? DBNull.Value);

                cmd.ExecuteNonQuery();
            }
        }
    }
}
```
