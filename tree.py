#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:34:07 2017

@author: sam0225
"""

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x,y,z=mc.player.getTilePos()


mc.setBlocks(x-1,y+4,z-1,x+3,y+7,z+3,22)
mc.setBlocks(x,y+1,z,x,y+8,z,1)
       



