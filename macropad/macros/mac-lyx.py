# MACROPAD Hotkeys example: Safari web browser for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode


app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Lyx', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Cite', [Keycode.COMMAND, Keycode.OPTION, 'c']),
        (0x004000, '', '', False),
        (0x400000, 'Paste', [Keycode.COMMAND, Keycode.OPTION, Keycode.CONTROL, 'v']),      # Scroll up
        # 2nd row ----------
        (0x202000, 'Next', [ConsumerControlCode.SCAN_NEXT_TRACK]),
        (0x202000, 'Vol -', [ConsumerControlCode.VOLUME_DECREMENT]),
        (0x400000, 'Vol +', [ConsumerControlCode.VOLUME_INCREMENT]),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Label', [Keycode.COMMAND, Keycode.OPTION, Keycode.CONTROL, 'x']),
        (0x000040, 'CrossRef', [Keycode.COMMAND, Keycode.OPTION, Keycode.CONTROL, 'i']),
        (0x000040, 'Latex', [Keycode.COMMAND, 'l'], False),
        # 4th row ----------
        (0x101010, 'View', [Keycode.COMMAND, 'r']),   
        (0x101010, 'Save', [Keycode.COMMAND, 's']),   
        (0x101010, 'Export', [Keycode.COMMAND, Keycode.OPTION, 'e']), 
        # Encoder button ---
        (0x202000, 'Play', [ConsumerControlCode.PLAY_PAUSE]) # Close window/tab
    ]
}
