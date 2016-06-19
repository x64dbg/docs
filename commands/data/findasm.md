
# findasm[,asmfind]

Find assembled instruction.

## arguments

  arg1: Instruction to look for (make sure to use "mov eax, ebx" to ensure you actually search for that instruction).
[arg2]: Address of/inside a memory page to look in. When not specified CIP will be used. 
[arg3]: The size of the data to search in.

## result 
The $result variable is set to the number of references found. 
