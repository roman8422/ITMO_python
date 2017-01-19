# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_widget.ui'
#
# Created: Thu Jan 19 21:52:17 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        loginDialog.setObjectName("loginDialog")
        loginDialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(loginDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(loginDialog)
        self.widget.setGeometry(QtCore.QRect(100, 90, 197, 62))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.loginField = QtWidgets.QLineEdit(self.widget)
        self.loginField.setObjectName("loginField")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.loginField)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.pwField = QtWidgets.QLineEdit(self.widget)
        self.pwField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwField.setObjectName("pwField")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pwField)

        self.retranslateUi(loginDialog)
        self.buttonBox.accepted.connect(loginDialog.accept)
        self.buttonBox.rejected.connect(loginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(loginDialog)

    def retranslateUi(self, loginDialog):
        _translate = QtCore.QCoreApplication.translate
        loginDialog.setWindowTitle(_translate("loginDialog", "Login Windows"))
        self.label.setText(_translate("loginDialog", "Login:"))
        self.label_2.setText(_translate("loginDialog", "Password:"))

