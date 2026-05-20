from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction, Color, Button
from pybricks.tools import wait, run_task, multitask
from pybricks.iodevices import XboxController
from pybricks.robotics import Car
from pybricks.iodevices import PUPDevice


Scholars ={'good': {'drive': Port.E, 'steer': Port.A, 'ultrasonic': Port.C, 'color': Color.GREEN, 'drive_direction': Direction.COUNTERCLOCKWISE},
           'experiment':  {'drive': Port.E, 'steer': Port.A, 'ultrasonic': None, 'color': Color.RED, 'drive_direction': Direction.CLOCKWISE}
}

ports = [Port.A,Port.B,Port.C,Port.D,Port.E,Port.F]

hub = PrimeHub()
controller=XboxController()
#headlamps_toggle = 0
pressed = []
while not any(pressed):
    pressed = hub.buttons.pressed()
    #print(pressed)
    #for port in ports:
    #    try:
    #        device = PUPDevice(port)
    #        print(f"{port}, {device.info()["id"]}")
    #        #print(device.info())
    #        #print()
    #    except OSError:
    #        pass
    #print(type(PUPDevice(Port.C).info()["id"]))
    if (Button.LEFT in pressed):# or (PUPDevice(Port.C).info()["id"] == 62):
        scholar_mode = Scholars['good']
    elif Button.RIGHT in pressed:
        scholar_mode = Scholars['experiment']

    try:
        # Initialize.
        drive = Motor(scholar_mode['drive'], positive_direction=scholar_mode['drive_direction'])
        steer = Motor(scholar_mode['steer'], positive_direction=Direction.CLOCKWISE)

        car = Car(steer, drive)

        try:
            eyes = UltrasonicSensor(scholar_mode['ultrasonic'])
            #eyes.lights.on(100)
        except OSError:
            pass
        except TypeError:
            pass

        hub.speaker.beep(frequency=1000, duration=100)
        hub.light.on(scholar_mode['color'])

        if any(pressed):
            pressed=[]
            break
    except NameError:
        pass



def obstacle_warning(UltrasonicSensor, Controller):
    
    distance = UltrasonicSensor.distance()
    if distance <= 100:
        Controller.rumble(power = (100-distance), duration = 300)
    #pass

def headlamps(value):
    value = value % 8

    value_options = {
        1: [0,0,0,0], 
        3: [100,100,0,0], 
        5: [0,0,100,100],
        7: [100,100,100,100]
    }
    if value != 0:
        return value_options[value]
    else:
        return value_options[1]

def trim_or_turbo(power, pressed_button):
    if 'Button.A' in str(pressed_button):
        return power
    elif 'Button.Y' in str(pressed_button):
        return power*0.25
    else:
        return power*0.75

async def steering():
    pass

def main():
    while True:
        #print(controller.dpad())
        if controller.dpad():
            #headlamps_toggle += controller.dpad()
            try:
                eyes.lights.on(headlamps(controller.dpad()))
            except NameError:
                pass

        drive_power_R = controller.triggers()[1] # Right Trigger Forward
        drive_power_L = -controller.triggers()[0] # Left Trigger Reverse
        drive_power = drive_power_R + drive_power_L
        steer_input_R = controller.joystick_right()[0]  # Horizontal only
        steer_input_L = controller.joystick_left()[0]  # Horizontal only
        combined_steer = steer_input_R + steer_input_L
        steer_input = max(-100, min(combined_steer, 100))
        #print(f"Steer: {steer_input} \t Left Steer: {steer_input_L} \t Right Steer {steer_input_R}")
        #print(f"D Pad: {controller.buttons.pressed()}")

        car.drive_power(trim_or_turbo(drive_power, controller.buttons.pressed()))
        car.steer(steer_input)


        try:
            obstacle_warning(Controller=controller,UltrasonicSensor=eyes)
        except:
            pass

        wait(2)

main()