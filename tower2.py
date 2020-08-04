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

mc.setBlock(x-1,y,z+1,47)
time.sleep(0.5)
mc.setBlock(x-1,y,z,47)
time.sleep(0.5)
mc.setBlock(x-1,y,z,47)
time.sleep(0.5)
mc.setBlock(x-1,y,z-1,47)
time.sleep(0.5)
mc.setBlock(x,y,z-1,47)
time.sleep(0.5)
mc.setBlock(x+1,y,z-1,47)
time.sleep(0.5)
mc.setBlock(x+1,y,z,47)
time.sleep(0.5)
mc.setBlock(x+1,y,z+1,47)
time.sleep(0.5)
mc.setBlock(x,y,z+1,47)



