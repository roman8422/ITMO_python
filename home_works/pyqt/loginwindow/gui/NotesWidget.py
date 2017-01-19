# coding: utf-8

from PyQt5.QtWidgets import QWidget
# from PyQt5.uic import loadUi
from .ui.Ui_NotesWidget import Ui_Form


class NotesWidget(QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        # loadUi('gui/ui/notes_widget.ui', self)
        self.setupUi(self)
