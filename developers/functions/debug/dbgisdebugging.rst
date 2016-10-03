==============
DbgIsDebugging
==============
Determines if the debugger is currently debugging an opened file or attached process.

::

	bool DbgIsDebugging();

----------
Parameters
----------
This function has no parameters.

-------------
Return Values
-------------
This function returns true if currently debugging, or false otherwise.

-----------
C++ Example
-----------

::

	if(!DbgIsDebugging())
	{
		GuiAddLogMessage(tr("You need to be debugging to use this option!\n").toUtf8().constData());
		break;
	}

------------
Masm Example
------------

::

	.data
	szMsg db "You need to be debugging to use this option!",13,10,0 ; CRLF
	
	.code
	Invoke DbgIsDebugging
	.IF eax == FALSE
		Invoke GuiAddLogMessage, Addr szMsg
	.ENDIF
