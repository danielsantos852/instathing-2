# Imports
import random
import sys
import time

from ppadb.client import Client as AdbClient
from ppadb.device import Device as AdbDevice

from .execution import time_sleep


# Global Variables (Configurations)
PATH_TO_ANDROID_TMP_FOLDER = '/storage/emulated/0/DCIM/temp/offer.png'
DEFAULT_LINK_STICKER_TEXT = 'ver oferta'
DEFAULT_DEVICE_SCREEN_WIDTH = 1080
DEFAULT_DEVICE_SCREEN_LENGTH = 2400


# Post IG Story function
def post_ig_story(
    device:AdbDevice = None,
    img_src:str = None,
    stckr_url:str = 'google.com',
    stckr_text:str = DEFAULT_LINK_STICKER_TEXT,
    close_friends:bool = True,
    restart_ig_app:bool = True,
) -> None:
    """ 
    Post IG story from computer through connected Android device using ADB.
    
    Parameters:
        device (AdbDevice): a ppadb device object
        img_src (str): path to a 720x1280 PNG file
        stckr_url (str): a valid URL to be used to IG link sticker
        stckr_text (str): text to be displayed on IG link sticker
        close_friends (bool): post to close friends only?
        restart_ig_app (bool): restart IG app before posting?

    Returns:
        None
    """
    # Copy post image from computer to android device
    copy_file_to_device(src=img_src,
                        dest=PATH_TO_ANDROID_TMP_FOLDER,
                        device=device)

    # (Re)Start IG app
    launch_ig_app(device=device,
                  force_stop=restart_ig_app)

    # Get maximum values for x and y coordinates
    x_max, y_max = get_device_screen_res(device)

    # Wait
    time_sleep(1.8)

    # Click on "New post" button
    input_touchscreen_tap_randomized(
        device=device,
        x0=0.416667,    # 450px/1080px
        x1=0.583330,    # 630px/1080px
        y0=0.895834,    # 2150px/2400px
        y1=0.9375,      # 2250px/2400px
        xmax=x_max,
        ymax=y_max
    )

    # Wait
    time_sleep(t_base=3.5)
    
    # Click on "Story" option
    input_touchscreen_tap_randomized(
        device=device,
        x0=0.5712963,   # 617px/1080px
        x1=0.574074,    # 620px/1080px
        y0=0.8625,      # 2070px/2400px
        y1=0.885416,    # 2125px/2400px
        xmax=x_max,
        ymax=y_max
    )

    # Wait
    time_sleep(t_base=0.7)

    # Click on "Open Phone Gallery" button
    input_touchscreen_tap_randomized(
        device=device,
        x0=0.0092593,   # 10px/1080px
        x1=0.157407,    # 170px/1080px
        y0=0.845834,    # 2030px/2400px
        y1=0.904166,    # 2170px/2400px
        xmax=x_max,
        ymax=y_max
    )

    # Wait
    time_sleep(t_base=2.0)

    # Select first gallery image
    input_touchscreen_tap_randomized(
        device=device,
        x0=0.0092593,   # 10px/1080px
        x1=0.3240741,   # 350px/1080px
        y0=0.2875,      # 690px/2400px
        y1=0.533333,    # 1280px/2400px
        xmax=x_max,
        ymax=y_max
    )

    # Wait
    time_sleep(t_base=0.9)

    # Click on "Add Sticker" button
    input_touchscreen_tap_randomized(
        device=device,
        x0=0.5092593,   # 550px/1080px
        x1=0.5925925,   # 640px/1080px
        y0=0.0625,      # 150px/2400px
        y1=0.1,         # 240px/2400px
        xmax=x_max,
        ymax=y_max
    )

    # Wait
    time_sleep(t_base=0.5)

    # Click on "Search" field
    input_touchscreen_tap_randomized(
        device=device,
        x0=0.055556,    # 60px/1080px
        x1=0.925925,    # 1000px/1080px
        y0=0.229167,    # 550px/2400px
        y1=0.254166,    # 610px/2400px
        xmax=x_max,
        ymax=y_max
    )

    # Wait
    time_sleep(t_base=4.0)

    # Type "link" on search field
    device.shell('input text "link"')
    
    # Wait
    time_sleep(t_base=0.5)

    # Click on "Link" sticker
    input_touchscreen_tap_randomized(
        device=device,
        x0=0.0462963,   # 50px/1080px
        x1=0.212962,    # 230px/1080px
        y0=0.254167,    # 610px/2400px
        y1=0.325,       # 780px/2400px
        xmax=x_max,
        ymax=y_max
    )

    # Wait
    time_sleep(t_base=0.5)

    # Input sticker URL
    device.shell(f'input text "{stckr_url}"')

    # Wait
    time_sleep(t_base=0.5)

    # Click on "Customize sticker text"
    input_touchscreen_tap_randomized(
        device=device,
        x0=0.055556,    # 60px/1080px
        x1=0.925925,    # 1000px/1080px
        y0=0.304167,    # 730px/2400px
        y1=0.316666,    # 760px/2400px
        xmax=x_max,
        ymax=y_max
    )

    # Wait
    time_sleep(t_base=0.5)

    # Input sticker text
    device.shell(f'input text "{stckr_text}"')

    # Wait
    time_sleep(t_base=1.7)

    # Click on "Done"
    input_touchscreen_tap_randomized(
        device=device,
        x0=0.851852,    # 920px/1080px
        x1=0.981481,    # 1060px/1080px
        y0=0.1375,      # 330px/2400px
        y1=0.1875,      # 450px/2400px
        xmax=x_max,
        ymax=y_max
    )

    # Change link sticker color (click it 3x)
    for _ in range(3):
        
        # Wait
        time_sleep(t_base=1.2)

        # Tap on link sticker (changes color)
        input_touchscreen_tap_randomized(
            device=device,
            x0=0.444445,    # 480px/1080px
            x1=0.555555,    # 600px/1080px
            y0=0.420834,    # 1010px/2400px
            y1=0.45,        # 1080px/2400px
            xmax=x_max,
            ymax=y_max
        )

    # Wait
    time_sleep(t_base=1.0)

    # Drag link sticker to desired position
    input_touchscreen_swipe_randomized(
        device=device,
        x0=0.601851852,    # 650px/1080px
        x1=0.680555555,    # 735px/1080px
        dx=0,
        y0=0.420833334,    # 1010px/2400px
        y1=0.458333333,    # 1100px/2400px
        dy=1060,
        xmax=x_max,
        ymax=y_max,
        delay=1500
    )

    # Wait
    time_sleep(t_base=2)

    # If posting to Close Friends:
    if close_friends==True:
        
        # Click on "Close Friends story" (and post offer)
        input_touchscreen_tap_randomized(
            device=device,
            x0=0.3240741,   # 350px/1080px
            x1=0.5092592,   # 550px/1080px
            y0=0.864584,    # 2075px/2400px
            y1=0.880833,    # 2115px/2400px
            xmax=x_max,
            ymax=y_max
        )

    # If posting to all followers:
    else:

        # Click on "Your story" (and post offer)
        input_touchscreen_tap_randomized(
            device=device,
            x0=0.0694445,   # 75px/1080px
            x1=0.2268518,   # 245px/1080px
            y0=0.864584,    # 2075px/2400px
            y1=0.880833,    # 2115px/2400px
            xmax=x_max,
            ymax=y_max
        )

    # Remove offer image from device's internal storage
    device.shell(f'rm {PATH_TO_ANDROID_TMP_FOLDER}')

    # Return nothing
    return None


# Get Available Devices function
def get_available_devices(
    client=AdbClient(host="127.0.0.1", port=5037)
) -> list:
    """
    Fetches a list of android devices currently connected to the computer.

    Parameters:
        client (AdbClient): a ppadb client object

    Returns:
        devices (list): list of available devices
    """
    # Get devices list
    devices = client.devices()

    # Print devices' serials list
    print(f'Available Devices: {[device.serial for device in devices]}')
    
    # Return devices list
    return devices


# Connect to Device function
def connect_to_device(
    device_serial:str, 
    client=AdbClient(host="127.0.0.1", port=5037)
) -> AdbDevice:
    """
    Connects to an available Android device.

    Parameters:
        device_serial (str): device's serial number
        client (AdbClient): a ppadb client object

    Returns
        device (AdbDevice): a ppadb device object
    """  
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


# Get Device Screen Resolution function
def get_device_screen_res(device:AdbDevice) -> tuple:
    """
    Fetches an Android device's screen width and height values (in pixels) 
    using ADB shell.

    Parameters:
        device (AdbDevice): a ppadb device object

    Returns:
        width, height (tuple): device's screen width and height (in pixels)
    """
    # Get device's physical screen size data (as str)
    data = device.shell('wm size') # e.g.: 'Physical size: [width]x[height]'

    # Remove non-relevant substring
    data = data.replace('Physical size: ', '') # e.g.: '[width]x[height]'

    # Split width and height values
    width, height = data.split(sep='x') # e.g.: ('[width]', '[height]')

    # Cast values to int
    width = int(width)
    height = int(height)

    # Return width and height values
    return width, height


# Input Touchscreen Tap (Randomized) function
def input_touchscreen_tap_randomized(
    device: AdbDevice,
    x0:float = 0.5,
    x1:float = 0.5,
    y0:float = 0.5,
    y1:float = 0.5,
    xmax:int = DEFAULT_DEVICE_SCREEN_WIDTH,
    ymax:int = DEFAULT_DEVICE_SCREEN_LENGTH,
    double_tap:bool = False,
    double_tap_delay:float= 0.1
) -> None:
    """
    Performs a "more human" touchscreen tap on an Android device using ADB 
    shell. Tap occurs in a random (x,y) position inside area delimited by x0, 
    x1, y0, and y1.

    Parameters:
        device (AdbDevice): a ppadb device object
        x0 (float): leftmost position of the tap
        x1 (float): rightmost position of the tap
        y0 (float): upmost position of the tap
        y1 (float): downmost position of the tap
        xmax (int): screen width (in pixels)
        ymax (int): screen height (in pixels)
        double_tap (bool): double tap?
        double_tap_delay (float): delay between taps (in seconds)
    
    Returns:
        None

    Additional information:
        x0, x1 = 0.0 are the leftmost pixels on the screen
        x0, x1 = 1.0 are the rightmost pixels on the screen
        y0, y1 = 0.0 are the topmost pixels on the screen
        y0, y1 = 1.0 are the downmost pixels on the screen
    """
    # Get random x value within [x0*xmax , x1*xmax]
    x = round(random.SystemRandom().uniform(x0,x1)*xmax)

    # Get random y value within [y0*ymax , y1*ymax]
    y = round(random.SystemRandom().uniform(y0,y1)*ymax)

    # Perform tap (first time)
    input_touchscreen_tap(device, x, y)

    # If double tap:
    if double_tap==True:

        # Wait for double tap delay
        time.sleep(double_tap_delay)

        # Perform tap (second time)
        input_touchscreen_tap(device, x, y)

    # Return nothing
    return None


# Input Touchscreen Tap function
def input_touchscreen_tap(
    device: AdbDevice,
    x:int = 0,
    y:int = 0,
) -> None:
    """
    Performs a touchscreen tap on an Android device using ADB shell.

    Parameters:
        device (AdbDevice): a ppadb device object
        x (int): tap's x coordinate value (in pixels)
        y (int): tap's y coordinate value (in pixels)
    
    Returns:
        None

    Additional information:
        (x,y)=(0,0) is the top-left-most pixel of the screen.
    """
    # Input touchscreen tap on (x,y) using adb shell
    device.shell(f'input touchscreen tap {x} {y}')

    # Print tap message
    print(f'Tapped on (x,y)=({x}, {y}).')

    # Return nothing
    return None


# Imput Tourchscreen Swipe (Randomized) function
def input_touchscreen_swipe_randomized(
    device:AdbDevice = None,
    x0:float = 0.5,
    x1:float = 0.5,
    y0:float = 0.5,
    y1:float = 0.5,
    dx:int = 0,
    dy:int = 0,
    xmax:int = DEFAULT_DEVICE_SCREEN_WIDTH,
    ymax:int = DEFAULT_DEVICE_SCREEN_LENGTH,
    duration:int = 1000
) -> None:
    """
    Performs a "more human" touchscreen swipe on an Android device using ADB 
    shell. Swipe start from a random (x,y) position inside area delimited by 
    x0, x1, y0, and y1.

    Parameters:
        device (AdbDevice): a ppadb device object
        x0 (float): leftmost starting position of the swipe
        x1 (float): rightmost starting position of the swipe
        y0 (float): upmost starting position of the swipe
        y1 (float): downmost starting position of the swipe
        xmax (int): screen width (in pixels)
        ymax (int): screen height (in pixels)
        dx (int): horizontal dislocation (in pixels)
        dy (int): vertical dislocation (in pixels)
        duration(int): swipe duration (in ms)
    
    Returns:
        None

    Additional information:
        x,y = 0.0 means left/top of the screen
        x,y = 0.5 means center of the screen
        x,y = 1.0 means right/down of the screen
        dx > 0 means swiping right
        dx < 0 means swiping left
        dy > 0 means swiping down
        dy < 0 means swiping up
    """
    # Get random x value within [x0*xmax , x1*xmax]
    x = round(random.SystemRandom().uniform(x0,x1)*xmax)

    # Get random y value within [y0*ymax , y1*ymax]
    y = round(random.SystemRandom().uniform(y0,y1)*ymax)

    # Input touchscreen swipe
    input_touchscreen_swipe(device, x, y, dx, dy, duration)

    # Return nothing
    return None


# Input Touchscreen Swipe function
def input_touchscreen_swipe(
    device:AdbDevice = None,
    x:int = 0,
    y:int = 0,
    dx:int = 0,
    dy:int = 0,
    duration:int = 1000
) -> None:
    """
    Performs a touchscreen swipe on an Android device using ADB shell.
        
    Parameters:
        device (AdbDevice): a ppadb device object
        x (int): swipe's starting x coordinate value (in pixels)
        y (int): swipe's starting y coordinate value (in pixels)
        dx (int): horizontal dislocation (in pixels)
        dy (int): vertical dislocation (in pixels)
        duration (int): swipe duration (in ms)
    
    Returns:
        None

    Additional information:
        (x,y)=(0,0) is the top-left-most pixel of the screen.
        dx > 0 means swiping right
        dx < 0 means swiping left
        dy > 0 means swiping down
        dy < 0 means swiping up
    """
    # Input drag-and-drop command into adb shell
    device.shell(f'input draganddrop {x} {y} {x+dx} {y+dy} {duration}')

    # Print swipe message
    print(f'Drag-and-drop from (x,y)=({x}, {y}) to (x,y)=({x+dx}, {y+dy})')

    # Return nothing
    return None


# Copy File to Device function
def copy_file_to_device(
    src:str,
    dest:str,
    device:AdbDevice
) -> None:
    """ 
    Copies a file from computer to Android device using ADB push.
    
    Parameters:
        src (str): path to source file (in the computer)
        dest (str): path for destination file (in the device)
        device (AdbDevice): a ppadb device object

    Returns:
        None
    """
    # Copy offer JPG file from computer to device
    device.push(src, dest)

    # Make Android device "recognize" JPG file as a media file
    device.shell(f'am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file://{dest}')

    # Return nothing
    return None


# Launch IG App Android function
def launch_ig_app(
    device:AdbDevice = None,
    force_stop:bool = False,
) -> None:
    """
    Launches IG app on Android device using ADB shell.

    Parameters:
        device (AdbDevice): a ppadb device object
        force_stop (bool): force-stop before starting app?

    Returns:
        None
    """
    # Force-stop IG app, if required:
    if force_stop==True:
        device.shell('am force-stop com.instagram.android')

    # Start IG app
    device.shell('monkey -p com.instagram.android 1')

    # Return nothing
    return None