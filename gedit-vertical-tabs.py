from gi.repository import GObject, Gtk, Gedit
import os, subprocess

def widget_search(curr, tgt_name):
    widgets = []
    if tgt_name in curr.get_name():
        widgets.append(curr)
    if isinstance(curr, Gtk.Container):
        for widget in curr.get_children():
            widgets.extend(widget_search(widget, tgt_name))
    return widgets


class VerticalTabsPlugin(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "VerticalTabsPlugin"
    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        widget_search(self.window, "GeditNotebook") [0].set_tab_pos(Gtk.PositionType.LEFT)

    def do_deactivate(self):
        widget_search(self.window, "GeditNotebook") [0].set_tab_pos(Gtk.PositionType.TOP)

