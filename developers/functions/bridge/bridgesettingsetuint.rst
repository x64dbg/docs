====================
BridgeSettingSetUint 
====================
Writes an integer value to an ini file's section for a specified key.

::

	bool BridgeSettingSetUint(
	const char* section, // ini section name to write to
	const char* key, // ini key in the section to write
	duint* value // an integer variable to hold the value read
	);

----------
Parameters
----------

:section: ini section name to write to

:key: ini key in the section to write

:value: an integer variable to write

-------------
Return Values
-------------
This function returns true if successful or false otherwise.
