# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pyfile\lianxi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
# 这个文件是配合处理识别原始表格.py文件用的
#学习git用
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 60, 321, 121))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 3)
        self.fileButton = QtWidgets.QPushButton(self.widget)
        self.fileButton.setObjectName("fileButton")
        self.gridLayout.addWidget(self.fileButton, 1, 3, 1, 1)
        self.rpngButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.rpngButton.setFont(font)
        self.rpngButton.setObjectName("rpngButton")
        self.gridLayout.addWidget(self.rpngButton, 2, 0, 1, 2)
        self.rjpgButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.rjpgButton.setFont(font)
        self.rjpgButton.setObjectName("rjpgButton")
        self.gridLayout.addWidget(self.rjpgButton, 2, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "不理数据"))
        self.label.setText(_translate("Form", "选择文件"))
        self.fileButton.setText(_translate("Form", "选择文件"))
        self.rpngButton.setText(_translate("Form", "单张表格"))
        self.rjpgButton.setText(_translate("Form", "多张表格"))
        self.pushButton.setText(_translate("Form", "开始修理"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

