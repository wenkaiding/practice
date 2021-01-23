# coding:utf-8
__author__ = 'dingwenkai'

from homework.Animal import Animal
from homework.log_decorator import log_decorator


class Cat(Animal):

    def __init__(self, color, age, sex):
        self.name = "猫"
        self.color = color
        self.sex = sex
        self.age = age

    @log_decorator
    def run(self, speed):
        place = "屋顶"
        print(f"{self.age}岁的{self.name}以{speed}米每秒的速度在{place}跳跃着")


if __name__ == '__main__':
    cat = Cat("红色", "3", "公")
    cat.run(3)
