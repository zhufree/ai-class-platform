# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ai-teach.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1120, 558)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(250, 0, 371, 591))
        self.stackedWidget.setStyleSheet(u"")
        self.facePage = QWidget()
        self.facePage.setObjectName(u"facePage")
        self.faceDetectBtn = QPushButton(self.facePage)
        self.faceDetectBtn.setObjectName(u"faceDetectBtn")
        self.faceDetectBtn.setGeometry(QRect(130, 30, 121, 51))
        self.faceDetectBtn.setStyleSheet(u"")
        self.faceRegBtn = QPushButton(self.facePage)
        self.faceRegBtn.setObjectName(u"faceRegBtn")
        self.faceRegBtn.setGeometry(QRect(130, 110, 121, 51))
        self.faceRegBtn.setStyleSheet(u"")
        self.faceSearchBtn = QPushButton(self.facePage)
        self.faceSearchBtn.setObjectName(u"faceSearchBtn")
        self.faceSearchBtn.setGeometry(QRect(130, 190, 121, 51))
        self.faceSearchBtn.setStyleSheet(u"")
        self.faceMultiSearchBtn = QPushButton(self.facePage)
        self.faceMultiSearchBtn.setObjectName(u"faceMultiSearchBtn")
        self.faceMultiSearchBtn.setGeometry(QRect(130, 270, 121, 51))
        self.faceMultiSearchBtn.setStyleSheet(u"")
        self.faceMatchBtn = QPushButton(self.facePage)
        self.faceMatchBtn.setObjectName(u"faceMatchBtn")
        self.faceMatchBtn.setGeometry(QRect(130, 350, 121, 51))
        self.faceMatchBtn.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.facePage)
        self.voicePage = QWidget()
        self.voicePage.setObjectName(u"voicePage")
        self.stackedWidget.addWidget(self.voicePage)
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(20, 60, 211, 71))
        font = QFont()
        font.setPointSize(12)
        self.titleLabel.setFont(font)
        self.titleLabel.setLayoutDirection(Qt.LeftToRight)
        self.titleLabel.setStyleSheet(u"")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.faceRecPageBtn = QPushButton(self.centralwidget)
        self.faceRecPageBtn.setObjectName(u"faceRecPageBtn")
        self.faceRecPageBtn.setGeometry(QRect(60, 150, 141, 81))
        font1 = QFont()
        font1.setPointSize(14)
        self.faceRecPageBtn.setFont(font1)
        self.faceRecPageBtn.setStyleSheet(u"")
        self.voiceRecPageBtn = QPushButton(self.centralwidget)
        self.voiceRecPageBtn.setObjectName(u"voiceRecPageBtn")
        self.voiceRecPageBtn.setGeometry(QRect(60, 260, 141, 81))
        self.voiceRecPageBtn.setFont(font1)
        self.voiceRecPageBtn.setStyleSheet(u"")
        self.fileSelectBtn = QPushButton(self.centralwidget)
        self.fileSelectBtn.setObjectName(u"fileSelectBtn")
        self.fileSelectBtn.setGeometry(QRect(810, 30, 141, 51))
        self.fileSelectBtn.setStyleSheet(u"")
        self.showPicLabel = QLabel(self.centralwidget)
        self.showPicLabel.setObjectName(u"showPicLabel")
        self.showPicLabel.setGeometry(QRect(680, 100, 411, 261))
        self.showPicLabel.setAlignment(Qt.AlignCenter)
        self.funcBtn = QPushButton(self.centralwidget)
        self.funcBtn.setObjectName(u"funcBtn")
        self.funcBtn.setGeometry(QRect(752, 427, 271, 51))
        self.funcBtn.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1120, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.faceDetectBtn.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u8138\u68c0\u6d4b", None))
        self.faceRegBtn.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u8138\u6ce8\u518c", None))
        self.faceSearchBtn.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u81381\uff1aN\u641c\u7d22", None))
        self.faceMultiSearchBtn.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u8138M\uff1aN\u641c\u7d22", None))
        self.faceMatchBtn.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u8138\u5339\u914d", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528\n"
"\u4eba\u5de5\u667a\u80fd\u6559\u5b66\u652f\u6301\u5e73\u53f0", None))
        self.faceRecPageBtn.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u8138\u8bc6\u522b", None))
        self.voiceRecPageBtn.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u97f3\u8bc6\u522b", None))
        self.fileSelectBtn.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.showPicLabel.setText("")
        self.funcBtn.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c:", None))
    # retranslateUi

