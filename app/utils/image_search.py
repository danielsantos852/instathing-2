# Imports
from io import BytesIO

from PIL import Image
import pyautogui
from pyscreeze import Box
from ppadb.device import Device as AdbDevice


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


# Find in Image function
def find_in_img(
    needle_img:str|None = None,
    haystack_img:str|None = None,
    sureness:float = 0.9,
) -> Box|None:
    """
    Finds a smaller, "needle" image inside a bigger, "haystack" image.
    Returns coordinates and size of needle image occurrence in haystack image;
    or None, if no match.
    
    Parameters:
    - needle_img (str): image to search for;
    - haystack_img (str): image where to look for;
    - sureness (float): match sureness percentage (1.0 means "100% sure").

    Returns
    - box (Box): a pyscreeze Box object; or
    - None: if needle image not found in haystack image.
    """
    
    # force pyautogui's use of ImageNotFoundException
    pyautogui.useImageNotFoundException()

    # Try this:
    try:
    
        # Locate subset image coordinates and size in image
        box = pyautogui.locate(needleImage=needle_img,
                               haystackImage=haystack_img,
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