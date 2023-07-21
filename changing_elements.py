from PySide6.QtCore import QTime
from PySide6.QtGui import QPixmap
import random


def change_duration(self, duration):
    self.ui.sldr_progress.setValue(0)
    self.ui.sldr_progress.setRange(0, duration)


def song_progress_change(self, position):
    self.current_time = position
    self.player.setPosition(position)


def song_position_change(self, position):
    self.ui.sldr_progress.setValue(position)


def change_volume(self, position):
    self.audio_output.setVolume(position / 100.0)


def change_song(self):
    self.ui.label.setText(self.current_song)


def change_time_label(self, position):
    seconds = (position / 1000) % 60
    minutes = (position / 60000) % 60
    hours = (position / 2600000) % 24

    time_label = QTime(hours, minutes, seconds)
    self.ui.label_time.setText(time_label.toString())
    if self.ui.sldr_progress.value() == self.player.duration():
        if self.loop_flag is True:
            self.play_audio()
        else:
            if self.random_flag is True:
                self.current_song = random.choice(self.playlist)
                self.change_song()
                self.play_audio()
            else:
                self.next_song()


def change_btn_loop(self, theme_index):
    if self.ui.btn_loop.isFlat():
        if theme_index == 0:
            self.ui.btn_loop.setStyleSheet('background-color: #b3d9ff;')
        elif theme_index == 1:
            self.ui.btn_loop.setStyleSheet('background-color: rgb(203, 236, 199);')
        elif theme_index == 2:
            self.ui.btn_loop.setStyleSheet('background-color: #cccccc;')
        elif theme_index == 3:
            self.ui.btn_loop.setStyleSheet('background-color: # 70db70;')
        self.loop_flag = False
        self.ui.btn_loop.setFlat(False)
    else:
        if theme_index == 0:
            self.ui.btn_loop.setStyleSheet('background-color: #0073e6;')
        elif theme_index == 1:
            self.ui.btn_loop.setStyleSheet('background-color: rgb(232, 199, 236);')
        elif theme_index == 2:
            self.ui.btn_loop.setStyleSheet('background-color: #999999;')
        elif theme_index == 3:
            self.ui.btn_loop.setStyleSheet('background-color: #33cc33;')
        self.loop_flag = True
        self.ui.btn_loop.setFlat(True)

def random_song(self, theme_index):
    if self.ui.btn_randow.isFlat():
        if theme_index == 0:
            self.ui.btn_randow.setStyleSheet('background-color: #b3d9ff;')
        elif theme_index == 1:
            self.ui.btn_randow.setStyleSheet('background-color: rgb(203, 236, 199);')
        elif theme_index == 2:
            self.ui.btn_randow.setStyleSheet('background-color: #cccccc;')
        elif theme_index == 3:
            self.ui.btn_randow.setStyleSheet('background-color: # 70db70;')
        self.ui.btn_randow.setFlat(False)
        self.random_flag = False
    else:
        if theme_index == 0:
            self.ui.btn_randow.setStyleSheet('background-color: #0073e6;')
        elif theme_index == 1:
            self.ui.btn_randow.setStyleSheet('background-color: rgb(232, 199, 236);')
        elif theme_index == 2:
            self.ui.btn_randow.setStyleSheet('background-color: #999999;')
        elif theme_index == 3:
            self.ui.btn_randow.setStyleSheet('background-color: #33cc33;')
        self.random_flag = True
        self.ui.btn_randow.setFlat(True)
        self.ui.random_flag = True

def change_album_cover(self):
    self.img_album_cover = QPixmap('icons/album_cover_sample.png')
    self.ui.lbl_photo.setPixmap(self.img_album_cover)
