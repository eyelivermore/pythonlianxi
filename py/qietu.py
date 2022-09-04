from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
import sys
from Ui_qietuui import Ui_Form
import os
from PIL import Image


class Winfile(QMainWindow,Ui_Form):
    def __init__(self):
        super(Winfile,self).__init__()
        self.setupUi(self)
        self.show()
        self.filename = 'C:/'

    @pyqtSlot()
    def on_pathButton_clicked(self):
        #获取文件名
        self.filename = QFileDialog.getOpenFileName(None,'选择文件',self.filename)
        #输入框显示文件路径和文件名
        self.pathEdit.setText(self.filename[0])


    @pyqtSlot()
    def on_fnameButton_clicked(self):
        #获取输入枢的文件名
        value = self.fnameEdit.text()
        #把文件字分割取目录路径
        path = self.filename[0].rsplit('/',maxsplit = 1)[0]
        print(path+'/'+value+".jpg")
        #打开文件
        p = Image.open(self.filename[0])
        size = p.size#获取图像大小
        x = 0
        for i in range(0,size[1],size[0]):
            if (size[1]-i)>size[0]:
                #切图
                p1 = p.crop((0,i,size[0],i+size[0]))
                #保存切图
                p1.save(path+'/'+value+f"{x}.jpg")
            else:
                p1 = p.crop((0,i,size[0],size[1]))
                p1.save(path+'/'+value+f"{x}.jpg")
            x += 1
        self.Labeltext.setText(f"总共切了{x}张")    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Winfile()
    sys.exit(app.exec_())

    

