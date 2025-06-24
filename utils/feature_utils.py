import cv2
import numpy as np

def compute_histogram(image_path):
    image = cv2.imread(image_path)
    hist = []
    for i in range(3):  # BGR
        h = cv2.calcHist([image], [i], None, [64], [0, 256]) #Histogram
        h = cv2.normalize(h, h).flatten()
        hist.extend(h)
    return np.array(hist).tolist()
