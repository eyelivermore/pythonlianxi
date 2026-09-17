class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

#实例化Song这个类,happy_bday是Song的实例
happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])
#bulls_on_parade是Song的另外一个实例
bulls_on_parade = Song(["They rally around tha family",
"With pockets full of shells"])

#调用happy_bday这个对象的sing_me_a_song()的这个方法
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
#调用bulls_on_parade这个对象的sing_me_a_song方法