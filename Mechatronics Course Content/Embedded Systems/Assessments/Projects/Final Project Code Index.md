# Final Project Code Index

Return to the [[Final Project Overview]] · [[Embedded Systems Assessment Index|Assessment index]] · [[Embedded Systems Overview|Subject overview]].

Core firmware and C# GUI source for the laser condensation-risk simulator, pasted as Obsidian notes with syntax-highlighted code blocks.

## Firmware (C)

- [[Final Project Firmware]] - `final_project_firmware.c` (AT90USB1287 control loop, dew point, risk, heater/fan, UART protocol)

## GUI (C#)

- [[Final Project Program]] - application entry point
- [[Final Project IAppBoard]] - hardware-abstraction interface
- [[Final Project AppBoard]] - real serial board implementation
- [[Final Project SimulatorBoard]] - offline simulator board
- [[Final Project LaserSimContract]] - shared opcodes / protocol constants
- [[Final Project DatabaseLogger]] - MySQL session logging
- [[Final Project MainForm]] - main operator UI and PI control
- [[Final Project HelpForm]] - help window

## Related concepts

- [[Architectural Design]] · [[Embedded Digital Communications]] · [[File Handling and Serial Ports]] · [[GUI and Event-Driven Programming]] · [[Virtual Override Abstract and Sealed]]
