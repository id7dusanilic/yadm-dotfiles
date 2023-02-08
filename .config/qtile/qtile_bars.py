# QTILE Bars Definitions
# Dusan Ilic 2021

from libqtile import bar, widget, qtile
from qtile_colors import *
from ipaddress_widget import IPAddress
from custom_volume_widget import CustomVolume

import psutil

interfaces = list(psutil.net_if_addrs().keys())
interfaces.remove('lo')


# Shared monitors
battery_monitor = \
    widget.Battery(
        battery=0,
        charge_char='CHR',
        discharge_char='BAT',
        empty_char='BAT',
        full_char='BAT',
        unknown_char='BAT',
        update_interval=5,
        notify_below=10,
        format='[ {char}: {percent:2.0%} ]',
        padding=5,
    )

RAM_monitor = \
    widget.Memory(
        format='[ RAM: {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm} ]',
        padding=5,
    )

clock = \
    widget.Clock(
        format='%H:%M:%S',
        padding=10,
    )

calendar = \
    widget.Clock(
        format='%a, %B %d',
        padding=10,
    )


def basic_elements():
    tmp = [
        widget.GroupBox(
            active=colors[3],
            inactive=colors[2],
            block_highlight_text_color=colors[3],
            disable_drag=True,
            highlight_method='block',
            this_screen_border=colors[0],
            this_current_screen_border=colors[0],
            other_current_screen_border=colors[1],
            other_screen_border=colors[1],
            padding=5,
            border=0,
            hide_unused=True,
        ),
        widget.CurrentLayoutIcon(
            scale=0.7,
        ),
        widget.CurrentScreen(
            active_text='',
            inactive_text=' ',
            active_color=colors[0],
        ),
        widget.TaskList(
            highlight_method="block",
            icon_size=0,
            border=colors[0],
            padding_y=0,
            rounded=False,
            unfocused_border="#444444",
            title_width_method="uniform"
        ),
        widget.Spacer(),
        calendar,
        clock,
    ]
    return tmp


def status_elements():
    tmp = [
        widget.GroupBox(
            active=colors[3],
            inactive=colors[2],
            block_highlight_text_color=colors[3],
            disable_drag=True,
            highlight_method='block',
            this_screen_border=colors[0],
            this_current_screen_border=colors[0],
            other_current_screen_border=colors[1],
            other_screen_border=colors[1],
            padding=5,
            border=0,
            hide_unused=True,
        ),
        widget.CurrentLayoutIcon(
            scale=0.7,
        ),
        widget.CurrentScreen(
            active_text='',
            inactive_text=' ',
            active_color=colors[0],
        ),
        widget.TaskList(
            highlight_method="block",
            icon_size=0,
            border=colors[0],
            padding_y=0,
            rounded=False,
            unfocused_border="#444444",
            title_width_method="uniform"
        ),
        widget.Spacer(),
        widget.CPU(
            padding=5,
            fmt='[ CPU: {} ]',
            format='{freq_current}GHz {load_percent}%'
        ),
        widget.ThermalSensor(
            padding=5,
            tag_sensor='Package id 0',
            update_interval=1,
            fmt='[ CPU: {} ]',
        ),
        widget.NvidiaSensors(
            padding=5,
            fmt='[ GPU: {} ]',
            format='{temp}.0°C',
            update_interval=1,
        ),
        *[IPAddress(
            interface=iface,
            padding=5,
        ) for iface in interfaces],
        widget.Wlan(
            interface='wlan0',
            disconnected_message='[ WIFI: Disconnected ]',
            format='[ WIFI: {essid} {percent:2.0%} ]',
        ),
        CustomVolume(
            padding=5,
        ),
        RAM_monitor,
        battery_monitor,
        widget.KeyboardLayout(
            fmt='[ {} ]',
            padding=5,
            display_map={'us': 'US', 'rs': 'PC', 'rs latin': 'RS'},
        ),
        calendar,
        clock,
        widget.Image(
            filename="~/.config/qtile/clarity-shutdown-icon.svg",
            margin=5,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("dmenu_system")}
        ),
    ]
    return tmp


# Bar definitions
def sec_bar():
    tmp_bar = bar.Bar(
        basic_elements(),
        size=24,
        background=color_dark_gray,
        opacity=1,
    )
    return tmp_bar


def main_bar():
    tmp = status_elements()
    tmp.append(widget.Systray())
    tmp_bar = bar.Bar(
        tmp,
        size=24,
        background=color_dark_gray,
        opacity=1,
    )
    return tmp_bar
