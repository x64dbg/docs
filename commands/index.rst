Commands
========

This is the documentation of x64dbg commands.

FAQ:

# Please note that all integer constants are represented in hex. For example, after executing the following command, `$i` will be 256 (0x100): `mov $i, 100` . This also means a variable cannot begin with letters from A to F.
# For commands with two or more arguments, a comma (,) is used to separate these arguments. Do not use a space to separate the arguments.
# x64dbg only supports integer in expressions. Strings, Floating point numbers and SSE/AVX data is not supported. Therefore you cannot use `[eax]=="abcd"` operator to compare strings. Instead, you can compare the first DWORD/QWORD of the string, or use an appropriate plugin which provides such feature.
# The "==" operator is used to test if both operands are equal. The "=" operator is used to transfer the value of the expression to the destination.

**Contents:**

.. toctree::
   :maxdepth: 1
   
   general-purpose/index
   debug-control/index
   breakpoint-control/index
   conditional-breakpoint-control/index
   tracing/index
   thread-control/index
   memory-operations/index
   operating-system-control/index
   watch-control/index
   variables/index
   searching/index
   user-database/index
   analysis/index
   types/index
   plugins/index
   script/index
   gui/index
   misc/index
