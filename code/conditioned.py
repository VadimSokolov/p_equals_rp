import random, json, time, math
from collections import deque
rng=random.Random(11)
def energy(p):
    n=len(p); c=0
    for i in range(n):
        for j in range(i+1,n):
            if abs(p[i]-p[j])==j-i: c+=1
    return c
def find_solution(n):
    # backtracking with random order
    x=[-1]*n; used=[False]*n
    def rec(i):
        if i==n: return True
        cols=list(range(n)); rng.shuffle(cols)
        for c in cols:
            if used[c]: continue
            if any(abs(x[j]-c)==i-j for j in range(i)): continue
            x[i]=c; used[c]=True
            if rec(i+1): return True
            used[c]=False
        return False
    rec(0); return x
def enum_completions_le1(n,fixed):
    # fixed: dict row->col. enumerate full permutations consistent with fixed, with at most 1 attacking pair overall
    x=[-1]*n; used=[False]*n
    for r,c in fixed.items(): x[r]=c; used[c]=True
    base=0
    fr=sorted(fixed)
    for a in range(len(fr)):
        for b in range(a+1,len(fr)):
            if abs(fixed[fr[a]]-fixed[fr[b]])==fr[b]-fr[a]: base+=1
    if base>1: return []
    out=[]
    free=[r for r in range(n) if r not in fixed]
    def rec(k,conf):
        if k==len(free): out.append(tuple(x)); return
        i=free[k]
        for c in range(n):
            if used[c]: continue
            add=0
            for j in range(n):
                if x[j]>=0 and j!=i and abs(x[j]-c)==abs(i-j):
                    add+=1
                    if conf+add>1: break
            if conf+add>1: continue
            x[i]=c; used[c]=True; rec(k+1,conf+add); x[i]=-1; used[c]=False
    rec(0,base); return out
def analyse(n,states,free):
    idx={s:i for i,s in enumerate(states)}
    seen=[False]*len(states); comps=[]
    for s0 in range(len(states)):
        if seen[s0]: continue
        q=deque([s0]); seen[s0]=True; size=0; sols=0
        while q:
            u=q.popleft(); size+=1; p=states[u]
            if energy(p)==0: sols+=1
            for a in range(len(free)):
                for b in range(a+1,len(free)):
                    i,j=free[a],free[b]
                    r=list(p); r[i],r[j]=r[j],r[i]; v=idx.get(tuple(r))
                    if v is not None and not seen[v]: seen[v]=True; q.append(v)
        comps.append((size,sols))
    n0=sum(s for _,s in comps); n1=len(states)-n0
    withsol=[s for _,s in comps if s>0]
    return dict(N0=n0,N1=n1,comps_with_sol=len(withsol),largest_sol=max(withsol) if withsol else 0)
res={}
n=13
for k in [2,4,6,8]:
    rows=[]
    t0=time.time()
    for inst in range(12):
        sol=find_solution(n)
        fixrows=rng.sample(range(n),k)
        fixed={r:sol[r] for r in fixrows}
        free=[r for r in range(n) if r not in fixed]
        states=enum_completions_le1(n,fixed)
        a=analyse(n,states,free); rows.append(a)
    res[k]=rows
    frac=[r['largest_sol']/r['N0'] for r in rows if r['N0']>0]
    print(k, "instances",len(rows),"mean N0",sum(r['N0'] for r in rows)/len(rows),"mean comps",sum(r['comps_with_sol'] for r in rows)/len(rows),"mean giant frac",sum(frac)/len(frac) if frac else None,"min giant frac",min(frac) if frac else None, "secs",round(time.time()-t0),flush=True)
json.dump(res,open("conditioned.json","w"))
