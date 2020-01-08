# import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

#INPUT
T=298.15
G=1000

#PARAMETER
Iscn=8.21
Ipvn=Iscn
Ki=3.18*0.001
Kv=-0.123
Vocn=32.9
a=1.2
Ns=54
Np=1
Tn=298.15
Rs=0.221
Rp=415.405
k=1.38*(10**-23)
q=1.6*(10**-19)
Vt=Ns*(k*T/q)
#Vt=Ns*8.61*(10**-5)
Io=(Iscn + Ki * (T - Tn)) / (-1.0 + np.exp((Vocn + Kv * (T-Tn)) / (Vt * a)))   

li,lv=[],[]
#ITERATION TO IMPOSE THE VOLTAGE VALUE
for V in np.arange(0,Vocn,0.1): 
    x=V+Rs*1 #FIRST, I use "x" to subtite the term (V+Rs*I) and assume that the current I=1 A. 
    #EQUATION
    Ipv=0.001*(Ipvn+Ki*(T - Tn))*G

    #Id=I0 * (np.exp((V + Rs * I) / (Vt * a))-1)
    Id=Io * (np.exp((x) / (Vt * a))-1)

    #Ir=(V + Rs * I) / Rp
    Ir=x/Rp

    #Ix=-Np*(Ipv-Id-Ir)
    Ix=Np*(Ipv-Id-Ir) #SECOND, I calculate the value of I(x)

    #x=V+(Rs*I)
    Vx=x-Rs*Ix #THIRD, I calculate the value of voltage V(x)
    
    #OUTPUT
    if Vx<0:
        I=Vx*Np/(Rs+Rp)
    elif Vx>Vocn:
        I=0
    else:
        I=Ix
    lv.append(Vx)
    li.append(I)

#PLOT VALUE
plt.plot(lv, li)
plt.xlabel('Current (A)')
plt.ylabel('Voltage (V)')
plt.title('Voltage VS Current at T=298K and G=1000W/m2')
plt.show()

lp=np.multiply(lv,li)
plt.plot(lv, lp)
plt.xlabel('Voltage (V)')
plt.ylabel('Power (W)')
plt.title('Power VS Voltage at T=298K and G=1000W/m2')
plt.show()
