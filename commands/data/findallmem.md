# findallmem/findmemall

Find all occurrences of a pattern in the entire memory map.

## arguments

`arg1` The address to start searching from.

`arg2` The byte pattern to search for. This byte pattern can contain wildcards (?) for example: `EB0?90??8D`.

`[arg3]` The size of the data to search in. Default is the entire memory map.

## result

`$result` is set to the number of occurrences.
