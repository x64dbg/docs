===========
BridgeAlloc 
===========
Allocates memory for reading in .ini setting values - this function is used in the BridgeSettingRead function.

::

	void* BridgeAlloc(
	size_t size // memory size to allocate
	);

----------
Parameters
----------

:size: memory size to allocate.

-------------
Return Values
-------------
Returns a pointer to the memory block allocated. If an error occurs allocating memory, then x64dbg is closed down.

