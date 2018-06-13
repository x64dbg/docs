# GuiMenuSetEntryIcon

Sets an icon for a specified menu entry.

```c++
void GuiMenuSetEntryIcon(int hEntry, const ICONDATA* icon)
```

## Parameters

`hEntry` Parameter description.

`icon` 

## Return Value

This function does not return a value.

## Example

```c++
ICONDATA rocket;
rocket.data = icon_rocket;
rocket.size = sizeof(icon_rocket);
hNewMenuEntry = GuiMenuAddEntry(hMenu, &szMenuEntryText);
GuiMenuSetEntryIcon(hNewMenuEntry,&rocket);
```

## Related functions

- [GuiMenuAdd](./GuiMenuAdd.md)
- [GuiMenuAddEntry](./GuiMenuAddEntry.md)
- [GuiMenuAddSeparator](./GuiMenuAddSeparator.md)
- [GuiMenuClear](./GuiMenuClear.md)
- [GuiMenuSetIcon](./GuiMenuSetIcon.md)

Note: Plugin developers should make use of the plugin functions provided:

- [plugin_menuadd](../../plugins/API/menuadd.rst)
- [plugin_menuaddentry](../../plugins/API/menuaddentry.rst)
- [plugin_menuaddseparator](../../plugins/API/menuaddseparator.rst)
- [plugin_menuclear](../../plugins/API/menuclear.rst)
- [plugin_menuentryseticon](../../plugins/API/menuentryseticon.rst)
- [plugin_menuseticon](../../plugins/API/menuseticon.rst)