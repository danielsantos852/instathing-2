# Third-party imports
from PIL import ImageDraw, ImageFont
from PIL.PngImagePlugin import PngImageFile
import pyautogui
from pyscreeze import Box

# Internal imports
from context import config as cfg


# Global Variables
FONT_FILE_PATH = cfg.DEFAULT_FONT_FILE_PATH


# Functions
def find_in_image(
    needle_img:str|None = None,
    haystack_img:str|None = None,
    sureness:float = 90.0,
) -> Box|None:
    """
    Searches for a smaller (needle) image inside a bigger (haystack) image.

    :param needle_img: Path to image to be found
    :type needle_img: str
    :param haystack_img: Path to image to be searched
    :type haystack_img: str
    :param sureness: Match sureness level (0-100% sure)
    :type sureness: float

    :return: Coordinates of needle image occurrence inside haystack image
    :rtype: pyscreeze.Box|None
    """
    # Force pyautogui's use of ImageNotFoundException
    pyautogui.useImageNotFoundException()
    
    # Try to:
    try:
    
        # Locate needle image inside haystack image
        box = pyautogui.locate(needleImage=needle_img,
                               haystackImage=haystack_img,
                               confidence=sureness/100)

    # If needle image not found:
    except pyautogui.ImageNotFoundException:

        # Return None
        return None

    # Return image box
    return box


def add_textbox_to_image(
    im:PngImageFile = None,
    x:int = 0,
    y:int = 0,
    txt:str = '',
    txt_align:str = 'left',
    font:str = FONT_FILE_PATH,
    font_size:int = 12,
) -> PngImageFile:
    """
    Adds a textbox to an image

    :param im: Base image
    :type im: PIL.PngImagePlugin.PngImageFile
    :param x: x coordinate of textbox's top-left-most pixel;
    :type x: int
    :param y: y coordinate of textbox's top-left-most pixel;
    :type y: int
    :param txt: Textbox's text
    :type txt: str
    :param txt_align: Text alignment
    :type txt_align: str
    :param font: Path to font file
    :type font: str
    :param font_size: Font size
    :type font_size: int
    
    :return: Base image with added textbox
    :rtype: PIL.PngImagePlugin.PngImageFile
    """
    # Get an ImageFont object
    text_font = ImageFont.truetype(font=font,
                                   size=font_size,
                                   encoding='unic')
    
    # Get an ImageDraw object
    draw = ImageDraw.Draw(im=im)
    
    # Add textbox to image
    draw.multiline_text(xy=(x, y),
                        text=txt,
                        fill=(0, 0, 0),
                        font=text_font,
                        align=txt_align,
                        stroke_width=0)
    
    # Return image
    return im