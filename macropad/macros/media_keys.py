# MACROPAD Hotkeys: Media Keys

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control import ConsumerControl # REQUIRED if using ConsumerControlCode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode # REQUIRED if using ConsumerControlCode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Media Keys', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE   CONSUMER CONTROL
        # 1st row ----------
        (0xA50000, 'Play', 'CC', [ConsumerControlCode.PLAY_PAUSE], True),           # Play/Pause
        (0xA50000, 'Prev', 'CC', [ConsumerControlCode.SCAN_PREVIOUS_TRACK], True),  # Previous Track
        (0xA50000, 'Next', 'CC', [ConsumerControlCode.SCAN_NEXT_TRACK], True),      # Next Track
        # 2nd row ----------
        (0x000000, '', '', '', False),                                            # Not in use
        (0x000000, '','', '', False),                                            # Not in use
        (0x000000, '', '','', False),                                            # Not in use
        # 3rd row ----------
        (0x000000, '', '','', False),                                            # Not in use
        (0x000000, '','', '', False),                                            # Not in use
        (0x000000, '', '','', False),                                            # Not in use
        # 4th row ----------
        (0xA50000, 'Vol -','CC', [ConsumerControlCode.VOLUME_DECREMENT], True),    # Volume Down
        (0xA50000, 'Vol +','CC', [ConsumerControlCode.VOLUME_INCREMENT], True),    # Volume Up
        (0xA50000, 'Mute', 'CC', [ConsumerControlCode.MUTE], True),                 # Mute
        # Encoder# button ---
        (0x000000, '', '', '', False),                                            # Not in use
    ]
}