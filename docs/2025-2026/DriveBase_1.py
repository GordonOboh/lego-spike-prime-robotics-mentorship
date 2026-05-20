from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction, Color, Button, Stop
from pybricks.tools import wait, run_task, multitask
from pybricks.iodevices import XboxController
from pybricks.robotics import DriveBase, Car
from pybricks.iodevices import PUPDevice




# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.D)
motor_gripper = Motor(Port.E)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(motor_left, motor_right, wheel_diameter=56, axle_track=112)
controller=XboxController()
hub = PrimeHub()

hub.system.set_stop_button((Button.CENTER, Button.VIEW, Button.MENU, Button.GUIDE, Button.UPLOAD, Button.LB, Button.RB))

def transmission_manual(pressed_button, trim):
    #print(pressed_button)
    #print(type(pressed_button))
    pressed_button = str(pressed_button)
    print(pressed_button)
    if 'Button.UP' in pressed_button:
        trim += 0.5
        wait(200) 
    elif 'Button.DOWN' in pressed_button:
        trim -= 0.5
        wait(200) 

    return trim % 7

def gripper(pressed_button, mode = 'sure'):
    pressed_button = str(pressed_button)
    if mode == 'sure':
        if 'Button.B' in pressed_button:
            #motor_gripper.run_until_stalled(100, then=Stop.HOLD, duty_limit=25)
            motor_gripper.run_target(150, 45, then=Stop.HOLD, wait=False)
        elif 'Button.X' in pressed_button:
            #motor_gripper.run_until_stalled(-100, then=Stop.HOLD, duty_limit=25)
            motor_gripper.run_target(150, -45, then=Stop.HOLD, wait=False)

    elif mode == 'experimental':
        if 'Button.B' in pressed_button:
            motor_gripper.run_until_stalled(100, then=Stop.HOLD, duty_limit=25)
            print(motor_gripper.angle())
            rumble(power=(100,0,0,0), duration=300)
        elif 'Button.X' in pressed_button:
            motor_gripper.run_until_stalled(-100, then=Stop.HOLD, duty_limit=25)
            print(motor_gripper.angle())
            rumble(power=(0,100,0,0), duration=300)

        

def trim_or_turbo(power, pressed_button):
    pressed_button = str(pressed_button)
    if 'Button.A' in pressed_button:
        return power
    elif 'Button.Y' in pressed_button:
        return power*0.25
    else:
        return power*0.75

def rumble(power = 70, duration = 300):
    return controller.rumble(power = power, duration = duration)

def drive_power_calc(trim):
    drive_power_R = controller.triggers()[1] # Right Trigger Forward
    drive_power_L = -controller.triggers()[0] # Left Trigger Reverse
    drive_power = (drive_power_R + drive_power_L) * trim
    rumble(power=(0,0,(-1*drive_power_L),drive_power_R), duration=300)
    return drive_power

def drive_steer_calc():
    steer_input_R = controller.joystick_right()[0]  # Horizontal only
    steer_input_L = controller.joystick_left()[0]  # Horizontal only
    combined_steer = steer_input_R + steer_input_L
    steer_input = max(-100, min(combined_steer, 100))
    return steer_input

def shutdown(pressed_button):
    pressed_button = str(pressed_button)
    SHUTDOwN_BUTTONS = ['Button.CENTER', 'Button.VIEW', 'Button.MENU', 'Button.GUIDE', 'Button.UPLOAD', 'Button.LB', 'Button.RB']

    match pressed_button:
        case 'Button.LB':
            # code for yes
            return hub.system.shutdown()
        case 'Button.RB':
            return hub.system.shutdown()
            # code for no
        case 'Button.CENTER':
            # code for yes
            return hub.system.shutdown()
        case 'Button.VIEW':
            return hub.system.shutdown()    
        case 'Button.MENU':
            # code for yes
            return hub.system.shutdown()
        case 'Button.GUIDE':
            return hub.system.shutdown()   
        case 'Button.UPLOAD':
            # code for yes
            return hub.system.shutdown()
        case _:
            # code for other inputs
            return 0

    #if pressed_button in SHUTDOwN_BUTTONS:
    #    hub.system.shutdown()
    #elif 'Button.LB' in pressed_button:
    #    hub.system.shutdown()
    #pass
    #return 0



trim = 2
# The main program starts here.
while True:
    # Read remote state.
        hub.system.set_stop_button((Button.CENTER, Button.VIEW, Button.MENU, Button.GUIDE, Button.UPLOAD, Button.LB, Button.RB))
        trim = transmission_manual(controller.buttons.pressed(), trim)
        hub.display.number(trim)

        #Pincer, convert to function later
        #gripper(pressed_button=controller.buttons.pressed(), mode='sure')
        gripper(pressed_button=controller.buttons.pressed(), mode='experimental')

        #drive_base.drive(trim_or_turbo(drive_power, controller.buttons.pressed()), steer_input)
        drive_base.drive(trim_or_turbo(drive_power_calc(trim), controller.buttons.pressed()), drive_steer_calc())

        shutdown(controller.buttons.pressed())