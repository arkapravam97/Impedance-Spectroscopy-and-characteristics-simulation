# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 09:48:02 2022

@author: Arkaprava Mondal
"""


import matplotlib.pyplot as plt
T=[30,40,50,60,70,80,90,100,140,160,180]
R=[1120000,1100000,750000,420000,220000,34400,18000,17800,17600,17300,17200]
Rx=[1120000,1041700,670500,353220,173360,25284,10980,9701,7447.20,6842.15,6880]
Lx=[0.0438,0.0435,0.043,0.041,0.04,0.005,0.005,0.0035,0.002,0.0015,0.001]
C=[0.0000000035,0.0000000055,0.0000000075,0.000000009,0.00000001,0.000000057,0.000000055,0.000000057,0.00000008,0.00000009,0.0000001]
a=[0.0053,0.0053,0.0053,0.0053,0.0053,0.0053,0.0053,0.0053,0.0052,0.00465,0.004]


Tp=[100,150,200,250,300,400]
Rp=[1210000,340000,170000,100000,720,580]
Rxp=[1040600.0,258400.0,112199.99999999999,56000.00000000001,331.2,150.8]
Lxp=[0.05,0.042,0.04,0.03,0.0006,0.0004]
Cp=[0.00000000001,0.000000000018,0.0000000002,0.0000000025,0.0000003,0.0000004]
ap=[0.002,0.002,0.002,0.002,0.002,0.002]

Tt=[25,35,45,60,80,100,110]
Rt=[920000,730000,480000,219000,125000,78000,60000]
Rxt=[920000.0,719050.0,465600.0,207502.5,114687.5,69225.0,52350.0]
Lxt=[0.051,0.05,0.042,0.008,0.004,0.003,0.0025]
Ct=[0.000000001,0.0000000013,0.0000000051,0.00000001,0.000000013,0.0000000135,0.00000002]
at=[0.0015,0.0015,0.0015,0.0015,0.0015,0.0015,0.0015,]

def populate(X):
    X1=[]
    for i in range(0,len(X)-1):
        X1.append(X[i])
        res=(X[i+1]-X[i])/5
        for j in range(1,5):
            X1.append(X[i]+res*j)
    return(X1)

T1=populate(T)
R1=populate(R)
Rx1=populate(Rx)
Lx1=populate(Lx)
C1=populate(C)
a1=populate(a)

Tp1=populate(Tp)
Rp1=populate(Rp)
Rxp1=populate(Rxp)
Lxp1=populate(Lxp)
Cp1=populate(Cp)
ap1=populate(ap)

Tt1=populate(Tt)
Rt1=populate(Rt)
Rxt1=populate(Rxt)
Lxt1=populate(Lxt)
Ct1=populate(Ct)
at1=populate(at)

fig1, ax1 = plt.subplots()
ax1.plot(T1,R1,'o-',c='red',markersize=2)
#ax1.plot(Tp1,Rp1,'o-',c='blue',markersize=2)
#ax1.plot(Tt1,Rt1,'o-',c='green',markersize=2)
plt.xlabel('Temperature') 
plt.ylabel('R (logarithm)')
plt.yscale('log')
plt.title("R vs T")
#plt.savefig("VO2_RvsT.png",bbox_inches='tight',dpi=720)





fig2, ax2 = plt.subplots()
ax2.plot(T1,Rx1,'o-',c='red',markersize=2)
#ax2.plot(Tp1,Rxp1,'o-',c='blue',markersize=2)
#ax2.plot(Tt1,Rxt1,'o-',c='green',markersize=2)
plt.xlabel('Temperature') 
plt.ylabel('Rx') 
plt.title("Rx vs T")
plt.yscale('log')
#plt.savefig("TiO2_RvsT.png",bbox_inches='tight',dpi=720)


fig3, ax3 = plt.subplots()
ax3.plot(T1,C1,'o-',c='red',markersize=2)
#ax3.plot(Tp1,Cp1,'o-',c='blue',markersize=2)
#ax3.plot(Tt1,Ct1,'o-',c='green',markersize=2)
plt.xlabel('Temperature') 
plt.ylabel('Capacitance (F)') 
plt.title("C vs T")
#plt.savefig("VO2_CvsT.png",bbox_inches='tight',dpi=720)


fig4, ax4 = plt.subplots()
ax4.plot(T1,Lx1,'o-',c='red',markersize=2)
#ax4.plot(Tp1,Lxp1,'o-',c='blue',markersize=2)
#ax4.plot(Tt1,Lxt1,'o-',c='green',markersize=2)
plt.xlabel('Temperature')
plt.ylabel('Inductance (H)') 
plt.title("L vs T")
#plt.savefig("VO2_LvsT.png",bbox_inches='tight',dpi=720)





#fig5, ax5 = plt.subplots()
#ax5.plot(T1,a1,marker='s',markerfacecolor='lightgreen',markersize=10,markeredgecolor="black")
#plt.xlabel('Temperature') 
#plt.ylabel('Co-efficient of resistance') 
#plt.title("alpha vs T")

