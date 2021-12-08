import sys, os
from PySide6.QtWidgets import *
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtGui
from ai_teach_ui import Ui_MainWindow
from PIL import Image
from face.face_api import *
from face.face_register import *
from qt_material import apply_stylesheet

FACE_DETECT = 0
FACE_REG = 1
FACE_1_N_SAERCH = 2
FACE_M_N_SAERCH = 3
FACE_MATCH = 4

class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        qfile = QFile("ai-teach.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)
        self.func = FACE_DETECT
        self.current_img_path = ''
        self.second_img_path = ''
        self.ui.operationWidget.setCurrentIndex(0)
        self.ui.faceRecPageBtn.clicked.connect(self.show_face_rec_page)
        self.ui.voiceRecPageBtn.clicked.connect(self.show_voice_rec_page)
        self.ui.fileSelectBtn.clicked.connect(self.open_photo_file)
        self.ui.secondFileSelectBtn.clicked.connect(self.open_second_photo_file)
        self.ui.funcBtn.clicked.connect(self.on_func_clicked)

        self.ui.faceDetectBtn.clicked.connect(self.on_face_detect_clicked)
        self.ui.faceRegBtn.clicked.connect(self.on_face_register_clicked)
        self.ui.faceSearchBtn.clicked.connect(self.on_face_search_clicked)
        self.ui.faceMultiSearchBtn.clicked.connect(self.on_face_multi_clicked)
        self.ui.faceMatchBtn.clicked.connect(self.on_face_match_clicked)

    def show_stack(self, i):
        self.ui.functionFlowWidget.setCurrentIndex(i)

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

    def open_second_photo_file(self):
        imgName,imgType = QFileDialog.getOpenFileName(self, "选择照片", os.getcwd(), 
        "*.jpg;;*.png;;All Files(*)")
        self.second_img_path = imgName
        img = Image.open(imgName)
        w = img.size[0]
        h = img.size[1]
        if w > h:
            ratio = w/self.ui.showSecondPicLabel.width()
        else:
            ratio = h/self.ui.showSecondPicLabel.height()
        jpg = QtGui.QPixmap(imgName).scaled(int(w/ratio), int(h/ratio))
        self.ui.showSecondPicLabel.setPixmap(jpg)

    def on_face_detect_clicked(self):
        self.func = FACE_DETECT
        self.ui.operationWidget.setCurrentIndex(0)
        self.ui.funcBtn.setText('执行：人脸检测')

    def on_face_register_clicked(self):
        self.func = FACE_REG
        self.ui.operationWidget.setCurrentIndex(1)
        self.ui.nameInput.setEnabled(True)
        self.ui.funcBtn.setText('执行：人脸注册')

    def on_face_search_clicked(self):
        self.func = FACE_1_N_SAERCH
        self.ui.operationWidget.setCurrentIndex(1)
        self.ui.nameInput.setEnabled(True)
        self.ui.funcBtn.setText('执行：人脸1：N搜索')

    def on_face_multi_clicked(self):
        self.func = FACE_M_N_SAERCH
        self.ui.operationWidget.setCurrentIndex(1)
        self.ui.nameInput.setEnabled(False)
        self.ui.funcBtn.setText('执行：人脸M：N搜索')

    def on_face_match_clicked(self):
        self.func = FACE_MATCH
        self.ui.operationWidget.setCurrentIndex(2)
        self.ui.funcBtn.setText('执行：人脸匹配')

    def on_func_clicked(self):
        if self.func == FACE_DETECT:
            face_detect(self.current_img_path)
        elif self.func == FACE_REG:
            name = self.ui.nameInput.toPlainText()
            status = face_reg(self.current_img_path, name)
            self.ui.statusLabel.setText(status)
        elif self.func == FACE_1_N_SAERCH:
            result = face_search(self.current_img_path)
            if result is not None:
                self.ui.statusLabel.setText('匹配结果：{}，匹配度：{}'.format(result['user_id'], result['score']))
        elif self.func == FACE_M_N_SAERCH:
            result = face_multi_search(self.current_img_path)
            if result is not None:
                self.ui.statusLabel.setText(result)
        elif self.func == FACE_MATCH:
            result = face_match(self.current_img_path, self.second_img_path)
            if result['score']:
                self.ui.statusLabel.setText('匹配结果：相似度' + str(result['score']))
            else:
                self.ui.statusLabel.setText('匹配失败：' + result)



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
