import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        if color.upper() in COLOR_NAMES:
            self.rgb = COLOR_NAMES[color.upper()]
        else:
            self.rgb = None

    @staticmethod
    def hex2rgb(hex):
        """Class method that converts a hex value into an rgb one"""
        value = hex.lstrip('#')
        lv = len(value)
        if not lv == 6:
            raise ValueError
        return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))

    @staticmethod
    def rgb2hex(rgb):
        if not type(rgb) == tuple:
            raise ValueError
        for elem in rgb:
            int(elem)
            if not 0.0 <= elem/255 <= 1.0:
                raise ValueError

        """Class method that converts an rgb value into a hex one"""
        return '#%02x%02x%02x' % rgb

    def __repr__(self):
        """Returns the repl of the object"""
        return ("Color('{}')".format(self.color))

    def __str__(self):
        """Returns the string value of the color object"""
        if not self.rgb:
            return 'Unknown'
        else:
            return str(self.rgb)
