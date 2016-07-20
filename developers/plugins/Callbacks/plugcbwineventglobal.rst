PLUG_CB_WINEVENTGLOBAL
======================
Called before TranslateMessage and DispatchMessage Windows functions (PreTranslateMessage). 

Avoid calling user32 functions without precautions here, there will be a recursive call if you fail to take countermeasures. 

This function is global, so it also captures hotkeys (see Qt documentation)

::

    struct PLUG_CB_WINEVENTGLOBAL
    {
        MSG* message;
        bool retval; //only set this to true, never to false
    };
