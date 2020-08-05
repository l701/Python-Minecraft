#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:34:07 2017

@author: sam0225
"""

from mcpi.minecraft import Minecraft
import random
import time 

mc = Minecraft.create()
pos=mc.player.getTilePos()

while True:
    y=pos.y+30
    x=pos.x+random.uniform(-20,20)
    z=pos.z+random.uniform(-20,20)
    mc.spawnEntity(x,y,z,+93)
    time.sleep(0.2)

       



