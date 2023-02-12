import sys
from PySide2 import QtWidgets
from MainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj = None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate)
    
    def calculate(self):
        spin_box_val = self.spinBox.value()
        lineEdit_2_value = int(self.lineEdit_2.text())
        self.lineEdit_3.setText(str(spin_box_val + lineEdit_2_value))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()    