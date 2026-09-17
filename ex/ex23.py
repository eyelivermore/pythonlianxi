import sys
#script:文件名
#encoding:编码格式 默认填"utf-8"
#errors:引发的错误方式默认填"strict"
script, encoding, errors = sys.argv

def main(language_file, encoding,errors):
    line = language_file.readline()#读一行
    if line:#如果不为空向下执行
        print_line(line, encoding, errors)
        #调用Print_line函数
        return main(language_file,encoding, errors)
        #再次递归调用main函数

def print_line(line, encoding, errors):
    next_lang = line.strip()
    #把字符串头和尾指定的字符删除掉,默认是空格

    raw_bytes = next_lang.encode(encoding, errors = errors)
    #给出字符串编码,就是文字对应的UTF8数字编码

    cooked_string = raw_bytes.decode(encoding, errors = errors)
    #把编码转换成文字
    print(raw_bytes,"<====>", cooked_string)
    #前面是编码<====>后面是文字
language = open('languages.txt',encoding = 'utf-8')

main(language ,encoding ,errors)