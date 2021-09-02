# MACROPAD Hotkeys example: Safari web browser for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode


app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Lyx', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '', '','', False),
        (0x004000, '', '', '', False),
        (0x400000, 'Paste', 'KC', [Keycode.COMMAND, Keycode.OPTION, Keycode.CONTROL, 'v']),      # Scroll up
        # 2nd row ----------
        (0x202000, 'Cite', 'KC', [Keycode.COMMAND, Keycode.OPTION, 'c']),
        (0x202000, 'Foot', 'KC', [Keycode.CONTROL, Keycode.SHIFT, Keycode.COMMAND, 'f']),
        (0x400000, 'Margin', 'KC', [Keycode.COMMAND, Keycode.OPTION, Keycode.CONTROL, 'n']),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Label', 'KC', [Keycode.COMMAND, Keycode.OPTION, Keycode.CONTROL, 'x']),
        (0x000040, 'CrossRef', 'KC', [Keycode.COMMAND, Keycode.OPTION, Keycode.CONTROL, 'i']),
        (0x000040, 'Latex', 'KC', [Keycode.COMMAND, 'l'], False),
        # 4th row ----------
        (0x101010, 'View', 'KC', [Keycode.COMMAND, 'r']),   
        (0x101010, 'Master', 'KC', [Keycode.COMMAND, Keycode.OPTION, Keycode.CONTROL, 'r']),   
        (0x101010, 'Export', 'KC', [Keycode.COMMAND, Keycode.OPTION, 'e']), 
        # Encoder button ---
        (0x202000, 'Play', 'CC', [ConsumerControlCode.PLAY_PAUSE]) # Close window/tab
    ]
}
