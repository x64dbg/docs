# findall

Find all occurrences of a pattern.

## arguments

`arg1` The address to start searching from. Notice that the searching will stop when the end of the memory page this address resides in has been reached. This means you cannot search the complete process memory without enumerating the memory pages first.

`arg2` The byte pattern to search for. This byte pattern can contain wildcards (?) for example: `EB0?90??8D`.

`[arg3]` The size of the data to search in. Default is the size of the memory region.

## result

`$result` is set to the number of occurrences.
