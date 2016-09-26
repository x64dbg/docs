# Variables

This program supports variables. There are three types of variables:

*  USER: Variables created by the user using the `var` command. These variables have no access restrictions.

*  SYSTEM: Variables created by the system, that can be read and written, but cannot be deleted.

*  READONLY: Variables created by the system, that can be read, but not written or deleted.

## Reserved Variables

There are a few reserved variables:

*  `$res`/`$result`: General result variable.
*  `$resN`/`$resultN`: Optional other result variables (N= 1-4).
*  `$pid`: Process ID of the debugged executable.
*  `$hp`/`$hProcess`: Debugged executable handle.
*  `$lastalloc`: Last result of the `alloc` command.
*  `$breakpointcondition` : Controls the pause behaviour in the conditional breakpoint command.
*  `$breakpointcounter` : The hit counter of the breakpoint, set before the condition of the conditional breakpoint is evaluated.
*  `$breakpointlogcondition` : The log condition of the conditional breakpoint. It cannot be used to control the logging behavoiur.
