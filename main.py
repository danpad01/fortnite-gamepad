import vgamepad as vg
import time

def main():
    gamepad = vg.VX360Gamepad()
    while True:
        gamepad.left_joystick(x_value=32767, y_value=32767)
        gamepad.right_joystick(x_value=32767, y_value=-32767)
        gamepad.update()
        time.sleep(5)

main()