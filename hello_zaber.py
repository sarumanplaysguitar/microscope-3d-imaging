from zaber_motion import Units
from zaber_motion.ascii import Connection

# For reference: set your computer up to run this code by following the docs
# https://software.zaber.com/motion-library/docs/tutorials/install/py#_option-1-command-line-usage

# Below is modified starter code from
# https://software.zaber.com/motion-library/docs/tutorials/code

with Connection.open_serial_port("COM3") as connection:
    connection.enable_alerts()

    device_list = connection.detect_devices()
    print(device_list)
    print("Found {} devices".format(len(device_list)))

    y_motor = device_list[1] # "Device 2"
    x_motor = device_list[2] # "Device 3"
    z_motor = device_list[3] # "Device 4"

    print("moving y-axis")
    y_axis = y_motor.get_axis(1)
    if not y_axis.is_homed():
      y_axis.home()

    # Move to 10mm
    y_axis.move_relative(10, Units.LENGTH_MILLIMETRES)
    print("moving 10mm")
    y_axis.move_relative(-10, Units.LENGTH_MILLIMETRES)
    print("moving -10mm")

    # Move by an additional 5mm
    # axis.move_relative(5, Units.LENGTH_MILLIMETRES)
    # print("moving 5mm")

    print("homing x-axis")
    x_axis = x_motor.get_axis(1)
    if not x_axis.is_homed():
      x_axis.home()

    x_axis.move_relative(10, Units.LENGTH_MILLIMETRES)
    print("moving x-axis 10mm")
