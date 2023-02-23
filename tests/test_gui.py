import sys
import pytest
from PySide2 import QtWidgets
from PySide2 import QtTest
from PySide2 import QtCore
from tpyside import gui

class TestGui:
    @pytest.fixture(scope="class")
    def setup(self):
        self.__class__.app = QtWidgets.QApplication(sys.argv)
        self.__class__.window = gui.MainWindow2()
        self.window.show()

    def test_radioButotn_plus(self, setup):
        self.window.radioButton_plus.toggle()

        for i in range(-100, 101):
            for j in range(100):
                self.window.lineEdit_2.setText(str(i))
                self.window.spinBox.setValue(j)
                QtTest.QTest.mouseClick(self.window.pushButton, QtCore.Qt.LeftButton)

                expected_result = self.window.spinBox.value() + int(self.window.lineEdit_2.text())

                assert int(self.window.lineEdit_3.text()) == expected_result

    def test_radioButotn_minus(self, setup):
        self.window.radioButton_minus.toggle()

        for i in range(-100, 101):
            for j in range(100):
                self.window.lineEdit_2.setText(str(i))
                self.window.spinBox.setValue(j)
                QtTest.QTest.mouseClick(self.window.pushButton, QtCore.Qt.LeftButton)

                expected_result = self.window.spinBox.value() - int(self.window.lineEdit_2.text())

                assert int(self.window.lineEdit_3.text()) == expected_result

#test_button()