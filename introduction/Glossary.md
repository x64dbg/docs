# Glossary

This section describes various terms and concepts used by x64dbg.

-  **Breakpoint** A breakpoint defines a condition when the debuggee should be paused. There are 5 types of breakpoint, namely software breakpoint, hardware breakpoint, memory breakpoint, DLL breakpoint and exception breakpoint.
-  **Conditional Breakpoint** A conditional breakpoint lets you define some simple operations that executes automatically when the breakpoint is hit, and then conditionally resumes program execution. See [documentation for conditional breakpoint](./ConditionalBreakpoint.md) for more information.
-  **Conditional Tracing** Conditional tracing lets you execute the program step-by-step, and pause when the specified condition is met. See [documentation for conditional tracing](./ConditionalTracing.md) for more information.
-  **DLL Breakpoint** A DLL breakpoint specifies the name of a DLL. When the DLL is loaded or unloaded, the debuggee will be paused.
-  **Run trace** Run trace is a log of all traced instructions, typically displayed in the [Trace View](../gui/views/Trace.md). When enabled, all instructions are recorded in it during conditional tracing.
-  **Trace record** When enabled, Trace record records whether a byte has been executed, and how many times it is executed. An instruction that has been executed previously will be displayed in a different background color, by default green. It is analogous to leaving footprints while exploring a maze.
