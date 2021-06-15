#!/usr/bin/env python3

import numpy as np

def toFixed(numObj, digits=0):
    return float(f"{numObj:.{digits}f}")

def rotate(r, phi):
    M = np.matrix([[np.cos(np.radians(phi)), -np.sin(np.radians(phi))],
                   [np.sin(np.radians(phi)),  np.cos(np.radians(phi))]])
    return M * r

iA = np.matrix([[np.cos(np.radians(30)), np.sin(np.radians(30))],
               [0, 1]])
A = np.linalg.inv(iA)

for n in range(1, 101):
    #print(n)
    for phi in np.arange(0.5, 59.59, 0.01):
        r = np.matrix([[n], [0]])
        r = A * r
        r = rotate(r, phi)
        r = iA * r
        k = True
        for i in range(2):
            if toFixed(r.item(i), 3) % 1 < 0.999 and toFixed(r.item(i), 3) % 1 > 0.001:
            #if toFixed(r.item(i), 2) % 1 != 0:
                k = False
                
        if k == True:
            print(n, '\t', toFixed(phi, 2), '\t[', toFixed(r.item(0), 3), ',', toFixed(r.item(1), 3), ']')
