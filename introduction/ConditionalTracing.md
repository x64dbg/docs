# Conditional Tracing

This section describes the conditional tracing capability in x64dbg.

## Operations overview

When a trace step is hit, x64dbg will do the following things:

- Increment the *trace counter*;
- Set the system variable `$tracecounter` to the value of *trace counter*;
- If *break condition* is set, evaluate the [expression](./Expressions.rst) (defaults to `false`);
- Execute plugin callbacks (allowing plugins to change the *break condition*);
- If *log condition* is set, evaluate the [expression](./Expressions.rst) (defaults to `true`);
- If *command condition* is set, evaluate the [expression](./Expressions.rst) (defaults to *break condition*);
- If *log text* is set and *log condition* evaluated to `true`:
  - Format and print the *log text* (see [String Formatting](./Formatting.rst)).
- If *command text* is set and *command condition* evaluated to `true`:
  - Set the system variable `$tracecondition` to the *break condition*;
  - Set the system variable `$tracelogcondition` to the *log condition*;
  - Execute the command in *command text*;
  - The *break condition* will be set to the value of `$tracecondition`. So if you modify this system variable in the script, you will be able to control whether the debuggee would break.
- If *break condition* evaluated to `true`:
  - Print the standard log message; 
  - Break the debuggee and wait for the user to resume.

## Logging

The log can be formatted by x64dbg to log the current state of the program. See [formatting](./Formatting.rst) on how to format the log string.

## Trace record

If you use one of the trace record-based tracing options, the initial evaluation of *break condition* includes the type of trace record tracing that you specified. The normal *break condition* can be used to break before the trace record condition is satisfied. If you want to include trace record in your condition for full control, you can use the [expression functions](./Expression-functions.md).

## Notes

You should not use commands that can change the running state of the debuggee (such as `run`) inside the breakpoint command, because these commands are unstable when used here. You can use *break condition*, *command condition* or `$tracecondition` instead.

## See also

- [Tracing](../commands/tracing/index.rst)
- [Expressions](./Expressions.rst)
- [Expression Functions](./Expression-functions.md)
- [String Formatting](./Formatting.rst)
