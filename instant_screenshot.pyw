from PIL import ImageGrab
import os
import time

def screenGrab():
    box = (505,105,859,727)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()     