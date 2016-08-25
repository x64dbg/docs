=====
Debug
=====

This menu contains the following actions. You cannot use any of these menu items except "**Restart**" and "**Command**" when you are not debugging.

---
Run
---

Execute the command :doc:`../../commands/debug-control/run`.

---------------------
Run (Pass exceptions)
---------------------

Execute the command :doc:`../../commands/debug-control/erun`.

-----------------------
Run (swallow exception)
-----------------------

Execute the command :doc:`../../commands/debug-control/serun`.

-------------------
Run until selection
-------------------

Place a single-shoot software breakpoint at the selected instruction, and then execute the command :doc:`../../commands/debug-control/run` to run the debuggee.

--------------------
Run until expression
--------------------

Enter an address. The debugger will then place a software breakpoint at that address, and then execute the command :doc:`../../commands/debug-control/run` to run the debuggee.

-----
Pause
-----

Try to pause the debuggee when it is running. The command for this action is :doc:`../../commands/debug-control/pause`.

-------
Restart
-------

Execute the command :doc:`../../commands/debug-control/InitDebug` with the most recent used file.

-----
Close
-----

Execute the command :doc:`../../commands/debug-control/StopDebug`.

-------------------
Change Command Line
-------------------

Display the current command line arguments of the debuggee in a dialog, and allow you to change it. The command line arguments will be saved in the database for later use.

---------
Step Into
---------

Execute the command :doc:`../../commands/debug-control/StepInto`.

---------------------------
Step Into (pass exceptions)
---------------------------

Execute the command :doc:`../../commands/debug-control/eStepInto`.

-----------------------------
Step Into (swallow exception)
-----------------------------

Execute the command :doc:`../../commands/debug-control/seStepInto`.

------------------
Step Into (source)
------------------

Step into, until another source line is reached. The command for this menu entry is ``TraceIntoConditional src.line(cip) && !src.disp(cip)``.

--------------------------
Trace into until condition
--------------------------

Enter an expression. The debugger will execute the command :doc:`../../commands/debug-control/TraceIntoConditional`. Also see :doc:`../../introduction/Expressions` for the legal expression format.

---------
Step Over
---------

Execute the command :doc:`../../commands/debug-control/StepOver`.

---------------------------
Step Over (pass exceptions)
---------------------------

Execute the command :doc:`../../commands/debug-control/eStepOver`.

-----------------------------
Step Over (swallow exception)
-----------------------------

Execute the command :doc:`../../commands/debug-control/seStepOver`.

------------------
Step Over (source)
------------------

Step over, until another source line is reached. The command for this menu entry is ``TraceOverConditional src.line(cip) && !src.disp(cip)``.

----------------
Run to User Code
----------------

Execute the command :doc:`../../commands/debug-control/RunToUserCode`.

--------------------------
Trace over until condition
--------------------------

Enter an expression. The debugger will execute the command :doc:`../../commands/debug-control/TraceOverConditional`. Also see :doc:`../../introduction/Expressions` for the legal expression format.

-------------------
Execute till return
-------------------

Step over the instructions, until the current instruction pointed to by ``EIP`` or ``RIP`` is ``ret`` instruction.

---------------------
Skip next instruction
---------------------

Execute the command :doc:`../../commands/debug-control/skip`.

------------
Trace Record
------------

---------------------
Undo last instruction
---------------------

Execute the command :doc:`../../commands/debug-control/InstrUndo`.

-------
Command
-------

Set focus to the command box at the bottom of the window, so that you can enter a command to execute.

-------------------
Hide debugger (PEB)
-------------------

Execute the command :doc:`../../commands/misc/HideDebugger`.