# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'English.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets,QtCore
from GetDulieu import dictionary,list3
from RandomCH import taonganhang
import time
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(538, 353)
        self.key1 = QtWidgets.QPushButton(Form)
        self.key1.setGeometry(QtCore.QRect(40, 110, 221, 91))
        self.key1.setObjectName("key1")
        self.key2 = QtWidgets.QPushButton(Form)
        self.key2.setGeometry(QtCore.QRect(280, 110, 221, 91))
        self.key2.setObjectName("key2")
        self.key3 = QtWidgets.QPushButton(Form)
        self.key3.setGeometry(QtCore.QRect(40, 220, 221, 91))
        self.key3.setObjectName("key3")
        self.key4 = QtWidgets.QPushButton(Form)
        self.key4.setGeometry(QtCore.QRect(280, 220, 221, 91))
        self.key4.setObjectName("key4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 461, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def clicked_0(self):
        if (self.dapan[0]==self.dapandung):
            self.key1.setStyleSheet("background-color: green")
            self.s=QtCore.QTimer()
            self.s.timeout.connect(self.dowork)
            self.s.start(750)
        else :
            self.key1.setStyleSheet("background-color: red")
            self.find()
            self.s=QtCore.QTimer()
            self.s.timeout.connect(self.dowork)
            self.s.start(750)
    def clicked_1(self):
        if (self.dapan[1]==self.dapandung):
            self.key2.setStyleSheet("background-color: green")
            self.s=QtCore.QTimer()
            self.s.timeout.connect(self.dowork)
            self.s.start(750)        
        else :
            self.key2.setStyleSheet("background-color: red")
            self.find()
            self.s=QtCore.QTimer()
            self.s.timeout.connect(self.dowork)
            self.s.start(750) 
    def clicked_2(self):
        if (self.dapan[2]==self.dapandung):
            self.key3.setStyleSheet("background-color: green")
            self.s=QtCore.QTimer()
            self.s.timeout.connect(self.dowork)
            self.s.start(750)        
        else :
            self.key3.setStyleSheet("background-color: red")
            self.find()
            self.s=QtCore.QTimer()
            self.s.timeout.connect(self.dowork)
            self.s.start(750) 
    def clicked_3(self):
        if (self.dapan[3]==self.dapandung):
            self.key4.setStyleSheet("background-color: green")
            self.s=QtCore.QTimer()
            self.s.timeout.connect(self.dowork)
            self.s.start(750)      
        else :
            self.key4.setStyleSheet("background-color: red")
            self.find()
            self.s=QtCore.QTimer()
            self.s.timeout.connect(self.dowork)
            self.s.start(750)  
    def thamso(self):
        self.cauhoi=readfile.readline()
        self.dapandung=readfile.readline()
        self.dapan=[0,0,0,0]
        self.dapan[0]=readfile.readline()
        self.dapan[1]=readfile.readline()
        self.dapan[2]=readfile.readline()
        self.dapan[3]=readfile.readline()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.thamso()
        self.key1.setText(_translate("Form", self.dapan[0]))
        self.key2.setText(_translate("Form", self.dapan[1]))
        self.key3.setText(_translate("Form", self.dapan[2]))
        self.key4.setText(_translate("Form", self.dapan[3]))
        self.label.setText(_translate("Form", self.cauhoi))
        self.key1.clicked.connect(self.clicked_0)
        self.key2.clicked.connect(self.clicked_1)
        self.key3.clicked.connect(self.clicked_2)
        self.key4.clicked.connect(self.clicked_3)
    def dowork(self):
        self.key1.setStyleSheet("background-color: white")
        self.key2.setStyleSheet("background-color: white")
        self.key3.setStyleSheet("background-color: white")
        self.key4.setStyleSheet("background-color: white")
        self.s.start()
        self.s.stop()
        self.retranslateUi(Form)
    def find(self):
        if (self.dapan[0]==self.dapandung):
            self.key1.setStyleSheet("background-color: green")
        elif (self.dapan[1]==self.dapandung):
            self.key2.setStyleSheet("background-color: green")
        elif (self.dapan[2]==self.dapandung):
            self.key3.setStyleSheet("background-color: green")
        else :
            self.key4.setStyleSheet("background-color: green")
if __name__ == "__main__":
    import sys
    taonganhang()
    readfile=open('BankAnswer.txt','r')
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    readfile.close()
 