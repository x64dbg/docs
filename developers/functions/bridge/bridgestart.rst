===========
BridgeStart 
===========
Called after BridgeInit, this function reads in the .ini settings (if the .ini file exists, otherwise uses default setting values)
::

	const wchar_t* BridgeStart();

----------
Parameters
----------
This function has no parameters.

-------------
Return Values
-------------
Returns 0 if successful, otherwise a string indicating the error that occured.

