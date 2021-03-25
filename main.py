from ui.orario import OrarioWindow
from PyQt5 import QtGui, QtWidgets

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = OrarioWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
