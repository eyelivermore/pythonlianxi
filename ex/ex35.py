from sys import exit


def gold_room():
    """黄金房间"""
    print("This room is full of gold. How much do you take?这个房间充满了黄金,你拿了多少钱?")
    choice = input("请输入多少钱>>>> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.先生请输入钱数")
    if how_much < 50:
        print("Nice, you're not greedy, you win!很好你不贪心,你赢了")
        exit(0)
    else:
        dead("You greedy bastard!你是个贪心的混蛋")

def bear_room():
    """选择左的房间"""
    print ("There is a bear here.这里有一只熊")
    print ("The bear has a bunch of honey.熊有一堆蜂蜜")
    print ("The fat bear is in front of another door.胖熊在另一扇门前面")
    print ("How are you going to move the bear?你打算如何移动熊")
    bear_moved = False


    while True:
        choice = input("请输入你的选择 拿蜂蜜'take honey'或 嘲讽承担'taunt bear'>>>>>> ")
        if choice == "take honey":#拿蜂蜜
            dead("The bear looks at you then slaps your face off.熊见你拍死了你")#熊看见你然后拍死你
        elif choice == "taunt bear" and not bear_moved:#嘲讽承担
            print("The bear has moved from the door.熊已经离开了门")#熊已经离开了门
            print("You can go through it now. open door你现在可以通过了")#你现在可以通过了
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.熊生气了咬断了你的腿")#熊生气咬断了你的腿
        elif choice == "open door" and bear_moved:#打开门
            gold_room()
        else:
            print ("I got no idea what that means.我不知道这意味着什么")


def cthulhu_room():
    """右房间"""
    print ("Here you see the great evil Cthulhu.在这里你可以看到邪恶的邪神")
    print ("He, it, whatever stares at you and you go insane.他，无论什么盯着你，你都疯了")
    print ("Do you flee for your life or eat your head?你逃命还是吃头？")
    choice = input("请选择flee 或 head >>>>  ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!你很好吃")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    """开始"""
    print ("You are in a dark room.你在一个黑暗的房间")#你在一个黑暗的房间
    print ("There is a door to your right and left.你的左右各有一扇门")
    print ("Which one do you take?你选择那一扇门")
    choice = input("输入你的选择 left 或 right >>>> ")
    if choice == "left":#如果选择左路
        bear_room()
    elif choice == "right":#如果选择右
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.你饿死在房间")

start()
#开始....