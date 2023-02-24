import sys
from PySide2 import QtWidgets
from tpyside import MainWindow

class MainWindow2(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, *args, obj = None, **kwargs):
        super(MainWindow2, self).__init__(*args, **kwargs)
        self.setupUi(self)
        #memo:Make it an instance variable for use from the test module
        self.output_val = 0
        self.pushButton.clicked.connect(self._process_pushed)
 
    def _process_pushed(self):
        self._calculate()
        self._output_to_dialog()
        self._update_operation_result()
    
    def _calculate(self):
        spin_box_val = self.spinBox.value()
        lineEdit_2_value = int(self.lineEdit_2.text())

        if self.radioButton_plus.isChecked():
            self.output_val = spin_box_val + lineEdit_2_value
        elif self.radioButton_minus.isChecked():
            self.output_val = spin_box_val - lineEdit_2_value
   
    def _output_to_dialog(self):
        if self.checkBox.isChecked():
            self.labelWindow = LabelWindow(self.output_val)
            self.labelWindow.show()
    
    def _update_operation_result(self):
        self.lineEdit_3.setText(str(self.output_val))

class LabelWindow(QtWidgets.QWidget):
    def __init__(self, output_val):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel(str(output_val))
        layout.addWidget(self.label)
        self.setLayout(layout)