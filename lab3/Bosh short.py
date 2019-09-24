#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from graph import *
import tkinter
from PIL import Image

fl=1
t=0
T=0
FL=1
def update():
    global t, T, FL
    
    global fl
    T+=FL
    if T==255:
        Fl=-1
    t=t+fl
    if t>=1:
        fl=-1
    if t<-1:
        fl=1
    for i in range(dwidth):
        for j in range(dheight):
                r=dpix[i, j][0]+T
                g=dpix[i, j][1]-T
                b=dpix[i, j][2]+0.5*T*2*t
                if not (r>140 and g>140 and b>140):
                    moveObjectBy(objdoot[i][j], 5*fl, -5*fl)
                    
                    
    eimage=Image.open("Eye.jpg")
    ewidth=eimage.size[0]
    eheight=eimage.size[1]
    epix=eimage.load()
    obje=list()
    for i in range(ewidth):
        obje.append([])
        for j in range(eheight):
            obje[i].append([])
            r=max(min(epix[i, j][0]+T, 255), 0)
            g=max(min(epix[i, j][1]-T, 255), 0)
            b=max(min(epix[i, j][2]+T*2*t, 255), 0)
            print(r, g , b, type(r))
            penColor(int(r), int(g), int(b))
            brushColor(int(r), int(g), int(b))
            if not (r>140 and g>140 and b>140):
                r+=100
                g+=100
                b+=100
                obje[i][j]=rectangle(gwidth*0.7*scale+i*scale, gheight*0.32*scale+j*scale, gwidth*0.7*scale+i*scale+scale, gheight*0.32*scale+j*scale+scale)
                
    
    
    



image=Image.open("images.jpeg")

gwidth=image.size[0]
gheight=image.size[1]
pix=image.load()
scale=3
print(3)


canvasSize(gwidth*scale, gheight*scale)
windowSize(gwidth*scale, gheight*scale)

for i in range(gwidth):
    for j in range(gheight):
        r=pix[i, j][0]
        g=pix[i, j][1]
        b=pix[i, j][2]
        penColor(r, g, b)
        brushColor(r, g, b)
        rectangle(i*scale, j*scale, i*scale+scale, j*scale+scale)
    
        
image=Image.open("Bosh ball.jpg")
width=image.size[0]
height=image.size[1]
pix=image.load()
objball=list()
for i in range(width):
    objball.append([])
    for j in range(height):
        objball[i].append([])
        r=pix[i, j][0]
        g=pix[i, j][1]
        b=pix[i, j][2]
        penColor(r, g, b)
        brushColor(r, g, b)
        if not (r>140 and g>140 and b>140):
            objball[i][j]=rectangle(gwidth*0.74*scale+i*scale, gheight*0.16*scale+j*scale, gwidth*0.74*scale+i*scale+scale, gheight*0.16*scale+j*scale+scale)


            
print(3)
dimage=Image.open("Doot.jpg")
dwidth=dimage.size[0]
dheight=dimage.size[1]
dpix=dimage.load()
objdoot=list()
for i in range(dwidth):
    objdoot.append([])
    for j in range(dheight):
        objdoot[i].append([])
        r=dpix[i, j][0]
        g=dpix[i, j][1]
        b=dpix[i, j][2]
        penColor(r, g, b)
        brushColor(r, g, b)
        if not (r>140 and g>140 and b>140):
            objdoot[i][j]=rectangle(gwidth*0.13*scale+i*scale, gheight*0.58*scale+j*scale, gwidth*0.13*scale+i*scale+scale, gheight*0.58*scale+j*scale+scale)
            
eimage=Image.open("Eye.jpg")
ewidth=eimage.size[0]
eheight=eimage.size[1]
epix=eimage.load()
obje=list()
for i in range(ewidth):
    obje.append([])
    for j in range(eheight):
        obje[i].append([])
        r=epix[i, j][0]
        g=epix[i, j][1]
        b=epix[i, j][2]
        penColor(r, g, b)
        brushColor(r, g, b)
        if not (r>140 and g>140 and b>140):
            obje[i][j]=rectangle(gwidth*0.7*scale+i*scale, gheight*0.32*scale+j*scale, gwidth*0.7*scale+i*scale+scale, gheight*0.32*scale+j*scale+scale)
print(3)
onTimer(update, 50)

run()
