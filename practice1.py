# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:31 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()



a=0
a=a+1

while a<50:
    color=random.randrange(9)
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,38,color)
    time.sleep(0.2)





