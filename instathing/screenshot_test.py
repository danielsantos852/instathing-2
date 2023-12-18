# Imports
from utils import get_available_devices, connect_to_device


# Main function
def main():

    # Connect to first available android device
    device = connect_to_device(get_available_devices()[0].serial)

    # Take screenshot
    img_print = device.screencap()

    # Save screenshot to disk
    with open("./temp/screenshots/screen.png", "wb") as file:
        file.write(img_print)


# If this is the script being run, call main()
if __name__=='__main__': main()