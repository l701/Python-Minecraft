#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:34:07 2017

@author: sam0225
"""

from mcpi.minecraft import Minecraft
import time 

time.sleep(3)

mc = Minecraft.create()
x,y,z=mc.player.getTilePos()

for i in range(20):
    mc.setBlock(x+i,y-1,z+i,1)
    mc.setBlock(x+i-1,y-1,z+i,1)
    mc.setBlock(x+i,y-1,z+i+1,1)
    
    time.sleep(1)




