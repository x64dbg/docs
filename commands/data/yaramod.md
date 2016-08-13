# yaramod

Apply Yara rules to a module.

YARA is a tool aimed at (but not limited to) helping malware researchers to identify and classify malware samples. With YARA you can create descriptions of malware families (or whatever you want to describe) based on textual or binary patterns. Each description, a.k.a rule, consists of a set of strings and a boolean expression which determine its logic.

Yara is a separate project. You can view its documentation at [http://yara.readthedocs.io](http://yara.readthedocs.io). x64dbg also maintains a list of Yara signatures at [https://github.com/x64dbg/yarasigs](https://github.com/x64dbg/yarasigs).

## arguments

`arg1` Rules file to apply. This should be a full path.

`arg2` Name of the module to apply the rules to.

## result

This command does not set any result variables.
