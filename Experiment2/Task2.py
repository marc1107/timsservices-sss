import numpy as np
import matplotlib.pyplot as plt 
import cv2

fileName = "Black"

images = []

for n in range(1, 11):
    frame = cv2.imread("Images/BlackImages/Black" + str(n) + ".png")
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    images.append(grey)

average_black_image = np.zeros(images[0].shape, np.uint8)

for x in range(images[0].shape[1]):
    for y in range(images[0].shape[0]):
        pixel = 0.0
        for n in range(0, 10):
            pixel = pixel + images[n][y, x]
            
        pixel = pixel // 10.0
        average_black_image[y, x] = pixel

cv2.imshow("AverageBlackImage", average_black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("AverageBlackImage.png", average_black_image)

# Maximize contrast 
image_enhanced = cv2.equalizeHist(average_black_image)
cv2.imshow("enhanced", image_enhanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("AverageBlackImageMaxContrast.png", image_enhanced)

