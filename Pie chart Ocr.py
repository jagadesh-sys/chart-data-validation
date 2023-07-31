import io
import cv2
import webcolors
from colorthief import ColorThief
import extcolors
file = "pie1.png"
colors, pixel_count = extcolors.extract_from_path(file)
colors_list = []
for c in colors:
    colors_list.append(c[0])
file1 = io.open(file, "rb", buffering = 0)
# print(file.read())
color_thief = ColorThief(file1)
# print(color_thief.get_color(quality=1))
# print(color_thief.get_palette(quality=1))
colour_dict = {}
All_colours = (color_thief.get_palette(quality=1))

def get_colour_name(rgb_triplet):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb_triplet[0]) ** 2
        gd = (g_c - rgb_triplet[1]) ** 2
        bd = (b_c - rgb_triplet[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

# for colors in All_colours:
#     colour_dict[colors] = get_colour_name(colors)
# print(colour_dict)


def calcPercentage(msk):
    height, width = msk.shape[:2]
    num_pixels = height * width
    count_white = cv2.countNonZero(msk)
    percent_white = (count_white / full_count) * 100
    percent_white = str(round(percent_white)) + "%"
    # cv2.imshow("mask", msk)
    # cv2.waitKey()
    return percent_white


img = cv2.imread(file)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

full1 = cv2.inRange(img_hsv, (0, 1, 1), (255, 254, 255))
# cv2.imshow("full",full1)
full_count = cv2.countNonZero(full1)

mask1 = cv2.inRange(img_hsv, (0, 50, 20), (5, 255, 255))
mask2 = cv2.inRange(img_hsv, (175, 50, 20), (180, 255, 255))
# print(get_colour_name(colour))
mask = cv2.bitwise_or(mask1, mask2)
croped = cv2.bitwise_and(img, img, mask=mask)
print(calcPercentage(msk=mask),"red")
# cv2.imshow("mask", mask)
# cv2.imshow("croped", croped)
cv2.waitKey()
# if 150 <= colour[2] <= 255:
mask1 = cv2.inRange(img_hsv, (78, 158, 124), (138, 255, 255))
croped1 = mask1
print(calcPercentage(msk=croped1),"blue")
# cv2.imshow("mask", mask1)
# cv2.imshow("croped", croped)
# cv2.waitKey()

# if 140 <= colour[2] <= 255 & 100 <= colour[0] <= 150:
mask1 = cv2.inRange(img_hsv, (129, 50, 70), (158, 255, 255))
croped2 = mask1
print(calcPercentage(msk=croped2),"violet")
# cv2.imshow("mask", mask1)
# cv2.imshow("croped", croped)
# cv2.waitKey()

# if 200 <= colour[0] <= 255 & 100 <= colour[1] < 150:
mask1 = cv2.inRange(img_hsv, (10, 50, 70), (24, 255, 255))
croped3 = mask1
print(calcPercentage(msk=croped3),"orange")
# cv2.imshow("mask", mask1)
# cv2.imshow("croped", croped)
# cv2.waitKey()

# if 150 <= colour[1] <= 200:
mask1 = cv2.inRange(img_hsv, (36, 50, 70), (89, 255, 255))
croped4 = mask1
print(calcPercentage(msk=croped4),"Green")
# cv2.imshow("mask", mask1)
# cv2.imshow("croped", croped)
# cv2.waitKey()

mask2 = cv2.inRange(img_hsv, (78, 140, 200), (138, 200, 255))
croped4 = mask2
print(calcPercentage(msk=croped4),"Blue Gray")
# cv2.imshow("mask2", mask2)
# cv2.imshow("croped", croped)
# cv2.waitKey()