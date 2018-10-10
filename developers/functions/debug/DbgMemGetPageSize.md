# DbgMemGetPageSize

Function description.

```c++
Function definition.
```

## Parameters

`param1` Parameter description.

## Return Value

Return value description.

## Example

```c++
Example code.
    SELECTIONDATA sel;		// Define Address the slected line in the Assembly window ( begin , End )
		GuiSelectionGet(GUI_DISASSEMBLY, &sel); // Get the value of sel(begin addr , End addr )
		duint pagesize=DbgMemGetPageSize(sel.start);  // get the page size of the section from the selected memory addr
		duint sctionbase = DbgMemFindBaseAddr(sel.start, &pagesize); // get the base of this section ( begin addr of the section )
```

## Related functions

- List of related functions
