# coding: utf-8

from PyQt5.QtWidgets import QWidget
from .ui.Ui_LoginDialog import Ui_loginDialog


class LoginWidget(QWidget, Ui_loginDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setupUi(self)

    def accept(self):
        pass

    def reject(self):
        pass
