# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(752, 339)
        self.startButton = QPushButton(Widget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setEnabled(False)
        self.startButton.setGeometry(QRect(340, 290, 75, 24))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 711, 41))
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 60, 421, 51))
        self.source = QLabel(self.groupBox)
        self.source.setObjectName(u"source")
        self.source.setGeometry(QRect(10, 20, 51, 31))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 20, 229, 22))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.imageRadioButton = QRadioButton(self.layoutWidget)
        self.imageRadioButton.setObjectName(u"imageRadioButton")
        self.imageRadioButton.setEnabled(False)
        self.imageRadioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.imageRadioButton)

        self.videoRadioButton = QRadioButton(self.layoutWidget)
        self.videoRadioButton.setObjectName(u"videoRadioButton")

        self.horizontalLayout.addWidget(self.videoRadioButton)

        self.cameraRadioButton = QRadioButton(self.layoutWidget)
        self.cameraRadioButton.setObjectName(u"cameraRadioButton")

        self.horizontalLayout.addWidget(self.cameraRadioButton)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(40, 120, 421, 51))
        self.inputFile = QLabel(self.groupBox_2)
        self.inputFile.setObjectName(u"inputFile")
        self.inputFile.setGeometry(QRect(10, 20, 51, 31))
        self.inputFileLocationText = QLineEdit(self.groupBox_2)
        self.inputFileLocationText.setObjectName(u"inputFileLocationText")
        self.inputFileLocationText.setGeometry(QRect(90, 20, 231, 22))
        self.inputBrowseButton = QPushButton(self.groupBox_2)
        self.inputBrowseButton.setObjectName(u"inputBrowseButton")
        self.inputBrowseButton.setGeometry(QRect(340, 20, 75, 24))
        self.inputBrowseButton.setCheckable(True)
        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(40, 180, 421, 51))
        self.outputFile = QLabel(self.groupBox_3)
        self.outputFile.setObjectName(u"outputFile")
        self.outputFile.setGeometry(QRect(10, 20, 71, 31))
        self.outputFileLocationText = QLineEdit(self.groupBox_3)
        self.outputFileLocationText.setObjectName(u"outputFileLocationText")
        self.outputFileLocationText.setEnabled(False)
        self.outputFileLocationText.setGeometry(QRect(90, 20, 231, 22))
        self.outputBrowseButton = QPushButton(self.groupBox_3)
        self.outputBrowseButton.setObjectName(u"outputBrowseButton")
        self.outputBrowseButton.setEnabled(False)
        self.outputBrowseButton.setGeometry(QRect(340, 20, 75, 24))
        self.outputBrowseButton.setCheckable(True)

        self.retranslateUi(Widget)

        self.inputBrowseButton.setDefault(True)
        self.outputBrowseButton.setDefault(True)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.startButton.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Human Detection", None))
        self.groupBox.setTitle("")
        self.source.setText(QCoreApplication.translate("Widget", u"Source", None))
        self.imageRadioButton.setText(QCoreApplication.translate("Widget", u"Image", None))
        self.videoRadioButton.setText(QCoreApplication.translate("Widget", u"Video", None))
        self.cameraRadioButton.setText(QCoreApplication.translate("Widget", u"Camera", None))
        self.groupBox_2.setTitle("")
        self.inputFile.setText(QCoreApplication.translate("Widget", u"Input File", None))
        self.inputBrowseButton.setText(QCoreApplication.translate("Widget", u"Browse", None))
        self.groupBox_3.setTitle("")
        self.outputFile.setText(QCoreApplication.translate("Widget", u"Output File", None))
        self.outputBrowseButton.setText(QCoreApplication.translate("Widget", u"Browse", None))
    # retranslateUi

