# Inability

This section gives a list of features currently not supported in x64dbg. You are always welcome to contribute to x64dbg to help fixing them.

* Fine-grained memory breakpoint. Unlike other debuggers, memory breakpoint is supported only on a whole memory page, but not on a subrange of the memory page.
* Search for non-English strings. Searching for non-English strings via the built-in strings search may not be able to find all the non-English strings.
* Log non-English strings into log with built-in "{s:[...]}" syntax.
* Other pending issues at http://issues.x64dbg.com