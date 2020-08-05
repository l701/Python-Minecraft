#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:34:07 2017

@author: sam0225
"""

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

def plantTree(x,y,z):
    mc.setBlocks(x-1,y+4,z-1,x+3,y+6,z+3,47)
    mc.setBlocks(x,y,z,x,y+6,z,1)
       

x,y,z=mc.player.getTilePos()

for i in range(6):
    for j in range(6):
        plantTree(x+i*8,y+j*i,z)

