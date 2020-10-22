from fpdf import FPDF
from PIL import Image
import os

max_width = 0
max_height = 0


def resize_pic(list_image):
    global max_width
    global max_height
    for image_address in list_image:
        image = Image.open(image_address)
        width, height = image.size
        if width > max_width:
            max_width = width
        if height > max_height:
            max_height = height

    # resize
    for image_address in list_image:
        image = Image.open(image_address)
        image_width, image_height = image.size
        rate_width = max_width / image_width
        rate_height = max_height / image_height
        if rate_width > rate_height:
            rate = rate_height
        else:
            rate = rate_width
        new_size = (int(image_width * rate), int(image_height * rate))
        new_image = image.resize(new_size)
        new_image.save("temp\\" + image_address)


def makePdf(pdf_file_name, list_pages):
    global max_width
    global max_height
    pdf = FPDF(unit="pt", format=[max_width, max_height])
    for page in list_pages:
        pdf.add_page()
        pdf.image(page, 0, 0)
    pdf.output(pdf_file_name, "F")


imageIds = []
file_list = os.listdir(".")
for f in file_list:
    if os.path.isfile(f):
        if f.endswith(".jpg") or f.endswith(".png"):
            imageIds.append(f)

resize_pic(imageIds)
new_address = []
for image in imageIds:
    new_address.append("temp\\" + image)
makePdf("result.pdf", new_address)

