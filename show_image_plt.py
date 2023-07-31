import os
import matplotlib.pyplot as plt
import matplotlib.image as img

test_folder = r"C:\Users\JagadeshP-Kairos\Downloads\bardata(1031)\bardata(1031)\bar\images\val2019"

lst = [image for image in (os.listdir(test_folder))[0:5]]


def show_prdicts(image):
    testImage = img.imread(os.path.join(test_folder, image))
    plt.imshow(testImage)


for i in lst:
    show_prdicts(i)
