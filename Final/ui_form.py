# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        font = QFont()
        font.setBold(True)
        Widget.setFont(font)
        Widget.setStyleSheet(u"QWidget {\n"
"    background-color: rgba(0, 0, 0, 0.7); \n"
"}\n"
"")
        self.ok_button = QPushButton(Widget)
        self.ok_button.setObjectName(u"ok_button")
        self.ok_button.setGeometry(QRect(400, 500, 130, 25))
        self.ok_button.setStyleSheet(u"QPushButton {\n"
"    background-color: blue;\n"
"    color: white; /* Text color set to white for better contrast */\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: darkblue;\n"
"    border-radius: 4px; /* Adjust the radius to your preference */\n"
"    padding: 5px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.exit_button = QPushButton(Widget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(680, 40, 80, 40))
        self.exit_button.setStyleSheet(u"QPushButton {\n"
"    background-color: red;\n"
"    color: white; /* Setting text color to white for better readability */\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
"")
        self.userNumLabel = QLabel(Widget)
        self.userNumLabel.setObjectName(u"userNumLabel")
        self.userNumLabel.setGeometry(QRect(270, 470, 260, 25))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.userNumLabel.setFont(font1)
        self.userNumLabel.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"}\n"
"")
        self.userNumLabel.setAlignment(Qt.AlignCenter)
        self.userNum = QLineEdit(Widget)
        self.userNum.setObjectName(u"userNum")
        self.userNum.setGeometry(QRect(270, 500, 130, 25))
        self.userNum.setStyleSheet(u"QLineEdit {\n"
"    color: white; /* Set text color */\n"
"    /* Add other styling properties as needed */\n"
"}\n"
"")
        self.movieNameLabel = QLabel(Widget)
        self.movieNameLabel.setObjectName(u"movieNameLabel")
        self.movieNameLabel.setGeometry(QRect(200, 550, 400, 25))
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(True)
        self.movieNameLabel.setFont(font2)
        self.movieNameLabel.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"}\n"
"")
        self.movieNameLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel_1 = QLabel(Widget)
        self.imageLabel_1.setObjectName(u"imageLabel_1")
        self.imageLabel_1.setGeometry(QRect(550, 120, 250, 350))
        self.imageLabel_1.setStyleSheet(u"image: url(:/jupiter.PNG);")
        self.imageLabel_2 = QLabel(Widget)
        self.imageLabel_2.setObjectName(u"imageLabel_2")
        self.imageLabel_2.setGeometry(QRect(275, 75, 250, 375))
        self.imageLabel_2.setStyleSheet(u"image: url(:/adaline.PNG);")
        self.imageLabel_3 = QLabel(Widget)
        self.imageLabel_3.setObjectName(u"imageLabel_3")
        self.imageLabel_3.setGeometry(QRect(0, 120, 250, 350))
        self.imageLabel_3.setStyleSheet(u"image: url(:/xmen.PNG);")
        self.title = QLabel(Widget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(200, 0, 400, 55))
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setItalic(True)
        self.title.setFont(font3)
        self.title.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"}\n"
"")
        self.title.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.ok_button.setText(QCoreApplication.translate("Widget", u"OK", None))
        self.exit_button.setText(QCoreApplication.translate("Widget", u"Exit", None))
        self.userNumLabel.setText(QCoreApplication.translate("Widget", u"Enter a random number", None))
        self.movieNameLabel.setText(QCoreApplication.translate("Widget", u"Movie name will appear here", None))
        self.imageLabel_1.setText("")
        self.imageLabel_2.setText("")
        self.imageLabel_3.setText("")
        self.title.setText(QCoreApplication.translate("Widget", u"Fantasy Movie Selector", None))
    # retranslateUi

