import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import ai_teach_ui

def show_stack(i):
    ui.stackedWidget.setCurrentIndex(i)

def show_face_rec_page():
    show_stack(0)

def show_voice_rec_page():
    show_stack(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ai_teach_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.faceRecPageBtn.clicked.connect(show_face_rec_page)
    ui.voiceRecPageBtn.clicked.connect(show_voice_rec_page)
    sys.exit(app.exec_())
