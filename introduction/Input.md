# Input

When using x64dbg you can often use various things as input.

## Commands

Commands have the following format:

```
command arg1, arg2, argN
```

## Variables

Variables optionally start with a `$` and can only store one DWORD (QWORD on x64).

## Registers

All registers of all sizes up to 32-bit (eg: RAX, EAX, AL) can be used as variables.

XMM, YMM, ZMM or any other 64-bit registers may not be used as variables, but they may be logged via the [String Formatting](https://help.x64dbg.com/en/latest/introduction/Formatting.html) `f` type.

### Remarks

- The variable names for most registers are the same as the names for them, except for the following registers: 
 - **x87 Control Word Flag**: The flags for this register is named like this: `_x87CW_UM`
- In addition to the registers in the architecture, x64dbg provides the following registers: `CAX` , `CBX` , `CCX` , `CDX` , `CSP` , `CBP` , `CSI` , `CDI` , `CIP`. These registers are mapped to 32-bit registers on 32-bit platform, and to 64-bit registers on 64-bit platform. For example, `CIP` is `EIP` on 32-bit platform, and is `RIP` on 64-bit platform. This feature is intended to support architecture-independent code.

## Memory locations

You can read/write from/to a memory location by using one of the following expressions:
- `[addr]` read a DWORD/QWORD from `addr`.
- `n:[addr]` read n bytes from `addr`.
- `seg:[addr]` read a DWORD/QWORD from a segment at `addr`.
- `byte:[addr]` read a BYTE from `addr`.
- `word:[addr]` read a WORD from `addr`.
- `dword:[addr]` read a DWORD from `addr`.
- `qword:[addr]` read a QWORD from `addr` (x64 only).

### Remarks

- `n` is the amount of bytes to read, this can be anything smaller than 4 on x32 and smaller than 8 on x64 when specified, otherwise there will be an error.
- `seg` can be `gs`, `es`, `cs`, `fs`, `ds`, `ss`. Only `fs` and `gs` have an effect.

## Flags

Debug flags (interpreted as integer) can be used as input. Flags are prefixed with an `_` followed by the flag name. Valid flags are: `_cf`, `_pf`, `_af`, `_zf`, `_sf`, `_tf`, `_if`, `_df`, `_of`, `_rf`, `_vm`, `_ac`, `_vif`, `_vip` and `_id`.

## Numbers

**All numbers are interpreted as hex by default!** If you want to be sure, you can `x` or `0x` as a prefix. Decimal numbers can be used by prefixing the number with a dot: `.123=7B`.

## Expressions

See the [expressions](Expressions.rst) section for more information.

## Labels/Symbols

User-defined labels and symbols are a valid expressions (they resolve to the address of said label/symbol).

## Module Data

### DLL exports

Type `GetProcAddress` and it will automatically be resolved to the actual address of the function. To explicitly define from which module to load the API, use: `[module].dll:[api]` or `[module]:[api]`. In a similar way you can resolve ordinals, try `[module]:[ordinal]`. Another macro allows you to get the loaded base of a module. When `[module]` is an empty string `:GetProcAddress` for example, the module that is currently selected in the CPU will be used.

### Loaded module bases

If you want to access the loaded module base, you can write: `[module]:0`, `[module]:base`, `[module]:imagebase` or `[module]:header`.

### RVA/File offset

If you want to access a module RVA you can either write `[module]:0+[rva]` or you can write `[module]:$[rva]`. If you want to convert a file offset to a VA you can use `[module]:#[offset]`. When `[module]` is an empty string `:0` for example, the module that is currently selected in the CPU will be used. 

### Module entry points

To access a module entry point you can write `[module]:entry`, `[module]:oep` or `[module]:ep`. Notice that when there are exports with the names `entry`, `oep` or `ep` the address of these will be returned instead.

### Remarks

Instead of the `:` delimiter you can also use a `.` If you need to query module information such as `[module]:imagebase` or `[module]:entry` you are advised to use a `?` as delimiter instead: `[module]?entry`. The `?` delimiter does checking for named exports later, so it will still work when there is an export called `entry` in the module.

## Last words

Input for arguments can always be done in any of the above forms, except if stated otherwise.
