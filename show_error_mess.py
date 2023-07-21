from PySide6.QtWidgets import QMessageBox


def show_error_message(self, message):
    """Shows error messages"""
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setText(message)
    msg_box.setWindowTitle('Error!')
    msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg_box.exec()
