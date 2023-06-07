
from PySide2.QtWidgets import *
from PySide2 import QtGui, QtCore


import sys
app = QApplication()

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.resize(300, 100)
        self.setLayout(QVBoxLayout())

        button = QPushButton('Submit')
        button.clicked.connect(self.onclick)
        self.layout().addWidget(button)

    def onclick(self):
        self.close()
        message = "<font size = 5 color = gray > Rich Html Title </font> <br/><br/>The clickable link <a href='http://www.google.com'>Google.</a> The lower and upper case text."
        messagebox = QMessageBox(QMessageBox.Warning, "Successful", message, parent=self)
        messagebox.addButton("ResetRole Left Most", QMessageBox.ResetRole)
        messagebox.addButton("ApplyRole Left", QMessageBox.ApplyRole)
        messagebox.addButton("RejectRole Right", QMessageBox.RejectRole)
        messagebox.exec_()
        # print('exe: %s  clickedButton: %s'%(exe, messagebox.clickedButton())

        # message = "<font size = 5 > Complete </font>"
        # messagebox = QMessageBox(QMessageBox.Information, "Successful", message, parent=self)
        # messagebox.addButton("folder open", QMessageBox.ResetRole)
        # messagebox.addButton("ok", QMessageBox.ApplyRole)
        # messagebox.exec_()



dialog = Dialog()
dialog.show()
app.exec_()