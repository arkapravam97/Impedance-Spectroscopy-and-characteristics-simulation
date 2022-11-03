# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:39:59 2022

@author: Arkaprava Mondal
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

f1=pd.read_csv('R Data.csv')
Freq=f1['Frequency']
A30=f1["30"]
A300=f1["300"]
A40=f1["40"]
A400=f1["400"]
A50=f1["50"]
A500=f1["500"]
A60=f1["60"]
A600=f1["600"]
A70=f1["70"]
A700=f1["700"]
A80=f1["80"]
A800=f1["800"]
A90=f1["90"]
A900=f1["900"]
A100=f1["100"]
A1000=f1["1000"]
A110=f1["110"]
A1100=f1["1100"]
A120=f1["120"]
A1200=f1["1200"]
A130=f1["130"]
A1300=f1["1300"]
A140=f1["140"]
A1400=f1["1400"]
A150=f1["150"]
A1500=f1["1500"]
A160=f1["160"]
A1600=f1["1600"]
A170=f1["170"]
A1700=f1["1700"]
A180=f1["180"]
A1800=f1["1800"]
A190=f1["190"]
A1900=f1["1900"]
A200=f1["200"]
A2000=f1["2000"]



A2000n=[-term for term in A2000]
A1800n=[-term for term in A1800]
A1600n=[-term for term in A1600]
A1400n=[-term for term in A1400]
A1500n=[-term for term in A1500]
A1200n=[-term for term in A1200]
A1300n=[-term for term in A1300]
A1100n=[-term for term in A1100]
A1000n=[-term for term in A1000]
A900n=[-term for term in A900]
A800n=[-term for term in A800]
A600n=[-term for term in A600]
A400n=[-term for term in A400]
A500n=[-term for term in A500]
A300n=[-term for term in A300]
A700n=[-term for term in A700]

F=[]
for i in range(0,len(A180)):
    F.append(0)

#col1 = "Real"
#col2 = "Imaginary"
#data = pd.DataFrame({col1:A60,col2:A600})
#data.to_excel('60 Exp data t.xlsx', sheet_name='sheet1', index=False)


#fig, ax = plt.subplots()
fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.plot(A70, A700n,'o', c='blue',label='70')
#ax.plot(A80, A800n,'o', c='green',label='80')
#ax.plot(A60, A600n,'o', c='violet',label='60')
#ax.plot(A50, A500n,'o', c='red',label='50')
#ax.plot(A40, A400n,'o', c='indigo',label='40')
#ax.plot(A40,A400n,'o',label='40',markerfacecolor='white',markersize=8,markeredgecolor="orangered")
#ax.plot(A50,A500n,'o',label='50',markerfacecolor='white',markersize=8,markeredgecolor="teal")
#ax.plot(A60,A600n,'o',label='60',markerfacecolor='white',markersize=8,markeredgecolor="grey")
#ax.plot(A70,A700n,'o',label='70',markerfacecolor='white',markersize=8,markeredgecolor="saddlebrown")
#ax.plot(A80,A800n,'o',label='80',markerfacecolor='white',markersize=8,markeredgecolor="magenta")


#ax.plot(A30, A300n,'o', c='orange',label='30')
#ax.plot(A90, A900n,'o',c='blue',label='90')

#ax.plot(A200, A2000n,'o-','blue',label='200')
#ax.plot(A180, A1800n,'o',c='green',label='180')
#ax.plot(A160, A1600n,'o', c='violet',label='160')
#ax.plot(A140, A1400n,'o', c='pink',label='140')
#ax.plot(A120, A1200n,'o', c='pink',label='120')
#ax.plot(A100, A1000n,'o', c="red",label='100')
#ax.plot(A90, A900n,'o',c='blue',label='90')
#ax.plot(Zdn,Zddn,'black')
#plt.xlim([0,10000])
#plt.ylim([0,5000])
#plt.show()




def realpart(R,Rx,Lx,C,f):
    omega=2*(22/7)*f
    A=((Rx/(Rx**2+(omega*Lx)**2))+(1/R))
    B=((omega*C)-((omega*Lx)/(Rx**2+(omega*Lx)**2)))
    T=A/(A**2+B**2)
    return(T)
def imgpart(R,Rx,Lx,C,f):
    omega=2*(22/7)*f
    A=((Rx/(Rx**2+(omega*Lx)**2))+(1/R))
    B=((omega*C)-((omega*Lx)/(Rx**2+(omega*Lx)**2)))
    T=-B/(A**2+B**2)
    return(T)

Colours=['orangered','teal','grey','saddlebrown','magenta']
Label=['40','50','60','70','80']
f=pd.Series([np.log(i) for i in range(100,1000000)])
def fitplot(T,a,R,Lx,C,x,c):
    Rx=R*(1-a*(T-30))
    Zd=[]
    Zdd=[]
    for i in range(100,1000000):
        Zd.append(realpart(R,Rx,Lx,C,i))
        Zdd.append(imgpart(R,Rx,Lx,C,i))
    Zddn=[(-term) for term in Zdd]
    Zdn=[((x*term)+850) for term in Zd]
    ax.plot3D(Zdn,f,Zddn,Colours[c],label=Label[c])
    
#    ax.plot(Zdn,Zddn,Colours[c])
#    col1 = "Z''"
#    col2 = "Z'"
#    data = pd.DataFrame({col1:Zddn,col2:Zd})
#    data.to_excel('60 C data.xlsx', sheet_name='sheet1', index=False)




fitplot(80,0.0053,34400,0.005,0.0000000057,1.8,4)
fitplot(70,0.0053,220000,0.004,0.00000001,1.8,3)
fitplot(60,0.0053,420000,0.0041,0.000000009,2.2,2)
fitplot(50,0.0053,750000,0.0043,0.0000000075,2.8,1)
fitplot(40,0.0053,1100000,0.00435,0.0000000055,2.8,0)
#current_values = plt.gca().get_zticks()
#plt.gca().set_zticklabels(['{:.1e}'.format(x) for x in current_values])
#plt.savefig("High resoltion.png",dpi=300)
#fitplot(30,0.0053,700000,0.00438,0.0000000075,2.8)
#fitplot(140,0.0053,17600,0.002,0.000000009,1.22)
#fitplot(100,0.0065,17800,0.0035,0.0000000008,1.22)
#fitplot(90,0.0065,18000,0.005,0.0000000005,1.22)
#fig1, ax1 = plt.subplots()
#ax1.plot(A200, A2000n,'o-','blue',label='200')
#ax1.plot(A180, A1800n,'o',c='green',label='180')
#ax1.plot(A160, A1600n,'o-', c='violet',label='160')
#ax1.plot(A140, A1400n,'o', c='indigo',label='140')
#ax1.plot(A120, A1200n,'o-', c='pink',label='120')
#ax1.plot(A100, A1000n,'o', c="red",label='100')
#ax1.plot(A90, A900n,'o',c='blue',label='90')
#ax.plot(Zdn,Zddn,'black')
ax.view_init(30,290)
ax.set_xlabel("Z'(ohm)")
ax.set_ylabel("Frequency (log f)")
for label in (ax.get_xticklabels() + ax.get_yticklabels() + ax.get_zticklabels()):
	label.set_fontsize(8)
ax.set_zlabel("Z''(ohm)")
#ax.zaxis.set_label_coords(400000,15)
#ax.xaxis.set_label_coords(.9, -.1)
#plt.xlim([0,10000])
#plt.ylim([0,5000])
#plt.show()
plt.savefig("VO2_40_80_3d.png",dpi=3000)
#ax.plot(Zdn,Zddn,'black')
#plt.show()
#plt.xlim([0,50000])
#plt.ylim([0,25000])
#plt.legend()