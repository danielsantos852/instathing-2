# ============================================================================
#                           === CONFIGURATION FILE ===
# ============================================================================

# Imports
from pyscreeze import Box

# ----------------------------------------------------------------------------
#                           --- TRANSFORM SETTINGS ---
#               Options for the transform part of the pipeline.
# ----------------------------------------------------------------------------

# Example Social Soul XML file for testing.
SOCIAL_SOUL_EXAMPLE_XML_FILE = './rsc/xml/LomadeeDownload.xml'

# When refining a Social Soul offers dataframe, keep these columns.
COLUMNS_OF_INTEREST = [
    'offerName',            # Offer name
    #'sellerId',
    #'sellerThumbnail',
    'offerLink',            # URL to offer
    'offerThumbnail',       # Picture of product in white background
    'priceFrom',            # Price before discount
    #'sellerName',
    'priceTo',              # Price after discount
    #'sku',
    #'categoryName',
    #'categoryId',
]

# Font used in IG story image creation.
DEFAULT_FONT = './rsc/fnt/open_sans.ttf'

# Story template image used in IG story image creation.
DEFAULT_STORY_TEMPLATE = './rsc/img/tmpl_story_720x1280_final.png'

# On the computer, temporary image files will be stored in this folder.
DEFAULT_TEMP_IMG_FOLDER = './temp/img/'

# Temporary parquet files will be stored in this folder.
DEFAULT_TEMP_PARQUET_FOLDER = './temp/parquet/'

# After transform, export offers dataframe as a parquet file with this name.
DEFAULT_LOAD_READY_PARQUET_FILE_NAME = 'offers_ig_ready'

# ----------------------------------------------------------------------------
#                           --- LOAD SETTINGS ---
#               Options for the load (post) part of the pipeline.
# ----------------------------------------------------------------------------

# On the Android device, temporary image files will be stored in this folder.
DEFAULT_TEMP_IMG_FOLDER_ANDROID = '/storage/emulated/0/DCIM/temp/'

# Default name for temporary image file on Android device
DEFAULT_TEMP_STORY_IMG_FILE_NAME_ANDROID = 'offer.png'

# Visual elements for IG bot navigation are located in this folder:
PATH_TO_VE_FOLDER = './rsc/ve/'

# Screenshots taken during bot navigation will be stored in this folder:
DEFAULT_TEMP_SS_FOLDER = './temp/ss/'

# When adding a link sticker to IG story post, use this display text:
DEFAULT_LINK_STICKER_TEXT = 'ver oferta'

# ----------------------------------------------------------------------------
#                           --- VISUAL ELEMENTS ---
#   Visual elements to be used by IG bot for navigation in the IG app.
# ----------------------------------------------------------------------------

# Blue "new story" button in IG home screen
BTN_NEW_STORY = f'{PATH_TO_VE_FOLDER}00a_btn_newstory.png'

# "Add to story" header in IG story gallery screen
HDR_ADD_TO_STORY = f'{PATH_TO_VE_FOLDER}01a_hdr_addtostory.png'

# Region of first image in IG story gallery screen
BOX_1ST_STORY_GALLERY_IMG = Box(left=3, top=668, width=353, height=627)
 
# "Add sticker" button in story build screen
BTN_ADD_STICKER = f'{PATH_TO_VE_FOLDER}02a_btn_addsticker.png'
 
# Search field in "Add Sticker" screen
FLD_SEARCH_STICKER = f'{PATH_TO_VE_FOLDER}03a_fld_searchsticker.png'
 
# Search field region in "Add Sticker" screen
RGN_SEARCH_STICKER = f'{PATH_TO_VE_FOLDER}04a_rgn_search.png'

# Sticker link in "Add sticker" screen
STCKR_LINK = f'{PATH_TO_VE_FOLDER}05a_stckr_link.png'
 
# "URL" field in "Add sticker" screen
FLD_STICKER_URL = f'{PATH_TO_VE_FOLDER}06a_fld_stickerurl.png'

# "Customize sticker text" button in "Add sticker" screen
BTN_CUSTOMIZE_STICKER_TEXT = f'{PATH_TO_VE_FOLDER}06b_btn_customstickertext.png'

# "Sticker text" region in "Add sticker" screen
RGN_CUSTOMIZE_STICKER_TEXT = f'{PATH_TO_VE_FOLDER}07a_rgn_stickertext.png'
 
# "Done" button in "Add sticker" screen
BTN_DONE = f'{PATH_TO_VE_FOLDER}07b_btn_done.png'

# Link sticker icon (multiple colors)
ICO_LINK_STICKER_BLUE = f'{PATH_TO_VE_FOLDER}08a_ico_linksticker.png'
ICO_LINK_STICKER_WHITE = f'{PATH_TO_VE_FOLDER}09a_ico_linksticker.png'
ICO_LINK_STICKER_BLACK = f'{PATH_TO_VE_FOLDER}10a_ico_linksticker.png'
ICO_LINK_STICKER_PURPLE = f'{PATH_TO_VE_FOLDER}11a_ico_linksticker.png'
 
# Post to your story button in story build screen
BTN_YOUR_STORY = f'{PATH_TO_VE_FOLDER}12a_btn_yourstory.png'
 
# Post to close friends button in story build screen
BTN_CLOSE_FRIENDS = f'{PATH_TO_VE_FOLDER}12b_btn_closefriends.png'