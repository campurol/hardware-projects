# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x202000, '7', 'KC', ['7']),
        (0x202000, '8','KC',  ['8']),
        (0x202000, '9', 'KC', ['9']),
        # 2nd row ----------
        (0x202000, '4', 'KC', ['4']),
        (0x202000, '5','KC',  ['5']),
        (0x202000, '6','KC',  ['6']),
        # 3rd row ----------
        (0x202000, '1','KC',  ['1']),
        (0x202000, '2', 'KC', ['2']),
        (0x202000, '3', 'KC', ['3']),
        # 4th row ----------
        (0x101010, '*', 'KC', ['*']),
        (0x800000, '0', 'KC', ['0']),
        (0x101010, '#', 'KC', ['#']),
        # Encoder button ---
        (0x000000, '','KC',  [Keycode.BACKSPACE])
    ]
}
