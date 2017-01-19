# coding: utf-8

from PyQt5.QtWidgets import QMainWindow

from .ui.Ui_MainWindow import Ui_MainWindow
from .NotesWidget import NotesWidget
from .LoginWidget import LoginWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.loggedin = False

        self.init_ui()
        self.init_signals()


    def init_ui(self):
        self.setupUi(self)

        self.notesWidget = NotesWidget(self)
        self.stackedWidget.addWidget(self.notesWidget)

        if not self.loggedin:
            self.disable_controls()
        else:
            self.enable_controls()

        self.loginWidget = LoginWidget(self)
        self.stackedWidget.addWidget(self.loginWidget)
        self.stackedWidget.setCurrentWidget(self.loginWidget)

    def init_signals(self):
        pass

    def disable_controls(self):
        self.toolBar.setEnabled(False)
        self.menubar.setEnabled(False)

    def enable_controls(self):
        self.toolBar.setEnabled(True)
        self.menubar.setEnabled(True)
