# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:31 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
a=0
while a<20:
    mc.setBlocks(x-30,y-1,z,x+30,y-30,z,19)
    z=z+6
    a=a+1
    
    








