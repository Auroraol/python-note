#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/23 22:18
# @Author  : JingDao
# @Email   : 1665834268@qq.com
# @File    : hm_04_.py
import pygame
pygame.init()

# 创建游戏窗口480x852
screen = pygame.display.set_mode((480,852))

# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("./Aircraft material/backdrop/background.png")
# 2> blit 绘制图像到屏幕
screen.blit(bg,(0,0))
# 3> update 更新屏幕显示
pygame.display.update()


while True:
    pass





pygame.quit()

