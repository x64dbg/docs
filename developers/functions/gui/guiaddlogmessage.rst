.. _GuiAddLogMessage:
================
GuiAddLogMessage
================
Adds a message to the log. The message will be shown in the log window and on the status bar at the bottom of x64dbg.

::

	void GuiAddLogMessage(
	const char* msg // string containg message to add to log
	);

----------
Parameters
----------
:msg: string containg message to add to log. Ensure that a carriage line and return feed are included with the string for it to properly display it.

-------------
Return Values
-------------
This function does not return a value.

-----------
C++ Example
-----------

::

	GuiAddLogMessage(tr("This text will be displayed in the log view.\n").toUtf8().constData());

------------
Masm Example
------------

::

	.data
	szMsg db "This text will be displayed in the log view",13,10,0 ; CRLF
	
	.code
	Invoke GuiAddLogMessage, Addr szMsg

--------
See Also
--------
:ref:`GuiLogClear <GuiLogClear>`
