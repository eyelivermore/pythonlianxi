import jieba    
import wordcloud
#实例调云
w = wordcloud.WordCloud(font_path="msyh.ttc",width=1000,height=700,max_words=100,background_color = "white")
#文件路径
txtpash = "C:/Users/FSir/新建文本文档.txt"

#打开读取文件
with open(txtpash, "r", encoding = "utf-8") as f:
    txt = f.read()

#解霸解词
words = jieba.lcut(txt)
ls= " ".join(words)
#生成词云云图片
w.generate(ls)
#保存图片
w.to_file("txt.jpg")
