# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:31 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import random
import time
mc=Minecraft.create()

time.sleep(5)

x,y,z=mc.player.getTilePos()

while True:
    color=random.randrange(16)
    mc.setBlocks(x+20,y-1,z+20,x-20,y-1,z-20,0,color)
    time.sleep(0.5)




