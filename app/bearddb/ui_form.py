# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QWidget)

class Ui_Beardb(object):
    def setupUi(self, Beardb):
        if not Beardb.objectName():
            Beardb.setObjectName(u"Beardb")
        Beardb.resize(800, 600)
        self.frame = QFrame(Beardb)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 791, 591))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 10, 181, 581))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 71, 31))
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 10, 71, 32))
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 50, 181, 521))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 179, 519))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Beardb)

        QMetaObject.connectSlotsByName(Beardb)
    # setupUi

    def retranslateUi(self, Beardb):
        Beardb.setWindowTitle(QCoreApplication.translate("Beardb", u"Beardb", None))
        self.label.setText(QCoreApplication.translate("Beardb", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Projects</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Beardb", u"New", None))
    # retranslateUi

