from aip import AipSpeech
import os
import pyaudio, wave
import keyboard
from pydub import AudioSegment
from pydub.playback import play


""" 你的 APPID AK SK """
APP_ID = '25322432'
API_KEY = 'fUneEWdu6CtTdv8qgbnoCUjH'
SECRET_KEY = 'WRW4A3rBV9iUl0x1jvGbiaPqPbEu6koz'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

CHUNK = 1024  # 每个缓冲区的帧数
FORMAT = pyaudio.paInt16  # 采样位数
CHANNELS = 1  # 单声道
RATE = 16000  # 采样频率

def record_voice():
    """ 录音功能 """
    p = pyaudio.PyAudio()  # 实例化对象
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)  # 打开流，传入响应参数
    wf = wave.open('temp.wav', 'wb')  # 打开 wav 文件。
    wf.setnchannels(CHANNELS)  # 声道设置
    wf.setsampwidth(p.get_sample_size(FORMAT))  # 采样位数设置
    wf.setframerate(RATE)  # 采样频率设置

    while True:
        data = stream.read(CHUNK)
        wf.writeframes(data)  # 写入数据
        if keyboard.is_pressed('enter'):
            break
    stream.stop_stream()  # 关闭流
    stream.close()
    p.terminate()
    wf.close()


def play_voice(file_input_path):
    if file_input_path.endswith('.wav'):
        song = AudioSegment.from_wav(file_input_path)
    elif file_input_path.endswith('.mp3'):
        song = AudioSegment.from_mp3(file_input_path)
    if song != None:
        play(song)
    else:
        return 'Can not recognize audio file.'



# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 1537    普通话(纯中文识别)  语音近场识别模型    有标点 支持自定义词库
# 1737    英语      无标点 不支持自定义词库
# 1637    粤语      有标点 不支持自定义词库
# 1837    四川话     有标点 不支持自定义词库
# 1936    普通话远场   远场模型    有标点 不支持
def voice_to_text():
    # 识别本地文件
    result = client.asr(get_file_content('temp.wav'), 'wav', RATE, {
        'dev_pid': 1537, # 普通话
    })
    os.remove('temp.wav')
    if result['err_no'] == 0 and result['result'] != None and len(result['result']) > 0:
        return result['result'][0]
    else:
        return result['err_msg']

def text_to_voice(text):
    result  = client.synthesis(text, 'zh', 1, {
        'vol': 5,
    })
    text = text.replace(' ', '')

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('{}-result.mp3'.format(text), 'wb') as f:
            f.write(result)
        return play_voice('{}-result.mp3'.format(text))

def test():
    record_voice()
    voice_to_text()
    # text_to_voice('磕死我了')


if __name__ == '__main__':
    # test()
    pass