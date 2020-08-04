# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:31 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

time.sleep(5)
x,y,z=mc.player.getTilePos()

mc.setBlock(x,y,z,47)
time.sleep(0.5)
mc.setBlock(x,y+1,z,47)
time.sleep(0.5)
mc.setBlock(x,y+2,z,47)
time.sleep(0.5)
mc.setBlock(x,y+3,z,47)
time.sleep(0.5)
mc.setBlock(x,y+4,z,47)
time.sleep(0.5)
mc.setBlock(x,y+5,z,47)
time.sleep(0.5)
mc.setBlock(x,y+6,z,47)
time.sleep(0.5)
mc.setBlock(x,y+7,z,47)
time.sleep(0.5)
mc.setBlock(x,y+8,z,47)
time.sleep(0.5)
mc.setBlock(x,y+9,z,47)


