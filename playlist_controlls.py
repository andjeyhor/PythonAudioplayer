import os

from PySide6.QtWidgets import QFileDialog

from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtCore import QUrl
from PySide6.QtGui import QPixmap

import show_error_mess


def play_audio_from_playlist(self):
    """Start playing audio from playlist after double click"""
    if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
        self.player.stop()
    self.current_song = self.get_current_item_in_playlist()
    audio_path = self.path + '/' + self.current_song
    self.player.setSource(QUrl.fromLocalFile(audio_path))
    self.change_song()
    self.duration_of_song = self.player.duration()
    self.player.play()


def get_current_item_in_playlist(self):
    """Return current item in List View"""
    return self.ui.lst_playlist.currentItem().text()


def create_playlist(self):
    """Creating playlist and adding it to ListView"""
    self.path = QFileDialog.getExistingDirectory(self, 'Select Directory')
    temp_playlist = []
    if self.path:
        temp_playlist = os.listdir(self.path)

    if temp_playlist:
        self.playlist.clear()
        for song in temp_playlist:
            if '.mp3' in song or '.wav' in song or '.ogg' in song:
                self.playlist.append(song)

        if len(self.playlist) > 0:
            self.current_song = self.playlist[0]
            self.ui.lst_playlist.clear()
            self.ui.lst_playlist.addItems(self.playlist)
            self.save_playlists(self.path)
        else:
            self.show_error_message('This directory does\'nt have a audio files')

        for file in temp_playlist:
            if '.jpg' in file or '.png' in file:
                self.img_album_cover = QPixmap(self.path + '\\' + file)
                self.ui.lbl_photo.setPixmap(self.img_album_cover)
                break
            else:
                self.change_album_cover()

    else:
        self.show_error_message('This directory does\'nt have a audio files')




def show_error_message(self, message):
    """Shows error messages"""
    show_error_mess.show_error_message(self, message)
