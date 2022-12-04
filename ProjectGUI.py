import PySimpleGUI as sg
import motorControl
import numpy as py
import numpy as np
import time
import math
import cv2
import io
import os

from picamera2 import Picamera2, Preview
from tensorflow import keras
from pathlib import Path
from PIL import Image
#import smbus
#from picamera.array import PiRGBArray

totalStride = 1755
strideLength = 200


file_types = [("All files (*.*)","*.*")]

sg.theme('DarkTanBlue')
mc = motorControl.MotorControl()
camera = Picamera2()

def SNR(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return np.max(cv2.convertScaleAbs(cv2.Laplacian(gray, 3)))

def findBestFocus(images):
    print("Finding best image")
    result = None
    retSNR = None
    for idx, image in images:
        snr = SNR(image)
        if snr == 0:
            continue
        if retSNR is None:
            retSNR = snr
            result = [idx, image]
        if snr > retSNR:
            retSNR = snr
            result = [idx, image]

    if result is None:
        raise TypeError("Incorrect Frame Type")

    # returning image and its corresponding index
    return result
def get_frames(vidDir):
    cap = cv2.VideoCapture(vidDir)
    i = 0
    # a variable to set how many frames you want to skip
    frame_skip = 50
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if i > frame_skip - 1:
            frames.append(frame)
            i = 0
            continue
        i += 1

    cap.release()
    cv2.destroyAllWindows()
    return frames

def load_image_win():
    sg.theme('DarkTanBlue')
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
        ],
    ]
    window = sg.Window("Load Images", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
    window.close()

def reset_focuser():
    
    mc.stride(-1*totalStride)
    time.sleep(0.5)

def autofocus():
    print("resetting")
    reset_focuser()
    print("scanning")
    idxs, frames = scan(demo=False)
        
    if idxs is None:
            
        frames = get_frames("videos/final_video5.mp4") # 25 fps; frame per 2 seconds
        for frame in frames:
            img = Image.fromarray(frame, 'RGB')

            # print(SNR(frame))
            # img.show()

        idx, frame = findBestFocus(zip([f for f in range(len(frames))], frames))
        goToPositionFromScan(idx)
        img = Image.fromarray(frame, 'RGB')
        img.show()
    
    else:
        idx, frame = findBestFocus(zip(idxs, frames))
        goToPositionFromScan(idx)
        img = Image.fromarray(frame, 'RGB')
        img.show()

camera_config = camera.create_still_configuration(lores={"size": (640, 480)})
camera.configure(camera_config)

def scan(demo = False):
    if not demo:
        # camera.start_preview(fullscreen = False, window = (100,20,640,480))
        camera.resolution = (640, 480)
    #camera.start_recording('scan_video.h264')
    images = []
    idx = [x for x in range(math.floor(abs(totalStride/strideLength)))]
    for i in idx:
        mc.stride(strideLength)
        time.sleep(1)
        if not demo:
            
            yuv420 = camera.capture_array("lores")
            rgb = cv2.cvtColor(yuv420, cv2.COLOR_YUV420p2BGR)
            cv2.imshow("Camera", rgb)
            
            images.append(rgb)
    
    if demo:
        return None, None
    else:
        # camera.stop_preview()
        # camera.close()
        return idx, images
    
def goToPositionFromScan(idx):
    
    op = (math.floor(abs(totalStride/strideLength)) - idx) * strideLength * -1
    mc.stride(op)
def optimizeImage(fileDirectory):
    target = cv2.imread(fileDirectory, cv2.IMREAD_COLOR)

    filename = Path(fileDirectory).stem

    (T, output) = cv2.threshold(target,40,255,cv2.THRESH_TOZERO)

    # Save image
    cv2.imwrite(os.path.join("optimized",str(filename + '_optimized.jpg')), output)

def optimizer():
    sg.theme('DarkTanBlue')
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Optimize Image"),
        ],
    ]
    window = sg.Window("Optimizer", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Optimize Image":
            filename = values["-FILE-"]
            optimizeImage(filename)
            #if os.path.exists(filename):
             #   image = Image.open(values["-FILE-"])
              #  image.thumbnail((400, 400))
               # bio = io.BytesIO()
                #image.save(bio, format="PNG")
                #window["-IMAGE-"].update(data=bio.getvalue())
    window.close()
    # Initialize parser
    #parser = argparse.ArgumentParser()

    # Adding optional argument
    #parser.add_argument("-d", "--directory", help="Directory to Image File", type=str, required=True)

    # Read arguments from command line
    #args = parser.parse_args()

    # getting optimized image
    
        
def capture_image():
    layout = [
            [sg.Text("File name"),
            sg.InputText(size=(25, 1), key='filename'),
            sg.Button("Capture Image"),]
            ]
    window = sg.Window('Capturing Image',layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event =='Exit':
            break
        if event == "Capture Image":
            file_name = values['filename']
            
            #camera.iso = 800
            #camera.shutter_speed = 6000000
            #camera.start_preview(fullscreen = False, window = (100,20,640,480))
            #time.sleep(2)
            #camera_config = camera.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
            #camera.configure(camera_config)
            #camera.start_preview(Preview.QTGL)
            #camera.start()
            time.sleep(2)
            #camera.capture_file("testpicam2.jpg")
            camera.capture_file(file_name)
            #camera.stop_preview()
            #camera.close()
            
def main():
    sg.theme('DarkTanBlue')
    layout = [ [sg.Image(filename = "/home/pi/Pictures/newHeads.png")],
                   [sg.Text('Choose Operation: ')],
                   [sg.Button('Autofocus Telescope')],
                   [sg.Button('Capture Image')],
                   [sg.Button('Optimize Image')],
                   [sg.Button('Load Image')],
                   [sg.Button('Exit')]]
    window = sg.Window('Telescope Autofocuser Main Menu', layout, size = (640,450))
    camera.start()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            camera.close()
            break
        if event == 'Load Image':
            load_image_win()
        if event == 'Capture Image':
            capture_image()
        if event == 'Autofocus Telescope':
            autofocus()
        if event == 'Optimize Image':
            optimizer()
        #if event == 'Scan':
         #   scan()
        #capture image
   # else if event = 'Optimize Image':
        #optimization function
    #else if event = 'Autofocus Image':
        #autofocus telescope       
    window.close()
        
if __name__ == "__main__":
    main()
