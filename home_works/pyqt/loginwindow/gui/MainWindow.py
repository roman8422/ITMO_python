# coding: utf-8

from PyQt5.QtWidgets import QMainWindow

from .ui.Ui_MainWindow import Ui_MainWindow
from .NotesWidget import NotesWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.init_ui()
        self.init_signals()

    def init_ui(self):
        self.setupUi(self)

        self.notesWidget = NotesWidget(self)
        self.stackedWidget.addWidget(self.notesWidget)
        self.stackedWidget.setCurrentWidget(self.notesWidget)

    def init_signals(self):
        pass
