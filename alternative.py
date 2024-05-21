
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
result = cloudinary.uploader.upload("1.pdf", ocr="adv_ocr:document")
if result["info"]["ocr"]["adv_ocr:document"]["status"] == "complete":
    data = result["info"]["ocr"]["adv_ocr:document"]["data"][0]["textAnnotations"]

# data_json = json.dumps(data, indent=2, ensure_ascii=False)
# print("OCR Data JSON: \n", data_json)

# 指定的矩形区域


# 提取在指定矩形区域中的所有文字
extracted_text = ["",""]


targets = ["纳税人识别号:", "名 称:"]
i = 0;
for target_text in targets:
    found_target = False
    description = ""
    newLoop = True
    for item in data:
        if newLoop :
            newLoop = False
            continue

        description += item["description"]

        if found_target:
        # 如果找到了目标文本，提取下一个文本并退出循环
            extracted_text[i] = item["description"]
            i += 1
            break

    # 检查当前文本是否是目标文本
        if description.__contains__(target_text):
            found_target = True


print("开户行及账号:", extracted_text[0])
print("税务合计小写:", extracted_text[1])


