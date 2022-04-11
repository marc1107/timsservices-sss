import numpy as np
import matplotlib.pyplot as plt 
import cv2

darkImageName = "AverageBlackImage"
otherImageName = "GreyscaleCorrectedWithBlackWhiteImage"

whiteImageName = "AverageWhiteImage"

frame = cv2.imread(whiteImageName + ".png")
whiteImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

frame = cv2.imread(darkImageName + ".png")
darkImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

frame = cv2.imread(otherImageName + ".png")
otherImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

otherImageBlackCorrected = otherImage.copy()

for x in range(otherImageBlackCorrected.shape[1]):
    for y in range(otherImageBlackCorrected.shape[0]):
        otherImageBlackCorrected[y, x] -= darkImage[y, x]
        
otherImageBlackWhiteCorrected = otherImageBlackCorrected.copy()
        
# get number of total pixels
nPixel = float(whiteImage.shape[0]) * float(whiteImage.shape[1])
print(nPixel)

# calculate the average of all pixels in the white image
pixelAverage = 0.0
for x in range(whiteImage.shape[1]):
    for y in range(whiteImage.shape[0]):
        pixelAverage += float(whiteImage[y, x])
        
pixelAverage = pixelAverage / nPixel
print(pixelAverage)
        
# get normalized white image: divide every pixel by the average of all pixels
normalizedWhiteImage = np.zeros(whiteImage.shape, np.float64)
for x in range(whiteImage.shape[1]):
    for y in range(whiteImage.shape[0]):
        normalizedWhiteImage[y, x] = float(whiteImage[y, x]) / pixelAverage
        #print(normalizedWhiteImage[y, x])

# get corrected image with black and white correction:
# divide every pixel in the other image by every pixel in the normalized image
for x in range(otherImageBlackWhiteCorrected.shape[1]):
    for y in range(otherImageBlackWhiteCorrected.shape[0]):
        otherImageBlackWhiteCorrected[y, x] = \
        float(otherImageBlackWhiteCorrected[y, x]) / normalizedWhiteImage[y, x]


print(otherImageBlackWhiteCorrected[100, 200])
print(otherImageBlackCorrected[100, 200])


#cv2.imwrite(str(otherImageName) + "CorrectedWithBlackImage" + ".png", otherImageBlackCorrected)
#cv2.imwrite(str(otherImageName) + "CorrectedWithBlackWhiteImage" + ".png", otherImageBlackWhiteCorrected)
cv2.imwrite("2timesCorrectedGreyscale" + ".png", otherImageBlackWhiteCorrected)

cv2.imshow("Noramlized White Image", normalizedWhiteImage)
cv2.imshow("Original", otherImage)
cv2.imshow("Corrected with black image", otherImageBlackCorrected)
cv2.imshow("Corrected with black and white image", otherImageBlackWhiteCorrected)
cv2.waitKey(0)
cv2.destroyAllWindows()
