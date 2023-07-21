# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'des-sub.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import res_sub_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(700, 120)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(600, 120))
        icon = QIcon()
        icon.addFile(u":/icons/icons/playlist.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(199, 203, 236);\n"
"    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;\n"
"    font-size: 16px;\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(203, 236, 199);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(232, 199, 236)\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(199, 221, 236)\n"
"}\n"
"QLineEdit {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(203, 236, 199);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 1px solid rgb(232, 199, 236);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ln_url = QLineEdit(Dialog)
        self.ln_url.setObjectName(u"ln_url")

        self.verticalLayout.addWidget(self.ln_url)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet(u"padding-left: 10px;\n"
"padding-right: 10px;")

        self.horizontalLayout.addWidget(self.pushButton)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setStyleSheet(u"border-radius: 10px;\n"
"padding-left: 10px;\n"
"padding-right:10px;")

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.btn_enter = QPushButton(Dialog)
        self.btn_enter.setObjectName(u"btn_enter")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_enter.sizePolicy().hasHeightForWidth())
        self.btn_enter.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.btn_enter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.ln_url.setPlaceholderText(QCoreApplication.translate("Dialog", u"Link to the video\\playlist", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Paste copy link above", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Save to: ", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Select...", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Video", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Playlist", None))

        self.btn_enter.setText(QCoreApplication.translate("Dialog", u"Enter", None))
    # retranslateUi

