import sys
from PySide2 import QtWidgets
#import tpyside.MainWindow
from tpyside import MainWindow

class MainWindow2(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, *args, obj = None, **kwargs):
        super(MainWindow2, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate)
    
    def calculate(self):
        spin_box_val = self.spinBox.value()
        lineEdit_2_value = int(self.lineEdit_2.text())

        if self.radioButton_plus.isChecked():
            output_val = spin_box_val + lineEdit_2_value
        if self.radioButton_minus.isChecked():
            output_val = spin_box_val - lineEdit_2_value
        if self.checkBox.isChecked():
            self.labelWindow = LabelWindow(output_val)
            self.labelWindow.show()

        self.lineEdit_3.setText(str(output_val))

class LabelWindow(QtWidgets.QWidget):
    def __init__(self, output_val):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel(str(output_val))
        layout.addWidget(self.label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow2()
    window.show()
    app.exec_()    