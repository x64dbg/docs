Translate the x64dbg
====================
The x64dbg GUI is currently available in multiple languages. The launcher is available in both English and Chinese.

You may want to use x64dbg with your mother language. Here are the steps to do it:

1. Download http://translate.x64dbg.com/download/project/x64dbg.zip
2. Open x64dbg and check the [Engine] Language section in the INI:

::

    [Engine]
    BreakpointType=0
    CalculationType=1
    DisableDaatabaseCompression=0
    EnableDebugPrivilege=0
    EnableSourceDebugging=1
    Language=nl_NL  ←here
    ListAllPages=0
    SaveDatabaseInProgramDirectory=0
    TimeWastedDebugging=12C
    UndecorateSymbolNames=1
    ...

3. Copy a translated x64dbg.ts to x64dbg_nl_NL.ts (replace with your language) 
4. Install Qt and run the command : `lrelease x64dbg_nl_NL.ts`
5. Copy the generated QM file in the translations folder: `x64dbg\\release\\translations\\`
6. Your interface should now be translated.

You can contribute your translations at http://translate.x64dbg.com
