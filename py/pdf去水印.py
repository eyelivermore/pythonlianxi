from PIL import Image
from itertools import product #内置选代器库
import fitz #处理PDF的库
import os



#把图片的水印去掉
def remove_pdf(filename):
    '''去水印'''
    page_num = 0
    pdf_file = filename #PDF文件路径
    pdf = fitz.open(pdf_file)#打开PDF文件
    for page in pdf:
        pixmap = page.get_pixmap()#把每一页PDF返回一个像素图
        pixmap.clear_with(255,[0,0,596,90])#去除页眉
        pixmap.clear_with(255,[0,752,596,842])#去掉页脚
        print("清除页眉页脚")
        for pos in product(range(pixmap.width), range(pixmap.height)):#做成一个选代器
            rgb = pixmap.pixel(pos[0], pos[1])#操作像素
            if(sum(rgb) >= 640):#去除颜色的值
                pixmap.set_pixel(pos[0], pos[1], (255, 255, 255))   #符合的像素换成白色                    
        pixmap.pil_save(f"D:\\pyfile\\pdffff\\{page_num}.png")#保存为图片
        print(f"第{page_num}水印去除完成")
        page_num = page_num + 1




#把图片转为PDF
def pic2pdf(path):
    """把图片转为PDF"""
    pic_dir = str(path)
    pdf = fitz.open()#建立一个空白的PDF
    #对目录进行文件排序
    img_files = sorted(os.listdir(pic_dir),key=lambda x:int(str(x).split('.')[0]))
    for img in img_files:
        print(img)
        imgdoc = fitz.open(pic_dir + '/' + img) #打开图像文件 
        pdfbytes = imgdoc.convert_to_pdf()  #图像文件转PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        #pdf.insertPDF(imgpdf)
        pdf.insert_pdf(imgpdf)  #输入PDF     
    pdf.save("d:/demo.pdf")         
    pdf.close()


if __name__ == '__main__':
    files = "D:\\pyfile\\pdf.pdf"
    aa = 'D:\\pyfile\\pdffff'
    # remove_pdf(files)#去水印
    pic2pdf(aa)#转成PDF
