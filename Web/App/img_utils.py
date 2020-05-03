import base64
import io
import numpy as np
from PIL import Image

def rgb_to_buffer(rgb_array):
    pil_img = Image.fromarray(rgb_array.astype('uint8'))
    buff = io.BytesIO()
    pil_img.save(buff, format="JPEG")
    return buff.getvalue()

def buffer_to_base64_string(buffer):
    return base64.b64encode(buffer).decode("utf-8")

def base64_string_to_rgb(base64_string):
    img_data = base64.b64decode(str(base64_string))
    image = Image.open(io.BytesIO(img_data))
    return np.array(image)