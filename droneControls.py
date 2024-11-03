# Could be used with a input timeout feature
from timedinput import timedinput

class Move:
    def roll_right():
        print("ROLL RIGHT")

    def roll_left():
        print("ROLL LEFT")

    def pitch_forward():
        print("PITCH FORWARD")

    def pitch_backward():
        print("PITCH BACKWARD")

    def yaw_right():
        print("YAW RIGHT")

    def yaw_left():
        print("YAW LEFT")

    def throttle_increase():
        print("THROTTLE INCREASE")

    def throttle_decrease():
        print("THROTTLE DECREASE")

def await_key_press():
    key_pressed = input()
    if key_pressed == 'l':
        Move.roll_right()
    elif key_pressed == 'j':
        Move.roll_left()
    elif key_pressed == 'i':
        Move.pitch_forward()
    elif key_pressed == 'k':
        Move.pitch_backward()
    elif key_pressed == 'd':
        Move.yaw_right()
    elif key_pressed == 'a':
        Move.yaw_left()
    elif key_pressed == 'w':
        Move.throttle_increase()
    elif key_pressed == 's':
        Move.throttle_decrease()

if __name__ == '__main__':
    while 1:
        await_key_press()