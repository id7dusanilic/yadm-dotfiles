import subprocess
from libqtile import bar
from libqtile.widget import base


class CustomVolume(base.ThreadPoolText):
    '''Widget that displays volume'''

    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ('padding', 3, 'Padding left and right. Calculated if None.'),
        ('update_interval', 1, 'Update time in seconds.'),
        ('format', '[ VOL: {volume} ]', 'Output format.'),
    ]

    def __init__(self, **config) -> None:
        base.ThreadPoolText.__init__(self, '', **config)
        self.add_defaults(self.defaults)

    def poll(self) -> str:
        '''Determine the text to display

        Function returning a string with the volume
        '''
        if self.get_mute():
            return self.format.format(volume='M')
        else:
            return self.format.format(volume=self.get_volume()+'%')

    def get_volume(self):
        return subprocess.check_output(
                f'pamixer --get-volume',
                shell=True,
                encoding='utf8')[:-1]

    def get_mute(self):
        try:
            res = subprocess.check_output(
                    f'pamixer --get-mute',
                    shell=True,
                    encoding='utf8')
            return True if res == 'false' else False
        except subprocess.CalledProcessError:
            return False
