# docs

Documentation repository for [x64dbg](http://x64dbg.com) at [Read the Docs](https://readthedocs.org/projects/x64dbg).

## Building

1. `pip install sphinx recommonmark==0.4.0`
2. Add `relpath = relpath.replace(os.path.sep, '/')` to `C:\Python27\Lib\site-packages\recommonmark\transform.py` line `69`
3. run `makechm.bat`. It will build the .CHM help file.
