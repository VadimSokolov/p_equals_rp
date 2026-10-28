import math, json, sys, time
from collections import deque
sys.setrecursionlimit(10000)
# enumerate permutations with at most 1 attacking pair by backtracking
def enum_le1(n):
    out=[]
    x=[0]*n; used=[False]*n
    def rec(i,conf):
        if i==n:
            out.append(tuple(x)); return
        for c in range(n):
            if used[c]: continue
            k=0
            for j in range(i):
                if abs(x[j]-c)==i-j:
                    k+=1
                    if conf+k>1: break
            if conf+k>1: continue
            x[i]=c; used[c]=True
            rec(i+1,conf+k)
            used[c]=False
    rec(0,0)
    return out
def energy(p):
    n=len(p); c=0
    for i in range(n):
        for j in range(i+1,n):
            if abs(p[i]-p[j])==j-i: c+=1
    return c
res={}
for n in range(4,15):
    t0=time.time()
    states=enum_le1(n)
    n0=sum(1 for s in states if energy(s)==0); n1=len(states)-n0
    # components under swaps within S<=1, and components of solutions under swaps through S<=1
    idx={s:i for i,s in enumerate(states)}
    seen=[False]*len(states); comps=0; compsizes=[]; sol_in_comp=[]
    for s0 in range(len(states)):
        if seen[s0]: continue
        comps+=1; q=deque([s0]); seen[s0]=True; size=0; sols=0
        while q:
            u=q.popleft(); size+=1
            p=states[u]
            if energy(p)==0: sols+=1
            for i in range(n):
                for j in range(i+1,n):
                    r=list(p); r[i],r[j]=r[j],r[i]; r=tuple(r)
                    v=idx.get(r)
                    if v is not None and not seen[v]:
                        seen[v]=True; q.append(v)
        compsizes.append(size); sol_in_comp.append(sols)
    # solutions isolated under direct swaps (no swap leads to another solution)
    solset=set(s for s in states if energy(s)==0)
    isolated=0
    for p in solset:
        ok=False
        for i in range(n):
            for j in range(i+1,n):
                r=list(p); r[i],r[j]=r[j],r[i]
                if tuple(r) in solset: ok=True; break
            if ok: break
        if not ok: isolated+=1
    res[n]=dict(N0=n0,N1=n1,ratio=n0/n1 if n1 else None,comps=comps,largest=max(compsizes),
                comps_with_solutions=sum(1 for s in sol_in_comp if s>0),largest_sol=max(sol_in_comp),isolated=isolated,secs=time.time()-t0)
    print(n,res[n],flush=True)
    if time.time()-t0>400: break
json.dump(res,open("openprob.json","w"))
