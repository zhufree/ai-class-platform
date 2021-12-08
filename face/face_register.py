import base64
from aip import AipFace
from .util import image_to_base64, show_parse_img

APP_ID = '25168998'
API_KEY = 'XTLLZ55NyCjqpchcbGIrlMFh'
SECRET_KEY = 'iKpy7XEbq8AQRw6frGcwfuGvRHNut5pK'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

def face_reg(img_path, user_id):
    image = image_to_base64(img_path)
    imageType = "BASE64"
    groupId = "default"

    """ 调用人脸注册 """
    result = client.addUser(image, imageType, groupId, user_id)
    return result['error_msg']
    # 如果有可选参数
    # options = {}
    # options["user_info"] = "user's info"
    # options["quality_control"] = "NORMAL"
    # options["liveness_control"] = "LOW"
    # options["action_type"] = "REPLACE"

    # 带参数调用人脸注册 """
    # client.addUser(image, imageType, groupId, userId, options)

def get_face_list(user_id):
    groupId = "default"

    """ 调用获取用户人脸列表 """
    result = client.faceGetlist(user_id, groupId)


def face_delete(user_id, face_token):
    groupId = "default"
    """ 调用人脸删除 """
    client.faceDelete(user_id, groupId, face_token);

if __name__ == '__main__':
    face_reg('person/zyq.jpg', 'zyq')