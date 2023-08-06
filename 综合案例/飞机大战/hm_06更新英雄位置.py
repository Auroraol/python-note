#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/24 16:07
# @Author  : JingDao
# @Email   : 1665834268@qq.com
# @File    : hm_06更新英雄位置.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/24 10:28
# @Author  : JingDao
# @Email   : 1665834268@qq.com
# @File    : hm_05_绘制英雄.py
import pygame
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
#游戏循环 --> 意味着游戏正式开始！
while True:

    #可以指定循环体内部代码执行的频率
    clock.tick(60)

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



#   4调用update的方法更新显示

    pygame.display.update()





pygame.quit()

