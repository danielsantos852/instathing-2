# External imports
from PIL import Image, ImageDraw, ImageFont
from PIL.PngImagePlugin import PngImageFile
import requests
from textwrap import wrap


# Generate Instagram Story Image function
def generate_ig_story_image(
    offer_thumbnail:str = None,
    offer_name:str = None,
    offer_price_from:str = None,
    offer_price_to:str = None,
    file_path:str = None
) -> str:
    
    # Create empty IG story image from template
    im_ig_story = Image.open(fp='../resources/story_template_720x1280_final.png')
    
    # Add offer thumbnail to IG story image
    im_thumbnail = Image.open(requests.get(offer_thumbnail, stream=True).raw)
    im_thumbnail = im_thumbnail.resize(size=(640,640))
    im_ig_story.paste(im=im_thumbnail,box=(40, 130))
    
    # Add offer name to IG story image
    im_ig_story = add_text_to_image(
        im=im_ig_story,
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
        price_text = f'De R${offer_price_from:} por apenas R${offer_price_to}'
    
    # Add offer price text to IG story image
    im_ig_story = add_text_to_image(
        im=im_ig_story,
        font_size=37.5,
        x=27.5, # (10+17.5)
        y=1062.5, # (100+700+20+210+20+12.5)
        text=price_text,
        text_align='left'
    )
    
    # Save IG story image as PNG file
    im_ig_story.save(fp=file_path, format='png')
    
    # Return path to IG story image
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
    