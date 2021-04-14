from random import randint

STR = "!@#$%^&*()1234567890"


def chrismas_tree(height):
    for i in range(1, height + 1):
        level = ''
        level += ' ' * (height - i)
        for j in range(i * 2 - 1):
            level += STR[randint(0, len(STR))]

        print(level)

chrismas_tree(5)