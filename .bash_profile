#
# ~/.bash_profile
#

# Setup environment
[ -f ${HOME}/.local/share/setup_env.sh ] && . ${HOME}/.local/share/setup_env.sh

[[ -f ${HOME}/.bashrc ]] && . ${HOME}/.bashrc

# Start X server after login on tty1
if [[ -z ${DISPLAY} ]] && [[ $(tty) = /dev/tty1 ]]; then
	startx
fi
