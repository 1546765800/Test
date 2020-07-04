# -*- coding: utf-8 -*-
"""
Created on Mon May 21 21:34:37 2018

@author: Lenovo
"""
import numpy as np
from vpython import canvas,box,vector,color,arrow,cylinder,sphere,label,helix,cone,text,curve,shapes,extrusion


TargetType = 0  # 0:sphere 1:box
LabelShow = "Bessel Sheet"
FigurePath=r'BesselSheet.png'

mPosTarget=vector(-1.5,0.3,0.1)
mPosOrigin=vector(-0.05,0.0,0.0)

sce=canvas(title="Draw Light Sheet", width=800, height=700, background=color.white)
if TargetType == 0:
    target = sphere(pos=mPosTarget, radius=0.1, color=color.blue)
elif TargetType == 1:
    target = box(pos=mPosTarget, size=vector(0.2, 0.2, 0.2), color=color.blue)
mBoxMain=box(pos=vector(-1,0,0),color=color.white,length=2,width=0.01,height=1,texture={'file':FigurePath, 'place':['sides'], 'flipx':True,'flipy':True,'turn':-3})
# mBoxBack=box(pos=vector(0,0,0),width=0.8,length=0.1,height=1,color=vector(0.5,0.5,0.5))
# mHelix = helix(pos=vector(0,0,0),axis=vector(1,0,0), radius=0.3,color=color.green)
# mCylinder0=cylinder(pos=vector(0,0,0),axis=vector(1,0,0),color=vector(0.5,0.5,0.5),radius=0.4,opacity=0.5)
# mCylinder1=cylinder(pos=vector(0.0,-0.5,0.5),axis=vector(0.5,0,0),color=color.blue,radius=0.1)
# mCone=cone(pos=vector(0,-0.5,0.5),axis=vector(-0.2,0,0),radius=0.15,color=color.blue)
listBase = [target, mBoxMain ]

aclength=0.01
lenArrowOrigin = 1.00
lenArrowTarget = 0.75*lenArrowOrigin
mArrowOriginX=arrow(pos=mPosOrigin, axis=vector(-lenArrowOrigin, 0, 0)*0.6, shaftwidth=aclength, color=color.black)
mArrowOriginY=arrow(pos=mPosOrigin, axis=vector(0, lenArrowOrigin, 0), shaftwidth=aclength, color=color.black)
mArrowOriginZ=arrow(pos=mPosOrigin, axis=vector(0, 0, lenArrowOrigin), shaftwidth=aclength, color=color.black)
mArrowTargetX=arrow(pos=mPosTarget, axis=vector(-lenArrowTarget, 0, 0), shaftwidth=aclength, color=color.black)
mArrowTargetY=arrow(pos=mPosTarget, axis=vector(0, lenArrowTarget, 0), shaftwidth=aclength, color=color.black)
mArrowTargetZ=arrow(pos=mPosTarget, axis=vector(0, 0, lenArrowTarget), shaftwidth=aclength, color=color.black)
listArrows = [mArrowTargetX, mArrowTargetY, mArrowTargetZ, mArrowOriginX, mArrowOriginY, mArrowOriginZ]

lenArrowOrigin*=1.05
lenArrowTarget*=1.05
mTextOriginX = text(text='z', pos=mPosOrigin + vector(-lenArrowOrigin, 0, 0)*0.6, color=color.black, depth=0.05)
mTextOriginY = text(text='y', pos=mPosOrigin + vector(0, lenArrowOrigin, 0), color=color.black, depth=0.05)
mTextOriginZ = text(text='x', pos=mPosOrigin + vector(0, 0, lenArrowOrigin), color=color.black, depth=0.05)
mTextTargetX = text(text="z'", pos=mPosTarget + vector(-lenArrowTarget, 0, 0), color=color.black, depth=0.05)
mTextTargetY = text(text="y'", pos=mPosTarget + vector(0, lenArrowTarget, 0), color=color.black, depth=0.05)
mTextTargetZ = text(text="x'", pos=mPosTarget + vector(0, 0, lenArrowTarget), color=color.black, depth=0.05)
listArrowsText=[mTextOriginX, mTextOriginY, mTextOriginZ, mTextTargetX, mTextTargetY, mTextTargetZ]
for item in listArrowsText:
    item.length = 0.1*item.length
    item.height = 0.1 * item.height
    item.rotate( angle=1.5 )

mTextTitle = text(text=LabelShow, pos=vector(-1,-0.6,-0.2), align='center', color=color.black,depth=0.01)
mTextTitle.length = 0.15*mTextTitle.length
mTextTitle.height = 0.15 * mTextTitle.height
mTextTitle.rotate( angle=1.0 )
listArrowsText.append(mTextTitle)

curveTheta = curve(mPosTarget, mPosTarget+vector(-1,0.8,0), color = color.black, radius=0.005)
mAngleThetaBase = shapes.arc(radius=0.2, angle1=0, angle2=np.arctan(0.8))
mAngleTheta = extrusion(path=[mPosTarget-vector(0,0,0.01), mPosTarget+vector(0,0,0.01)], shape=mAngleThetaBase, color=color.black)
listAngle = [curveTheta, mAngleTheta]

objs=listBase + listArrows + listArrowsText + listAngle
objs=listBase + listArrows + listArrowsText
for item in objs:
    item.rotate(angle=-0.7,axis=vector(1,0,0),origin=vector(0,0,0))
    item.rotate(angle=0.5, axis=vector(0, 0, 1), origin=vector(0, 0, 0))