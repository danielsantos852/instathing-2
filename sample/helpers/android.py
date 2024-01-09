# Imports
from io import BytesIO
import random
import sys
import time

from PIL import Image
from ppadb.client import Client as AdbClient
from ppadb.device import Device as AdbDevice
import pyautogui
from pyscreeze import Box
from pyscreeze import center

import config as cfg
from ..utils.execution import time_sleep
from ..utils.image_search import find_on_device_screen


# Global Variables (Configurations)
LINK_STICKER_TEXT = cfg.DEFAULT_LINK_STICKER_TEXT
TMP_OFFER_IMG_FILEPATH = (f'{cfg.DEFAULT_TEMP_IMG_FOLDER_ANDROID}'
                          f'{cfg.DEFAULT_TEMP_STORY_IMG_FILE_NAME_ANDROID}')


# Post IG Story v2 function
def post_ig_story(
    device:AdbDevice|None = None,
    img_src:str|None = None,
    stckr_url:str|None = None,
    stckr_text:str|None = LINK_STICKER_TEXT,
    close_friends:bool = True,
    restart_ig_app:bool = True,
    temp_img_filepath_device:str = TMP_OFFER_IMG_FILEPATH
) -> None:
    """ 
    Post IG story from computer through connected Android device using ADB.
    
    Parameters:
    - device (AdbDevice): a ppadb device object;
    - img_src (str): path to a 720x1280 PNG file;
    - stckr_url (str): a valid URL to be used to IG link sticker;
    - stckr_text (str): text to be displayed on IG link sticker;
    - close_friends (bool): post to close friends only;
    - restart_ig_app (bool): restart IG app before posting.
    - temp_img_filepath_device (str): folder for temp image storage

    Returns nothing.
    """
    # Get screen width and height (in pixels)
    scrn_width, scrn_height = get_device_screen_res(device=device)
    print(f'Screen resolution: {scrn_width} by {scrn_height} pixels.')

    # Copy post image from computer to android device
    copy_file_to_device(src=img_src,
                        dest=temp_img_filepath_device,
                        device=device)

    # Start/Restart IG app on device
    launch_ig_app(device=device,
                  force_stop=restart_ig_app)

    # Wait a little
    time_sleep(3.0, 0.0)

    # Create a couple flags
    button_found = False
    button_clicked = False

    # Start an infinite loop
    while True:

        # Find "New story" button on device screen
        box = find_on_device_screen(needle_img=f'{cfg.BTN_NEW_STORY}',
                                    device=device,
                                    sureness=0.9)

        # If button found:
        if box != None:

            # Update "found" flag
            button_found = True

            # Click on button box
            input_touchscreen_tap(device=device,
                                  box=box,
                                  double_tap=False,
                                  double_tap_delay=0.1)
        
            # Update clicked flag
            button_clicked = True

        # If button not found:
        else:

            # If button already clicked:
            if button_clicked == True:

                # Print "not found but already clicked" message
                print('Button "New story" not found but already clicked, moving on...')
                
                # Break from infinite loop
                break

            # If button not clicked yet:
            else:

                # Print "button not found" message
                print('"New story" button not found, trying again.')

        # Wait a little
        time_sleep(1.0, 0.0)

    # Look for "Add to story" header on device screen
    box = find_on_device_screen(needle_img=f'{cfg.HDR_ADD_TO_STORY}',
                                device=device,
                                sureness=0.9)

    # If header found:
    if box != None:
        # Click on it
        input_touchscreen_tap(device=device,
                              box=cfg.BOX_1ST_STORY_GALLERY_IMG)
    # If not:
    else:
        # Stop program
        sys.exit('"Add to story" header not found, exiting...')

    # Wait a little
    time_sleep(1.0, 0.0)

    # Look for "Add sticker" button on device screen
    box = find_on_device_screen(needle_img=f'{cfg.BTN_ADD_STICKER}',
                                device=device,
                                sureness=0.9)

    # If button found:
    if box != None:
        # Click on it
        input_touchscreen_tap(device=device,
                              box=box)
    # If not:
    else:
        # Stop program
        sys.exit('"Add sticker" button not found, exiting...')

    # Wait a little
    time_sleep(1.0, 0.0)

    # Look for search field on device screen
    box = find_on_device_screen(needle_img=f'{cfg.FLD_SEARCH_STICKER}',
                                device=device,
                                sureness=0.9)

    # If field found:
    if box != None:
        # Click on it
        input_touchscreen_tap(device=device,
                              box=box)
    # If not:
    else:
        # Stop program
        sys.exit('"Search" field not found, exiting...')

    # Wait a little
    time_sleep(1.0, 0.0)

    # Look for active "Search" field region on device screen
    box = find_on_device_screen(needle_img=f'{cfg.RGN_SEARCH_STICKER}',
                                device=device,
                                sureness=0.9)

    # If active field found:
    if box != None:

        # Input "link" word on search field
        device.input_text('link')

    # If not:
    else:
        # Stop program
        sys.exit('Active "Search" field not found, exiting...')

    # Wait a little
    time_sleep(1.0, 0.0)

    # Look for link sticker on device screen
    box = find_on_device_screen(needle_img=f'{cfg.STCKR_LINK}',
                                device=device,
                                sureness=0.9)

    # If sticker found:
    if box != None:

        # Click on it
        input_touchscreen_tap(device=device,
                              box=box)

    # If not:
    else:
        # Stop program
        sys.exit('Link sticker not found, exiting...')

    # Wait a little
    time_sleep(1.0, 0.0)

    # Look for URL field on device screen
    box = find_on_device_screen(needle_img=f'{cfg.FLD_STICKER_URL}',
                                device=device,
                                sureness=0.9)

    # If URL field found:
    if box != None:
        # Input URL
        device.input_text(stckr_url)

    # If not:
    else:
        # Stop program
        sys.exit('URL field not found, exiting...')

    # Wait a little
    time_sleep(1.0, 0.0)

    # Look for "Customize sticker text" button on device screen
    box = find_on_device_screen(needle_img=f'{cfg.BTN_CUSTOMIZE_STICKER_TEXT}',
                                device=device,
                                sureness=0.9)

    # If button found:
    if box != None:
        # Click on it
        input_touchscreen_tap(device=device,
                              box=box)

    # If not:
    else:
        # Stop program
        sys.exit('"Customize sticker text" button not found, exiting...')

    # Wait a little
    time_sleep(1.0, 0.0)

    # Look for "Sticker text" field region on device screen
    box = find_on_device_screen(needle_img=f'{cfg.RGN_CUSTOMIZE_STICKER_TEXT}',
                                device=device,
                                sureness=0.9)

    # If field found:
    if box != None:
        # Input sticker text
        device.input_text(stckr_text)

    # If not:
    else:
        # Stop program
        sys.exit('"Sticker text" field not found, exiting...')

    # Wait a little
    time_sleep(1.0, 0.0)

    # Look for "Done" button on device screen
    box = find_on_device_screen(needle_img=f'{cfg.BTN_DONE}',
                                device=device,
                                sureness=0.9)

    # If button found:
    if box != None:
        # Click on it
        input_touchscreen_tap(device=device,
                              box=box)

    # If not:
    else:
        # Stop program
        sys.exit('"Done" button not found, exiting...')

    # Wait a little
    time_sleep(1.0, 0.0)

    # Look for blue sticker link icon on device screen
    box = find_on_device_screen(needle_img=f'{cfg.ICO_LINK_STICKER_BLUE}',
                                device=device,
                                sureness=0.9)

    # If icon found:
    if box != None:
        # Click on it 3x
        for _ in range(3):
            time_sleep(0.5, 0.0)
            input_touchscreen_tap(device=device,
                                  box=box)

    # If not:
    else:
        # Stop program
        sys.exit('Blue link sticker icon not found, exiting...')

    # Wait a little
    time_sleep(1.0, 0.0)

    # Look for purple sticker link icon on device screen
    box = find_on_device_screen(needle_img=f'{cfg.ICO_LINK_STICKER_PURPLE}',
                                device=device,
                                sureness=0.9)

    # If icon found:
    if box != None:
        # Drag it to desired position
        input_touchscreen_swipe(device=device,
                                box=box,
                                dx=0,
                                dy=920,
                                duration=2000,
                                drag_and_drop=True)

    # If not:
    else:
        # Stop program
        sys.exit('Purple link sticker icon not found, exiting...')

    # Wait a little
    time_sleep(1.0, 0.0)

    # If post to close friends only:
    if close_friends==True:

        # Get button visual
        button = cfg.BTN_CLOSE_FRIENDS

        # Set post message
        post_message = 'Posted story to close friends only.'

    # If not (post to all followers):
    else:

        # Get button visual
        button = cfg.BTN_YOUR_STORY

        # Set post message
        post_message = 'Posted story to all followers.'

    # Look for "Post" button on device screen
    box = find_on_device_screen(needle_img=f'{button}',
                                device=device,
                                sureness=0.9)

    # If button found:
    if box != None:
        
        # Click on it
        input_touchscreen_tap(device=device,
                              box=box)

        # Print post message
        print(post_message)

    # If not:
    else:
        # Stop program
        sys.exit('"Post" button not found, exiting...')

    # Remove offer image from device's internal storage
    device.shell(f'rm {temp_img_filepath_device}')

    # Return nothing
    return None


# Find on Device Screen function
def find_on_device_screen(
    needle_img: str|None = None,
    device:AdbDevice|None = None,
    sureness:float = 0.9
) -> Box|None:
    """
    Finds a smaller, "needle" image inside a screenshot from an Android device.
    Returns coordinates and size of needle image occurrence in screenshot; or
    None, if no match.
    
    Parameters:
    - needle_img (str): image to search for;
    - device (AdbDevice): a ppadb device object;
    - sureness (float): match sureness percentage (1.0 means "100% sure").

    Returns
    - box (Box): a pyscreeze Box object; or
    - None: if needle image not found in haystack image.
    """
    # Take a screenshot of device as PIL Image
    screenshot = Image.open(fp=BytesIO(device.screencap()),
                            mode='r')

    # force pyautogui's use of ImageNotFoundException
    pyautogui.useImageNotFoundException()

    # Try this:
    try:
    
        # Locate subset image coordinates and size in image
        box = pyautogui.locate(needleImage=needle_img,
                               haystackImage=screenshot,
                               confidence=sureness)

    # If image not found, print "I can't see" message
    except pyautogui.ImageNotFoundException:
        print('Needle image not found.')

        # Return None
        return None

    # Print "image found" message
    print(f'Needle image found at {box}')

    # Return image box
    return box


# Get Available Devices function
def get_available_devices(
    client=AdbClient(host="127.0.0.1", port=5037)
) -> list:
    """
    Fetches a list of android devices currently connected to the computer.

    Parameters:
    - client (AdbClient): a ppadb client object.

    Returns:
    - devices (list): list of available devices.
    """
    # Get devices list
    devices = client.devices()

    # Print devices' serials list
    print(f'Available Devices: {[device.serial for device in devices]}')
    
    # Return devices list
    return devices


# Connect to Device function
def connect_to_device(
    device_serial:str|None = None,
    client=AdbClient(host="127.0.0.1", port=5037)
) -> AdbDevice|None:
    """
    Connects to an available Android device.

    Parameters:
    - device_serial (str): an adb device's serial number;
    - client (AdbClient): a ppadb client object.

    Returns
    - device (AdbDevice): a ppadb device object; or
    - None, if device not found.
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
    
    # Print "device not found" message
    print(f'Device {device_serial} not found.')

    # Return nothing
    return None


# Get Device Screen Resolution function
def get_device_screen_res(
    device:AdbDevice|None = None
) -> tuple:
    """
    Fetches an Android device's screen width and height values (in pixels) 
    using ADB shell.

    Parameters:
    - device (AdbDevice): a ppadb device object.

    Returns:
    - width, height (tuple): device's screen width and height (in pixels).
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
    xmax:int|None = None,
    ymax:int|None = None,
    double_tap:bool = False,
    double_tap_delay:float= 0.1
) -> None:
    """
    Performs a "more human" touchscreen tap on an Android device using ADB 
    shell. Tap occurs in a random (x,y) position inside area delimited by x0, 
    x1, y0, and y1.

    Parameters:
    - device (AdbDevice): a ppadb device object;
    - x0 (float): leftmost position of the tap;
    - x1 (float): rightmost position of the tap;
    - y0 (float): upmost position of the tap;
    - y1 (float): downmost position of the tap;
    - xmax (int): screen width (in pixels);
    - ymax (int): screen height (in pixels);
    - double_tap (bool): perform double tap?
    - double_tap_delay (float): delay between taps (in seconds).
    
    Returns nothing.

    Additional information:
    - x0, x1 = 0.0 are the leftmost pixels on the screen;
    - x0, x1 = 1.0 are the rightmost pixels on the screen;
    - y0, y1 = 0.0 are the topmost pixels on the screen;
    - y0, y1 = 1.0 are the downmost pixels on the screen.
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
    device:AdbDevice|None = None,
    box:Box|None = None,
    double_tap:bool = False,
    double_tap_delay:float = 0.1
) -> None:
    """
    Performs a touchscreen tap on an Android device using ADB shell.

    Parameters:
    - device (AdbDevice): a ppadb Device object;
    - box (Box): a pyscreeze Box object;
    - double_tap (bool): double tap or not;
    - double_tap_delay (float): time between taps (in seconds).

    Returns nothing.
    """
    # Get box's center coordinates
    point = center(box)
    x = point.x
    y = point.y

    # Tap on (x,y)
    device.input_tap(x, y)

    # Set tap message
    tap_message = f'Tapped on (x,y)=({x}, {y}).'

    # If double tap:
    if double_tap:
        
        # Tap on (x,y) a second time
        time_sleep(double_tap_delay, 0.0)
        device.input_tap(x, y)

        tap_message = tap_message.replace('Tapped', 'Double-tapped')

    # Print tap message
    print(tap_message)

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
    xmax:int|None = None,
    ymax:int|None = None,
    duration:int = 1000
) -> None:
    """
    Performs a "more human" touchscreen swipe on an Android device using ADB 
    shell. Swipe start from a random (x,y) position inside area delimited by 
    x0, x1, y0, and y1.

    Parameters:
    - device (AdbDevice): a ppadb device object;
    - x0 (float): leftmost starting position of the swipe;
    - x1 (float): rightmost starting position of the swipe;
    - y0 (float): upmost starting position of the swipe;
    - y1 (float): downmost starting position of the swipe;
    - xmax (int): screen width (in pixels);
    - ymax (int): screen height (in pixels);
    - dx (int): horizontal dislocation (in pixels);
    - dy (int): vertical dislocation (in pixels);
    - duration(int): swipe duration (in ms).
    
    Returns nothing.

    Additional information:
    - x,y = 0.0 means left/top of the screen;
    - x,y = 0.5 means center of the screen;
    - x,y = 1.0 means right/down of the screen;
    - dx > 0 means swiping right;
    - dx < 0 means swiping left;
    - dy > 0 means swiping down;
    - dy < 0 means swiping up.
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
    device:AdbDevice|None = None,
    box:Box|None = None,
    dx:int = 0,
    dy:int = 0,
    duration:int = 1000,
    drag_and_drop:bool = False
) -> None:
    """
    Performs a touchscreen swipe on an Android device using ADB shell.

    Parameters:
    - device (AdbDevice): a ppadb device object;
    - box (Box): a pyscreeze Box object.
    - dx (int): horizontal dislocation (in pixels);
    - dy (int): vertical dislocation (in pixels);
    - duration (int): swipe duration (in ms).
    
    Returns nothing.

    Additional information:
    - dx>0 means swiping right;
    - dx<0 means swiping left;
    - dy>0 means swiping down;
    - dy<0 means swiping up.
    """
    # Get box's center coordinates
    point = center(box)
    x = point.x
    y = point.y

    # If drag-and-drop selected:
    if drag_and_drop==True:
        
        # Input drag-and-drop command into adb shell
        device.shell(f'input draganddrop {x} {y} {x+dx} {y+dy} {duration}')
        
        # Print drag-and-drop message
        print(f'Drag-and-drop from (x,y)=({x}, {y}) to (x,y)=({x+dx}, {y+dy})')
    
    # Else:
    else:

        # Input swipe command
        device.input_swipe(start_x=x,
                           start_y=y,
                           end_x=x+dx,
                           end_y=y+dy,
                           duration=duration)

        # Print swipe message
        print(f'Swipe from (x,y)=({x}, {y}) to (x,y)=({x+dx}, {y+dy})')

    # Return nothing
    return None


# Copy File to Device function
def copy_file_to_device(
    src:str|None = None,
    dest:str|None = None,
    device:AdbDevice|None = None
) -> None:
    """ 
    Copies a file from computer to Android device using ADB push.
    
    Parameters:
    - src (str): path to source file (in the computer);
    - dest (str): path for destination file (in the device);
    - device (AdbDevice): a ppadb device object.

    Returns nothing.
    """
    # Copy offer JPG file from computer to device
    device.push(src, dest)

    # Make Android device "recognize" JPG file as a media file
    device.shell(f'am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file://{dest}')

    # Return nothing
    return None


# Launch IG App function
def launch_ig_app(
    device:AdbDevice|None = None,
    force_stop:bool = False,
) -> None:
    """
    Launches IG app on Android device using ADB shell.

    Parameters:
    - device (AdbDevice): a ppadb device object;
    - force_stop (bool): force-stop before starting app.

    Returns nothing.
    """
    # Force-stop IG app, if required:
    if force_stop==True:
        device.shell('am force-stop com.instagram.android')

    # Start IG app
    device.shell('monkey -p com.instagram.android 1')

    # Return nothing
    return None


# Take Screenshot function    
def take_screenshot(
    device:AdbDevice|None = None,
    output_file:str|None = None
) -> str:
    """
    Takes a screenshot of an Android device's screen using ppadb and save it.

    Parameters:
    - device (AdbDevice): a ppadb Device object;
    - output_file (str): path to the output image file.

    Returns:
    - output_file (str): same as input.
    """
    # Take screenshot
    print = device.screencap()

    # Save screenshot to computer
    with open(output_file, 'wb') as file:
        file.write(print)

    # Return path to output image file
    return output_file