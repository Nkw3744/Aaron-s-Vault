# Final Project - Laser Condensation-Risk Simulator

Return to the [[Embedded Systems Overview|subject overview]] · Open the [[Embedded Systems Assessment Index|assessment index]].

> [!info] Report and code
> [[ENEL712Report_24232594.pdf|Full project report (PDF)]] · [[Final Project Code Index|All project source code]]

The final project is a laser-cutter **startup and condensation-risk simulator**: AT90USB1287 firmware paired with a C# Windows Forms GUI over a USART link. It models the real hazard that operators who skip warm-up/condensation procedures can cause serious damage to laser optics and machinery. Built collaboratively with Iyla and Amber confirming design choices.

## System at a Glance

- **Firmware (C)** on the AT90USB1287 runs the control loop: reads sensors, computes dew point and condensation risk, drives the heater and fan, manages safety interlocks, and reports state over UART. Source: [[Final Project Firmware]].
- **GUI (C#/.NET WinForms)** provides the operator interface: live gauges/charts, a PI temperature controller, risk indicators, a dew-point override, and MySQL data logging. Source: [[Final Project MainForm]] · [[Final Project AppBoard]] · [[Final Project IAppBoard]].
- The two halves communicate with a small framed opcode protocol over the serial port. Protocol: [[Final Project LaserSimContract]].

## Key Technical Elements

- **Dew point and risk**: ambient/target temperature and humidity feed a dew-point calculation that classifies condensation risk (LED risk bar on PORTC).
- **Thermal control**: heater and fan managed by a control loop; host-side PI controller with firmware hold timers and a session timeout to resolve host/firmware contention over PWM registers.
- **Safety interlocks**: laser enable, door, and track-limit conditions gate the "laser active" indicator - the core lesson from industry practice.
- **State machine** startup sequence - see [[Architectural Design]].

## Related Concepts

- [[Embedded Digital Communications]] and [[File Handling and Serial Ports]] - the UART bridge
- [[Virtual Override Abstract and Sealed]] - the `IAppBoard` hardware-abstraction interface
- [[GUI and Event-Driven Programming]] - the operator interface
- [[Advanced C Programming Techniques]] - register/bit manipulation and `volatile`
- [[Lab Board Knowledge]] - board peripherals used
