# Imports
from ppadb.client import Client as AdbClient # https://pypi.org/project/pure-python-adb/
import random
from utils import get_available_devices, connect_to_device, get_device_screen_res
from utils import input_touchscreen_tap, input_touchscreen_swipe, time_sleep

# Global variables
OFFER_IMG_SRC = '../resources/story_template_720x1280_final.jpg'
OFFER_IMG_DEST = '/storage/emulated/0/DCIM/temp/offer.jpg'


# Main Function
def main():
    
    # Connect to first available android device from devices at 127.0.0.1:5037
    device = connect_to_device(get_available_devices()[0].serial)

    # Get device's screen resolution
    x_max, y_max = get_device_screen_res(device)












# If this is the script being run
if __name__=='__main__':

    # Call Main Function
    main()