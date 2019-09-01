import cv2
# telegraphe-de-chappe

import cv2
print(cv2.__version__)

img = cv2.imread("img/messi5.jpg")
img2 = cv2.imread("img/OpenCV_Logo_with_text.png")
print(img.shape)    # return a tuple of nb raws, colums, channels
print(img.size)     # return Total nb of pixels is accessed
print(img.dtype)    # return image data type
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

# area cloning
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

# resize image
img = cv2.resize(img, (512,320))
img2 = cv2.resize(img2, (512,320))

# add methode
# dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, 0.8, img2, 0.2, 0)

# display
cv2.imshow("image area cloning", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
