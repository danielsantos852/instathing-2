# Imports
import config as cfg
from utils import get_available_devices, connect_to_device, take_screenshot, find_img_in_img


# Main function
def main():

    # Connect to first available android device
    device = connect_to_device(get_available_devices()[0].serial)

    # Find "New story" button on screen
    box = find_img_in_img(needle_img='./tmp/ss/story_gallery_first_image.png',
                          haystack_img='./tmp/ss/story_gallery.png',
                          sureness=0.9)


# If this is the script being run, call main function
if __name__=='__main__': main()