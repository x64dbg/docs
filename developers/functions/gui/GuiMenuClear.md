# GuiMenuClear

This function removes all entries and child menus from a menu. It will not remove the menu itself.

```c++
void GuiMenuClear(int hMenu)
```

## Parameters

`hMenu` Menu handle from a previously-added menu or from the main menu.

## Return Value

This function does not return a value.

## Example

```c++
hNewMenu = GuiMenuAdd(hMenu, &szMenuTitle);
GuiMenuClear(hMenuNew);
```

## Related functions

- [GuiMenuAdd](./GuiMenuAdd.md)
- [GuiMenuAddEntry](./GuiMenuAddEntry.md)
- [GuiMenuAddSeparator](./GuiMenuAddSeparator.md)
- [GuiMenuSetEntryIcon](./GuiMenuSetEntryIcon.md)
- [GuiMenuSetIcon](./GuiMenuSetIcon.md)

Note: Plugin developers should make use of the plugin functions provided:

- [_plugin_menuadd](../../plugins/API/menuadd.rst)
- [_plugin_menuaddentry](../../plugins/API/menuaddentry.rst
- [_plugin_menuaddseparator](../../plugins/API/menuaddseparator.rst
- [_plugin_menuclear](../../plugins/API/menuclear.rst
- [_plugin_menuentryseticon](../../plugins/API/menuentryseticon.rst
- [_plugin_menuseticon](../../plugins/API/menuseticon.rst