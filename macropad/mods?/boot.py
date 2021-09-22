import storage
import digitalio
import board

k1 = digitalio.DigitalInOut(board.KEY1)
k1.switch_to_input(digitalio.Pull.UP)
if k1.value:
    storage.disable_usb_drive()
