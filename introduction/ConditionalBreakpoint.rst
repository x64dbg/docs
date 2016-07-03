Conditional Breakpoints
=======================

This section describes the conditional breakpoint capability in x64dbg.

-------------------
Operations overview
-------------------

When a breakpoint is hit, x64dbg will do the following things:

1. Increment the *hit counter*;

2. Set the system variable ``$breakpointcounter`` to the value of *hit counter*.

3. If *break condition* is set, evaluate the expression (defaults to ``true``);

4. If *fast resume* is set and *break condition* evaluated to ``false``:
   
   - Resume execution of the debuggee (skip the next steps). This will also skip executing plugin callbacks and GUI updates.

5. If *log condition* is set, evaluate it (defaults to ``true``);

6. If *command condition* is set, evaluate the expression (defaults to *break condition*);

7. If *break condition* evaluated to ``true``:

   - Print the standard log message;
   - Execute plugin callbacks;

8. If *log text* is set and *log condition* evaluated to ``true``:

   - Format and print the *log text*.

9. If *command text* is set and *command condition* evaluated to ``true``:

   - Set the system variable ``$breakpointcondition`` to the *break condition* (True : 1, False : 0). Set the system variable ``$breakpointlogcondition`` to the *log condition* (True : 1, False : 0).
   - Execute the command in *command text*.
   - The *break condition* will be set to the value of ``$breakpointcondition``. So if you modify this system variable in the script, you will be able to control whether the debuggee would break.

10. If *break condition* evaluated to ``true``:

   - Break the debuggee and wait for the user to resume.

-----------
Hit counter
-----------

A hit counter records how many times a breakpoint has been reached. It will be incremented unconditionally, even if fast resume is enabled on this breakpoint. It may be viewed at breakpoint view and reset with :doc:`../commands/breakpoints-conditional/ResetBreakpointHitCount`

-------
Logging
-------

The log can be formatted by x64dbg to log the current state of the program. See :doc:`./Formatting` on how to format the log string.

-----
Notes
-----

You should not use commands that can change the running state of the debuggee (such as ``run``) inside the breakpoint command, because these commands are unstable when used here. You can use *break condition*, *command condition* or ``$breakpointcondition`` instead.

--------
See also
--------

:doc:`../commands/breakpoints-conditional/index`
