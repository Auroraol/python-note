#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/23 21:28
# @Author  : JingDao
# @Email   : 1665834268@qq.com
# @File    : hm_02_使用Rcet描述英雄.py
import pygame

hero_rect = pygame.Rect(100,500,120,125)

print("英雄的原点  %d  %d"% (hero_rect.x,hero_rect.y))
print("英雄的尺寸  %d %d "% (hero_rect.width,hero_rect.height))
print("%d %d "% hero_rect.size)
