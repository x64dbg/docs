# Trace

Trace view is a view in which you can see history of stepped instructions. This lets you examine the details of each instruction stepped when you are stepping manually or [tracing](../../introduction/ConditionalTracing.md) automatically, or view a trace history previously saved. This functionality must be enabled explicitly from trace view or [CPU view](CPU.rst). It features saving all the instructions, registers and memory accesses during a trace.

## Start Run Trace

To enable trace logging into trace view, you first enable it via "**Start Run Trace**" menu. It will pop up a dialog allowing you to save the recorded instructions into a file. The default location of this file is in the database directory.

Once started, every instruction you stepped or traced will appear immediately in Trace view. Instructions executed while the debuggee is running or stepping over will not appear here.

## Stop Run Trace

This menu can stop recording instructions.

## Close

Close current trace file and clear the trace view.

## Open

Open a trace file to view the content of it. It can be used when not debugging, but it is recommended that you debug the corresponding debuggee when viewing a trace, as it will be able to render the instructions with labels from the database of the debuggee.

## Recent files

Open a recent file to view the content of it.
