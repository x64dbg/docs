# setjit/jitset

Set the Just-In-Time Debugger in Windows. In WIN64 systems there are two JIT entries: one for a x32 debugger and other for a x64 debugger. In a WIN64 system when a x32 process crash: Windows attach the x32 debugger stored in the x32-JIT entry. Important notes:Its possible change the x32-JIT entry from the x64 debugger (using the x32 arg).Its possible change the x64-JIT entry from the   x32 debugger ONLY if the x32 debugger its running in a WIN64 System (using the x64 arg).

## arguments

without args: Set the current debugger as JIT.

`arg1` oldsave: Set the current debugger as     JIT and save the last JIT entry.restore: Set the old JIT entry     stored as JIT and remove it from debugger db.old (without arg2): Set the old     JIT entry stored as new JIT.old (with arg2): Set the arg2 as     old JIT entry stored.x32: Set the arg2 as new     x32-JIT entry.x64: Set the arg2 as new     x64-JIT entry.

## result

This command does not set any result variables.
