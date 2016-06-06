__author__ = 'martin'
import random
import string

# 随机生成字符串

class CreateRandomWord():
    def __init__(self):
        pass

    @staticmethod
    def create_random_word():
        new_word = string.join(random.sample(['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l'
                                                 , 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'], 6)).replace(
            ' ', '')
        print new_word
        return new_word


if __name__ == '__main__':
    # CreateRandomWord().create_random_word()
    pass
