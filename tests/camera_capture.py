import cv2
import datetime

# index 0 mean the first camera id, 1 is the second and so on
# to read video file, replace 0 index by 'filename.mp4'
cap = cv2.VideoCapture(2)

# save streaming in video file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video/output.avi', fourcc, 20.0, (640,480))

# read every time the camera streaming
# while stream or file is correct
while(cap.isOpened()):
    # read the streaming frame
    ret, frame = cap.read()
    if ret == True:

        # write streaming in video file
        # out.write(frame) <---- uncomment to record file !

        # color to gray conversion on the fly
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # write text on the fly
        # video size
        x = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        y = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        size_txt = f"{x} x {y}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        frame = cv2.putText(
            frame,size_txt,(5,275), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
        # display date & time
        h = str(datetime.datetime.now().hour)
        m = str(datetime.datetime.now().minute)
        s = str(datetime.datetime.now().second)
        dt = f"{h}:{m}:{s}"
        frame = cv2.putText(
            frame,dt,(5,30), font, 1, (0, 255, 255), 1, cv2.LINE_AA)

        # display the frame in real time
        cv2.imshow('Press q to quit', frame)
        # quit when 'q' pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# disconnect camera and close window
cap.release()
out.release()
cv2.destroyAllWindows()

