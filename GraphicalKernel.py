from PyQt5 import QtCore, QtGui, QtWidgets
import json
import os
import random
import sys
import time
from output import OutPut
from serialized_savor import Save

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1060, 700)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1060, 700))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(36, 203, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 40, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 203, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 40, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 203, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        MainWindow.setPalette(palette)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setWindowTitle("HI6Cypher")
        icon = QtGui.QIcon()
        path = f"{os.getcwd()}/icons/main.png" #path of main.png icon
        icon.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setAnimated(False)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_main = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_main.setGeometry(QtCore.QRect(160, 10, 891, 621))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 28, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 28, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.textBrowser_main.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Consolas") # Consolas, best font around the world
        font.setPointSize(10)
        self.textBrowser_main.setFont(font)
        self.textBrowser_main.setToolTip("")
        self.textBrowser_main.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_main.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser_main.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser_main.setObjectName("textBrowser_main")
        self.lineEdit_write = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_write.setEnabled(True)
        self.lineEdit_write.setGeometry(QtCore.QRect(160, 640, 841, 40))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_write.setFont(font)
        self.lineEdit_write.setTabletTracking(True)
        self.lineEdit_write.setToolTip("")
        self.lineEdit_write.setAutoFillBackground(False)
        self.lineEdit_write.setStyleSheet("")
        self.lineEdit_write.setInputMask("")
        self.lineEdit_write.setText("")
        self.lineEdit_write.setFrame(True)
        self.lineEdit_write.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_write.setCursorPosition(0)
        self.lineEdit_write.setObjectName("lineEdit_write")
        self.pushButton_snap = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_snap.setGeometry(QtCore.QRect(1010, 640, 40, 40))
        self.pushButton_snap.setToolTip("")
        self.pushButton_snap.setToolTipDuration(-1)
        self.pushButton_snap.setAutoFillBackground(False)
        self.pushButton_snap.setText("")
        icon1 = QtGui.QIcon()
        path = f"{os.getcwd()}/icons/snap.png" # path of snap.png icon
        icon1.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_snap.setIcon(icon1)
        self.pushButton_snap.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_snap.setAutoDefault(True)
        self.pushButton_snap.setDefault(True)
        self.pushButton_snap.setFlat(False)
        self.pushButton_snap.setObjectName("pushButton_snap")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 40, 141, 641))
        self.textBrowser.setObjectName("textBrowser")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 12.5, 55, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(110, 11, 40, 23))
        self.pushButton_save.setToolTip("Save history")
        self.pushButton_save.setToolTipDuration(-1)
        self.pushButton_save.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_del.setGeometry(QtCore.QRect(68, 11, 40, 23))
        self.pushButton_del.setToolTip("Delete history")
        self.pushButton_del.setToolTipDuration(-1)
        self.pushButton_del.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_del.setObjectName("pushButton_save")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.pushButton_snap.clicked.connect(self.Main) # to run Main function
        self.pushButton_save.clicked.connect(self.Save) # to run Save function
        self.pushButton_del.clicked.connect(self.Delete) # to run Delete function
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.lineEdit_write.returnPressed.connect(self.pushButton_snap.click) # to click snap Button when user press Enter

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.textBrowser_main.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_snap.setAccessibleName(_translate("MainWindow", "Snap!"))
        self.pushButton_snap.setAccessibleDescription(_translate("MainWindow", "Snap!"))
        self.comboBox.setItemText(0, _translate("MainWindow", "About"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Capabilities"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Orders"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Other"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_del.setText(_translate("MainWindow", "Delete"))
        self.sethtml()
        self.comboBox.currentIndexChanged.connect(self.IndexDecision)
        path = f"{os.getcwd()}/doc/saves.p" # path of saves.p file to restoring history
        self.textBrowser_main.append(Save.deserialization(path))
        app.processEvents()
        if self.textBrowser_main.toPlainText() == "" :
            with open("doc/greeting_keywords.json", "r") as file : # to show hi greeting while starting program
                message = json.load(file)
            ran = random.randint(0, len(message["hi"]) - 1)
            greet = "$ HI6Cypher ->\n\n%s" % (message["hi"][ran])
            self.textBrowser_main.append(greet)

    def sethtml(self) :
        _translate = QtCore.QCoreApplication.translate
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#1976c7;\">HI6Cypher</span><span style=\" font-size:8pt;\"> is an intelligent virtual assistant designed to provide you with interactivel experiences. this chatbot has written in Python, and it\'s so fast to in response your requests.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Key Features:</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fast: <span style=\" color:#1976c7;\">HI6Cypher</span>, is Pythonic and optimized to work fast.</li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Easy : <span style=\" color:#1976c7;\">HI6Cypher </span><span style=\" color:#000000;\">isn\'t like bash, command line or this stuff and it programmed word all type of users.</span></li>\n"
"<li style=\" font-size:8pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Open-source: source code of <span style=\" color:#1976c7;\">HI6Cypher </span>is open on GitHub and human readable.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Why Choose </span><span style=\" font-size:8pt; color:#1976c7;\">HI6Cypher</span><span style=\" font-size:8pt;\">?</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Instant Assistance: <span style=\" color:#1976c7;\">HI6Cypher</span> is available 24/7 to answer your questions and provide real-time support, saving you time and effort.</li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Useful: <span style=\" color:#1976c7;\">HI6Cypher</span> uses useful APIs(check source code) to fulfill your wishes.</li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Updating: <span style=\" color:#1976c7;\">HI6Cypher</span> will be updated alternately.</li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Email:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">huaweisclu31@hotmail.com</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GitHub:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">https://github.com/HI6Cypher/HI6Cypher</span></p></body></html>"))

    def Main(self) : # to call Output function to connect DataProcessing Kernel
        request_text = self.lineEdit_write.text()
        thinking_text = "\nThinking..."
        HI6Cypher_res = "\n$ HI6Cypher ->\n\n"
        user_req = "User:\n"
        request = f"{user_req}{self.lineEdit_write.text()}"
        if self.lineEdit_write.text() :
            self.lineEdit_write.clear()
            app.processEvents()
            self.textBrowser_main.append(request)
            self.lineEdit_write.setText(thinking_text)
            app.processEvents()
            time.sleep(0.5) # to sleep 0.5 second
            response = f"{HI6Cypher_res}{OutPut(request_text)}"
            self.lineEdit_write.clear()
            app.processEvents()
            self.textBrowser_main.append(response)
        else :
            pass

    def IndexDecision(self) : # to show indexes in comboBox
        path = f"{os.getcwd()}/doc/help(unreadble).json"
        with open(path, "r") as file :
            data = json.load(file)
        if self.comboBox.currentText() == "About" :
            self.sethtml()
        elif self.comboBox.currentText() == "Capabilities" :
            self.textBrowser.clear()
            self.textBrowser.append(data["Capabilities"])
        elif self.comboBox.currentText() == "Orders" :
            self.textBrowser.clear()
            self.textBrowser.append(data["Orders"])
        elif self.comboBox.currentText() == "Other" :
            self.textBrowser.clear()
            self.textBrowser.append(data["Other"])

    def Save(self) : # to save history
        path = f"{os.getcwd()}/doc/saves.p" # path of saves.p file
        try :
            Save.serialization(path, self.textBrowser_main.toPlainText())
        except :
            pass

    def Delete(self) : # to delete history
        path = f"{os.getcwd()}/doc/saves.p" # path of saves.p file
        self.textBrowser_main.clear()
        try :
            os.remove(path)
        except :
            pass

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())