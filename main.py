import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtGui import QPixmap

from design import Ui_MainWindow

import controls, playlist_controlls, work_with_file, work_with_youtube, changing_elements, themes, show_error_mess


class Audioplayer(QMainWindow):
    def __init__(self):
        super(Audioplayer, self).__init__()
        self.ui = Ui_MainWindow()  # Creating Main window
        self.ui.setupUi(self)
        self.path = ''  # Variable that save one path to playlist
        self.playlist = []  # Variable that save songs in playlist
        self.img_album_cover = QPixmap('icons/album_cover_sample.png')
        self.change_album_cover()
        self.load_playlists('playlists.txt')  # Loading latest playlist from file
        self.ui.label.setText('')
        self.ui.label_time.setText('')
        self.duration_of_song = 0
        self.loop_flag = False
        self.path_to_audio_from_youtube = 'music_from_youtube'
        self.random_flag = False
        self.theme_index = 0

        # Audio
        self.player = QMediaPlayer()  # Initializing audio source
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.current_time = 0  # Variable that save current time in song
        self.current_song = ''  # Variable that save name of song that playing now
        self.audio_output.setVolume(self.ui.sldr_volume.value())

        # Events
        self.ui.btn_add_playlist.clicked.connect(self.create_playlist)
        self.ui.btn_add_playlist_from_youtube.clicked.connect(self.create_playist_from_youtube)
        self.ui.btn_play.clicked.connect(self.play_audio)
        self.ui.btn_stop.clicked.connect(self.stop_audio)
        self.ui.btn_pause.clicked.connect(self.pause_audio)
        self.ui.lst_playlist.itemDoubleClicked.connect(self.play_audio_from_playlist)
        self.ui.sldr_progress.sliderMoved.connect(self.song_progress_change)
        self.ui.sldr_progress.valueChanged.connect(self.change_time_label)
        self.ui.sldr_volume.sliderMoved.connect(self.change_volume)
        self.ui.btn_next.clicked.connect(self.next_song)
        self.ui.btn_previous.clicked.connect(self.previous_song)
        self.ui.btn_loop.clicked.connect(self.change_btn_loop)
        self.ui.btn_mute.clicked.connect(self.mute)
        self.ui.btn_randow.clicked.connect(self.random)
        self.ui.btn_theme.clicked.connect(self.change_theme)


        # Events for audio source
        self.player.durationChanged.connect(self.change_duration)
        self.player.positionChanged.connect(self.song_position_change)

    def play_audio(self):
        controls.play_audio(self)

    def play_audio_from_playlist(self):
        playlist_controlls.play_audio_from_playlist(self)

    def get_current_item_in_playlist(self):
        return self.ui.lst_playlist.currentItem().text()

    def stop_audio(self):
        controls.stop_audio(self)

    def mute(self):
        controls.mute(self, self.theme_index)

    def pause_audio(self):
        controls.pause_audio(self)

    def next_song(self):
        controls.next_song(self)

    def previous_song(self):
        controls.previous_song(self)

    def create_playlist(self):
        playlist_controlls.create_playlist(self)

    def check_playlist_when_add(self, input_path, checked_path):
        if input_path == checked_path + '\n':
            return True
        else:
            return False

    def save_playlists(self, path_dir):
        work_with_file.save_playlists(self, self.path)

    def load_playlists(self, path):
        work_with_file.load_playlists(self, path)

    def create_playist_from_youtube(self):
        work_with_youtube.create_playlist_from_youtube(self)

    def download_from_youtube(self):
        work_with_youtube.download_from_youtube(self)

    def change_duration(self, duration):
        changing_elements.change_duration(self, duration)

    def song_progress_change(self, position):
        changing_elements.song_progress_change(self, position)

    def song_position_change(self, position):
        changing_elements.song_position_change(self, position)

    def change_volume(self, position):
        changing_elements.change_volume(self, position)

    def change_song(self):
        changing_elements.change_song(self)

    def change_time_label(self, position):
        changing_elements.change_time_label(self, position)

    def change_btn_loop(self):
        changing_elements.change_btn_loop(self, self.theme_index)

    def change_album_cover(self):
        changing_elements.change_album_cover(self)

    def random(self):
        changing_elements.random_song(self, self.theme_index)

    def change_path_for_youtube_music(self):
        work_with_youtube.change_path_for_youtube_music(self)

    def change_theme(self):
        if self.theme_index + 1 > 3:
            self.theme_index = 0
        else:
            self.theme_index += 1
        themes.change_theme(self, self.theme_index)

    def show_error_message(self, message):
        """Shows error messages"""
        show_error_mess.show_error_message(self, message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Audioplayer()
    window.show()

    sys.exit(app.exec())
