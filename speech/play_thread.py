from .speech_api import *
from PySide6.QtCore import QThread

class PlayThread(QThread):
    def  __init__(self, text, status_ui, parent=None):
        super(PlayThread,self).__init__(parent)
        self.text = text
        self.ui = status_ui

    def run(self):
        result = text_to_voice(self.text)
        if result != None:
            self.ui.setText(result)

    def __del__(self):
        self.working=False
        self.wait()