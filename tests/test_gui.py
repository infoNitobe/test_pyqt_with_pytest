import sys
import pytest
from PySide2 import QtWidgets
from PySide2 import QtTest
from PySide2 import QtCore
from tpyside import gui
class TestGui:
    @pytest.fixture(scope="class")
    def setup(self):
        TestGui.app = QtWidgets.QApplication(sys.argv)
        TestGui.window = gui.MainWindow2()
        TestGui.window.show()
        #TestGui.app.exec_()
    def test_radioButotn_plus(self, setup):
        TestGui.window.radioButton_plus.toggle()
        for i in range(-100, 101):
            for j in range(100):
                TestGui.window.lineEdit_2.setText(str(i))
                TestGui.window.spinBox.setValue(j)
                QtTest.QTest.mouseClick(TestGui.window.pushButton, QtCore.Qt.LeftButton)
                expected_result = TestGui.window.spinBox.value() + int(TestGui.window.lineEdit_2.text())
                assert int(TestGui.window.lineEdit_3.text()) == expected_result
    def test_radioButotn_minus(self, setup):
        TestGui.window.radioButton_minus.toggle()
        for i in range(-100, 101):
            for j in range(100):
                TestGui.window.lineEdit_2.setText(str(i))
                TestGui.window.spinBox.setValue(j)
                QtTest.QTest.mouseClick(TestGui.window.pushButton, QtCore.Qt.LeftButton)
                expected_result = TestGui.window.spinBox.value() - int(TestGui.window.lineEdit_2.text())
                assert int(TestGui.window.lineEdit_3.text()) == expected_result
#test_button()