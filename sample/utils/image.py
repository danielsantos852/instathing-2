# Imports
from PIL import ImageDraw, ImageFont
from PIL.PngImagePlugin import PngImageFile

import pyautogui
from pyscreeze import Box

import config as cfg


# Global Variables
FONT_FILE_PATH = cfg.DEFAULT_FONT


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


# Add Text To Image function
def add_text_to_image(
    im:PngImageFile = None,
    x:int = 0,
    y:int = 0,
    text:str = '',
    text_align:str = 'left',
    font:str = FONT_FILE_PATH,
    font_size:int = 12,
) -> PngImageFile:
    """
    Adds text to an image.
    
    Parameters:
        im (PngImageFile): an image;
        x (int): x coordinate of textbox's top-left-most pixel;
        y (int): y coordinate of textbox's top-left-most pixel;
        text (str): actual text to be written;
        text_align (str): text alignment;
        font (str): path to TTF font file;
        font_size (int): font size.

    Returns:
        im (PngImageFile): input image with added text.
    """
    # Set font
    text_font = ImageFont.truetype(font=font,
                                   size=font_size,
                                   encoding='unic')
    
    # Get a drawing context
    draw = ImageDraw.Draw(im=im)
    
    # Add text to image
    draw.multiline_text(xy=(x,y),
                        text=text,
                        fill=(0,0,0),
                        font=text_font,
                        align=text_align,
                        stroke_width=0)
    
    # Return image
    return im