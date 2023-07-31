import cv2
import pandas as pd
import numpy as np
import imutils

img = cv2.imread('test_images/download.png')
width, height, _ = img.shape
pallet = []
img_src = imutils.resize(img, height=800)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(img_hsv, (1, 0, 1), (255, 255, 255))
croped = cv2.bitwise_and(img, img, mask=mask)
full_count = cv2.countNonZero(mask)
cv2.imshow("mask", mask)
cv2.imshow("croped", croped)
cv2.waitKey()
colour_set = []
for x in range(0, width, 50):
    for y in range(0, height, 50):
        r,g,b = img[x, y]
        # if r == 0 and g == 0 and b == 255 :
        pallet.append((r,g,b))
colour_set = set(pallet)
# print(set(pallet))

index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv(r'C:\Users\JagadeshP-Kairos\PycharmProjects\ChartDataAnalyzor\python-project-color-detection/colors.csv', names=index, header=None)

def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        full_count = cv2.countNonZero(mask)
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname


def calcPercentage(msk):
    height, width = msk.shape[:2]
    num_pixels = height * width
    count_white = cv2.countNonZero(msk)
    percent_white = (count_white / full_count) * 100
    percent_white = (round(percent_white))
    # cv2.imshow("mask", msk)
    # cv2.waitKey()
    return percent_white


black = np.array([0,0,0])
white = np.array([255, 255, 255])
for i in colour_set:
    c = np.array(i)
    r = int(i[0])
    g = int(i[1])
    b = int(i[2])
    if not (np.array_equiv(black, c)) and not (np.array_equiv(white, c)):
        # print(getColorName(b,g,r))
        upper = np.array([r + 10, g + 10, b + 40])
        lower = np.array([r - 10, g - 10, b - 40])
        # for idx, u in enumerate(upper):
        #     if upper[idx] > 255:
        #         upper[idx] = 255
                # for idx , l in enumerate(lower):
                #     if lower[idx] <= 10:
                #         lower[idx] += 10
        # print(upper, lower)

        image_mask = cv2.inRange(img, lower, upper)
        croped = cv2.bitwise_and(img_hsv, img_hsv, mask=image_mask)
        # cv2.imshow("mask", image_mask)
        # cv2.imshow("croped", croped)
        # cv2.waitKey(0)
        if int(calcPercentage(msk=image_mask)) > 0:
            print(getColorName(b,g,r), f"- {calcPercentage(msk=image_mask)}%")
            # print(convert_rgb_to_names((r, g, b)))
