# Imports
from pyscreeze import Box

# ============================================================================
#                           === CONFIGURATION FILE ===
# ============================================================================
# ----------------------------------------------------------------------------
#                           --- EXTRACT SETTINGS ---
#               Options for the extract part of the pipeline.
# ----------------------------------------------------------------------------
# Path to test XML file with raw offer data generated by Social Soul:
EXAMPLE_SOCIAL_SOUL_INPUT_XML_FILE_PATH = './rsc/xml/LomadeeDownload.xml'


# ----------------------------------------------------------------------------
#                           --- TRANSFORM SETTINGS ---
#               Options for the transform part of the pipeline.
# ----------------------------------------------------------------------------
# When refining a Social Soul offers dataframe, keep the following columns:
COLUMNS_OF_INTEREST_LIST = [
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

# When creating a new offer image for IG, use this font:
DEFAULT_FONT_FILE_PATH = './rsc/fnt/open_sans.ttf'

# When creating a new offer image for IG, use this story template:
DEFAULT_STORY_TEMPLATE_IMG_FILE_PATH = './rsc/img/tmpl_story_720x1280_final.png'

# During execution, temporary image files will be stored in this folder:
PATH_TO_TMP_IMAGE_FOLDER = './tmp/img/'

# During execution, temporary parquet files will be stored in this folder:
PATH_TO_TMP_PARQUET_FOLDER = './tmp/parquet/'

# After transform, export offers dataframe as a parquet file with this name:
DEFAULT_LOAD_READY_PARQUET_FILE_NAME = 'offers_ig_ready'

# ----------------------------------------------------------------------------
#                           --- LOAD SETTINGS ---
#               Options for the load (post) part of the pipeline.
# ----------------------------------------------------------------------------
# Before being used in IG story post, offer image will be temporarily stored 
# in Android device using this folder path and name:
PATH_TO_TMP_IMAGE_FOLDER_ANDROID = '/storage/emulated/0/DCIM/temp/'
DEFAULT_TMP_STORY_IMG_FILE_NAME_ANDROID = 'offer.png'

# Visual elements for IG bot navigation are located in this folder:
PATH_TO_VE_DIR = './rsc/ve/'
PATH_TO_TMP_SS_DIR = './tmp/ss/'

# When adding a link sticker to IG story post, use this display text:
DEFAULT_LINK_STICKER_TXT = 'ver oferta'


# ----------------------------------------------------------------------------
#                           --- CONSTANTS ---
#               
# ----------------------------------------------------------------------------
# IG bot will use the following visual elements as clues to navigate IG app.
# 
# IG logo in home screen
LOGO_IG = f'{PATH_TO_VE_DIR}e00a_logo_ig.png'
# 
# Blue "new story" button in home screen
BTN_NEW_STORY = f'{PATH_TO_VE_DIR}e00b_btn_newstory.png'
# 
# "New post" button in home screen
BTN_NEW_POST = f'{PATH_TO_VE_DIR}e00c_btn_newpost.png'
# 
# "New Post" title
TITLE_NEW_POST = f'{PATH_TO_VE_DIR}e01a_title_newpost.png'
# 
# Slider menu (when "POST" option selected)
SLDR_MENU_POST_SEL = f'{PATH_TO_VE_DIR}e01b_sldr_menu.png'
# 
# (Highlighted) "POST" word in slider menu
TXT_POST_HIGHLIGHT = f'{PATH_TO_VE_DIR}e01c_txt_post.png'
# 
# "STORY" word in slider menu
TXT_STORY = f'{PATH_TO_VE_DIR}e01c_txt_story.png'
# 
# "New story" screen
BTN_TAKE_PICTURE = f'{PATH_TO_VE_DIR}e02a_btn_takepic.png'
# 
# Slider menu (when "STORY" option selected)
SLDR_MENU_STORY_SEL = f'{PATH_TO_VE_DIR}e02b_sldr_menu.png'
# 
# "POST" word in slider menu
TXT_POST = f'{PATH_TO_VE_DIR}e02c_txt_post.png'
# 
# (Highlighted) "STORY" word in slider menu
TXT_STORY_HIGHLIGHT = f'{PATH_TO_VE_DIR}e02d_txt_story.png'
# 
# IG story gallery top bar
BAR_STORY_GALLERY = f'{PATH_TO_VE_DIR}e03a_bar_storygallery.png'
# 
# "Add to story" header in IG story gallery
HDR_ADD_TO_STORY = f'{PATH_TO_VE_DIR}e03b_title_addtostory.png'
#
# Region of first image in IG story gallery
BOX_1ST_IMG_IN_STRY_GAL = Box(left=3, top=668, width=353, height=627)
# 
# "Add sticker" button
BTN_ADD_STICKER = f'{PATH_TO_VE_DIR}e04a_btn_addsticker.png'
# 
# Search field in "Add Sticker" context
FLD_SEARCH_STICKER = f'{PATH_TO_VE_DIR}e05a_field_search.png'
# 
# Search field in "Add sticker" context
CONTEXT_SEARCH = f'{PATH_TO_VE_DIR}e06a_context_search.png'
# 
# "Search" word in "Add sticker" context
TXT_SEARCH = f'{PATH_TO_VE_DIR}e06b_txt_search.png'
# 
# Sticker link in "Add sticker" context
STCKR_LINK = f'{PATH_TO_VE_DIR}e07a_stckr_link.png'
# 
# "Add link" title in "Add link sticker" context
TITLE_ADD_LINK = f'{PATH_TO_VE_DIR}e08a_title_addlink.png'
# 
# "URL" field in in "Add link sticker" context
CONTXT_URL = f'{PATH_TO_VE_DIR}e08b_context_url.png'
# 
# URL field's URL in "Add link sticker" context
FLD_URL = f'{PATH_TO_VE_DIR}e08c_field_url.png'
# 
# "Customize sticker text" button in "Add link sticker" context
BTN_CUSTOM_STCKR_TXT = f'{PATH_TO_VE_DIR}e08d_btn_customstckrtxt.png'
# 
# "Customize sticker text" text in "Add link sticker" context
TXT_CUSTOM_STCKR_TXT = f'{PATH_TO_VE_DIR}e08e_txt_customstckrtxt.png'
# 
# "Sticker text" field in "Add link sticker" context
FIELD_STICKER_TEXT = f'{PATH_TO_VE_DIR}e09a_field_stickertext.png'
# 
# "Done" button in "Add link sticker" context
BTN_DONE = f'{PATH_TO_VE_DIR}e09b_btn_done.png'
# 
# Link sticker's icon in story build screen (multiple colors)
ICO_LINK_STICKER_BLUE = f'{PATH_TO_VE_DIR}e10a_ico_linksticker.png'
ICO_LINK_STICKER_WHITE = f'{PATH_TO_VE_DIR}e11a_ico_linksticker.png'
ICO_LINK_STICKER_BLACK = f'{PATH_TO_VE_DIR}e12a_ico_linksticker.png'
ICO_LINK_STICKER_ORANGE = f'{PATH_TO_VE_DIR}e13a_ico_linksticker.png'
# 
# IG story audience options context in story build screen
CONTEXT_AUDIENCE_OPTIONS = f'{PATH_TO_VE_DIR}e14a_context_audienceoptions.png'
# 
# "Your story" button in story build screen
BTN_YOUR_STORY = f'{PATH_TO_VE_DIR}e14b_btn_yourstory.png'
# 
# "Close Friends" button in story build screen
BTN_CLOSE_FRIENDS = f'{PATH_TO_VE_DIR}e14c_btn_closefriends.png'