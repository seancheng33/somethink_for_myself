'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2019/3/14
@Program      : 选任意一张牌比大小的小游戏。
'''
import random
suits = ['clubs','diamonds','hearts','spades']
faces = ['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
keep_going = True

while keep_going:
    my_face = random.choice(faces)
    my_suits = random.choice(suits)
    your_face = random.choice(faces)
    your_suits = random.choice(suits)
    print('I have the', my_face, 'of',my_suits)
    print('You have the',your_face, 'of', your_suits)
    if faces.index(my_face) > faces.index(your_face):
        print('I win!')
    elif faces.index(my_face) < faces.index(your_face):
        print('You win!')
    else:
        print('It`s a tie!')
    answer = input('Hit [Enter] to keep going,any key to exit:')
    keep_going = (answer == '')
