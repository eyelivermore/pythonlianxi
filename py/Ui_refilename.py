# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pyfile\refilename.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 241, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.choiceButton = QtWidgets.QPushButton(Form)
        self.choiceButton.setGeometry(QtCore.QRect(280, 60, 75, 23))
        self.choiceButton.setObjectName("choiceButton")
        self.gogoButton = QtWidgets.QPushButton(Form)
        self.gogoButton.setGeometry(QtCore.QRect(140, 140, 75, 23))
        self.gogoButton.setObjectName("gogoButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 110, 231, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 90, 181, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.choiceButton.clicked.connect(Form.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.choiceButton.clicked.connect(self.filename)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.choiceButton.setText(_translate("Form", "选择目录"))
        self.gogoButton.setText(_translate("Form", "开始"))
        self.label.setText(_translate("Form", "输入日期或要修改的名字"))

    def filename(self):
        fname =  QtWidgets.QFileDialog.getExistingDirectory(None,'选择文件夹','D:\\桌面')
        print(fname)
        self.lineEdit.setText(fname)
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
