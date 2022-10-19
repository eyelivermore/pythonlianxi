import re
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from Ui_lianxi import Ui_Form #这一个是UI文件
import sys
import os 
import pandas as pd
#这是一个处理每天整理识别快递单后的表格工具
class WinLabel(QMainWindow,Ui_Form):
    def __init__(self):
        super(WinLabel,self).__init__()
        self.setupUi(self)
        self.show()
        self.filename = "c:/"
        self.sheet= None
        self.path = None

    @pyqtSlot()
    def on_fileButton_clicked(self):
        #获取文件名
        self.filename = QFileDialog.getOpenFileName(None,'选择文件',self.filename)
        #输入框显示文件路径和文件名
        self.lineEdit.setText(self.filename[0])
    @pyqtSlot()
    def on_pushButton_clicked(self):
        #把文件字分割取目录路径
        self.path = self.filename[0].rsplit('.',maxsplit = 1)[0]
        if self.sheet ==1:
            self.editsheetone()
        elif self.sheet == 2:
            self.editsheettow()
  
    @pyqtSlot()
    def on_rjpgButton_clicked(self):
        self.label.setText('现在处理多张表格')
        self.sheet = 2
    @pyqtSlot()
    def on_rpngButton_clicked(self):
        self.label.setText('现在处理单张表格')
        self.sheet = 1

    def editsheetone(self):
        #处理Excel文件就一张表的函数
        df = pd.read_excel(self.filename[0],header=None,names=['原数据','姓名','电话','地址','类目'])
        #下面是读取字段 
        df['原数据'] = df['原数据'].apply(lambda x:str(x).strip())
        df['原数据'] = df['原数据'].apply(lambda x:str(x).replace('\n',''))
        df['姓名'] = df['原数据'].apply(lambda x:str(x).split('1',1)[0]) 
        df['电话'] = df['原数据'].str.extract(r'(\d{11})',expand = False)
        df['地址'] = df['原数据'].str.extract(r'\d{11}(.*)',expand = False)
        df['类目'] = df['地址'].apply(self.expand)
        df['地址'] = df['地址'].apply(self.expandz)
        df['类目'] = df['类目'].apply(self.expandy)
        df.to_excel(self.path+"整理后的.xlsx",index=False)
        #保存整理后的表格

    def editsheettow(self):
        #处理文件里面有多张表的函数
        df = pd.read_excel(self.filename[0],sheet_name=None,header=None,names=['原数据','姓名','电话','地址','类目'])
        l = list(df.keys())
        #只是先读取先一个表格，再用for循环分别读取每一个表的字段
        for i in l:
            df[i]['原数据'] = df[i]['原数据'].apply(lambda x:str(x).strip())
            df[i]['原数据'] = df[i]['原数据'].apply(lambda x:str(x).replace('\n',''))
            df[i]['姓名'] = df[i]['原数据'].apply(lambda x:str(x).split('1',1)[0]) 
            df[i]['电话'] = df[i]['原数据'].str.extract(r'(\d{11})',expand = False)
            df[i]['地址'] = df[i]['原数据'].str.extract(r'\d{11}(.*)',expand = False)
            df[i]['类目'] = df[i]['地址'].apply(self.expand)
            df[i]['地址'] = df[i]['地址'].apply(self.expandz)
            df[i]['类目'] = df[i]['类目'].apply(self.expandy)
        with pd.ExcelWriter(self.path+"整理后.xlsx") as writer:
        #保存整理后的表格也和单张表的方式不一样，用pd.Excelwriter保存
            for i in l:
                df[i].to_excel(writer,sheet_name = i,index=False)
    
    def expand(self,x):
    #识别类目
        if "一建" in x:
            p = re.search(r'一建(.*)',x).group()
        elif '二建' in x:
            p = re.search(r'二建(.*)',x).group()
        elif '二级消防' in x:
            p = re.search(r'二级消防(.*)',x).group()
        elif '消防' in x:
            p = re.search(r'消防(.*)',x).group()
        elif '护士' in x:
            p = re.search(r'护士(.*)',x).group()
        elif '初级' in x:
            p = re.search(r'初级(.*)',x).group()
        elif '中级会计' in x:
            p = re.search(r'中级(.*)',x).group()
        elif '中级经济师' in x:
            p = re.search(r'中级(.*)',x).group()
        elif '司法' in x:
            p = re.search(r'司法(.*)',x).group()
        elif '证券' in x:
            p = re.search(r'证券(.*)',x).group()
        elif '基金' in x:
            p = re.search(r'基金(.*)',x).group()
        elif '安全' in x:
            p = re.search(r'中级(.*)',x).group()
        elif "注册会计" in x:
            p = re.search(r'CPA(.*)',x).group()
        elif '造价' in x:
            p = re.search(r'造价(.*)',x).group()
        elif '四川' in x:
            p = re.search(r'四川(.*)',x).group()
        elif '广东' in x:
            p = re.search(r'广东(.*)',x).group()
        elif '护理学' in x:
            p = re.search(r'护理学(.*)',x).group()
        elif '护师' in x:
            p = re.search(r'护师(.*)',x).group()
            
        else:
            return "无法识别"
        return p

    def expandz(self,x):
        #去除地址中的店名和类目名
        if "竹义"in x:
            p = re.sub(r'竹义(.*)',"",x)
        elif '星辰' in x:
            p = re.sub(r'星辰(.*)',"",x)       
        elif '易恒' in x:
            p = re.sub(r'易恒(.*)',"",x)        
        elif '才俊' in x:
            p = re.sub(r'才俊(.*)',"",x)       
        elif '库达' in x:
            p = re.sub(r'库达(.*)',"",x)
        else:
            return x
        return p

    def expandy(self,x):
        #去除地址中的店名
        if "竹义"in x:
            p = re.sub(r'竹义图书',"",x)
        elif '星辰' in x:
            p = re.sub(r'星辰图书',"",x)    
        elif '易恒' in x:
            p = re.sub(r'易恒图书',"",x)    
        elif '才俊' in x:
            p = re.sub(r'才俊图书',"",x)        
        elif '库达' in x:
            p = re.sub(r'库达图书',"",x)
        else:
            return x
        return p


    
        

        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = WinLabel()
    sys.exit(app.exec_())
