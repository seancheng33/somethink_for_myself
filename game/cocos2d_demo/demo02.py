"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 18/8/29
@Program      : cocos2d练习,添加精灵和动画
"""
import cocos
from cocos.actions import ScaleBy, Repeat, Reverse, RotateBy


class Title(cocos.layer.Layer):
    def __init__(self):
        super(Title, self).__init__()
        label = cocos.text.Label(
            '测试Cocos2d的适应性',
            font_size=32,
            anchor_x='center', anchor_y='center'
        )
        label.position = 320, 260
        self.add(label)
        sprite = cocos.sprite.Sprite('horngirl.png')
        sprite.position = 320, 320
        sprite.scale = 3
        self.add(sprite, z=1)

        scale = ScaleBy(3, duration=2)
        label.do(Repeat(scale + Reverse(scale)))
        self.do(RotateBy(360, duration=10))

    def on_mouse_motion(self, x, y, dx, dy):
        # 鼠标移动事件
        print(x, y, dx, dy)

cocos.director.director.init()
title = Title()
main_scene = cocos.scene.Scene(title)
cocos.director.director.run(main_scene)