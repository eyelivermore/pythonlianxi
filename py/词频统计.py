#--encoding = utf-8--
import jieba
import wordcloud
w = wordcloud.WordCloud(font_path="msyh.ttc",width=1000,height=700,max_words=100,background_color = "white")

wd = "D:\\pythonlianxi\\ipynd\\txt8.txt"
#txt = open(wd, "r", encoding = "utf-8").read()
with open(wd, "r", encoding = "utf-8") as f:
    txt = f.read()
words = jieba.lcut(txt)
ls = " ".join(words)
w.generate(ls)
w.to_file("2019中央政府报告.jpg")
name = ['以上','优化','各类','我国','地方','我们','今年','取得','合理','政府']
counts = {}
for wo in words:
    if len(wo) == 1:
        continue
    # elif wo == "萧峰" or wo == "乔帮主":
    #     rwo = "乔峰"
    # elif wo == '段公子':
    #     rwo = '段誉'
    # elif wo == '王姑娘':
    #     rwo = "王语嫣"
    elif wo in name:
        #过滤掉以上列表里的词组
        continue
    else:  
        rwo = wo
    counts[rwo] = counts.get(rwo,0)+1
        
# print("天龙八部人物出场次数")
items = list(counts.items())
items.sort(key = lambda x:x[1] , reverse = True)


for i in range(100):
    a,b = items[i]
    print("{0:<10}出现了{1:>5}次".format(a,b))
