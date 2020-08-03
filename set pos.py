# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:31 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()

x=-91
y=65
z=380

mc.player.setTilePos(x,y,z)