from sys import exit
from random import randint
from textwrap import dedent


class Scene():
    """场景"""
    def enter(self):
        print("此场景尚未配置。对它进行子类化并实现enter（）")
        print(" 对它进行子类化和实现enter()")
        exit(1)


class Engine():
    """游戏引擎"""
    def __init__(self, scene_map):
        self.scene_map = scene_map
        #先初始化这个场景,地图类传进来的一个场景类实例
        
    def play(self):
        #开始
        current_scene = self.scene_map.opening_scene()
        #map实例的这个opening_scene方法返回的是一个字典的值,字典的值是其中的一个初始场景类
        #这个初始场景类是中央走郎
        last_scene = self.scene_map.next_scene('finished')
        #用地图类的next_scene()方法初始一个结束类
        while current_scene != last_scene:
            #如果不是结束类就继续循环
            next_scene_name = current_scene.enter()
            #调用其中一个类的enter()方法返回的字符串(就是场景的名字)给这个变量
            current_scene = self.scene_map.next_scene(next_scene_name)
            #调用这个self.scene_map地图实例的next_scene()方法把上个变量得到的类名字传next_scene给这个方法
            #然后再赋值给current_scene,然后得到相应的类也相当于实例化这个类
        
        current_scene.enter()


class Death(Scene):
    """死亡"""
    quips = ["你死了。你有点吮吸这个",
            "你的妈妈会感到骄傲......如果她更聪明",
            "这样的luser",
            "我有一只小狗",
            "它在这方面更好"
            ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        #随机调用上面列表中的一句话
        exit(1)
        

class CentralCorridor(Scene):
    """中央走廊"""
    def enter(self):
        
        print(dedent("""行星Percal＃25的Gothons侵入了你的船
                    并摧毁了“你的整个船员。你是最后一个幸存的成员，
                    你的最后一个任务是从武器军械库获得中子毁灭炸弹，
                    把它放在桥上，然后吹船在进入一个逃生舱之后。
                    当Gothon跳出来时，你正沿着中央走廊跑到武器军械库，
                    红色鳞状皮肤，
                    黑暗肮脏的牙齿和邪恶的小丑服装在他充满仇恨的身体周围流动。
                    他正阻挡着军械库和即将拉动武器爆炸你.请选择:shoot,dodge,tell a joke"""))
        action = input(">>>>> ")
        if action == "shoot":
            print(dedent("""快速抽签，你把你的冲击波拉出来，
                    然后在哥特顿开火。他的小丑服装在他的身体周围流动和移动，
                    ”抛出“”你的目标。你的激光击中了他的服装，但完全错过了他
                    。这彻底毁掉了他母亲给他买的全新服装，
                    “这让他飞起来陷入一种疯狂的愤怒，
                    并在脸上反复爆炸，直到“你死了。然后他吃了你"""))
            return "death"
        elif action == "dodge":
            print(dedent("""像一个你躲闪，编织，滑动和向右滑动的世界级拳击手
            当Gothon的冲击波将激光从你的头上射出来。
            在你狡猾的躲闪中间，你的脚滑了，你将你的头撞在金属墙上然后昏倒。
            你只是在Gothon踩踏后不久醒来”打印“你的头并吃掉"""))
            return 'death'
        elif action == "tell a joke":
            print(dedent("""幸运的是，他们让你学会了Gothon对学院的侮辱。
            你告诉你一个Gothon的笑话你知道：
            Lbhe zbgure vf fb sng，jura fur fvgf nebhaq gur ubhfr，fur fvgf nebhaq gur ubhfr。
            Gothon停下来，尽量不要笑，然后笑出来，不能动弹。
            当他在笑的时候，你跑起来并将他射向头部
            让他失望，然后跳过武器军械库的门。"""))
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

        



class LaserWeaponArmory(Scene):
    """激光武器库"""
    def enter(self):
        print(dedent("""你潜入武器军械库，蹲伏并扫描房间
                更多可能隐藏的Gothons。它已经安静了，太安静了。
                你站起来跑到房间的另一边，在容器里找到
                的中子炸弹。盒子上有一个键盘锁
                你需要代码来取出炸弹。
                如果你得到的话代码错了10次，
                然后锁永远关闭，你不能
                得到炸弹。代码是3位数。"""))
        code =  "{}{}{}".format(randint(1,9),randint(1,9),randint(1,9))
        #code = "555"
        guess = input("请输入密码,你有10次机会>")
        guesses = 1
        while guess != code and guesses < 10:
            opportunity = 10 - guesses
            print("密码错误!")
            guesses += 1
            guess = input(f"请重新输入密码,你还有{opportunity}机会")
        if guess == code:
            print(dedent("""容器点击打开，密封破裂，让气体排出。
                    你抓住中子弹，尽可能快地跑到
                    桥上，你必须把它放在正确的位置。"""))
            return 'the_bridge'
        else:
            print(dedent("""最后一次锁定嗡嗡声，
            然后当机制融合在一起时，你会听到令人作呕的
                            声音。
                            你决定坐在那里，
                            最后Gothons从他们的船上炸掉了
                            船，你就死了。"""))
            return 'death'

class TheBridge(Scene):
    """主控舱"""
    def enter(self):
        print (dedent("""你蹲在桥上，
        手臂上放着一颗毁坏炸弹的炸弹，
        让那些试图控制船只的5名Gothons感到惊讶。
        他们每个人都有一个比上一个更丑陋的小丑服装。
        他们还没有把他们的“武器”拉出来，
        因为他们看到你手臂下的活动炸弹并且不想把它关掉
        throw the bomb,slowly place the bomd"""))
        action = input("> >> >")
        if action == "throw the bomb":
            print (dedent("""在恐慌中，
            你将炸弹扔到Gothons集团并向门进行跳跃。
            就在你放下它的时候，Gothon会在后面向你射击，
            杀死你。当你死了，
            你看到另一个哥特人疯狂地试图解除炸弹的武器。
            你知道他们可能会在它熄火时爆炸"""))
            return 'death'
        elif action == "slowly place the bomb":
            print (dedent("""你把你的冲击波指向你手臂下的炸弹“并且Gothons举起手来开始出汗。
                    你向后靠近门，打开它，然后小心地“将炸弹放在地板上，指着你的爆炸声。
                    然后你跳回门，按下关闭按钮“并锁定锁定，
                    以便Gothons无法离开。”现在炸弹被放置，
                    你跑到逃生舱“下车这罐头。"""))
            return 'escape_pod'
        else:
            print ("DOES NOT COMPUTE!")
            return "the_bridge"

class EscapePod(Scene):
    """救生舱"""
    def enter(self):
        print(dedent("""在整艘船爆炸之前，你拼命地试图让它
                逃生舱。看起来
                几乎没有任何Gothons在船上，所以你的行程没有”印刷“干扰。你带着逃生舱到达房间，
                现在需要选择一个。有些可能会被损坏
                但你没时间看。有5个豆荚，其中一个
                做你拿？"""))

        good_pod = randint(1,5)
        guess = input("[pod #]>")
        if int(guess) != good_pod:
            print(dedent("""你跳进pod {}然后点击弹出按钮。
                    吊舱逃逸到空间的空隙中，随着船体破裂，
                    内爆，将您的身体
                    成果酱果冻""".format(guess)))
            return 'death'
        else:
            print(dedent("""你跳进pod {}然后点击弹出按钮。
            豆荚很容易滑入太空，朝向
            下面的行星。当它飞向地球时，你看起来
            回来，看到你的船内爆然后爆炸像一个”
            明亮的星星，取出Gothon在相同的
            时间发货。你赢了！""".format(guess)))
            return 'finished'

class Finished(Scene):
    """结束类"""
    def enter(self):
        print("You won! Good job.")
        return 'finished'

class Map():
    """地图类"""

    scenes = {
            'central_corridor': CentralCorridor(),
            'laser_weapon_armory': LaserWeaponArmory(),
            'the_bridge': TheBridge(),
            'escape_pod': EscapePod(),
            'death': Death(),
            'finished': Finished(),
            }
            #这是6个场景
    def __init__(self, start_scene):
        self.start_scene = start_scene
        #初始化一个开始场景

    def next_scene(self, scene_name):
        #这个设计太精妙了
        #用场景的建来调用场景的值
        val = Map.scenes.get(scene_name)
        return val
        #返回的是一个场景的类
    def opening_scene(self):
        #这一个设计太精炒了
        #调用返回next_scene()这个方法
        return self.next_scene(self.start_scene)



a_map = Map('central_corridor')#把地图类实例化传给他一个初始的场景
a_game = Engine(a_map)#把地图这个实例做为参数传给这个引擎类的实例

a_game.play()#调用这个实例的方法play()