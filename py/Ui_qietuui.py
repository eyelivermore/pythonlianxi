# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pyfile\qietuui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 361, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pathEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.pathEdit.setObjectName("pathEdit")
        self.gridLayout.addWidget(self.pathEdit, 1, 0, 1, 1)
        self.pathButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pathButton.setObjectName("pathButton")
        self.gridLayout.addWidget(self.pathButton, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.fnameEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.fnameEdit.setObjectName("fnameEdit")
        self.gridLayout.addWidget(self.fnameEdit, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.Labeltext = QtWidgets.QLabel(Form)
        self.Labeltext.setGeometry(QtCore.QRect(30, 210, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Labeltext.setFont(font)
        self.Labeltext.setText("这里显示切了多少张图片")
        self.Labeltext.setObjectName("Labeltext")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "切图"))
        self.pathButton.setText(_translate("Form", "选择文件"))
        self.pushButton_2.setText(_translate("Form", "开始切图"))
        self.label.setText(_translate("Form", "选择文件"))
        self.label_2.setText(_translate("Form", "切图后文件名"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

