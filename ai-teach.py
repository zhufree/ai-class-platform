import sys, os
from PySide6.QtWidgets import *
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtGui
from ai_teach_ui import Ui_MainWindow
from PIL import Image
from face.face_api import *
from qt_material import apply_stylesheet

FACE_DETECT = 0
FACE_REG = 1
FACE_1_N_SAERCH = 2
FACE_M_N_SAERCH = 3
FACE_MATCH = 4

class MainWindow(QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__()
        # 从ui文件中加载UI定义
        qfile = QFile("ai-teach.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        # 从UI定义中动态创建一个相应的窗口对象
        self.ui = QUiLoader().load(qfile)
        self.func = FACE_DETECT
        self.current_img_path = ''
        self.ui.faceRecPageBtn.clicked.connect(self.show_face_rec_page)
        self.ui.voiceRecPageBtn.clicked.connect(self.show_voice_rec_page)
        self.ui.fileSelectBtn.clicked.connect(self.open_photo_file)
        self.ui.funcBtn.clicked.connect(self.on_func_clicked)

        self.ui.faceDetectBtn.clicked.connect(self.on_face_detect_clicked)
        self.ui.faceRegBtn.clicked.connect(self.on_face_register_clicked)
        self.ui.faceSearchBtn.clicked.connect(self.on_face_search_clicked)
        self.ui.faceMultiSearchBtn.clicked.connect(self.on_face_multi_clicked)

    def show_stack(self, i):
        self.ui.stackedWidget.setCurrentIndex(i)

    def show_face_rec_page(self):
        self.show_stack(0)

    def show_voice_rec_page(self):
        self.show_stack(1)

    def open_photo_file(self):
        imgName,imgType = QFileDialog.getOpenFileName(self, "选择照片", os.getcwd(), 
        "*.jpg;;*.png;;All Files(*)")
        self.current_img_path = imgName
        img = Image.open(imgName)
        w = img.size[0]
        h = img.size[1]
        if w > h:
            ratio = w/self.ui.showPicLabel.width()
        else:
            ratio = h/self.ui.showPicLabel.height()
        jpg = QtGui.QPixmap(imgName).scaled(int(w/ratio), int(h/ratio))
        self.ui.showPicLabel.setPixmap(jpg)

    def on_face_detect_clicked(self):
        self.func = FACE_DETECT
        self.ui.funcBtn.setText('执行：人脸检测')

    def on_face_register_clicked(self):
        self.func = FACE_REG
        self.ui.funcBtn.setText('执行：人脸注册')

    def on_face_search_clicked(self):
        self.func = FACE_1_N_SAERCH
        self.ui.funcBtn.setText('执行：人脸1：N搜索')

    def on_face_multi_clicked(self):
        self.func = FACE_M_N_SAERCH
        self.ui.funcBtn.setText('执行：人脸M：N搜索')

    def on_func_clicked(self):
        if self.func == FACE_DETECT:
            face_detect(self.current_img_path)
        elif self.func == FACE_1_N_SAERCH:
            face_search(self.current_img_path)
        elif self.func == FACE_M_N_SAERCH:
            face_multi_search(self.current_img_path)
        # elif self.func = FACE_MATCH:
        #     face_match(self.current_img_path)



if __name__ == '__main__':
    app = QApplication([])
    apply_stylesheet(app, theme='light_blue.xml')
    # MainWindow = QMainWindow()
    # ui = ai_teach_ui.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    win = MainWindow()
    win.ui.show()
    sys.exit(app.exec())
