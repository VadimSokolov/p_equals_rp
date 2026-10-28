import math, random, json, time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
rng=random.Random(7)

def energy(p):
    n=len(p); c=0
    for i in range(n):
        for j in range(i+1,n):
            if abs(p[i]-p[j])==j-i: c+=1
    return c
def delta_energy(p,i,j):
    n=len(p); old=0; new=0
    q=list(p); q[i],q[j]=q[j],q[i]
    for k in range(n):
        if k!=i and k!=j:
            if abs(p[i]-p[k])==abs(i-k): old+=1
            if abs(p[j]-p[k])==abs(j-k): old+=1
            if abs(q[i]-q[k])==abs(i-k): new+=1
            if abs(q[j]-q[k])==abs(j-k): new+=1
    if abs(p[i]-p[j])==abs(i-j): old+=1
    if abs(q[i]-q[j])==abs(i-j): new+=1
    return new-old

def find_solution(n):
    # min conflicts heuristic
    p=list(range(n)); rng.shuffle(p); e=energy(p)
    while e>0:
        i,j=rng.sample(range(n),2); d=delta_energy(p,i,j)
        if d<=0 or rng.random()<0.05:
            p[i],p[j]=p[j],p[i]; e+=d
    return p

def run_chain(p,e,m,steps,stat):
    n=len(p); out=[]
    for _ in range(steps):
        i,j=rng.sample(range(n),2); d=delta_energy(p,i,j)
        if e+d<=m:
            p[i],p[j]=p[j],p[i]; e+=d
        out.append(stat(p))
    return out

def iat(x):
    x=np.array(x,float); x-=x.mean(); v=x.var()
    if v==0: return float('inf')
    n=len(x); tau=1.0
    for k in range(1,n//4):
        c=np.dot(x[:-k],x[k:])/((n-k)*v)
        if c<0.02: break
        tau+=2*c
    return tau

res={}
for n in [8,10,12,14,16,18,20,24,28,32]:
    t0=time.time()
    stat=lambda p: p[0]  # column of first row queen
    taus=[]; frac0=[]
    for rep in range(6):
        p=find_solution(n); e=0
        steps=4000*n
        xs=run_chain(p,e,1,steps,lambda q:(q[0],energy(q)==0 if False else None))
        cols=[x[0] for x in xs]
        taus.append(iat(cols))
    # fraction of time at energy 0 within level set {S<=1}: separate run
    p=find_solution(n); e=0; z=0; steps=2000*n
    for _ in range(steps):
        i,j=rng.sample(range(n),2); d=delta_energy(p,i,j)
        if e+d<=1:
            p[i],p[j]=p[j],p[i]; e+=d
        z+= (e==0)
    res[n]=dict(iat_mean=float(np.mean(taus)),iat_sd=float(np.std(taus)),frac0=z/steps,secs=time.time()-t0)
    print(n,res[n],flush=True)
json.dump(res,open("mixing_results.json","w"))
ns=sorted(res)
fig,ax=plt.subplots(1,2,figsize=(8,3.3))
ax[0].errorbar(ns,[res[n]['iat_mean'] for n in ns],yerr=[res[n]['iat_sd'] for n in ns],fmt='o-',color='#1f4e79',capsize=3)
ax[0].set_yscale('log'); ax[0].set_xlabel('$N$'); ax[0].set_ylabel('integrated autocorrelation time (swaps)')
ax[0].set_title('Bottom rung chain on $\\{S \\le 1\\}$')
ax[1].plot(ns,[res[n]['frac0'] for n in ns],'s-',color='#c0392b')
ax[1].set_xlabel('$N$'); ax[1].set_ylabel('fraction of time at $S=0$'); ax[1].set_yscale('log')
ax[1].set_title('$\\hat Z_0 / \\hat Z_1$ from the bottom rung')
plt.tight_layout(); plt.savefig('fig_mixing.pdf')
