_plugin_menuentrysetchecked
===========================
This function sets the checked state of a menu entry.

::

    void _plugin_menuentrysetchecked (
    int pluginHandle, //plugin handle
    int hEntry, //handle of the menu entry
    bool checked //new checked state
    ); 

Parameters
----------
:pluginHandle: Handle of the calling plugin.
:hEntry: Menu handle from a previously-added child menu or from the main plugin menu.
:checked: New checked state.

Return Values
-------------
This function does not return a value.
