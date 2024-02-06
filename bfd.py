import numpy as np
import matplotlib.pyplot as plt
rs=np.linspace(3.445,3.60,2000)
N=500
x=.5+np.zeros(N)
endcap=np.arange(round(N*.9),N)
for ri in range(len(rs)):
    for n in range(N-1):
        x[n+1]=rs[ri]*x[n]*(1-x[n]) 
    u=np.unique(x[endcap])
    r=rs[ri]*np.ones(len(u))
    plt.xlabel('r')
    plt.ylabel('Population')
    plt.title('Bifurcation Diagram - Logistic Map {close up}')
    plt.plot(r,u,'.',markersize=1,color=[(np.sin(ri/len(rs)/2)+1)/2,1-ri/len(rs),.5])

plt.show()
