#!/bin/bash

# Set environment variables
export PATH=$PATH:$HOME/.local/bin/dmenu_scripts:$HOME/.local/bin/scripts:$HOME/.local/bin

# Default text editor
export EDITOR=nvim
export VISUAL=nvim

# Default browser
# export BROWSER=firefox
export BROWSER=qutebrowser

# Default terminal emulator, to be used by other scripts
export TERM_EMULATOR=st

# dmenu command used in scripts
export DMENU_COMMAND="rofi -dmenu"

# XDG Base directories
export XDG_CONFIG_HOME=$HOME/.config
export XDG_CACHE_HOME=$HOME/.cache
export XDG_DATA_HOME=$HOME/.local/share

# ~ Clean-up
export WGETRC="$HOME/.config/wget/wgetrc"
export LESSHISTFILE="-"
export PYLINTHOME="$XDG_CACHE_HOME"
export NPM_CONFIG_USERCONFIG="$XDG_CONFIG_HOME/npm/npmrc"
export GNUPGHOME="$XDG_DATA_HOME/gnupg"
export JUPYTER_CONFIG_DIR="$XDG_CONFIG_HOME/jupyter"
export XAUTHORITY="$XDG_RUNTIME_DIR/Xauthority"
export HISTFILE="$XDG_DATA_HOME/bash/history"

[ -d ${GNUPGHOME} ] || mkdir -p ${GNUPGHOME}
[ -d ${JUPYTER_CONFIG_DIR} ] || mkdir -p ${JUPYTER_CONFIG_DIR}
[ -d ${XDG_DATA_HOME}/bash ] || mkdir -p ${XDG_DATA_HOME}/bash

