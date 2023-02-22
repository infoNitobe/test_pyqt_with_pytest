import sys
from PySide2 import QtWidgets
from tpyside import gui

def test_button():
    app = QtWidgets.QApplication(sys.argv)
    window = gui.MainWindow2()
    window.show()
    app.exec_()

test_button()
