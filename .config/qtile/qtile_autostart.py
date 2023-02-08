# QTILE Autostart File
# Dusan Ilic 2021

# This file defines the autostart startup hooks to be executed
# on system startup

# startup_once hooks are executed only on system startup, while
# startup hooks are also executed each time qtile is renewed

from libqtile import hook

@hook.subscribe.startup
def autostart():
    import os
    # Set wallpaper
    os.system("set_wallpaper")
