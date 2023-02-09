#!/bin/bash
#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)

export WM=bspwm


# Numlock on
numlockx on

# Read Xresources
xrdb $HOME/.config/X11/Xresources

# Initialize keyboard layout
keyboard_layout --set us

autorandr --change --default mobile

# Start Network Manager applet
command -v nm-applet &> /dev/null && nm-applet &

# Setup cursor
xsetroot -cursor_name left_ptr

# Set background
set_wallpaper

# Setup keybindings
case $WM in
    bspwm)
        pgrep -x sxhkd > /dev/null || sxhkd -m 1 $HOME/.config/sxhkd/bspwmrc &
        ;;
    *)
        pgrep -x sxhkd > /dev/null || sxhkd -m 1 &
        ;;
esac

# Start window manager
case $WM in
    qtile)
        exec qtile start
        ;;
    dwm)
        exec dwm
        ;;
    bspwm)
        export _JAVA_AWT_WM_NONREPARENTING=1
        exec bspwm
        ;;
    leftwm)
        exec dbus-launch leftwm
        ;;
    *)
        exit 1
        ;;
esac
