import psutil
import socket

from libqtile import bar
from libqtile.widget import base


class IPAddress(base.ThreadPoolText):
    '''Widget that displays IPV4 address of a given interface'''

    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ('interface', 'wlan0', 'Interface Name'),
        ('padding', 3, 'Padding left and right. Calculated if None.'),
        ('update_interval', 5, 'Update time in seconds.'),
        ('format', '[ {interface}: {ipaddress} ]', 'Output format.'),
    ]

    def __init__(self, **config) -> None:
        base.ThreadPoolText.__init__(self, '', **config)
        self.add_defaults(self.defaults)

        self._ipaddress = 'a'

    def poll(self) -> str:
        '''Determine the text to display

        Function returning a string with IPV4 address of a given interface.
        '''
        if self.get_ipaddr():
            return self.format.format(interface=self.interface.upper(), ipaddress=self.get_ipaddr())
        else:
            return ''

    def get_ipaddr(self):
        ifaces = psutil.net_if_addrs()
        if self.interface in ifaces:
            if socket.AF_INET in [snicaddr.family for snicaddr in ifaces[self.interface]]:
                return ifaces[self.interface][0].address
            else:
                return ''
        else:
            return ''
