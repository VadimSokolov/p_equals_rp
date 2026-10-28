import json, math, random, time, itertools
from collections import deque
import numpy as np
rng=random.Random(21)
def energy(p):
    n=len(p); c=0
    for i in range(n):
        for j in range(i+1,n):
            if abs(p[i]-p[j])==j-i: c+=1
    return c
def solutions(n):
    out=[]; x=[0]*n; used=[False]*n
    def rec(i):
        if i==n: out.append(tuple(x)); return
        for c in range(n):
            if used[c]: continue
            if any(abs(x[j]-c)==i-j for j in range(i)): continue
            x[i]=c; used[c]=True; rec(i+1); used[c]=False
    rec(0); return out
def swap_energy(p,i,j):
    q=list(p); q[i],q[j]=q[j],q[i]; e=0
    n=len(p)
    for k in range(n):
        if k!=i and abs(q[i]-q[k])==abs(i-k): e+=1
        if k!=j and abs(q[j]-q[k])==abs(j-k): e+=1
    if abs(q[i]-q[j])==abs(i-j): e-=1  # counted twice
    return e
# 1. repair neighbourhood
rep={}
for n in range(6,13):
    sols=solutions(n); counts=[]; t0=time.time()
    for p in sols:
        c=sum(1 for i in range(n) for j in range(i+1,n) if swap_energy(p,i,j)<=1)
        counts.append(c)
    counts=np.array(counts); tot=n*(n-1)//2
    rep[n]=dict(Q=len(sols),mean=float(counts.mean()),min=int(counts.min()),max=int(counts.max()),frac=float(counts.mean()/tot),zero=int((counts==0).sum()),secs=time.time()-t0)
    print("repair",n,rep[n],flush=True)
json.dump(rep,open("repair.json","w"))
# 3. physics transition from exact dos
dos=json.load(open("dos.json"))
trans={}
for n in [8,9,10,11]:
    d={int(k):v for k,v in dos[str(n)].items()}
    betas=np.linspace(0,3,601); best=None; vals=[]
    for b in betas:
        w=np.array([d[s]*math.exp(-b*s) for s in sorted(d)]); ss=np.array(sorted(d))
        Z=w.sum(); m=(w*ss).sum()/Z; v=(w*ss*ss).sum()/Z-m*m; vals.append(v)
        if best is None or v>best[1]: best=(b,v,m)
    trans[n]=dict(beta_c=float(best[0]),var_max=float(best[1]),mean_at=float(best[2]),var_curve=[float(x) for x in vals[::20]])
    print("transition",n,best)
json.dump(trans,open("transition.json","w"))
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6,3.4))
for n in [8,9,10,11]:
    d={int(k):v for k,v in dos[str(n)].items()}; ss=np.array(sorted(d)); cnt=np.array([d[s] for s in ss])
    betas=np.linspace(0,3,301); vs=[]
    for b in betas:
        w=cnt*np.exp(-b*ss); Z=w.sum(); m=(w*ss).sum()/Z; vs.append(((w*ss*ss).sum()/Z-m*m)/n)
    ax.plot(betas,vs,label='$N=%d$'%n)
ax.set_xlabel('inverse temperature $1/\\gamma$'); ax.set_ylabel('$\\mathrm{Var}(S)/N$'); ax.set_title('Energy fluctuations of the queens Boltzmann model'); ax.legend(fontsize=8)
plt.tight_layout(); plt.savefig('fig_transition.pdf')
