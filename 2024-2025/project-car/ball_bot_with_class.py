from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction, Color, Button
from pybricks.tools import wait, run_task, multitask
from pybricks.iodevices import XboxController
from pybricks.robotics import Car
from pybricks.iodevices import PUPDevice

Scholars = {
    'ball_bot': {
        'drive': Port.F, 
        'steer': Port.E, 
        'color': Color.BLUE, 
        'drive_direction': Direction.COUNTERCLOCKWISE, 
        'steer_direction': Direction.COUNTERCLOCKWISE
    }
}

class ScholarCar:
    def __init__(self):
        self.hub = PrimeHub()
        self.controller = XboxController()
        
        scholar_mode = Scholars['ball_bot']
        self.drive = Motor(scholar_mode['drive'], positive_direction=scholar_mode['drive_direction'])
        self.steer = Motor(scholar_mode['steer'], positive_direction=scholar_mode['steer_direction'])
        
        self.car = Car(self.steer, self.drive)
        
        self.hub.speaker.beep(frequency=1000, duration=100)
        self.hub.light.on(scholar_mode['color'])
    
    def trim_or_turbo(self, power, pressed_button):
        if 'Button.A' in str(pressed_button):
            return power
        elif 'Button.Y' in str(pressed_button):
            return power*0.25
        else:
            return power*0.75
    
    def main(self):
        while True:
            #Drive
            drive_power_R = self.controller.triggers()[1] # Right Trigger Forward
            drive_power_L = -self.controller.triggers()[0] # Left Trigger Reverse
            drive_power = drive_power_R + drive_power_L

            #Steer
            steer_input_R = self.controller.joystick_right()[0]  # Horizontal only
            steer_input_L = self.controller.joystick_left()[0]  # Horizontal only
            combined_steer = steer_input_R + steer_input_L
            steer_input = max(-100, min(combined_steer, 100))

            self.car.drive_power(self.trim_or_turbo(drive_power, self.controller.buttons.pressed()))
            self.car.steer(steer_input)

            wait(2)

# Run the program
if __name__ == '__main__':
    car = ScholarCar()
    car.main()