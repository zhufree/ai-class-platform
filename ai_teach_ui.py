# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ai-teach.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 640)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(260, 0, 421, 591))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 40, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 130, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 220, 101, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(self.page)
        self.line.setGeometry(QtCore.QRect(180, 70, 3, 61))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.page)
        self.line_2.setGeometry(QtCore.QRect(180, 150, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.page)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 310, 111, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.faceRecPageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.faceRecPageBtn.setGeometry(QtCore.QRect(40, 150, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.faceRecPageBtn.setFont(font)
        self.faceRecPageBtn.setObjectName("faceRecPageBtn")
        self.voiceRecPageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.voiceRecPageBtn.setGeometry(QtCore.QRect(40, 260, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.voiceRecPageBtn.setFont(font)
        self.voiceRecPageBtn.setObjectName("voiceRecPageBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "人脸检测"))
        self.pushButton_3.setText(_translate("MainWindow", "人脸注册"))
        self.pushButton_4.setText(_translate("MainWindow", "人脸1：N搜索"))
        self.pushButton_6.setText(_translate("MainWindow", "人脸M：N搜索"))
        self.label.setText(_translate("MainWindow", "欢迎使用\n"
"人工智能教学支持平台"))
        self.faceRecPageBtn.setText(_translate("MainWindow", "人脸识别"))
        self.voiceRecPageBtn.setText(_translate("MainWindow", "语音识别"))