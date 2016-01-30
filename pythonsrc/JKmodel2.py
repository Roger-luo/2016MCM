from numpy import exp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

#constant parameters
alpha=0.05
beta=0.1
person_min=0.02
person_max=0.02*20
ext=0
Wps=1
K=600
lam=0.01


#iteration parameters
P=[500]
W=[100000]
Wc=[100]


dt=0.1
t_max=2000
step=int(t_max/dt)

#middle parameters
def A(Wc,W):
    return Wc/W

def gamma(Wc,P):
    return 1-exp(-Wc/P-person_min)

def Wns(Wc):
    return Wc-alpha*Wc-Wps

#iteration parameters
def P_itter(Pn,gamma):
    return Pn+dt*lam*Pn*(1-Pn/(gamma*K))
def W_itter(Wn,Wnsn,Wcn):
    return Wn+dt*(ext-Wnsn+beta*Wcn)
def Wc_itter(Wcn,Pn,An):
    #return Wcn+dt*An*Pn
    #return Wcn+dt*Pn*((person_max-person_min)*exp(-An/0.01)+person_min)
    return Pn*((person_max-person_min)*exp(-An/0.01)+person_min)
A_ying = []
for i in range(step):
    Pn1 = P_itter(P[-1], gamma(Wc[-1],P[-1]))
    P.append(Pn1)
    Wn1 = W_itter(W[-1], Wns(Wc[-1]), Wc[-1])
    W.append(Wn1)
    A_ying.append(A(Wc[-1],W[-1]))
    Wcn1 = Wc_itter(Wc[-1],P[-1], A(Wc[-1],W[-1]))
    Wc.append(Wcn1)

    if(Wcn1>Wn1):
        break

plt.figure()
plt.subplot(4,1,1)
plt.ylabel("P")
plt.plot(P)
plt.subplot(4,1,2)
plt.ylabel("W")
plt.plot(W)
plt.subplot(4,1,3)
plt.ylabel("Wc")
plt.plot(Wc)
plt.subplot(4,1,4)
plt.ylabel("A")
plt.plot(A_ying)
plt.show()
plt.close()

