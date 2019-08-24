import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LowerHue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LowerSaturation", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LowerValue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UpperHue", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UpperSaturation", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UpperValue", "Tracking", 255, 255, nothing)

while True:
    # read image
    frame = cv2.imread("img/smarties.png")
    # lower range
    l_h = cv2.getTrackbarPos("LowerHue", "Tracking")
    l_s = cv2.getTrackbarPos("LowerSaturation", "Tracking")
    l_v = cv2.getTrackbarPos("LowerValue", "Tracking")
    # upper range
    u_h = cv2.getTrackbarPos("UpperHue", "Tracking")
    u_s = cv2.getTrackbarPos("UpperSaturation", "Tracking")
    u_v = cv2.getTrackbarPos("UpperValue", "Tracking")


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    l_b = np.array([l_h, l_s, l_v])   # lower blue color
    u_b = np.array([u_h, u_s, u_v])   # upper blue color

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    key = cv2.waitKey(1)
    if key == 27:
        break

# close window
cv2.destroyAllWindows()

