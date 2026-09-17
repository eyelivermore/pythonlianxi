from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtPrintSupport import *
import sys
from Ui_dialogui import Ui_Form

class Run_dailog(QMainWindow,Ui_Form):
    """运行对话框打开文件,修改字体,修改颜色"""
    def __init__(self):
        super(Run_dailog ,self).__init__()
        self.setupUi(self)
        self.printer = QPrinter()
        self.show()

 

    @pyqtSlot()
    def on_b1_clicked(self):
        """打开文件对话框"""
        fname = QFileDialog.getOpenFileName(self,'无意的学习打印','./')
        if fname[0]:
            with open(fname[0],'r',encoding='utf-8',errors='ignore') as f:
                self.textEdit.setText(f.read())
            
    @pyqtSlot()
    def on_b2_clicked(self):
        """打开字体对话框"""
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setCurrentFont(font)
        

    @pyqtSlot()
    def on_b3_clicked(self):
        """打开颜色对话框"""
        col = QColorDialog.getColor()
        if col.isValid():
            self.textEdit.setTextColor(col)

    @pyqtSlot()
    def on_b4_clicked(self):
        """打印文件"""
        printdialog = QPrintDialog(self.printer,self)
        if QDialog.Accepted == printdialog.exec_():
            self.textEdit.print(self.printer)
        

    @pyqtSlot()
    def on_b5_clicked(self):
        """保存文件"""
        filename = QFileDialog.getSaveFileName(self,"保存文件","./",'text files (*.txt)')
        if filename[0]:
            with open(filename[0],'w',encoding = "utf-8",errors = 'ignore') as f:
                f.write(self.textEdit.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = Run_dailog()
    sys.exit(app.exec_())