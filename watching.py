# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:31 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()
t=0

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat('You are located on X:'+str(x)+',Y:'+str(y)+',Z:'+str(z))

