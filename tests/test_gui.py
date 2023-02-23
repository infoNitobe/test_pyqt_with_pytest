import sys
from PySide2 import QtWidgets
from PySide2 import QtTest
from PySide2 import QtCore
from tpyside import gui

def test_button():
    app = QtWidgets.QApplication(sys.argv)
    window = gui.MainWindow2()
    window.show()

    for i in range(1, 10000):
        window.lineEdit_2.setText(str(i))
        window.radioButton_plus.toggle()

        output_before_calc = window.output_val
        QtTest.QTest.mouseClick(window.pushButton, QtCore.Qt.LeftButton)
        output_after_calc = window.output_val
        assert output_before_calc != output_after_calc
        #assert output_after_calc != 5000

    app.exec_()

#test_button()