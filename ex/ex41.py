import random
import sys
#from urllib3 import urlopen
import requests 

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []
PHRASES = {
        "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
        "class %%%(object):\n\tdef __init__(self, ***)" :
        "class %%% has-a __init__ that takes self and *** parameters.",
        "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
        "*** = %%%()":
        "Set *** to an instance of class %%%.",
        "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@.",
        "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
        }
# 判断是不是两个参数 并且第二个参数是english
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = True
# 读取连接下面的文件
txt = requests.get(WORD_URL).text
txt2 = txt.splitlines()
for word in txt2:
    WORDS.append(word.strip())
    #把连接请求的文件的逐行加到WORDS这个列表
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
    random.sample(WORDS, snippet.count("%%%"))]#从列表WORDS中随机选择 count返回出现的次数
    other_names = random.sample(WORDS, snippet.count("***"))#从列表WORDS中随机选择
    results = []
    param_names = []
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)#返回一个随机的整数
        param_names.append(', '.join(random.sample(WORDS, param_count)))
        #随机选择1到3个用,连接添加到param_names列表

    for sentence in snippet, phrase:
        result = sentence[:]
    # 把索引的结果给result变量
        for word in class_names:
            result = result.replace("%%%", word, 1)
        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
    #       用新的换掉老的1次
        for word in param_names:
            result = result.replace("@@@", word, 1)
        results.append(result)
    return results
    #返回列表results
# 
try:
    while True:#开始循环
        snippets = list(PHRASES.keys())#把键反回一个迭代器
        random.shuffle(snippets)#随机播放列表
        for snippet in snippets:#迭代这个列表
            phrase = PHRASES[snippet]#把字典的值取出来给这个变量
            question, answer = convert(snippet, phrase)#运行这个函数
            if PHRASE_FIRST:
                question, answer = answer, question
            print (question)
            input("---> ")
            print ("ANSWER: %s\n\n" % answer)
except EOFError:
    print("\nBye")


