What is x64dbg?
===============

This is a x64/x32 debugger that is currently in active development.

The debugger (currently) has three parts:

* DBG
* GUI
* Bridge

DBG is the debugging part of the debugger. It handles debugging (using TitanEngine) and will provide data for the GUI.

GUI is the graphical part of the debugger. It is built on top of Qt and it provides the user interaction.

Bridge is the communication library for the DBG and GUI part (and maybe in the future more parts). The bridge can be used to work on new features, without having to update the code of the other parts.