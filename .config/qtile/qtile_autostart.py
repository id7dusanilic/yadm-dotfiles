# QTILE Autostart File
# Dusan Ilic 2021

# This file defines the autostart startup hooks to be executed
# on system startup

# startup_once hooks are executed only on system startup, while
# startup hooks are also executed each time qtile is renewed

import os
from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    # Setup monitors
    # os.system("xrandr --output HDMI-2 --primary --left-of eDP-1")
    # Set wallpaper
    # os.system("set_wallpaper")
    # Setup keybindings
    # os.system("sxhkd -m 1 &")
    # Start systray network manager
    # os.system("nm-applet &")
    # Allow transparent windows
    # os.system("xcompmgr &")
    # Initialize keyboard layout
    # os.system("keyboard_layout --set us")
    pass
