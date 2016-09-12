# Expression Functions

You may use functions in an expression. The following functions are defined by the debugger:

## GUI Interaction

* `disasm.sel()`/`dis.sel()` : Get the selected address in the disassembly view.
* `dump.sel()` : Get the selected address in the dump view.
* `stack.sel()` : Get the selected address in the stack view.

## Source

* `src.disp(addr)` : Get displacement of `addr` relative to last source line.
* `src.line(addr)` : Get the source line number of `addr`.

## Modules

* `mod.party(addr)` : Get the party of the module `addr`. `0` is user module, `1` is system module.
* `mod.base(addr)` : Get the base address of the module `addr`.
* `mod.size(addr)` : Get the size of the module `addr`.
* `mod.hash(addr)` : Get the hash of the module `addr`.
* `mod.entry(addr)` : Get the entry address of the module `addr`.

## Process Information

* `peb()` : Get PEB address.
* `teb()` : Get TEB address.
* `tid()` : Get the current thread ID.

## General Purpose

* `bswap(value)` : Byte-swap `value`.
* `ternary(condition, val1, val2)` : If condition is nonzero, return `val1`, otherwise return `val2`.
* `GetTickCount()` : Tick count of x64dbg.

## Memory

* `mem.valid(addr)` : True if `addr` is a valid memory address.
* `mem.base(addr)` : Returns the base of the memory page (can change depending on your memory map mode).
* `mem.size(addr)` : Returns the size of the memory page (can change depending on your memory map mode).
* `mem.iscode(addr)` : True if `addr` is a page that is executable.
* `mem.decodepointer(ptr)` : Equivalent to the `DecodePointer` API, only works on Vista+.

## Disassembly

* `dis.len(addr)` : Get the length of the instruction at `addr`.
* `dis.iscond(addr)` : True if the instruction at `addr` is a conditional branch.
* `dis.isbranch(addr)` : True if the instruction at `addr` is a branch (jcc/call).
* `dis.isret(addr)` : True if the instruction at `addr` is a `ret`.
* `dis.ismem(addr)` : True if the instruction has a memory operand.
* `dis.branchdest(addr)` : Branch destination of the instruction at `addr` (what it follows if you press enter on it).
* `dis.branchexec(addr)` : True if the branch at `addr` is going to execute.
* `dis.imm(addr)` : Immediate value of the instruction at `addr`.
* `dis.brtrue(addr)` : Branch destination of the instruction at `addr`.
* `dis.brfalse(addr)` : Address of the next instruction if the instruction at `addr` is a conditional branch.

## Trace record

* `tr.enabled(addr)` : True if the trace record is enabled at `addr`.
* `tr.hitcount(addr)` : Number of hits on the trace record at `addr`.

## Plugins

Plugins can register their own expression functions. See the documentation of your plugin for details.