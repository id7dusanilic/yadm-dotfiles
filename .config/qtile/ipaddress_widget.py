import subprocess
from libqtile import bar
from libqtile.widget import base


class IPAddress(base.ThreadPoolText):
    """Widget that displays IPV4 address of a given interface"""

    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ("interface", "wlan0", "Interface Name"),
        ("padding", 3, "Padding left and right. Calculated if None."),
        ("update_interval", 5, "Update time in seconds."),
        ("format", '[ {interface}: {ipaddress} ]', "Output format."),
    ]

    def __init__(self, **config) -> None:
        base.ThreadPoolText.__init__(self, "", **config)
        self.add_defaults(self.defaults)

        self._ipaddress = "a"

    def poll(self) -> str:
        """Determine the text to display

        Function returning a string with IPV4 address of a given interface.
        """
        if self.get_ipaddr():
            return self.format.format(interface=self.interface.upper(), ipaddress=self.get_ipaddr())
        else:
            return ""

    def get_ipaddr(self):
        return subprocess.check_output(
                f"ifconfig | grep {self.interface} -A 1 | grep 'inet ' | awk '{{print $2}}'",
                shell=True,
                encoding='utf8',
                )[:-1]
