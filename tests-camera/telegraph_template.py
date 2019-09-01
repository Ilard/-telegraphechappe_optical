"""
Description:    Compare de camera view (or fix image if no camera)
                with a image template file.

Principle:      - Capture the camera or read fix image
                - Current image is grey scale convert.
                - A threshold black/white separation is apply.
                - Read the template image file.
                - Compare the  2 images and

2019-09-01:     Creation
"""
import cv2

# constants definitions
#   internal webcam = 0 and 1
#   JC's external camera = 2
#   SAM's external camera = 3
CAMERA_ID = 3
CAMERA_USED = False
# init
camera_access = None
key = None
frame = None
th1 = None

# threshold black/white trackbar callback not use here
def nothing(x):
    pass

# threshold black/white trackbar window definition
cv2.namedWindow("Threshold_w")
cv2.createTrackbar("Threshold_tb", "Threshold_w", 0, 255, nothing)
# camera hardware channel definition
if CAMERA_USED:
    camera_access = cv2.VideoCapture(CAMERA_ID)

# continuous read and processing
while(key != 27):
    if CAMERA_USED:
        ret, frame = camera_access.read()
    else:
        frame = cv2.imread("img-replace-camera/replace-camera001.png")
    # convert to grey
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # threshold operation
    # _, th1 = cv2.threshold(grey, 50, 255, cv2.THRESH_BINARY)
    threshold_value = cv2.getTrackbarPos("Threshold_tb", "Threshold_w")
    _, th1 = cv2.threshold(grey, threshold_value, 255, cv2.THRESH_BINARY)
    # display original & threshold
    cv2.imshow("Original capture", frame)
    cv2.imshow("Threshold capture", th1)

    # waiting escape key to write finals files
    key = cv2.waitKey(1)

# disconnect camera
if CAMERA_USED:
    camera_access.release()
# close window
cv2.destroyAllWindows()
