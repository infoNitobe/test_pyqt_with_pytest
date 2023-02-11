import sys
from PyQt6 import QtWidgets, uic

def create_window():
    app = QtWidgets.QApplication(sys.argv)
    windows = uic.loadUi("mainwindow.ui")
    windows.show()
    app.exec()

create_window()