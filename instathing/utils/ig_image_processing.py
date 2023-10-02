# External imports
from PIL import Image, ImageDraw, ImageFont
from PIL.PngImagePlugin import PngImageFile
import requests
from textwrap import wrap


def generate_ig_stories_image(
    offer_thumbnail:str = None,
    offer_name:str = None,
    offer_price_from:str = None,
    offer_price_to:str = None,
    file_path:str = None
) -> str:
    
    # STEP 1: Create empty IG Stories image from template
    # Create empty story from template
    im_ig_stories = Image.open(fp='../resources/story_template_720x1280_final.png')
    
    
    # STEP 2: Add offer thumbnail to IG Stories image
    # Get offer thumbnail
    im_thumbnail = Image.open(requests.get(offer_thumbnail, stream=True).raw)
    # Resize offer thumbnail
    im_thumbnail = im_thumbnail.resize(size=(640,640))
    # Paste offer thumbnail to story image
    im_ig_stories.paste(im=im_thumbnail,box=(40, 130))
    
    
    # STEP 3: Add offer name to IG Stories image
    # Add offer name
    im_ig_stories = add_text_to_image(
        im=im_ig_stories,
        font_size=40,
        x=27.5, # (10+17.5)
        y=827.5, # (100+700+20+7.5)
        text= '\n'.join(wrap(text=offer_name, width=30)),
        text_align='left'
    )
    
    
    # STEP 4: Add offer price to IG Stories image
    # If no priceFrom:
    if offer_price_from == None:
        price_text = f'Por apenas R${offer_price_to:.2f}!'
    # Else (if priceFrom):
    else:
        price_text = f'De R${offer_price_from:.2f} por apenas R${offer_price_to:.2f}!'
    # Add offer price to IG Stories image
    im_ig_stories = add_text_to_image(
        im=im_ig_stories,
        font_size=37.5,
        x=27.5, # (10+17.5)
        y=1062.5, # (100+700+20+210+20+12.5)
        text=price_text,
        text_align='left'
    )
    
    
    # STEP 5: Save IG Stories image to temp folder
    im_ig_stories.save(fp=file_path, format='png')
    
    
    # Return path fo IG Stories image
    return file_path


# Add Text To Image function
def add_text_to_image(
    im:PngImageFile,
    font:str = '../resources/fonts/OpenSans-VariableFont_wdth,wght.ttf',
    font_size:int = 12,
    x:int = 0,
    y:int = 0,
    text:str = 'No text provided',
    text_align:str = 'left',
):
    
    # Get a drawing context
    draw = ImageDraw.Draw(im=im)
    
    # Set font
    text_font = ImageFont.truetype(
        font=font,
        size=font_size,
        encoding='unic'
    )
    
    # Add text to image
    draw.multiline_text(
        xy=(x,y),
        text=text,
        fill=(0,0,0),
        font=text_font,
        align=text_align,
        stroke_width=0
    )
    
    # Return image (with added text)
    return im
    