import cv2
# telegraphe-de-chappe

import cv2
print(cv2.__version__)

image = cv2.imread("img/dessin-telegraph.jpg")
print(image)
cv2.imshow("test", image)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("img/dessin-telegraph_copy.png", image)
    cv2.destroyAllWindows()
