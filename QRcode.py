from pyzbar.pyzbar import decode
from PIL import Image, ImageDraw
import cv2
import json


def main():
    # Begin capturing video. You can modify what video source to use with VideoCapture's argument. It's currently set
    # to be your webcam.
    capture = cv2.VideoCapture(0)

    while True:
        # To quit this program press q.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Breaks down the video into frames
        ret, frame = capture.read()

        # Displays the current frame
        cv2.imshow('QR Code Reader', frame)

        # Converts image to grayscale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Uses PIL to convert the grayscale image into a ndary array that can be decoded by pyzbar
        image = Image.fromarray(gray)
        width, height = image.size
        the_image = decode((image.tobytes(), width, height))

        #decode each qr code and overwrite existing qr code in the data.txt file
        for decoded in the_image:
            data = {}  
            data['qr_codes'] = []  
            data['qr_codes'].append({  
                'data': decoded.data.decode("utf-8"),
            })
            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile, indent=4)


if __name__ == "__main__":
    main()
