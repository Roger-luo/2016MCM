from numpy import exp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

alpha=0.05
beta=0.1
person_min=0.001
person_max=0.001*200
sigma=person_max-person_min
A0=0.001
ext=0.1
const=0.1
K=600
lam=0.01

P_init=500
W_init=1000

dt=0.1
t_max=5000
step=int(t_max/dt)

def gamma(A):
    return 1-exp(-(person_max-person_min)*exp(-A/A0)/sigma)

def Wc(P,A):
    return P*((person_max-person_min)*exp(-A/A0)+person_min)

def A(W,Wc):
    return Wc/W

def P_iter(P,gamma,dt,lam):
    return P+dt*lam*(1-P/(K))
    #return P+dt*lam*(1-P/(K*gamma))

def W_iter(W,Wc):
    return W+dt*(ext+const-(1-alpha-beta)*Wc)

def solve_A_Wc(P,W):
    def func(x):
        A=x[0]
        Wc=x[1]
        return [P*((person_max-person_min)*exp(-A/A0)+person_min), (Wc/W)-A]
    return fsolve(func, [A0, 1])

def iter(P,W):
    A,Wc = solve_A_Wc(P,W);
    return [P_iter(P,gamma(A),dt,lam), W_iter(W, Wc)]

ts=[i*dt for i in range(step)]
Ps=[P_init]
Ws=[W_init]

for i in range(step-1):
    PW=iter(Ps[-1],Ws[-1])
    Ps.append(PW[0])
    Ws.append(PW[1])

plt.figure(1)
plt.plot(ts, Ps)
plt.show()

plt.figure(2)
plt.plot(ts, Ws)
plt.show()
