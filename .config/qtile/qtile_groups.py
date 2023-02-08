# QTILE Groups definition
# Dusan Ilic 2021

from libqtile.config import Group, ScratchPad, DropDown

# The groups variable is used to define groups
# Index in the list starting from 1 determines the
# keybinding used to manage the group
groups = [
    Group('1'),
    Group('2'),
    Group('3'),
    Group('4'),
    Group('5'),
    Group('6'),
    Group('7'),
    Group('8'),
    Group('9'),
    ScratchPad(
        'scratchpad',
        [DropDown(
            'ranger_scratchpad',
            'xterm -e ranger',
            height=0.6,
            width=0.9,
            x=0.05,
            y=0,
            on_focus_lost_hide=True,),
         DropDown(
            'ssh_scratchpad',
            'st -e ssh -YC user@192.168.0.120',
            height=0.6,
            width=0.9,
            x=0.05,
            y=0.2,
            on_focus_lost_hide=True,)]),
]
