#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/25 11:14
# @Author  : JingDao
# @Email   : 1665834268@qq.com
# @File    : plane_sprites.py
import random
import pygame

# 定义一个屏幕大小的常量,以后修改可以直接修改常量就行
SCREEN_RECT = pygame.Rect(0,0,480,750)
# 刷新的帧率
Frame_Rate = 60
# 创建计时器常量
CREACT_ENEMY_EVENY = pygame.USEREVENT
# 创建英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1

# pygame.sprite.sprite是pygame自带的一个类
class GameSprinte(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self,image_name,speed=1):
        #调用父类的初始化方法
        super().__init__()

        #定义对象属性

        self.image = pygame.image.load(image_name)
        # image.get_rect可以创建的矩形对象
        self.rect = self.image.get_rect()
        # 飞行速度
        self.speed = speed

    def update(self):
#update方法是让对象在屏幕的垂直方向移动
        self.rect.y +=self.speed


class BackGround(GameSprinte):
    """游戏背景精灵"""
    def __init__(self,is_alt = False):
    #     1调用父类方法实现父类调用
         super().__init__("Aircraft material/backdrop/background.png",2)

    #     2判断是否是交替图像。默认为真
         if is_alt:

            self.rect.y = -self.rect.height
            #
            # self.rect.y = self.rect.bottom

    # 重写update
    def update(self):
        # 1调用父类的方法实现
        super().update()
        # 判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


class Enemy(GameSprinte):
    """敌机精灵"""

    def __init__(self):
        # 1调用父类方法（父类可以创建图像），创建敌机精灵，同时指定敌机图片
        super().__init__("Aircraft material/Enemy/fly/enemy1.png")

        # 2指定敌机的初始速度位置  1-3
        self.speed = random.randint(1,3)
        # 3指定敌机的初始随机位置
        # 1 y方向的初始位置
        self.rect.bottom = 0
        # 2 x方向的初始位置
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)



        pass

    def update(self):
        # 1调用父类方法（因为父类中以及实现了垂直方向上的飞行）
        super().update()
        # 2判断是否飞出屏幕，如果是需要从精灵组中删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            print("飞出屏幕，需要销毁")
            # kill方法可以将精灵从所有精灵组中删除，精灵可以自动销毁
            self.kill()


    def __del__(self):
        # print("敌机挂了 %s" % self.rect)
        pass


class Hero(GameSprinte):
    """英雄敌机"""

    def __init__(self):
        # 1 调用父类方法，设置imagespeed  ，初始速度是0
        super().__init__("Aircraft material/fighter/fly/hero1.png",0)
        # 2  设置英雄的初始化设置
        # 居中
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom -120

        # 创建子弹的精灵
        self.bullets = pygame.sprite.Group()

    def update(self):

        # 英雄在水平方向移动，直接重写
        self.rect.x += self.speed
        if self.rect.x <0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹")
        # 改造成发三颗子弹
        for i in (0,1,2):
            # 1创建子弹精灵
            bullet = Bullet()

            # 2设置精灵位置,子弹应该比英雄的位置要小一些
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx

            # 3将精灵添加到精灵组,通过add方法
            self.bullets.add(bullet)


class Bullet(GameSprinte):
    """子弹精灵"""
    def __init__(self):
        # 调用父类方法，设置子弹图片，设置初始速度
        super().__init__("Aircraft material/bullet/bullet1.png",-3)

    def update(self):
        # 调用父类方法，让子弹垂直飞行
        super().update()
       # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁")


# class PresSdown(GameSprinte):
#     """按下操作"""
#     super().__init__()
#     print("按下按键")


















