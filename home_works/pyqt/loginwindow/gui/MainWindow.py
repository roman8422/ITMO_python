# coding: utf-8

from PyQt5.QtWidgets import QMainWindow, QMessageBox

from .ui.Ui_MainWindow import Ui_MainWindow
from .NotesWidget import NotesWidget
from .LoginWidget import LoginWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.loggedin = False

        self.creds = {
            'user': {
                'password': '123'
            }
        }

        self.init_ui()
        self.init_signals()

    def init_ui(self):
        self.setupUi(self)

        self.notesWidget = NotesWidget(self)
        self.stackedWidget.addWidget(self.notesWidget)

        self.loginWidget = LoginWidget(self)
        self.stackedWidget.addWidget(self.loginWidget)
        self.stackedWidget.setCurrentWidget(self.loginWidget)

        if not self.loggedin:
            self.disable_controls()

    def init_signals(self):
        self.loginWidget.buttonBox.accepted.connect(self.yes)

    def yes(self):
        username_entered = self.loginWidget.loginField.text()
        password_entered = self.loginWidget.pwField.text()
        if username_entered in self.creds:
            if self.creds[username_entered]['password'] == password_entered:
                self.loggedin = True
                self.enable_controls()
                self.stackedWidget.setCurrentWidget(self.notesWidget)
            else:
                self.wrong_auth()
        else:
            self.wrong_auth()

    def disable_controls(self):
        self.toolBar.setEnabled(False)
        self.menubar.setEnabled(False)

    def enable_controls(self):
        self.toolBar.setEnabled(True)
        self.menubar.setEnabled(True)

    def wrong_auth(self):
        self.loginWidget.loginField.setText('')
        self.loginWidget.pwField.setText('')
        QMessageBox.critical(self, 'Authentication error', 'Wrong username or password\nTry again')
