String Formatting
=================

This section explains the simple string formatter built into x64dbg.

The basic syntax is ``{?:expression}`` where ``?`` is the optional type of the expression. The default type is ``x``. To output ``{`` or ``}`` in the result, escape them as ``{{`` or ``}}``.

-----
Types
-----

- ``d`` signed **d**\ ecimal: ``-3``
- ``u`` **u**\ nsigned decimal: ``57329171``
- ``p`` zero prefixed **p**\ ointer: ``0000000410007683``
- ``s`` **s**\ tring pointer: ``this is a string``
- ``x`` he\ **x**: ``3C28A``
- ``a`` **a**\ ddress info: ``00401010 <module.EntryPoint>``
- ``i`` **i**\ nstruction text: ``jmp 0x77ac3c87``

------------
Complex Type
------------

``{mem;size@address}`` will print the ``size`` bytes starting at ``address`` in hex.

``{winerror@code}`` will print the name of windows error code(returned with ``GetLastError()``) and the description of it(with ``FormatMessage``). It is similar to ErrLookup utility.

``{ntstatus@code}`` will print the name of NTSTATUS error code and the description of it(with ``FormatMessage``).

--------
Examples
--------

- ``rax: {rax}`` formats to ``rax: 4C76``
- ``password: {s:4*ecx+0x402000}`` formats to ``password: L"s3cret"``

-------
Plugins
-------

Plugins can use ``_plugin_registerformatfunction`` to register custom string formatting functions. The syntax is ``{type;arg1;arg2;argN@expression}`` where ``type`` is the name of the registered function, ``argN`` is any string (these are passed to the formatting function as arguments) and ``expression`` is any valid expression.
