# Imports
import pyautogui
from pyscreeze import Box


# Find Image in Image function
def find_img_in_img(
    needle_img = None,
    haystack_img = None,
    sureness:float = 1.00,    # 1.0=100%
) -> Box | None:
    """
    Finds a smaller, "needle" image inside a bigger, "haystack" image.
    Returns coordinates and size of needle image occurrence in haystack image;
    or None, if no match.
    
    Parameters:
        needle_img (str): image to look for;
        haystack_img (str): image where to look for;
        sureness (float): match sureness percentage (1.0 = "100% sure").

    Returns
        box (Box): a pyscreeze Box object; or
        None: if needle image not found in haystack image.
    """
    
    # force use of ImageNotFoundException
    pyautogui.useImageNotFoundException()

    # If image found, print "I can see" message
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

    # Return image box
    return box