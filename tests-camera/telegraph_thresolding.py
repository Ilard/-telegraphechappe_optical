import cv2
import datetime
# init
frame = None
th1 = None

def nothing(x):
    pass

# image capture
capture = cv2.VideoCapture(3)
cv2.namedWindow("Thresholding_w")
cv2.createTrackbar("Thresholding_tb", "Thresholding_w", 0, 255, nothing)

# continuous read
while(capture.isOpened()):
    ret, frame = capture.read()
    # convert to grey
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # thresholding operation
    # _, th1 = cv2.threshold(grey, 50, 255, cv2.THRESH_BINARY)
    thresholding_value = cv2.getTrackbarPos("Thresholding_tb", "Thresholding_w")
    _, th1 = cv2.threshold(grey, thresholding_value, 255, cv2.THRESH_BINARY)
    # display/save original & thresholding
    cv2.imshow("Original capture", frame)
    cv2.imshow("Thresholding capture", th1)

    # find contours in the binary image
    # im2, contours, hierarchy = cv2.findContours(th1, cv2.RETR_TREE,
    #                                             cv2.CHAIN_APPROX_SIMPLE)
    # for c in contours:
    #     # calculate moments for each contour
    #     M = cv2.moments(c)
    #
    #     # calculate x,y coordinate of center
    #     cX = int(M["m10"] / M["m00"])
    #     cY = int(M["m01"] / M["m00"])
    #     cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
    #     cv2.putText(frame, "centroid", (cX - 25, cY - 25),
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    #
    #     # display the image
    #     cv2.imshow("Image", img)

    # waiting escape key to write finals files
    key = cv2.waitKey(1)
    if key == 27:
        # disconnect camera
        capture.release()
# save original & thresholding images
y = str(datetime.datetime.now().year)
mo = str(datetime.datetime.now().month)
d = str(datetime.datetime.now().day)
h = str(datetime.datetime.now().hour)
m = str(datetime.datetime.now().minute)
s = str(datetime.datetime.now().second)
dt = f"{y}-{mo}-{d}_{h}.{m}.{s}"
if frame.any() and th1.any():
    cv2.imwrite(f"img-output/{dt}_telegraph-original.png", frame)
    cv2.imwrite(f"img-output/{dt}_telegraph-thresholding.png", th1)
# close window
cv2.destroyAllWindows()
