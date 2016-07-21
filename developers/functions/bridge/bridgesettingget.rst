================
BridgeSettingGet 
================
Reads an ini file section for a specified key and return the string value associated with that key.

::

	bool BridgeSettingGet(
	const char* section, // ini section name to read
	const char* key, // ini key in the section to read
	char* value // string to hold the value read
	);

----------
Parameters
----------

:section: ini section name to read

:key: ini key in the section to read

:value: string to hold the value read

-------------
Return Values
-------------
This function returns true if successful or false otherwise.

