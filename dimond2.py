# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:31 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import random
mc=Minecraft.create()


x,y,z=mc.player.getTilePos()

color=random.randrange(16)
mc.setBlocks(x+20,y-1,z+20,x-20,y-1,z-20,0)




