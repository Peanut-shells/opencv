import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('unknown.png')
img1 = cv.imread('unknown.png', 0)
color = ('b', 'g', 'r')
histr = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histr)
plt.xlim([0, 256])

plt.show()
