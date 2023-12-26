# Imports
from PIL import ImageDraw, ImageFont
from PIL.PngImagePlugin import PngImageFile

import config as cfg


# Global Variables
FONT_FILE_PATH = cfg.DEFAULT_FONT


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