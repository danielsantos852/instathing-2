# Imports
import config as cfg
from utils import get_available_devices, connect_to_device, take_screenshot, find_img_in_img


# Main function
def main():

    # Connect to first available android device
    device = connect_to_device(get_available_devices()[0].serial)
  
    # Take device screenshot
    path = take_screenshot(device=device,output_file='./tmp/ss/000.png'),

    # Print message
    print(f'Screenshot saved as "{path}".')


# If this is the script being run, call main function
if __name__=='__main__': main()