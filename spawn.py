#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:34:07 2017

@author: sam0225
"""

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x,y,z=mc.player.getTilePos()
mc.spawnEntity(x,y,z,12)

       



