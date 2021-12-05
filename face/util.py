import cv2
import base64
import requests


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
        print("Succeed: %s >> 图片转换成base64" % img_path)
        return data.decode('ascii')


def show_parse_img(img_path, result_data):
    if result_data['result'] != None:
        # 解析位置信息
        location=result_data['result']['face_list'][0]['location']

        left_top=(int(location['left']),int(location['top']))
        right_bottom=(left_top[0]+int(location['width']),left_top[1]+int(location['height']))
        img=cv2.imread(img_path)
        cv2.rectangle(img,left_top,right_bottom,(0,0,255),2)
        if result_data['result']['face_list'][0]['landmark72']:
            landmark = result_data['result']['face_list'][0]['landmark72']
            for m in landmark:
                cv2.circle(img, (int(m['x']), int(m['y'])), 2, (0, 255, 0), 4)
        cv2.namedWindow("img",0)
        # 按比例缩放
        w = img.shape[1]
        h = img.shape[0]
        if h > w:
            ratio = 700/h
        else:
            ratio = 1000/w

        cv2.resizeWindow("img", int(img.shape[1]*ratio), int(img.shape[0]*ratio))
        cv2.imshow('img',img)
        cv2.waitKey(0)