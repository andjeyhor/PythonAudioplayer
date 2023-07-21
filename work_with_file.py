import os

from PySide6.QtGui import QPixmap


def save_playlists(self, path_dir):
    """Saving all existing playlists"""
    if os.path.exists('playlists.txt'):
        with open('playlists.txt', 'r') as file:
            paths = file.readlines()
            if len(paths) > 0:
                indicator = False
                for existing_path in paths:
                    if self.check_playlist_when_add(existing_path, path_dir):
                        indicator = True
                        break
                if indicator is not True:
                    with open('playlists.txt', 'a') as file_for_add:
                        file_for_add.write(path_dir + '\n')
            else:
                with open('playlists.txt', 'a') as file_for_add:  # Add first row of playlist
                    file_for_add.write(path_dir + '\n')
    else:
        with open('playlists.txt', 'w') as file:  # Create file and add playlist
            file.write(path_dir + '\n')


def load_playlists(self, path):
    """Loading last saving playlist"""
    if os.path.exists('playlists.txt'):
        with open('playlists.txt', 'r') as file:
            playlist_names = file.readlines()
            if playlist_names:
                last_playlist = playlist_names[-1]
                songs = os.listdir(last_playlist[:-1])
                self.path = last_playlist[:-1]
                if songs:
                    for song in songs:
                        if '.mp3' in song or '.wav' in song or '.ogg' in song:
                            self.playlist.append(song)
                        elif '.jpg' in song or '.png' in song:
                            self.img_album_cover = QPixmap(self.path + '\\' + song)
                            self.ui.lbl_photo.setPixmap(self.img_album_cover)
                        else:
                            self.change_album_cover()

        self.ui.lst_playlist.clear()
        self.ui.lst_playlist.addItems(self.playlist)

