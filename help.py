"""This module assocated to Graphical_Kernel module
and it can't run independently"""
import os
import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(412, 300)
        Form.setMaximumSize(QtCore.QSize(412, 300))
        Form.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        icon = QtGui.QIcon()
        path = f"{os.getcwd()}/icons/helpform.png"
        icon.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(16, 11, 80, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textBrowser_help = QtWidgets.QTextBrowser(Form)
        self.textBrowser_help.setGeometry(QtCore.QRect(16, 37, 381, 251))
        self.textBrowser_help.setObjectName("textBrowser_help")

        self.retranslateUi(Form)
        with open("doc/help(unreadble).json", "r") as file :
                    data = json.load(file)
        self.textBrowser_help.append(data["Capabilities"])
        self.comboBox.currentIndexChanged['int'].connect(self.Index)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Help"))
        self.comboBox.setItemText(0, _translate("Form", "Capabilities"))
        self.comboBox.setItemText(1, _translate("Form", "Orders"))
        self.comboBox.setItemText(2, _translate("Form", "Other"))

    def Index(self) :
        try :
            if self.comboBox.currentText() == "Capabilities" :
                with open("doc/help(unreadble).json", "r") as file :
                    data = json.load(file)
                self.textBrowser_help.clear()
                self.textBrowser_help.append(data["Capabilities"])
                app.processEvents()
            elif self.comboBox.currentText() == "Orders" :
                app.processEvents()
                with open("doc/help(unreadble).json", "r") as file :
                    data = json.load(file)
                self.textBrowser_help.clear()
                self.textBrowser_help.append(data["Orders"])
                app.processEvents()
            elif self.comboBox.currentText() == "Other" :
                with open("doc/help(unreadble).json", "r") as file :
                    data = json.load(file)
                self.textBrowser_help.clear()
                self.textBrowser_help.append(data["Other"])
            else :
                pass
        except :
            self.textBrowser_help.append("help file not found!")
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()