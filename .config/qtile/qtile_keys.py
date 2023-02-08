# QTILE Keybindings definitions
# Dusan Ilic 2021

from libqtile.config import Key, ScratchPad
from libqtile.lazy import lazy

# To define keybindings for group managment
from qtile_groups import groups

# Mod key - super
mod = "mod4"

# Using the environment variable to spawn terminal
terminal = "sh -c $TERM_EMULATOR"

# The keys variable defines key bindings
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.shrink_main(), lazy.layout.grow_left(), desc="Grow window to the left (Columns), Shrink master (Monad)"),
    Key([mod, "control"], "l", lazy.layout.grow_main(), lazy.layout.grow_right(), desc="Grow window to the right (Columns), Grow maser (Monad)"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), lazy.layout.shrink(), desc="Grow window down (Columns), shrink secondary (Monad)"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), lazy.layout.grow(), desc="Grow window up (Columns), grow secondary (Monad)"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Focus screens
    Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
    Key([mod], "comma", lazy.prev_screen(), desc="Move focus to next monitor"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle split"),

    # Spawn terminal emulator
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "o", lazy.to_layout_index(0), desc="Layout with index 0"),
    Key([mod], "t", lazy.to_layout_index(1), desc="Layout with index 1"),
    Key([mod], "m", lazy.to_layout_index(2), desc="Layout with index 2"),
    Key([mod], "u", lazy.to_layout_index(3), desc="Layout with index 3"),

    # Kill focused window
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    # Toggle bar visibility
    Key([mod], "b", lazy.hide_show_bar(), desc="Toggle bar visibility"),

    # Exit and restart qtile
    Key([mod, "shift"], "Escape", lazy.restart(), desc="Restart Qtile"),
    Key([mod], "Escape", lazy.shutdown(), desc="Shutdown Qtile"),

    # Spawn programs using dmenu
    # Key([mod], "p", lazy.spawn("dmenu_run"), desc="Spawn dmenu_run"),

    # Spawn programs using dmenu
    Key([mod], "p", lazy.spawn("rofi -show run"), desc="Spawn rofi"),

    # Toggle ranger scratchpad
    Key([mod], 's', lazy.group['scratchpad'].dropdown_toggle('ranger_scratchpad')),

    # Toggle ssh scratchpad
    Key([mod, "shift"], 's', lazy.group['scratchpad'].dropdown_toggle('ssh_scratchpad')),
]

for index, g in enumerate(groups):
    if not isinstance(g, ScratchPad):
        keys.extend(
            [
                # Focus group on current screen
                Key([mod], str(index + 1), lazy.group[g.name].toscreen(), desc=f"Focus group {g.name} on screen"),

                # Move current window to group
                Key([mod, "shift"], str(index + 1), lazy.window.togroup(g.name), desc=f"Move focused window to group {g.name}")
            ]
        )
