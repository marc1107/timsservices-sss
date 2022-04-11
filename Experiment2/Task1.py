import numpy as np
import matplotlib.pyplot as plt 
import cv2


frame = cv2.imread("Greyscale.png")
img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

whiteSlice = img[:500, :140]
whiteGreySlice = img[:500, 175:315]
greySlice = img[:500, 320:460]
greyBlackSlice = img[:500, 465:605]
blackSlice = img[:500, 610:800]

cv2.imshow("Original", img)
cv2.imshow("whiteSlice", whiteSlice)
cv2.imshow("whiteGreySlice", whiteGreySlice)
cv2.imshow("greySlice", greySlice)
cv2.imshow("greyBlackSlice", greyBlackSlice)
cv2.imshow("blackSlice", blackSlice)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("whiteSlice.png", whiteSlice)
cv2.imwrite("whiteGreySlice.png", whiteGreySlice)
cv2.imwrite("greySlice.png", greySlice)
cv2.imwrite("greyBlackSlice.png", greyBlackSlice)
cv2.imwrite("blackSlice.png", blackSlice)

whiteAverage = np.average(whiteSlice)
whiteStd = np.std(whiteSlice)

whiteGreyAverage = np.average(whiteGreySlice)
whiteGreyStd = np.std(whiteGreySlice)

greyAverage = np.average(greySlice)
greyStd = np.std(greySlice)

greyBlackAverage = np.average(greyBlackSlice)
greyBlackStd = np.std(greyBlackSlice)

blackAverage = np.average(blackSlice)
blackStd = np.std(blackSlice)

fig = plt.figure(dpi=300)
ax = fig.add_subplot(1,1,1)
table_data=[
    ["", "Average            ", "Standard Derivation"],
    ["White Image", whiteAverage, whiteStd],
    ["White-Grey Image", whiteGreyAverage, whiteGreyStd],
    ["Grey Image", greyAverage, greyStd],
    ["Grey-Black Image", greyBlackAverage, greyBlackStd],
    ["Black Image", blackAverage, blackStd],
]
table = ax.table(cellText=table_data, loc='center')
table.set_fontsize(14)
table.scale(1,4)
ax.axis('off')
plt.show()