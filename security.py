import cv2
import dropbox
import time
import random

start_time = time.time()

#take_snapshot()

#upload_file()


def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()
