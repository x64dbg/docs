# Expression Functions

You may use functions in an expression. The following functions are defined by the debugger:

## GUI Interaction

*  `disasm.sel()`/`dis.sel()` : Get the selected address in the disassembly view.
*  `dump.sel()` : Get the selected address in the dump view.
*  `stack.sel()` : Get the selected address in the stack view.

## Program Information

*  `mod.base(addr)` : Get the base address of the module `addr`.
*  `mod.entry(addr)` : Get the entry address of the module `addr`.
*  `mod.party(addr)` : Get the party of the module `addr`. `0` is user module, `1` is system module.
*  `mod.size(addr)` : Get the size of the module `addr`.
*  `peb()` : Get PEB address.
*  `teb()` : Get TEB address.

## Source

*  `src.disp(addr)` : Get displacement of `addr` relative to last source line.
*  `src.line(addr)` : Get the source line number of `addr`.

## General Purpose

*  `bswap(value)` : Byte-swap `value`.

## Plugins

Plugins can register their own expression functions. See the documentation of your plugin for details.