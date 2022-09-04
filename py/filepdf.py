
from itertools import product #内置选代器库
import fitz #处理PDF的库
import os



#把图片的水印去掉
def remove_pdf(filename):
    '''去水印'''
    page_num = 0
    pdf_file = filename 
    
    pdf = fitz.open(pdf_file)
    os.mkdir
    for page in pdf:
        pixmap = page.get_pixmap()
        pixmap.clear_with(255,[0,0,596,90])
        pixmap.clear_with(255,[0,752,596,842])
        print("清除页眉页脚")
        for pos in product(range(pixmap.width), range(pixmap.height)):
            rgb = pixmap.pixel(pos[0], pos[1])
            if(sum(rgb) >= 690):
                pixmap.set_pixel(pos[0], pos[1], (255, 255, 255))   
        pixmap.pil_save(os.path.join(os.getcwd(),f"{page_num}.png"))       
        # pixmap.pil_save(f"D:\\pyfile\\pdffff\\{page_num}.png")
        print(f"第{page_num}水印去除完成")
        page_num = page_num + 1




#把图片转为PDF
def pic2pdf(path):
    """把图片转为PDF"""
    pic_dir = str(path)
    pdf = fitz.open()#建立一个空白的PDF
    img_files = sorted(os.listdir(pic_dir),key=lambda x:int(str(x).split('.')[0]))
    for img in img_files:
        print(img)
        imgdoc = fitz.open(pic_dir + '/' + img)  
        pdfbytes = imgdoc.convertToPDF()   
        imgpdf = fitz.open("pdf", pdfbytes)
        pdf.insertPDF(imgpdf)       
    pdf.save("d:/demo.pdf")         
    pdf.close()




files = "D:\\讯雷下载\\2022年中级经济师《工商管理》考试大纲.pdf"
aa = 'D:\\pyfile\\pdffff'
#remove_pdf(files)
pic2pdf(aa)
