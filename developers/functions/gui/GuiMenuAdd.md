# GuiMenuAdd

This function adds a new child menu to a menu.

```c++
int GuiMenuAdd(int hMenu, const char* title)
```

## Parameters

`hMenu` Menu handle from a previously-added menu or from the main menu.

`title` A const char repesenting the text title of the menu item to be added.

## Return Value

Returns the menu handle (unique), or -1 on failure.

## Example

```c++
hNewMenu = GuiMenuAdd(hMenu, &szMenuTitle);
```

## Related functions

- [GuiMenuAddEntry](./GuiMenuAddEntry.md)
- [GuiMenuAddSeparator](./GuiMenuAddSeparator.md)
- [GuiMenuClear](./GuiMenuClear.md)
- [GuiMenuSetEntryIcon](./GuiMenuSetEntryIcon.md)
- [GuiMenuSetIcon](./GuiMenuSetIcon.md)

Note: Plugin developers should make use of the plugin functions provided:

- [plugin_menuadd](../../plugins/API/menuadd.rst)
- [plugin_menuaddentry](../../plugins/API/menuaddentry.rst)
- [plugin_menuaddseparator](../../plugins/API/menuaddseparator.rst)
- [plugin_menuclear](../../plugins/API/menuclear.rst)
- [plugin_menuentryseticon](../../plugins/API/menuentryseticon.rst)
- [plugin_menuseticon](../../plugins/API/menuseticon.rst)