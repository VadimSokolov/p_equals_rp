import itertools, math, json
from collections import Counter
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def attacks(p):
    n=len(p); c=0
    for i in range(n):
        for j in range(i+1,n):
            if abs(p[i]-p[j])==j-i: c+=1
    return c

res={}
for n in range(4,10):
    cnt=Counter()
    for p in itertools.permutations(range(n)):
        cnt[attacks(p)]+=1
    res[n]=dict(sorted(cnt.items()))
    print(n, math.factorial(n), cnt[0], dict(sorted(cnt.items())))
json.dump(res, open("dos.json","w"))

# Figure 1: density of states for n=8 and Lambda(s)
n=8; d=res[8]; tot=math.factorial(8)
ss=sorted(d); counts=[d[s] for s in ss]
fig,ax=plt.subplots(1,2,figsize=(8,3.2))
ax[0].bar(ss,counts,color="#1f4e79")
ax[0].set_xlabel("attacking pairs $s$"); ax[0].set_ylabel("number of permutations $N(s)$")
ax[0].set_title("Density of states, $N=8$")
# Lambda(u): likelihood L = exp(-S); Lambda(u)=value y such that fraction u of draws have L>y
cum=np.cumsum(counts)/tot
u=np.concatenate([[0],cum]); 
xs=[];ys=[]
for k,s in enumerate(ss):
    xs+= [u[k],u[k+1]]; ys+=[math.exp(-s)]*2
ax[1].plot(xs,ys,color="#c0392b",lw=2)
ax[1].set_yscale("log"); ax[1].set_xlabel("$u$"); ax[1].set_ylabel("$\\Lambda(u)=e^{-s}$")
ax[1].set_title("Lorenz quantile curve $\\Lambda$, $N=8$")
plt.tight_layout(); plt.savefig("fig_dos8.pdf")

# Figure 2: rarity
sol=[1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596,2279184]
alpha=1.942
ns=list(range(1,16))
ratio=[sol[i]/math.factorial(ns[i]) for i in range(15)]
fig,ax=plt.subplots(figsize=(6,3.4))
nn=[k for k in ns if sol[k-1]>0]
ax.plot(nn,[math.log10(sol[k-1]/math.factorial(k)) for k in nn],"o-",color="#1f4e79",label="$\\log_{10}(Q(N)/N!)$ exact")
ax.plot(nn,[math.log10(sol[k-1]/k**k) for k in nn],"s-",color="#c0392b",label="$\\log_{10}(Q(N)/N^N)$ exact")
ax.plot(nn,[k*(math.log10(k)-alpha/math.log(10))-math.log10(math.factorial(k)) for k in nn],"--",color="gray",label="Simkin $((1+o(1))Ne^{-\\alpha})^N/N!$")
ax.set_xlabel("$N$"); ax.set_ylabel("log probability"); ax.legend(fontsize=8)
ax.set_title("Solutions are rare events")
plt.tight_layout(); plt.savefig("fig_rarity.pdf")

# Figure 3: product estimator on n=8 using exact level set probabilities
d=res[8]; ss=sorted(d); tot=math.factorial(8)
Zm=[sum(d[s] for s in ss if s<=m)/tot for m in ss]
print("Z(m)",list(zip(ss,[round(z,6) for z in Zm])))
ratios=[Zm[i]/Zm[i+1] for i in range(len(Zm)-1)]
print("ratios",ratios)
