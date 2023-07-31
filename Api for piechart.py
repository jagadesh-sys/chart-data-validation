import numpy as np
import pandas as pd
import uvicorn
from flask import request
from fastapi import Form
from fastapi import FastAPI, File
import cv2
app = FastAPI()

@app.post("/piechart/")
def process_image(image: bytes= File(...),chartType: str = Form(...)):
    req_body = request.form
    chartType = req_body.get('chartType')
    image = request.files.get('image')
    print(image)
    # ext = image
    file = request.files['image'].read()
    nparr = np.frombuffer(file, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    width, height, _ = img.shape
    pallet = []
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img_hsv, (0, 1, 1), (255, 255, 255))
    # cv2.imshow("mask", mask)
    # cv2.waitKey(0)
    croped = cv2.bitwise_and(img, img, mask=mask)
    full_count = cv2.countNonZero(mask)
    colour_set = []
    for x in range(0, width, 50):
        for y in range(0, height, 70):
            r, g, b = img[x, y]
            # if r == 0 and g == 0 and b == 255 :
            pallet.append((r, g, b))
    colour_set = set(pallet)
    # print(colour_set)

    index = ["color", "color_name", "hex", "R", "G", "B"]
    csv = pd.read_csv(r'C:\Users\JagadeshP-Kairos\PycharmProjects\ChartDataAnalyzor\python-project-color-detection/colors.csv', names=index, header=None)

    def getColorName(R, G, B):
        minimum = 10000
        for i in range(len(csv)):
            d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
            if (d <= minimum):
                minimum = d
                cname = csv.loc[i, "color_name"]
                color_code = csv.loc[i, "hex"]
        return cname, color_code

    def calcPercentage(msk):
        height, width = msk.shape[:2]
        num_pixels = height * width
        count_white = cv2.countNonZero(msk)
        percent_white = (count_white / full_count) * 100
        percent_white = (round(percent_white))
        # cv2.imshow("mask", msk)
        # cv2.waitKey()
        return percent_white

    black = np.array([0, 0, 0])
    white = np.array([255, 255, 255])
    segment_list = []
    def colour_percentage():
        count = 0
        for i in colour_set:
            segment_dict = {}
            c = np.array(i)
            r = int(i[0])
            g = int(i[1])
            b = int(i[2])
            if not (np.array_equiv(black, c)) and not (np.array_equiv(white, c)):
                # print(getColorName(b,g,r))
                upper = np.array([r + 10, g + 10, b + 40])
                lower = np.array([r - 10, g - 10, b - 40])

                image_mask = cv2.inRange(img, lower, upper)
                croped = cv2.bitwise_and(img_hsv, img_hsv, mask=image_mask)
                # cv2.imshow("mask", image_mask)
                # cv2.imshow("croped", croped)
                # cv2.waitKey(0)
                if int(calcPercentage(msk=image_mask)) > 0:
                    colorname, colorcode = getColorName(b, g, r)
                    if 'White' not in colorname:
                        if 'Snow' not in colorname:
                            if 'Black' not in colorname:
                                segment_dict["ColorName"] = colorname
                                segment_dict["ColorCode"] = colorcode
                                segment_dict["RelativeSizeInPercent"] = calcPercentage(msk=image_mask)
                                count = count + 1
                                segment_dict1 = {}
                                if colorcode not in segment_dict1:
                                    segment_dict1.update(segment_dict)
                                    segment_list.append(segment_dict1)
                                    # output_dict[getColorName(b, g, r)] = calcPercentage(msk=image_mask)
                                    output_dict = {"Image": ext,
                                                    "ChartType": chartType,

                                                      "Data": {

                                                        "NoOfSegments": count,

                                                        "Segments": segment_list

                                                      },
                                                   }
        return output_dict
    return jsonify(colour_percentage())
    # return jsonify({'msg': 'success'})

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


# if __name__ == "__main__":
#     app.run(host="localhost", port=8000, debug=True)