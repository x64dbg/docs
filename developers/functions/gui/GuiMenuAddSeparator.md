# GuiMenuAddSeparator

Adds a menu separator to a menu.

```c++
void GuiMenuAddSeparator(int hMenu)
```

## Parameters

`hMenu` Menu handle from a previously-added menu or from the main menu.

## Return Value

This function does not return a value.

## Example

```c++
hNewMenu = GuiMenuAdd(hMenu, &szMenuTitle);
GuiMenuAddEntry(hNewMenu, &szMenuEntry1Text);
GuiMenuAddEntry(hNewMenu, &szMenuEntry2Text);
GuiMenuAddSeparator(hNewMenu);
GuiMenuAddEntry(hNewMenu, &szMenuEntry3Text);
GuiMenuAddEntry(hNewMenu, &szMenuEntry4Text);

```

## Related functions

- [GuiMenuAdd](./GuiMenuAdd.md)
- [GuiMenuAddEntry](./GuiMenuAddEntry.md)
- [GuiMenuClear](./GuiMenuClear.md)
- [GuiMenuSetEntryIcon](./GuiMenuSetEntryIcon.md)
- [GuiMenuSetIcon](./GuiMenuSetIcon.md)

Note: Plugin developers should make use of the plugin functions provided:

- [_plugin_menuadd](../../plugins/API/menuadd.rst)
- [_plugin_menuaddentry](../../plugins/API/menuaddentry.rst
- [_plugin_menuaddseparator](../../plugins/API/menuaddseparator.rst
- [_plugin_menuclear](../../plugins/API/menuclear.rst
- [_plugin_menuentryseticon](../../plugins/API/menuentryseticon.rst
- [_plugin_menuseticon](../../plugins/API/menuseticon.rst