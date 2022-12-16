#
# ~/.bashrc
#

# Do not source if the shell is not interactive
# [[ $- != *i* ]] && return

# Enable vi mode
# set -o vi

# Enable bash_completion
[ -r /usr/share/bash-completion/bash_completion ] && . /usr/share/bash-completion/bash_completion

LS_ALT=lsd

# General aliases to improve terminal
alias cp='cp -iv'               # confirm before overwriting something
alias mv='mv -iv'               # confirm before overwriting something
alias grep='grep --color=auto'  # add color to grep
alias ccat='highlight --out-format=ansi'    # Colored cat with syntax highlight

# add color to ls
case $LS_ALT in
    lsd)
        alias ls="$LS_ALT --color=auto --group-dirs first"
        ;;
    exa)
        alias ls="$LS_ALT --color=auto --group-directories-first"
        ;;
    *)
        alias ls='ls --color=auto --group-directories-first'
        ;;
esac
alias l.='ls -ld .*'            # list hidden files in long format
alias ll='ls -l '               # list in long format
alias la='ls -la'               # list all files in long format

# Misc aliases
alias gs='git status'
alias e='nvim'
alias eh="e $HISTFILE"
alias p="sudo pacman"
alias r="ranger"

# Allow root X Server access
xhost +local:root > /dev/null 2>&1

# Bash won't get SIGWINCH if another process is in the foreground.
# Enable checkwinsize so that bash will check the terminal size when
# it regains control.
shopt -s checkwinsize

# Auto cd into directories
shopt -s autocd

# Setup environment
[ -f $HOME/.local/share/setup_env.sh ] && source $HOME/.local/share/setup_env.sh

# Default terminal emulator, to be used by other scripts
export TERM_EMULATOR=/usr/local/bin/st

# History settings
shopt -s cmdhist                # multiple commands on one line show up as a single line
shopt -s histappend             # Enable history appending instead of overwriting
export HISTCONTROL=ignoreboth:erasedups   # ignore duplicates in command history
export HISTSIZE=1000            # increase history size to 1000 lines
export PROMPT_COMMAND="history -a; history -c; history -r"
export HISTIGNORE='ls*:ll*:la*:gs:pwd:history:clear:cd*:startx:htop:top:ranger:lsblk:neofetch:python:vim*:nvim*:e *:tmux:fg'

# Prompt style
export PS1="\[$(tput bold)\]\[$(tput setaf 2)\] \w \\$ \[$(tput sgr0)\]"
# export PS1="\[$(tput bold)\]\[$(tput setaf 2)\]>_ \u: \W \\$ \[$(tput sgr0)\]"
# export PS1="\u: \W $ "
# export PS1='\[\033[01;32m\][\u@\h\[\033[01;37m\] \W\[\033[01;32m\]]\$\[\033[00m\] '
# export PS1='\[\033[01;32m\][\u \W\[\033[01;32m\]]\$\[\033[00m\] '
