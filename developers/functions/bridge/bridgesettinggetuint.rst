====================
BridgeSettingGetUint 
====================
Reads an ini file section for a specified key and return the integer value associated with that key.

::

	bool BridgeSettingGetUint(
	const char* section, // ini section name to read
	const char* key, // ini key in the section to read
	duint* value // an integer variable to hold the value read
	);

----------
Parameters
----------

:section: ini section name to read

:key: ini key in the section to read

:value: an integer variable to hold the value read

-------------
Return Values
-------------
This function returns true if successful or false otherwise.

