# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setMinimumSize(QSize(700, 600))
        icon = QIcon()
        icon.addFile(u":/icons/icons/loop_v1_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #e6f2ff;\n"
"    \n"
"    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;\n"
"    font-size: 16px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #b3d9ff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #3399ff;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #0066cc;\n"
"}\n"
"QListView {\n"
"    background-color: #99ccff;\n"
"    border: 5px solid #001a33;\n"
"    border-radius: 10px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #99ccff;\n"
"	background-color: #001a33;\n"
"    height: 5px;\n"
"    margin: 0px;\n"
"    }\n"
"QSlider::handle:horizontal {\n"
"    background-color: #000000;\n"
"    border: none;\n"
"	border-radius: 10px;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: -15px 0px;\n"
"    }\n"
"QSlider::handle:vertical {\n"
"    background-color: #000000;\n"
"    border: none;\n"
"	border-radius: 10px;\n"
"    height: 20px;\n"
"    }\n"
""
                        "QSlider::groove:vertical {\n"
"    border: 1px solid #99ccff;\n"
"	background-color: white;\n"
"	width: 10px;\n"
"    margin: 0px;\n"
"    }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_photo = QLabel(self.centralwidget)
        self.lbl_photo.setObjectName(u"lbl_photo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_photo.sizePolicy().hasHeightForWidth())
        self.lbl_photo.setSizePolicy(sizePolicy)
        self.lbl_photo.setMinimumSize(QSize(1, 1))
        self.lbl_photo.setMaximumSize(QSize(350, 350))
        self.lbl_photo.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 10px;")
        self.lbl_photo.setPixmap(QPixmap(u":/icons/icons/album_cover_sample.png"))
        self.lbl_photo.setScaledContents(True)
        self.lbl_photo.setAlignment(Qt.AlignCenter)
        self.lbl_photo.setMargin(0)

        self.verticalLayout.addWidget(self.lbl_photo)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_time = QLabel(self.centralwidget)
        self.label_time.setObjectName(u"label_time")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_time.sizePolicy().hasHeightForWidth())
        self.label_time.setSizePolicy(sizePolicy2)
        self.label_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_time)

        self.sldr_progress = QSlider(self.centralwidget)
        self.sldr_progress.setObjectName(u"sldr_progress")
        self.sldr_progress.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.sldr_progress)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_stop = QPushButton(self.centralwidget)
        self.btn_stop.setObjectName(u"btn_stop")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/stop_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_stop.setIcon(icon1)
        self.btn_stop.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.btn_stop, 1, 2, 1, 1)

        self.btn_theme = QPushButton(self.centralwidget)
        self.btn_theme.setObjectName(u"btn_theme")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/theme.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_theme.setIcon(icon2)
        self.btn_theme.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.btn_theme, 2, 1, 1, 1)

        self.btn_randow = QPushButton(self.centralwidget)
        self.btn_randow.setObjectName(u"btn_randow")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/random_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_randow.setIcon(icon3)
        self.btn_randow.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.btn_randow, 1, 0, 1, 1)

        self.btn_loop = QPushButton(self.centralwidget)
        self.btn_loop.setObjectName(u"btn_loop")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/loop_v2_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_loop.setIcon(icon4)
        self.btn_loop.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.btn_loop, 1, 3, 1, 1)

        self.btn_pause = QPushButton(self.centralwidget)
        self.btn_pause.setObjectName(u"btn_pause")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/pause_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pause.setIcon(icon5)
        self.btn_pause.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.btn_pause, 0, 1, 1, 1)

        self.btn_next = QPushButton(self.centralwidget)
        self.btn_next.setObjectName(u"btn_next")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/next_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_next.setIcon(icon6)
        self.btn_next.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.btn_next, 0, 3, 1, 1)

        self.btn_previous = QPushButton(self.centralwidget)
        self.btn_previous.setObjectName(u"btn_previous")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/previous_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_previous.setIcon(icon7)
        self.btn_previous.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.btn_previous, 0, 0, 1, 1)

        self.btn_add_playlist = QPushButton(self.centralwidget)
        self.btn_add_playlist.setObjectName(u"btn_add_playlist")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/playlist_add_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_playlist.setIcon(icon8)
        self.btn_add_playlist.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.btn_add_playlist, 2, 3, 1, 1)

        self.btn_mute = QPushButton(self.centralwidget)
        self.btn_mute.setObjectName(u"btn_mute")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/mute.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_mute.setIcon(icon9)
        self.btn_mute.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.btn_mute, 1, 1, 1, 1)

        self.btn_play = QPushButton(self.centralwidget)
        self.btn_play.setObjectName(u"btn_play")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/play_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_play.setIcon(icon10)
        self.btn_play.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.btn_play, 0, 2, 1, 1)

        self.btn_add_playlist_from_youtube = QPushButton(self.centralwidget)
        self.btn_add_playlist_from_youtube.setObjectName(u"btn_add_playlist_from_youtube")
        self.btn_add_playlist_from_youtube.setEnabled(True)
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/playlist.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_playlist_from_youtube.setIcon(icon11)
        self.btn_add_playlist_from_youtube.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.btn_add_playlist_from_youtube, 2, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sldr_volume = QSlider(self.centralwidget)
        self.sldr_volume.setObjectName(u"sldr_volume")
        sizePolicy.setHeightForWidth(self.sldr_volume.sizePolicy().hasHeightForWidth())
        self.sldr_volume.setSizePolicy(sizePolicy)
        self.sldr_volume.setValue(80)
        self.sldr_volume.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.sldr_volume)

        self.lst_playlist = QListWidget(self.centralwidget)
        self.lst_playlist.setObjectName(u"lst_playlist")

        self.horizontalLayout.addWidget(self.lst_playlist)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_photo.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"SONG_AUTHOR - SONG_NAME", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_stop.setText("")
        self.btn_theme.setText("")
        self.btn_randow.setText("")
        self.btn_loop.setText("")
        self.btn_pause.setText("")
        self.btn_next.setText("")
        self.btn_previous.setText("")
        self.btn_add_playlist.setText("")
        self.btn_mute.setText("")
        self.btn_play.setText("")
        self.btn_add_playlist_from_youtube.setText("")
    # retranslateUi

