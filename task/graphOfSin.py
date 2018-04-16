# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 21:07:24 2018
dram the graph of function Sin
@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as mtl
x=np.arange(0,4*np.pi,0.01)
y=np.sin(x)
mtl.plot(x,y)
mtl.show()
