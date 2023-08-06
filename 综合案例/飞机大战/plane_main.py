#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/25 14:27
# @Author  : JingDao
# @Email   : 1665834268@qq.com
# @File    : plane_main.py
import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战 主游戏"""

    def __init__(self):
        print("游戏初始化")
        # 1创建游戏窗口
        # self.screen = pygame.display.set_mode(480,750)
        # 改造上行代码
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 参加窗口名称
        # self.screen = pygame.display.set_caption("飞机大战")


    #  2创建游戏的时钟
        self.clock = pygame.time.Clock()
    #  3调用私有方法，精灵精灵组创建
        self.__create_sprites()
    #  4创建定时器事件 - 创建敌机 隔多少时间创建一个 1s
        pygame.time.set_timer(CREACT_ENEMY_EVENY,1000)
    #  5创建英雄发射子弹事件
        pygame.time.set_timer(HERO_FIRE_EVENT,500)


    def __create_sprites(self):
        #     # 创建背景精灵和精灵组:
        #     bg1 = BackGround("Aircraft material/backdrop/background.png")
        #     # 因为只有bg1是会存在空白区域 改进:再创建一个背景图，并且初始位置要在最上方
        #     bg2 = BackGround("Aircraft material/backdrop/background.png")
        #     bg2.rect.y = -bg2.rect.height
        #
        #     self.back_group = pygame.sprite.Group(bg1,bg2)

        # # 改进 对精灵进行修改
        bg1 = BackGround()
        bg2 = BackGround(is_alt=True)
        # 创建精灵组
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄精灵
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        # # TODO 按下按键才执行
        # self.pressdown = PresSdown()
        # self.pressdown_group = pygame.sprite.Group(self.pressdown)





    def start_game(self):
        print("游戏开始...")

        while True:
            # 1设置刷新频率
            # self.clock.tick(60)
            # 这又是一个固定值所有定义为常量
            self.clock.tick(Frame_Rate)

            #  2事件监听
            self.__event_handler()
            # 3碰撞检测
            self.__check_collide()
            # 4更新和绘制精灵组
            self.__update_sprites()
            # 5更新显示
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit()
                # exit()
                # 这里用  封装的__game_over方法
                # 静态方法发调用 == 类名加方法名
                PlaneGame.__game_over()
            elif event.type == CREACT_ENEMY_EVENY:
                print("敌机出场...")
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机添加到敌机精灵组
                self.enemy_group.add(enemy)

            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # # TODO 按下按键再执行
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     print('鼠标按下')
            #     self.pressdown.

        # 使用键盘提供得方法获得键盘按键
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应按键的索引值
        if keys_pressed[pygame.K_RIGHT]:
            print("持续向右移动...")
            self.hero.speed = 3
        elif keys_pressed[pygame.K_LEFT]:
            print("持续向左移动")
            self.hero.speed = -3
        else:
            self.hero.speed = 0



    def __check_collide(self):

        #1子弹摧毁敌机(精灵组之间的)
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)

        # 2敌机摧毁英雄
        enemise = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        # 判断列表是否有内容、
        if len(enemise) > 0:
            # 1让英雄牺牲
            self.hero.kill()
            # 2结束游戏
            PlaneGame.__game_over()



    def __update_sprites(self):
        # 对精灵和精灵组进行更新屏幕
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        # 绘制子弹
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)



    @staticmethod
    def __game_over():

        print("游戏结束")
        pygame.quit()
        exit()







#测试（能否使用）
if __name__ == "__main__":
            #创建游戏对象
            game = PlaneGame()

            # 启动游戏
            game.start_game()



