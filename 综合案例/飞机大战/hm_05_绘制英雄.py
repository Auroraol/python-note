#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/24 10:28
# @Author  : JingDao
# @Email   : 1665834268@qq.com
# @File    : hm_05_绘制英雄.py
import pygame
pygame.init()


##在游戏循环上方的部分通常称为游戏的初始化

# 创建游戏窗口480x852
screen = pygame.display.set_mode((480,852))

# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("./Aircraft material/backdrop/background.png")
# 2> blit 绘制图像
screen.blit(bg,(0,0))
# 3> update 更新屏幕显示
# pygame.display.update()


# 绘制英雄的飞机!
# hero = pygame.image.load("../Browser Download/70bf787625b553882e28bda4d6f7fc9.jpg")
hero = pygame.image.load("./Aircraft material/fighter/fly/hero1.png")
screen.blit(hero,(150,500))
# pygame.display.update()

#可以在所有工作完成后统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()


#游戏循环 --> 意味着游戏正式开始！

i = 0
while True:

    #可以指定循环体内部代码执行的频率
    clock.tick(60)
    print(i)
    i +=1




    pass


pygame.quit()

