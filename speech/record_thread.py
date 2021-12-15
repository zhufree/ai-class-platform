from .speech_api import *
from PySide6.QtCore import QThread

class RecordThread(QThread):
    def  __init__(self,ui,audiofile='temp.wav',parent=None):
        super(RecordThread,self).__init__(parent)
        self.bRecord = True
        self.audiofile = audiofile
        self.ui = ui
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 2
        self.rate=16000

    def run(self):
        audio = pyaudio.PyAudio()
        wavfile = wave.open(self.audiofile,"wb")
        wavfile.setnchannels(self.channels)
        wavfile.setsampwidth(audio.get_sample_size(self.format))
        wavfile.setframerate(self.rate)
        wavstream = audio.open(format=self.format,
                             channels=self.channels,
                             rate=self.rate,
                             input=True,
                             frames_per_buffer=self.chunk)
        # self.dynamic_plot()
        while self.bRecord:
            wavfile.writeframes(wavstream.read(self.chunk))
            if keyboard.is_pressed('enter'):
                self.bRecord = False
                break
        wavstream.stop_stream()
        wavstream.close()
        wavfile.close()
        self.translate_to_text()


    def translate_to_text(self):
        self.ui.setText('识别中...')
        result = voice_to_text()
        self.ui.setText("识别结果：" + result)


    def __del__(self):
        self.working=False
        self.wait()
