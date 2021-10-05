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

* `mod.party(addr)` : Get the party number of the module `addr`. `0` is user module, `1` is system module.
* `mod.base(addr)` : Get the base address of the module `addr`.
* `mod.size(addr)` : Get the size of the module `addr`.
* `mod.hash(addr)` : Get the hash of the module `addr`.
* `mod.entry(addr)` : Get the entry address of the module `addr`.
* `mod.system(addr)` : True if the module at `addr` is a system module. False: module is a user module.
* `mod.user(addr)` : True if the module at `addr` is a user module. False: module is NOT a user module.
* `mod.main()` : Returns the base of the main module (debuggee). If this is a DLL it will return `0` until loaded.
* `mod.rva(addr)` : Get the RVA of `addr`. If `addr` is not inside a module it will return `0`.
* `mod.offset(addr)` : Get the file offset of `addr`. If `addr` is not inside a module it will return `0`.
* `mod.isexport(addr)` : True if `addr` is an exported function from a module.

## Process Information

* `peb()` : Get PEB address.
* `teb()` : Get TEB address.
* `tid()` : Get the current thread ID.

## General Purpose

* `bswap(value)` : Byte-swap `value`. For example, `bswap(44332211)` = 0x11223344.
* `ternary(condition, val1, val2)` : If condition is nonzero, return `val1`, otherwise return `val2`.
* `GetTickCount()` : Tick count of x64dbg.

## Strings

* `utf8(str)` : A UTF-8 string.
* `utf16(str)` : A UTF-16 string.
* `strstr(str1, str2)` : Find a substring. For example, `strstr(utf8(addr), "abc")`.
* `streq(str1, str2)` : Compare two strings. For example, `streq(utf8(addr), "abc")`.

## Memory

* `mem.valid(addr)` : True if `addr` is a valid memory address.
* `mem.base(addr)` : Returns the base of the memory page of `addr` (can change depending on your memory map mode).
* `mem.size(addr)` : Returns the size of the memory page of `addr` (can change depending on your memory map mode).
* `mem.iscode(addr)` : True if `addr` is a page that is executable.
* `mem.decodepointer(ptr)` : Equivalent to calling the `DecodePointer` API on `ptr`, only works on Vista+.

## Disassembly

* `dis.len(addr)` : Get the length of the instruction at `addr`.
* `dis.iscond(addr)` : True if the instruction at `addr` is a conditional branch.
* `dis.isbranch(addr)` : True if the instruction at `addr` is a branch (jcc/call).
* `dis.isret(addr)` : True if the instruction at `addr` is a `ret`.
* `dis.iscall(addr)` : True if the instruction at `addr` is a `call`.
* `dis.ismem(addr)` : True if the instruction at `addr` has a memory operand.
* `dis.isnop(addr)` : True if the instruction at `addr` is equivalent to a NOP.
* `dis.isunusual(addr)` : True if the instruction at `addr` is unusual.
* `dis.branchdest(addr)` : Branch destination of the instruction at `addr` (what it follows if you press enter on it).
* `dis.branchexec(addr)` : True if the branch at `addr` is going to execute.
* `dis.imm(addr)` : Immediate value of the instruction at `addr`.
* `dis.brtrue(addr)` : Branch destination of the instruction at `addr`.
* `dis.brfalse(addr)` : Address of the next instruction if the instruction at `addr` is a conditional branch.
* `dis.next(addr)` : Address of the next instruction from `addr`.
* `dis.prev(addr)` : Address of the previous instruction from `addr`.
* `dis.iscallsystem(addr)` : True if the instruction at `addr` goes to a system module.

## Trace record

* `tr.enabled(addr)` : True if the trace record is enabled at `addr`.
* `tr.hitcount(addr)` : Number of hits on the trace record at `addr`.
* `tr.runtraceenabled()` : True if run trace is enabled.

## Byte/Word/Dword/Qword/Ptr

* `ReadByte(addr)`,`Byte(addr)`,`byte(addr)` : Read a byte from `addr` and return the value. Example: `byte(eax)` reads a byte from memory location `[eax]`.
* `ReadWord(addr)`,`Word(addr)`,`word(addr)` : Read a word (2 bytes) from `addr` and return the value.
* `ReadDword(addr)`,`Dword(addr)`,`dword(addr)` : Read a dword (4 bytes) from `addr` and return the value.
* `ReadQword(addr)`,`Qword(addr)`,`qword(addr)` : Read a qword (8 bytes) from `addr` and return the value (only available on x64).
* `ReadPtr(addr)`,`ReadPointer(addr)`,`ptr(addr)`,`Pointer(addr)`,`pointer(addr)` : Read a pointer (4/8 bytes) from `addr` and return the value.

## Functions

* `func.start()` : Return start of the function `addr` is part of, zero otherwise.
* `func.end()` : Return end of the function `addr` is part of, zero otherwise.

## References

* `ref.count()` : Number of entries in the current reference view.
* `ref.addr(index)` : Get the address of the reference at `index`. Zero on failure.

## Arguments

This assumes the return address is on the stack (eg you are inside the function).

* `arg.get(index)` : Gets the argument at `index` (zero-based).
* `arg.set(index, value)` : Sets the argument at `index` (zero-based) to `value`.

## Exceptions

This is a set of functions to get information about the last exception. They can be used for exceptions breakpoints to construct more advanced conditions.

* `ex.firstchance()` : Whether the last exception was a first chance exception.
* `ex.addr()` : Last exception address.
* `ex.code()` : Last exception code.
* `ex.flags()` : Last exception flags.
* `ex.infocount()` : Last exception information count (number of parameters).
* `ex.info(index)` : Last exception information, zero if index is out of bounds.

## Plugins

Plugins can register their own expression functions. See the plugin documentation for more details.
