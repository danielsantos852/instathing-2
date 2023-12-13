# Imports
from PIL import Image, ImageDraw, ImageFont
from PIL.PngImagePlugin import PngImageFile
import requests
from textwrap import wrap


# Global Variables
PATH_TO_DEFAULT_STORY_IMAGE = './resources/story_template_720x1280_empty.png'
DEFAULT_STORY_IMAGE_OUTPUT_PATH = './temp/images/test.png'


# Generate Instagram Story Image from Offer function
def create_ig_story_image_from_offer(
    output_path:str = DEFAULT_STORY_IMAGE_OUTPUT_PATH,
    base_image:str =PATH_TO_DEFAULT_STORY_IMAGE,
    offer_thumbnail:str = './resources/images/example_offer_thumbnail_640x640.png',
    offer_name:str = 'Awesome product',
    offer_price_from:str = '0000.00',
    offer_price_to:str = '0000.00',
) -> str:
    """
    Generates a 720x1280 offer image fit for an IG story post.
    
    Parameters:
        output_path (str): path to output image file
        base_image (str): path to 720x1280 PNG/JPG image
        offer_thumbnail (str): url to product image
        offer_name (str): product description
        offer_price_from (str): product price (without discount)
        offer_price_to (str): product price (with discount)

    Returns:
        output_path (str): same as input
    """
    # Create new IG story image from base image
    im_story = Image.open(fp=base_image)
    
    # Download and paste offer thumbnail to IG story image
    im_thumbnail = Image.open(requests.get(offer_thumbnail, stream=True).raw)
    im_thumbnail = im_thumbnail.resize(size=(640,640))
    im_story.paste(im=im_thumbnail,box=(40, 130))
    
    # Clip offer name if max length exceeded
    max_name_length = 50
    if len(offer_name) > max_name_length:
        if offer_name[max_name_length-4]==' ':
            offer_name = f'{offer_name[:max_name_length-4]}...'
        else:
            offer_name = f'{offer_name[:max_name_length-3]}...'

    # Add offer name to IG story image
    im_story = add_text_to_image(
        im=im_story,
        font_size=40,
        x=27.5, # (10+17.5)
        y=827.5, # (100+700+20+7.5)
        text= '\n'.join(wrap(text=offer_name, width=30)),
        text_align='left'
    )
    
    # Prepare offer price text
    offer_price_to = f'{offer_price_to:.2f}'.replace('.',',')
    if offer_price_from == None:
        price_text = f'Por apenas R${offer_price_to}'
    else:
        offer_price_from = f'{offer_price_from:.2f}'.replace('.',',')
        price_text = f'De R${offer_price_from} por apenas R${offer_price_to}'
    
    # Add offer price text to IG story image
    im_story = add_text_to_image(
        im=im_story,
        font_size=37.5,
        x=27.5, # (10+17.5)
        y=982.5, # (100+700+15+140+15+12.5)
        text=price_text,
        text_align='left'
    )
    
    # Save IG story image as PNG file
    im_story.save(fp=output_path, format='png')
    
    # Return output path
    return output_path


# Add Text To Image function
def add_text_to_image(
    im:PngImageFile = None,
    x:int = 0,
    y:int = 0,
    text:str = '',
    text_align:str = 'left',
    font:str = './resources/fonts/OpenSans-VariableFont_wdth,wght.ttf',
    font_size:int = 12,
) -> PngImageFile:
    """
    Adds text to an image.
    
    Parameters:
        im (PngImageFile): an image
        x (int): x coordinate of textbox's top-left-most pixel (0 means left of image, grows rightwards)
        y (int): y coordinate of textbox's top-left-most pixel (0 means top of image, grows downwards)
        text (str): actual text to be written
        text_align (str): text alignment
        font (str): path to TTF font file
        font_size (int): font size

    Returns:
        im (PngImageFile): input image with added text
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