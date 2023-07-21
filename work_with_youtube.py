from PySide6.QtWidgets import QDialog, QFileDialog

from des_sub import Ui_Dialog

import asyncio
import async_for_youtube as async_m


def create_playlist_from_youtube(self):
    self.new_window = QDialog()
    self.ui_window = Ui_Dialog()
    self.ui_window.setupUi(self.new_window)
    self.ui_window.pushButton.clicked.connect(self.change_path_for_youtube_music)
    self.ui_window.btn_enter.clicked.connect(self.download_from_youtube)
    self.new_window.show()


def change_path_for_youtube_music(self):
    path_to_audio_from_youtube = QFileDialog.getExistingDirectory(self.new_window, 'Select Directory')
    if path_to_audio_from_youtube:
        self.path_to_audio_from_youtube = path_to_audio_from_youtube
        self.ui_window.label_2.setText(f'Save to: {self.path_to_audio_from_youtube}')


def download_from_youtube(self):
    url = self.ui_window.ln_url.text()
    if url:
        mode = self.ui_window.comboBox.currentText()
        asyncio.run(async_m.start_process(url, mode, self.path_to_audio_from_youtube))
        self.ui_window.label.setText('Completed!')
