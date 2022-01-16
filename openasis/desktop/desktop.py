from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QWidget
import openasis.core.core as core

class Window(QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.edit = QtWidgets.QLineEdit(self)
        self.edit.installEventFilter(self)
        self.text_area = QtWidgets.QTextEdit(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.text_area)

    def eventFilter(self, widget, event):
        if (event.type() == QtCore.QEvent.KeyPress and
            widget is self.edit):
            key = event.key()
            if key == QtCore.Qt.Key_Enter or key == QtCore.Qt.Key_Return:
                self.text_area.append(core.take_query(self.edit.text()))

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 300, 300, 300)
    window.show()
    sys.exit(app.exec_())