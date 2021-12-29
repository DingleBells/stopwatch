from PyQt5 import QtGui
from simpleAddition_UI import calculatorUI

class Calculator(calculatorUI):
    def __init__(self):
        calculatorUI.__init__(self)
        self.calculate.clicked.connect(self.handleCalculate)

    def handleCalculate(self):
        x = int(self.in_1.text())
        y = int(self.in_2.text())
        self.output.setText(str(x+y))

if __name__ == "__main__":
    import sys
    app = QtGui.QGuiApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())