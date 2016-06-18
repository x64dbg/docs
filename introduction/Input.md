# Input
This program accepts various options of input:

*  commands: Commands have the following format: "command[space]arg1,[optional space]arg2,argN".

*  variables: Variables optionally start with a $ and can only store one DWORD (QWORD on x64).

*  registers: All registers (of all sizes) can be used as variables.

*  memory locations: You can read/write from/to a memory location by using one of the following expressions:
   *  [addr]     - read a DWORD/QWORD, depending on the architecture.
   *  n:[addr]   - read n bytes from.
   *  seg:[addr] - read a DWORD/QWORD from a segment.

   **REMARKS**:
   - n is the amount of bytes to read, this can be anything smaller than 4 on x32 and smaller than 8 on x64 when specified, otherwise there will be an error.
   - seg can be gs, es, cs, fs, ds, ss. Only fs and gs have an effect.

*  flags: Debug flags (interpreted as integer) can be used as input. Flags are prefixed with an '_' followed by the flag name. Valid flags are: _cf, _pf, _af, _zf, _sf, _tf, _if, _df, _of, _rf, _vm, _ac, _vif, _vip and _id.

*  numbers: All numbers are interpreted as hex by default. If you want to be sure, you can use the "x" prefix or the "0x" prefix. Decimal numbers can be used by prefixing the number with a "." (.123=7B).

*  expressions: See "Expressions" for more information.

## Module Data:

*  DLL exports: Type 'GetProcAddress' and it will automatically be resolved to the actual address of the function. To explicitly define from which module to load the API, use: "[module].dll:[api]" or "[module]:[api]". In a similar way you can resolve ordinals, try "[module]:[ordinal]". Another macro allows you to get the loaded base of a module. When "[module]" is an empty string (":GetProcAddress" for example), the module that is currently selected in the CPU will be used.
*  Loaded Module Bases: If you want to access the loaded module base, you can write: "[module]:0", "[module]:base", "[module]:imagebase" or "[module]:header". 
*  RVA/File Offset: If you want to access a module RVA you can either write "[module]:0+[rva]" or you can write "[module]:$[rva]". If you want to convert a file offset to a VA you can use "[module]:#[offset]". When "[module]" is an empty string (":0" for example), the module that is currently selected in the CPU will be used. 
*  Module Entry Points: To access a module entry point you can write "[module]:entry", "[module]:oep" or "[module]:ep". Notice that when there are exports with the names "entry", "oep" or "ep" the address of these will be returned instead.

   Notice: Instead of the ':' delimiter you can also use a '.' If you need to query module information such as "[module]:imagebase" or "[module]":entry" you are advised to use a '?' as delimiter instead ("[module]?entry"). The '?' does checking for named exports later, so it will still work when there is an export called "entry" in the module.
labels/symbols: user-defined labels and symbols are a valid expressions.

**Input for arguments can always be done in any of the above forms, except if stated otherwise.**

