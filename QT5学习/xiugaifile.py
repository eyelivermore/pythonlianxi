from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
import sys

from Ui_xiugaifile import Ui_Form
import os 


class Winfile(QMainWindow,Ui_Form):
#class Winfile(Ui_Form):
    def __init__(self):
        super(Winfile,self).__init__()
        self.setupUi(self)
        self.show()
        self.filename = 'D:/桌面'
    
    #选择要修改的路径
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.filename = QFileDialog.getExistingDirectory(None,'选择文件夹',self.filename)
        self.lineEdit.setText(self.filename)
        shuzhi = len(os.listdir(self.filename))
        self.label_3.setText(f'文件夹有{shuzhi}个文件')

    #确定修改
    @pyqtSlot()
    def on_pushButtonXG_clicked(self):
        #path='D:\\网店图片\\京东宸雯图片\\初级会计\\2022版'
        #获取输入框输入的文字
        value = self.lineEdit_2.text()

        i=0
        #对目录下的文件进行遍历
        for file in os.listdir(self.filename):
        #判断是否是文件
            if os.path.isfile(os.path.join(self.filename,file))==True:
        #设置新文件名
                mmfile = value+f"第{i}张"+file[-4:]
        #替换 把file，换成mmfile然后复制给new_name
                new_name=file.replace(file,mmfile)
        #重命名，os.path.join(路径，文件名)连接路径和文件名的
                os.rename(os.path.join(self.filename,file),os.path.join(self.filename,new_name))
                i+=1

        zhongshu = f"共修改了{i}张"

        self.label_4.setText(zhongshu)

        






if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Winfile()
    sys.exit(app.exec_())
