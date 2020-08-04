# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:31 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

try:
    block = int(input('你要的方塊的ID?'))
    mc.setBlock(x,y,z,block)
except:
    mc.postToChat('只能輸入數字!')
    






