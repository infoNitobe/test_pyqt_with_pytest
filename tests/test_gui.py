import sys
from PySide2 import QtWidgets
#from tpyside import MainWindow2
import tpyside

def test_button():
    app = QtWidgets.QApplication(sys.argv)
    window = tpyside.Mainwindow2()
    window.show()
    app.exec_()    

test_button()
