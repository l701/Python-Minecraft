#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:34:07 2017

@author: sam0225
"""

from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()


while True:
    hits=mc.events.pollProjectileHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        time.sleep(0.5)
        mc.player.setTilePos(x,y,z)
        time.sleep(0.5)
        mc.spawnEntity(x,y,z,99)
        
       



