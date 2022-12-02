import numpy as np
import argparse
import cv2

from tensorflow import keras
from pathlib import Path


def optimizeImage(fileDirectory):
    srcnn_model = keras.models.load_model('SRCNNStars')

    target = cv2.imread(fileDirectory, cv2.IMREAD_COLOR)
    target = cv2.cvtColor(target, cv2.COLOR_BGR2YCrCb)
    shape = target.shape

    Y_img = cv2.resize(target[:, :, 0], (int(shape[1]), int(shape[0])), cv2.INTER_CUBIC)
    target[:, :, 0] = Y_img
    target = cv2.cvtColor(target, cv2.COLOR_YCrCb2BGR)

    Y = np.zeros((1, target.shape[0], target.shape[1], 1), dtype=np.float32)

    # Normalize
    Y[0, :, :, 0] = Y_img.astype(np.float32) / 255.

    # Predict
    pre = srcnn_model.predict(Y, batch_size=1) * 255.

    # Post process output
    pre[pre[:] > 255] = 255
    pre[pre[:] < 0] = 0
    pre = pre.astype(np.uint8)

    # Copy y channel back to image and convert to BGR
    output = cv2.cvtColor(target, cv2.COLOR_BGR2YCrCb)
    output[6: -6, 6: -6, 0] = pre[0, :, :, 0]
    output = cv2.cvtColor(output, cv2.COLOR_YCrCb2BGR)

    filename = Path(fileDirectory).stem
    # Save image
    cv2.imwrite(str(filename + '_optimized.jpg'), output)


def main():
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-d", "--directory", help="Directory to Image File", type=str, required=True)

    # Read arguments from command line
    args = parser.parse_args()

    # getting optimized image
    optimizeImage(args.directory)



if __name__ == "__main__":
    main()
