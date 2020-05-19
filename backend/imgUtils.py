import base64
from io import BytesIO
from PIL import Image

def rgbToBuffer(rgb_array):
    pil_img = Image.fromarray(rgb_array.astype('uint8'))
    buff = BytesIO()
    pil_img.save(buff, format="JPEG")
    return buff.getvalue()

def base64StringToRgb(base64_string):
    img_data = base64.b64decode(str(base64_string))
    image = BytesIO(img_data)
    return image