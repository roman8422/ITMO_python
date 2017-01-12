import sys
from PyQt5.QtCore import QObject, Qt

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QPushButton, QDoubleSpinBox,
    QVBoxLayout
)


class Course(QObject):
    def get(self):
        return 59.50


class CurrencyConverter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.initLayouts()
        self.initSignals()
        self.RUR_to_USD = True

    def initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.resultLabel = QLabel('Сумма в долларах', self)

        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999)
        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)

        self.convertBtn = QPushButton('Перевести', self)
        self.cleanBtn = QPushButton('Сбросить', self)

    def initSignals(self):
        self.convertBtn.clicked.connect(self.onClickConvertBtn)
        self.cleanBtn.clicked.connect(self.onClickCleanBtn)
        self.convertBtn.setDisabled(True)

        self.srcAmount.valueChanged.connect(self.ValChanged)
        self.resultAmount.valueChanged.connect(self.ValChanged)

    def keyPressEvent(self, e):
        if e.key() in [Qt.Key_Return, Qt.Key_Enter]:
            if self.convertBtn.isEnabled():
                self.convertBtn.click()

        if e.key() in [Qt.Key_Escape]:
            self.cleanBtn.click()

    def initLayouts(self):
        self.w = QWidget()

        self.mainLayout = QVBoxLayout(self.w)
        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn)
        self.mainLayout.addWidget(self.cleanBtn)

        self.setCentralWidget(self.w)

    def onClickConvertBtn(self):
        if self.RUR_to_USD:
            value = self.srcAmount.value()
            self.resultAmount.setValue(value / Course().get())
        else:
            value = self.resultAmount.value()
            self.srcAmount.setValue(value * Course().get())

    def onClickCleanBtn(self):
        self.srcAmount.setValue(0)
        self.resultAmount.setValue(0)

    def ValChanged(self):
        if self.srcAmount.value() != 0 and self.resultAmount.value() == 0:
            self.convertBtn.setEnabled(True)
            self.RUR_to_USD = True
        elif self.srcAmount.value() == 0 and self.resultAmount.value() != 0:
            self.convertBtn.setEnabled(True)
            self.RUR_to_USD = False
        else:
            self.convertBtn.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    converter = CurrencyConverter()
    converter.show()

    sys.exit(app.exec_())


# ДЗ:
# - добавить кнопку "Очистить"
# - блокировать кнопку "Перевести" при непонятном состоянии конвертера (например, когда в поле ввода 0)
# - сделать обратную конвертацию
