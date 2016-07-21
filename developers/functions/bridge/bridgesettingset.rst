================
BridgeSettingSet 
================
Writes a string value to an ini file's section for a specified key.

::

	bool BridgeSettingSet(
	const char* section, // ini section name to write to
	const char* key, // ini key in the section to write
	char* value // string value to write
	);

----------
Parameters
----------

:section: ini section name to write to

:key: ini key in the section to write

:value: string value to write

-------------
Return Values
-------------
This function returns true if successful or false otherwise.

