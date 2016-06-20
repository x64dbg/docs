# yara

Apply Yara rules to a memory range.

## arguments

arg1: Rules file to apply. This should be a full path.

\[arg2\]: Start address of the range to apply the rules to. If not specified, the disassembly selection will be used.

\[arg3\]: Size of the range to apply the rules  to. When not specified, the whole page will be used.

## result

This command does not set any result variables.
