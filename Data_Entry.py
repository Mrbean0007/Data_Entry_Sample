# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Data_Entry.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#p
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
import os


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(479, 253)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(9, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 1)

        self.lineEdit.textChanged.connect(self.texting)
        self.lineEdit_2.textChanged.connect(self.texting)
        self.lineEdit_3.textChanged.connect(self.texting)
        self.pushButton.clicked.connect(self.Createfile)
        self.pushButton_2.clicked.connect(lambda:Dialog.close())

        self.int=QIntValidator()
        self.lineEdit_3.setValidator(self.int)

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Submit"))
        self.pushButton_2.setText(_translate("Dialog", "Quit"))
        self.label.setText(_translate("Dialog", "Name:-"))
        self.label_2.setText(_translate("Dialog", "Email:-"))
        self.label_3.setText(_translate("Dialog", "Phone No:-"))
    def texting(self):
        self.name=self.lineEdit.text()
        self.email=self.lineEdit_2.text()
        self.phone=self.lineEdit_3.text()

    def Createfile(self):
        Entry=["Name","Email ID","Phone No"]
        data=[self.name,self.email,self.phone]

        df =pd.DataFrame([data],columns=Entry)
        #print(df.columns)
        if "@" and ".com" or ".in" in self.email:
            if os.path.isfile("Data_Entry_V1.csv"):
                df1=pd.read_csv("Data_Entry_V1.csv")
                print(df1,"read")
                #print(df1.columns)
                print(self.email.find("@"))

                f= pd.concat((df1,df))
               # print("f:",f0)
               # concat=df1.append(df)
                f.to_csv("Data_Entry_V1.csv",columns=Entry,index=False)


            else:
                df.to_csv("Data_Entry_V1.csv")
        else:
            print("No @")
            self.buttonReply=QMessageBox()
            self.buttonReply.setIcon(QMessageBox.Information)
            self.buttonReply.setText(f'Enter Email ID {self.email} is Invalid')
            self.buttonReply.setStandardButtons(QMessageBox.Ok)
            self.buttonReply.exec_()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
