class Machine:
  def move(self):
    print("Machine is moving...")

class Chargeable:
  def __init__(self, battery_level):
    self.battery_level = battery_level

  def get_battery_level(self):
    print(f"Battery level: {self.battery_level}")

class Robot(Machine, Chargeable):
  def __init__(self, battery_level):
    Chargeable.__init__(self, battery_level) # Alternative way to call specific base class constructor

# Create a robot object
robot = Robot(80)

robot.move()  # Inherited from Machine
robot.get_battery_level()  # Inherited from Chargeable
