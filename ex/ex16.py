from sys import argv

script, filename = argv

print(f"We're qning to erase {filename}.")
print("if you don't want that. hiT CTRL-C")
print('if you do want that. hit RETURN')

input("?")

print("Opening the file...")
target = open(filename,'w',encoding='utf-8')

print('Truncating the file.  Goodbye!')

target.truncate()
#清空target这个文件对象
print("Now I'm qning to ask you for three linee.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write thess to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("And finally. we close it.")

target.close()

