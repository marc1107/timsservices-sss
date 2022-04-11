import numpy as np
import matplotlib.pyplot as plt 
import cv2

frame = cv2.imread("AverageBlackImage.png")
blackImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

images = []

for n in range(1, 11):
    frame = cv2.imread("Images/WhiteImages/White" + str(n) + ".png")
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    images.append(grey)


average_white_image = np.zeros(images[0].shape, np.uint8)

for x in range(images[0].shape[1]):
    for y in range(images[0].shape[0]):
        pixel = 0.0
        for n in range(0, 10):
            pixel = pixel + images[n][y, x]
            
        pixel = pixel // 10.0
        average_white_image[y, x] = pixel - blackImage[y, x]

cv2.imshow("AverageWhiteImage", average_white_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("AverageWhiteImage.png", average_white_image)
# Kontrast maximieren
image_enhanced = cv2.equalizeHist(average_white_image)
cv2.imwrite("AverageWhiteImageMaxContrast.png", image_enhanced)