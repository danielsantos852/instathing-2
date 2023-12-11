# Imports
from ppadb.client import Client as AdbClient # https://pypi.org/project/pure-python-adb/
import random
import sys
import time


# Get Available Devices function
def get_available_devices(
    client=AdbClient(
        host="127.0.0.1",
        port=5037
    )
) -> list:
    
    # Get devices list
    devices = client.devices()

    # Print devices' serials list
    print(f'Available Devices: {[device.serial for device in devices]}')
    
    # Return devices list
    return devices


# Connect to Device function
def connect_to_device(
    device_serial:str, 
    client=AdbClient(
        host="127.0.0.1",
        port=5037
    )
) -> None:
    
    # Get devices list
    devices = client.devices()
    
    # Check if empty devices list
    if len(devices) == 0:
        sys.exit('No available devices. Exiting program...')

    # Go through devices list
    for device in devices:
        
        # If desired device found:
        if device.serial == device_serial:
    
            # Show "connected" message
            print (f'Connected to {device.serial}')        

            # Return device
            return device
        
    # If desired device not found:
    sys.exit(f'Device {device_serial} not found.')
    
    # Return nothing
    return None


# Get Device Screen Resolution function
def get_device_screen_res(device:AdbClient) -> tuple:
    
    # Get device's physical screen size data (as STR)
    # Example: "Physical size: [width]x[height]"
    data = device.shell('wm size')
    print(data)

    # Remove non-important substring (leaving "[width]x[height]")
    data = data.replace('Physical size: ', '')

    # Split width/height at the "x" (as STRs)
    # Example: "[width]x[height]"" -> (width, height)"
    width, height = data.split(sep='x')

    # Return width/height values (cast as INT)
    return int(width), int(height)


# Input Touchscreen Tap function
def input_touchscreen_tap(
    device: AdbClient,
    x0: float,
    x1: float,
    xmax: int,
    y0: float,
    y1: float,
    ymax: int,
    double_tap=False
) -> None:

    # Get random x within [x0*xmax , x1*xmax]
    x = round(random.SystemRandom().uniform(x0,x1)*xmax)

    # Get random y within [y0*ymax , y1*ymax]
    y = round(random.SystemRandom().uniform(y0,y1)*ymax)

    # Input touchscreen tap
    device.shell(f'input touchscreen tap {x} {y}')
    print(f'Tapped on (x,y)=({x}, {y})')
    
    # If double tap
    if double_tap==True:

        # Time between taps
        time.sleep(0.05)

        # Input touchscreen tap (again)
        device.shell(f'input touchscreen tap {x} {y}')
        print(f'Tapped on (x,y)=({x}, {y})')

    # Return nothing
    return None


# Imput Tourchscreen Swipe function
def input_touchscreen_swipe(
    device: AdbClient,
    x00: float,
    x01: float,
    xmax: int,
    dx: int,
    y00: float,
    y01: float,
    ymax: int,
    dy: float,
    delay: int
) -> None:
    
    # Get random x0 within [x00*xmax , x01*xmax]
    x0 = round(random.SystemRandom().uniform(x00,x01)*xmax)

    # Get random y0 within [y0*ymax , y1*ymax]
    y0 = round(random.SystemRandom().uniform(y00,y01)*ymax)

    # Calculate x1, y1
    x1 = x0 + dx
    y1 = y0 + dy

    # Input drag-and-drop command into adb shell
    device.shell(f'input draganddrop {x0} {y0} {x1} {y1} {delay}')

    # Debug
    print(f'Drag-and-drop from (x,y)=({x0}, {y0}) to (x,y)=({x1}, {y1})')

    # Return nothing
    return None