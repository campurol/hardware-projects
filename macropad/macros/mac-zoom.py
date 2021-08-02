# MACROPAD Hotkeys example: Safari web browser for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Zoom', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x800000, "Space", [Keycode.SPACEBAR]),  # Temporarily Unmute
        (0x202000, "Control", [Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND, 'h']),
        (0x800000, "Mute", [Keycode.COMMAND, Keycode.SHIFT, 'a']),  # Mute/Unmute Audio
        # 2nd row ----------
        (0x004000, "Video", [Keycode.SHIFT, Keycode.COMMAND, 'v']),  # Start/Stop Video
        (0x004000, "Camera", [Keycode.SHIFT, Keycode.COMMAND, 'n']),  # Switch Camera
        (0x004000, "Share", [Keycode.SHIFT, Keycode.COMMAND, 's']),  # Screen Sharing
        # 3rd row ----------
        (0x202000, "ID", [Keycode.COMMAND, '2']),  # Read Active Speaker Name
        (0x800000, "Record", [Keycode.SHIFT, Keycode.COMMAND, 'r']),  # Local Record
        (0x202000, "Capture", [Keycode.COMMAND, 't']),  # Chat Screenshot
        # 4th row ----------
        (0x101010, "FullSc", [Keycode.SHIFT, Keycode.COMMAND, 'f']),  # Full Screen
        (0x101010, "MinWin", [Keycode.SHIFT, Keycode.COMMAND, 'm']),  # Minimal
        (0x101010, "Gallery", [Keycode.SHIFT, Keycode.COMMAND, 'w']),  # View
        # Encoder button ---
        (0x000000, "", [Keycode.COMMAND, 'w']),  # Close Current Window
    ]
}





