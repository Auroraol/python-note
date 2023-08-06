#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/25 12:13
# @Author  : JingDao
# @Email   : 1665834268@qq.com
# @File    : hm_演练精灵.py

from plane_sprites import *

# 游戏初始化
pygame.init()

##在游戏循环上方的部分通常称为游戏的初始化

# 创建游戏窗口480x750
screen = pygame.display.set_mode((480,750))

# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("./Aircraft material/backdrop/background.png")
# 2> blit 绘制图像
screen.blit(bg,(0,0))
# 3> update 更新屏幕显示
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./Aircraft material/fighter/fly/hero1.png")
screen.blit(hero,(200,350))
# pygame.display.update()

#可以在所有工作完成后统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()


# 1定义一个rect的变量记录飞机的初始位置
hero_rect = pygame.Rect(200,350,102,126)

# 创建敌机的精灵（可以创建很多个）
enemy = GameSprinte("Aircraft material/Enemy/fly/enemy1.png")
enemy1 = GameSprinte("Aircraft material/Enemy/fly/enemy1.png",2)


# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)



#游戏循环 --> 意味着游戏正式开始！
while True:

    #可以指定循环体内部代码执行的频率
    clock.tick(60)
# #     捕获事件
#     event_list = pygame.event.get()
#     print(event_list)
#     监听事件
    for event in pygame.event.get():
        # 判断事件类型是否是（关闭）退出事件
        if event.type == pygame.QUIT:
            print("游戏退出...")
            # 卸载所有模块
            pygame.quit()
            # exit（）退出
            exit()


#   2修改飞机的位置
    hero_rect.y -= 1
    # 第4步
    # if hero_rect.y <= -126:
    #     hero_rect.y = 750
    if hero_rect.bottom <= 0:
        hero_rect.y = 750

#   3调用blit的方法绘制图像
#     重新绘制了背景图像，
    screen.blit(bg,(0,0))
    # 绘制英雄飞机到新的位置
    screen.blit(hero,hero_rect)
    # 让精灵组调用两个方法 update方法让组中所有精灵更新位置
    enemy_group.update()
    # draw可以再屏幕上绘制所有精灵
    enemy_group.draw(screen)

    #   4调用update的方法更新显示

    pygame.display.update()





pygame.quit()

