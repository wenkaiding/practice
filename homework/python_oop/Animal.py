# coding:utf-8
__author__ = 'dingwenkai'


# 父类，基类，超类，可被子类继承，重写
class Animal:
    # 静态变量
    speed = 0

    # 构造方法（类里面的叫方法，类外面的叫函数）
    def __init__(self, color, age, sex):
        # 名称（实例变量）
        self.name = "animal"
        # 毛发颜色
        self.color = color
        # 年龄
        self.age = age
        # 性别
        self.sex = sex

    # 跑（动态方法）
    def run(self, speed):
        print(f"名字叫{self.name}，毛发颜色为{self.color}开始以{speed}的速度跑起来了")

    # 叫
    def shout(self):
        print(f"毛发颜色为{self.color}的{self.name}，叫起来了")

    # 吃（私有方法）
    def eat(self):
        print(f"毛发颜色为{self.color}的{self.name}，吃起来了")

    # 休息
    def __rest(self):
        pass