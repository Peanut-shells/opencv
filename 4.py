import cv2

img1 = cv2.imread("unknown.png")
cv2.imshow("test", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
