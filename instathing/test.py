# Imports
import config as cfg
from utils import get_available_devices, connect_to_device, take_screenshot, find_img_in_img


# Main function
def main():

    # Connect to first available android device
    device = connect_to_device(get_available_devices()[0].serial)
  
    # Find button position in device screenshot
    box = find_img_in_img(needle_img='./rsc/img/e01c_btn_newpost.png',
                          haystack_img=take_screenshot(device=device,
                                                       output_file='./tmp/img/screenshot.png'),
                          sureness=0.9)
    
    # Print message
    print(f'Button found at {box}')


# If this is the script being run, call main function
if __name__=='__main__': main()