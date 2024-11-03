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

class Power:
    def power_on():
        print("Power turned on.")

    def power_off():
        print("Power turned off.")

    def power_switch():
        key_pressed = input("Power on? (y/n): ")
        if key_pressed == 'y':
            Power.power_on()
        elif key_pressed == 'n':
            Power.power_off()
        else:
            print("Invalid input.")

class GPS:
    latitude = 0.00
    longitude = 0.00
    altitude = 0.00

    def get_latitude():
        print(GPS.latitude)
    def get_longitude():
        print(GPS.longitude)
    def get_altitude():
        print(GPS.altitude)

    def set_latitude(lat):
        GPS.latitude = lat
    def set_longitude(lon):
        GPS.longitude = lon
    def set_altitude(alt):
        GPS.altitude = alt

if __name__ == '__main__':
    while 1:
        await_key_press()