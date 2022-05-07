# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pythonlianxi\pyqt\dialogui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 221, 261))
        self.textEdit.setObjectName("textEdit")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 10, 81, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.b1 = QtWidgets.QPushButton(self.layoutWidget)
        self.b1.setObjectName("b1")
        self.verticalLayout.addWidget(self.b1)
        self.b2 = QtWidgets.QPushButton(self.layoutWidget)
        self.b2.setObjectName("b2")
        self.verticalLayout.addWidget(self.b2)
        self.b3 = QtWidgets.QPushButton(self.layoutWidget)
        self.b3.setObjectName("b3")
        self.verticalLayout.addWidget(self.b3)
        self.b5 = QtWidgets.QPushButton(self.layoutWidget)
        self.b5.setObjectName("b5")
        self.verticalLayout.addWidget(self.b5)
        self.b4 = QtWidgets.QPushButton(self.layoutWidget)
        self.b4.setObjectName("b4")
        self.verticalLayout.addWidget(self.b4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.b1.setToolTip(_translate("Form", "打开一个文件"))
        self.b1.setText(_translate("Form", "打开文件"))
        self.b2.setStatusTip(_translate("Form", "选择一个字体"))
        self.b2.setText(_translate("Form", "选择字体"))
        self.b3.setStatusTip(_translate("Form", "选择字体颜色"))
        self.b3.setText(_translate("Form", "选择颜色"))
        self.b5.setText(_translate("Form", "保存文件"))
        self.b4.setText(_translate("Form", "打印文件"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
