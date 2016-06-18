# SetBreakpointFastResume
Set the fast resume flag of the breakpoint. If this flag is set, no GUI, plugin, logging or any other actions except the breakpoint counter increment, will be performed is the debugger would not break due to breakpoint condition.

## arguments
[arg1]: The address of an existing software breakpoint which you want to set the flag for.

[arg2]: The fast resume flag. If it is 0, fast resume is disabled, otherwise it is enabled

## result
This command does not set any result variables.
