import cv2
import base64
import requests
from PIL import Image, ImageDraw, ImageFont


access_token = '24.5200ee372c070dd4d3cf695a2205e007.2592000.1639542335.282335-25168998'
# 11.15 30天内有效

search_url = 'https://aip.baidubce.com/rest/2.0/face/v3/search?access_token={}'

def get_access_token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}' \
            .format(API_KEY, SECRET_KEY)
    response = requests.get(host)
    if response:
        print(response.json()['access_token'])


# image转换成base64并加上 前缀data:image/jpeg;base64,
def image_to_base64(img_path, **kwargs):
    """
    :param filename: image文件名
    :param path: image存放路径
    :param kwargs: 参数prefix(转换base64后需要加上的前缀)
    :return:
    """
    # 转为二进制格式
    with open(img_path, "rb") as f:
        data = base64.b64encode(f.read())
        # 转换base64后加上前缀
        if "prefix" in kwargs.keys():
            data = kwargs["prefix"] + data
            # base64_data = bytes(('data: image/jpeg;base64,%s' % str(base64.b64encode(f.read()), "utf-8")), "utf-8")
        # 转换为bytes对象
        return data.decode('ascii')


def show_parse_img(img_path, result_data):
    if result_data['result'] != None:
        # 解析位置信息
        img = Image.open(img_path)
        draw = ImageDraw.ImageDraw(img)
        for face in result_data['result']['face_list']:
            location = face['location']

            left_top = (int(location['left']), int(location['top']))
            right_bottom = (left_top[0] + int(location['width']), left_top[1] + int(location['height']))
            draw.rectangle((left_top, right_bottom), fill=None, outline=(0, 0, 255), width=2)
            if 'landmark72' in face.keys():
                landmark = face['landmark72']
                for m in landmark:
                    draw.ellipse(((int(m['x'])-2, int(m['y'])-2), (int(m['x'])+2, int(m['y'])+2)),
                        fill="green", outline=(0, 225, 0), width=5)
            if 'user_list' in face.keys() and len(face['user_list']) > 0:
                name = face['user_list'][0]['user_id']
                font = ImageFont.truetype('msyh.ttc', size=30)
                print(name)
                # Draw a label with a name below the face
                text_width, text_height = draw.textsize(name)
                draw.text((int(location['left']), int(location['top'] + location['height'])), 
                    name, font=font, fill=(255, 0, 0, 255), stroke_width=2)
        del draw
        img.show()