log
===
Put information in the log.

arguments
---------
[arg1]: Format string (see down for more information). When not specified, a newline will be logged.
[argN]: Data for the format string.

format string
-------------
A format string like "Info 1: {0}, Info 2: {1}\n Info 3:{2}". In place of {n} the n-th argument after the format string is inserted. You can specify how to format the inserted data by prepending a format type: "{s:0}" logs a string. Other types are: "d" (log as signed decimal), "u" (log as unsigned decimal), "p" (log as ????????).You can print a "{" by escaping it like "{{". Same for "{". "\n" inserts a newline.

result
------
This command does not set any result variables.
