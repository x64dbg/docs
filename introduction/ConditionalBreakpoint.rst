Conditional Breakpoint Overview
===============================

This section describes the conditional breakpoint capability in x64dbg.

-------------------
Operations overview
-------------------

When a breakpoint is hit, x64dbg can do the following things:

1.  Increment the hit counter
2.  Evaluate the breakpoint condition
3.  If the condition is not satisfied, and fast resume is enabled, then the debugger resumes.
4.  Output the default logging message if the debugger would break.
5.  Evaluate the logging condition if it exists and output the log.
6.  Notify the plugin that a breakpoint has been reached.
7.  Update the trace record.
8.  Evaluate the command condition if it exists and execute the specified command.
9.  Halt the debuggee and enter paused state.

-----------
Hit counter
-----------

A hit counter records how many times a breakpoint has been reached. It will 

be incremented unconditionally, even if fast resume is enabled on this 

breakpoint. It may be viewed at breakpoint view and resetted with 

:doc:`../commands/breakpoints-conditional/ResetBreakpointHitCount`

-------
Logging
-------

The log can be formatted by x64dbg to log the current state of the program.

--------
See also
--------
:doc:`../commands/breakpoints-conditional/index`

