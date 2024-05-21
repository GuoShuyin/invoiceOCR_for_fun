
# Set your Cloudinary credentials
# ==============================
from dotenv import load_dotenv
load_dotenv("file.env")

# Import the Cloudinary libraries
# ==============================
import cloudinary
from cloudinary import CloudinaryImage
import cloudinary.uploader
import cloudinary.api

# Import to format the JSON responses
# ==============================
import json

# Set configuration parameter: return "https" URLs by setting secure=True
# ==============================
config = cloudinary.config(secure=True)

# Log the configuration
# ==============================
print("****1. Set up and configure the SDK:****\nCredentials: ", config.cloud_name, config.api_key, "\n")

# print(cloudinary.uploader.upload("invoice.png",
#   ocr = "adv_ocr"))
result = cloudinary.uploader.upload("3.pdf", ocr="adv_ocr:document")
if result["info"]["ocr"]["adv_ocr:document"]["status"] == "complete":
    data = result["info"]["ocr"]["adv_ocr:document"]["data"][0]["textAnnotations"]

# data_json = json.dumps(data, indent=2, ensure_ascii=False)
# print("OCR Data JSON: \n", data_json)

dataType = ["购买方名称","购买方税号","购买方银行及账户","价税合计"]
# 指定的矩形区域
#购买方
rect_x1, rect_y1 = 209, 181
rect_x2, rect_y2 = 700, 204

rect_x3, rect_y3 = 219, 212
rect_x4, rect_y4 = 700, 237

rect_x5, rect_y5 = 200, 275
rect_x6, rect_y6 = 700, 301

rect_x7, rect_y7 = 985, 574
rect_x8, rect_y8 = 2500, 600

# 提取在指定矩形区域中的所有文字
extracted_text = ["","","","","","",""]
i = 0
for item in data:
    vertices = item["boundingPoly"]["vertices"]
    # 检查每个顶点是否在指定的矩形区域内
    if all(rect_x1 <= vertex["x"] <= rect_x2 and rect_y1 <= vertex["y"] <= rect_y2 for vertex in vertices):
        extracted_text[0] += (item["description"])
        i += 1
    elif all(rect_x3 <= vertex["x"] <= rect_x4 and rect_y3 <= vertex["y"] <= rect_y4 for vertex in vertices):
        extracted_text[1] += (item["description"])
        i += 1
    elif all(rect_x5 <= vertex["x"] <= rect_x6 and rect_y5 <= vertex["y"] <= rect_y6 for vertex in vertices):
        extracted_text[2] += (item["description"])
        i += 1
    elif all(rect_x7 <= vertex["x"] <= rect_x8 and rect_y7 <= vertex["y"] <= rect_y8 for vertex in vertices):
        extracted_text[3] += (item["description"])
        i += 1
for j in range(4):
    print(dataType[j] + " " + extracted_text[j] + "\n")


