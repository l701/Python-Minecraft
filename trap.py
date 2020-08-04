# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:31 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()


x,y,z=mc.player.getTilePos()

mc.setBlocks(x-1,y,z-1,x+1,y,z+1,57)




