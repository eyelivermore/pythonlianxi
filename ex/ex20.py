from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())#读取全部文件内容

def rewind(f):
    f.seek(36)#把文件指针放到第36个字符

def print_a_line(line_count,f):
    print(line_count,f.readline())#读取一行

current_file = open(input_file,encoding = "utf-8")#打开文件

print(u"first let's print the whole lile:\n")

print_all(current_file)

print(u"now let's rewind, kind of like a tagv.")

rewind(current_file)

print(u"let's print three lines")

current_line = 1
print_a_line(current_line,current_file)

current_line =current_line+1
print_a_line(current_line,current_file)

current_line =current_line+1
print_a_line(current_line,current_file)