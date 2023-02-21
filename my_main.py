import sys
from PySide2 import QtWidgets
#import tpyside.gui
from tpyside import gui

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = gui.MainWindow2()
    window.show()
    app.exec_()