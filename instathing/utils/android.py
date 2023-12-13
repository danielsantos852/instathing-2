# Imports
import random
import sys
import time

from ppadb.client import Client as AdbClient
from ppadb.device import Device as AdbDevice

from .execution import time_sleep


# Global Variables (Configurations)
PATH_TMP_STORY_IMG_ANDROID = ''
LINK_STICKER_TEXT = 'ver oferta'


# Post IG Story function
def post_ig_story(
    device:AdbDevice,
    img_src:str,
    url:str,
    stckr_text=LINK_STICKER_TEXT,
    close_friends=True,
    restart_ig_app=True,
) -> None:
    """ Post IG story from computer through connected Android device using ADB.
    
        Keyword arguments:
        device -- a ppadb Device object
        img_src -- path to a 720x1280 PNG file
        url -- a valid URL
        stckr_text -- text to be displayed on IG link sticker
        close_friends -- post to close friends only?
        restart_ig_app -- restart IG app before posting?
    """

    # Copy post image from computer to android device
    copy_file_to_device(path_origin=img_src,
                        path_destination=PATH_TMP_STORY_IMG_ANDROID,
                        device=device)

    # (Re)Start IG app
    launch_ig_app(device=device,
                  force_stop=restart_ig_app)

    # Get maximum values for x and y coordinates
    x_max, y_max = get_device_screen_res(device)

    # Wait
    time_sleep(1.8)

    # Click on "New post" button
    input_touchscreen_tap(
        device=device,
        x0=0.416667,    # 450px/1080px
        x1=0.583330,    # 630px/1080px
        xmax=x_max,
        y0=0.895834,    # 2150px/2400px
        y1=0.9375,      # 2250px/2400px
        ymax=y_max
    )

    # Wait
    time_sleep(t_base=3.5)
    
    # Click on "Story" option
    input_touchscreen_tap(
        device=device,
        x0=0.5712963,   # 617px/1080px
        x1=0.574074,    # 620px/1080px
        xmax=x_max,
        y0=0.8625,      # 2070px/2400px
        y1=0.885416,    # 2125px/2400px
        ymax=y_max
    )

    # Wait
    time_sleep(t_base=0.7)

    # Click on "Open Phone Gallery" button
    input_touchscreen_tap(
        device=device,
        x0=0.0092593,   # 10px/1080px
        x1=0.157407,    # 170px/1080px
        xmax=x_max,
        y0=0.845834,    # 2030px/2400px
        y1=0.904166,    # 2170px/2400px
        ymax=y_max
    )

    # Wait
    time_sleep(t_base=2.0)

    # Select first gallery image
    input_touchscreen_tap(
        device=device,
        x0=0.0092593,   # 10px/1080px
        x1=0.3240741,   # 350px/1080px
        xmax=x_max,
        y0=0.2875,      # 690px/2400px
        y1=0.533333,    # 1280px/2400px
        ymax=y_max
    )

    # Wait
    time_sleep(t_base=0.9)

    # Click on "Add Sticker" button
    input_touchscreen_tap(
        device=device,
        x0=0.5092593,   # 550px/1080px
        x1=0.5925925,   # 640px/1080px
        xmax=x_max,
        y0=0.0625,      # 150px/2400px
        y1=0.1,         # 240px/2400px
        ymax=y_max
    )

    # Wait
    time_sleep(t_base=0.5)

    # Click on "Search" field
    input_touchscreen_tap(
        device=device,
        x0=0.055556,    # 60px/1080px
        x1=0.925925,    # 1000px/1080px
        xmax=x_max,
        y0=0.229167,    # 550px/2400px
        y1=0.254166,    # 610px/2400px
        ymax=y_max
    )

    # Wait
    time_sleep(t_base=4.0)

    # Type "link" on search field
    device.shell('input text "link"')
    
    # Wait
    time_sleep(t_base=0.5)

    # Click on "Link" sticker
    input_touchscreen_tap(
        device=device,
        x0=0.0462963,   # 50px/1080px
        x1=0.212962,    # 230px/1080px
        xmax=x_max,
        y0=0.254167,    # 610px/2400px
        y1=0.325,       # 780px/2400px
        ymax=y_max
    )

    # Wait
    time_sleep(t_base=0.5)

    # Input sticker URL
    device.shell(f'input text "{url}"')

    # Wait
    time_sleep(t_base=0.5)

    # Click on "Customize sticker text"
    input_touchscreen_tap(
        device=device,
        x0=0.055556,    # 60px/1080px
        x1=0.925925,    # 1000px/1080px
        xmax=x_max,
        y0=0.304167,    # 730px/2400px
        y1=0.316666,    # 760px/2400px
        ymax=y_max
    )

    # Wait
    time_sleep(t_base=0.5)

    # Input sticker text
    device.shell(f'input text "{stckr_text}"')

    # Wait
    time_sleep(t_base=1.7)

    # Click on "Done"
    input_touchscreen_tap(
        device=device,
        x0=0.851852,    # 920px/1080px
        x1=0.981481,    # 1060px/1080px
        xmax=x_max,
        y0=0.1375,      # 330px/2400px
        y1=0.1875,      # 450px/2400px
        ymax=y_max
    )

    # Change link sticker color (click it 3x)
    for _ in range(3):
        
        # Wait
        time_sleep(t_base=1.2)

        # Tap on link sticker (changes color)
        input_touchscreen_tap(
            device=device,
            x0=0.444445,    # 480px/1080px
            x1=0.555555,    # 600px/1080px
            xmax=x_max,
            y0=0.420834,    # 1010px/2400px
            y1=0.45,        # 1080px/2400px
            ymax=y_max
        )

    # Wait
    time_sleep(t_base=1.0)

    # Drag link sticker to desired position
    input_touchscreen_swipe(
        device=device,
        x00=0.601851852,    # 650px/1080px
        x01=0.680555555,    # 735px/1080px
        xmax=x_max,
        dx=0,
        y00=0.420833334,    # 1010px/2400px
        y01=0.458333333,    # 1100px/2400px
        ymax=y_max,
        dy=1060,
        delay=1500
    )

    # Wait
    time_sleep(t_base=2)

    # If posting to Close Friends:
    if close_friends==True:
        
        # Click on "Close Friends story" (and post offer)
        input_touchscreen_tap(
            device=device,
            x0=0.3240741,   # 350px/1080px
            x1=0.5092592,   # 550px/1080px
            xmax=x_max,
            y0=0.864584,    # 2075px/2400px
            y1=0.880833,    # 2115px/2400px
            ymax=y_max
        )

    # If posting to all followers:
    else:

        # Click on "Your story" (and post offer)
        input_touchscreen_tap(
            device=device,
            x0=0.0694445,   # 75px/1080px
            x1=0.2268518,   # 245px/1080px
            xmax=x_max,
            y0=0.864584,    # 2075px/2400px
            y1=0.880833,    # 2115px/2400px
            ymax=y_max
        )

    # Remove offer image from device's internal storage
    device.shell(f'rm {PATH_TMP_STORY_IMG_ANDROID}')

    # Return nothing
    return None


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


# Copy File to Device function
def copy_file_to_device(
    src:str,
    dest:str,
    device:AdbDevice
) -> str:
    """ Push a file from computer to android device.
    
    Keyword arguments:
    src -- full path to source file
    dest -- full path for destination file
    device -- a ppadb Device object
    """

    # Copy offer JPG file from computer to device
    device.push(src, dest)

    # Make device "recognize" JPG file as media
    device.shell(f'am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file://{dest}')

    # Return destination path
    return dest


# Launch IG App Android function
def launch_ig_app(
    device:AdbDevice,
    force_stop=False,
) -> None:
    
    # Force-stop IG app, if required:
    if force_stop==True:
        device.shell('am force-stop com.instagram.android')

    # Start IG app
    device.shell('monkey -p com.instagram.android 1')

    # Return nothing
    return None