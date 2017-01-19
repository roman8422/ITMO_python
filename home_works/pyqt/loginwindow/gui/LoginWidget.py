# coding: utf-8

from PyQt5.QtWidgets import QWidget
from .ui.Ui_LoginDialog import Ui_loginDialog


class LoginWidget(QWidget, Ui_loginDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.creds = {
            'user': {
                'password': '123'
            }
        }

        self.init_ui()

    def init_ui(self):
        self.setupUi(self)

    def accept(self):
        username_entered = self.loginField.text()
        if username_entered in self.creds:
            print(self.creds[username_entered])
        else:
            self.loginField.setText('')
            self.pwField.setText('')

    def reject(self):
        pass
