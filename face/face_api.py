from aip import AipFace
from .util import image_to_base64, show_parse_img

APP_ID = '25168998'
API_KEY = 'XTLLZ55NyCjqpchcbGIrlMFh'
SECRET_KEY = 'iKpy7XEbq8AQRw6frGcwfuGvRHNut5pK'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

def face_detect(img_path):
    '''人脸检测:检测人脸并定位，返回五官关键点，及人脸各属性值'''
    image = image_to_base64(img_path)
    imageType = "BASE64"

    # 调用人脸检测
    # 如果有可选参数
    options = {}
    options["face_field"] = "landmark" # 默认只返回face_token、人脸框、概率和旋转角度
    # options["max_face_num"] = 2 # 最多检测人脸的数目，默认值1，最大值10,检测图片中面积最大的人脸；
    # options["face_type"] = "LIVE" 
    # LIVE表示生活照，IDCARD表示身份证芯片照
    # WATERMARK表示带水印证件照，CERT表示证件照片
    # options["liveness_control"] = "LOW"
    # LOW:较低的活体要求 NORMAL: 一般的活体要求 HIGH: 较高的活体要求

    # 带参数调用人脸检测
    result = client.detect(image, imageType, options)
    show_parse_img(img_path, result)


def face_search(img_path):
    '''1：N人脸搜索：也称为1：N识别，在指定人脸集合中，找到最相似的人脸
        需要先注册人脸'''
    image = image_to_base64(img_path)
    imageType = "BASE64"
    groupIdList = "default"

    # 调用人脸检测
    result= client.search(image, imageType, groupIdList)
    print(result)
    ''''
    result': {
    'face_token': 'eb2443749c2d5bc282159c8b63f7cf97', 
    'user_list': [
    {'group_id': 'default', 'user_id': 'zyq', 'user_info': '', 'score': 100}
    ]
    }
    '''

    # 如果有可选参数
    # options = {}
    # options["max_face_num"] = 3
    # options["match_threshold"] = 70
    # options["quality_control"] = "NORMAL"
    # options["liveness_control"] = "LOW"
    # options["user_id"] = "233451"
    # options["max_user_num"] = 3

    """ 带参数调用人脸搜索 """
    # client.search(image, imageType, groupIdList, options)


def face_multi_search(img_path):
    image = image_to_base64(img_path)
    imageType = "BASE64" # BASE64/URL

    groupIdList = "students"

    """ 调用人脸搜索 M:N 识别 """
    result = client.multiSearch(image, imageType, groupIdList);
    show_parse_img(img_path, result)
    
    # """ 如果有可选参数 """
    # options = {}
    # options["max_face_num"] = 3
    # options["match_threshold"] = 70
    # options["quality_control"] = "NORMAL"
    # options["liveness_control"] = "LOW"
    # options["max_user_num"] = 3

    # """ 带参数调用人脸搜索 M:N 识别 """
    # client.multiSearch(image, imageType, groupIdList, options)


def face_match(img_path_1, img_path_2):
    result = client.match([
        {
            'image': image_to_base64(img_path_1),
            'image_type': 'BASE64',
        },
        {
            'image': image_to_base64(img_path_2),
            'image_type': 'BASE64',
        }
    ])
    print('相似度为：' + result['score'])

if __name__ == "__main__":
    face_detect('person/zyq.jpg')
    # face_match('person/zyq.jpg','person/zyq1.jpg')