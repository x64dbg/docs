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

--------
Examples
--------

- ``rax: {rax}`` formats to ``rax: 4C76``
- ``password: {s:4*ecx+0x402000}`` formats to ``password: L"s3cret"``