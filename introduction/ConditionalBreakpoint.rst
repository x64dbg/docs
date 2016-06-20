Conditional Breakpoints
=======================

This section describes the conditional breakpoint capability in x64dbg.

-------------------
Operations overview
-------------------

When a breakpoint is hit, x64dbg will do the following things:

1. Increment the *hit counter*;

2. If *break condition* is set, evaluate the expression (defaults to ``true``);

3. If *fast resume* is set and *break condition* evaluated to ``false``:
   
   - Resume execution of the debuggee (skip the next steps). This will also skip executing plugin callbacks and GUI updates.

4. If *log condition* is set, evaluate it (defaults to ``true``);

5. If *command condition* is set, evaluate the expression (defaults to *break condition*);

6. If *break condition* evaluated to ``true``:

   - Print the standard log message;
   - Execute plugin callbacks;

7. If *log text* is set and *log condition* evaluated to ``true``:

   - Format and print the *log text*.

8. If *command text* is set and *command condition* evaluated to ``true``:

   - Execute the command in *command text*.

9. If *break condition* evaluated to ``true``:

   - Break the debuggee and wait for the user to resume.

-----------
Hit counter
-----------

A hit counter records how many times a breakpoint has been reached. It will be incremented unconditionally, even if fast resume is enabled on this breakpoint. It may be viewed at breakpoint view and reset with :doc:`../commands/breakpoints-conditional/ResetBreakpointHitCount`

-------
Logging
-------

The log can be formatted by x64dbg to log the current state of the program. See :doc:`./Formatting` on how to format the log string.

--------
See also
--------

:doc:`../commands/breakpoints-conditional/index`
