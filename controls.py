import random


from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtCore import QUrl

import show_error_mess


def play_audio(self):
    """Start playing audio when button was pushed"""
    if self.player.playbackState() == QMediaPlayer.PlaybackState.PausedState:
        self.player.setPosition(self.current_time)
        self.player.play()
    else:
        audio_path = self.path + '/' + self.current_song
        self.player.stop()
        self.player.setSource(QUrl.fromLocalFile(audio_path))
        self.player.setPosition(0)
        self.player.play()


def stop_audio(self):
    self.player.stop()


def mute(self, theme_index):
    """Muting song"""
    if self.ui.btn_mute.isFlat():
        if theme_index == 0:
            self.ui.btn_mute.setStyleSheet('background-color: #b3d9ff;')
        elif theme_index == 1:
            self.ui.btn_mute.setStyleSheet('background-color: rgb(203, 236, 199);')
        elif theme_index == 2:
            self.ui.btn_mute.setStyleSheet('background-color: #cccccc;')
        elif theme_index == 3:
            self.ui.btn_mute.setStyleSheet('background-color: # 70db70;')
        self.audio_output.setMuted(False)
        self.ui.btn_mute.setFlat(False)
    else:
        if theme_index == 0:
            self.ui.btn_mute.setStyleSheet('background-color: #0073e6;')
        elif theme_index == 1:
            self.ui.btn_mute.setStyleSheet('background-color: rgb(232, 199, 236);')
        elif theme_index == 2:
            self.ui.btn_mute.setStyleSheet('background-color: #999999;')
        elif theme_index == 3:
            self.ui.btn_mute.setStyleSheet('background-color: #33cc33;')
        self.audio_output.setMuted(True)
        self.ui.btn_mute.setFlat(True)


def pause_audio(self):
    """Pause"""
    self.current_time = self.player.position()
    self.player.pause()


def next_song(self):
    """Switches the song further"""
    if self.player.playbackState() == QMediaPlayer.PlaybackState.PausedState:
        pass
    elif self.random_flag:
        self.current_song = random.choice(self.playlist)
        self.change_song()
        self.play_audio()
    else:
        if self.current_song:
            current_index = self.playlist.index(self.current_song)
            current_index += 1
            if current_index >= len(self.playlist):
                pass
            else:
                self.current_song = self.playlist[current_index]
                self.change_song()
                self.duration_of_song = self.player.duration()
                self.play_audio()


def previous_song(self):
    """Switches the song back"""
    if self.player.playbackState() == QMediaPlayer.PlaybackState.PausedState:
        pass
    else:
        if self.current_song:
            current_index = self.playlist.index(self.current_song)
            current_index -= 1
            if current_index < 0:
                pass
            else:
                self.current_song = self.playlist[current_index]
                self.change_song()
                self.duration_of_song = self.player.duration()
                self.play_audio()

