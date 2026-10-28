import math, random, json
rng=random.Random(3)
exec(open("conditioned.py").read().split("res={}")[0])
def levelset_chain(p,e,m,steps,free):
    for _ in range(steps):
        i,j=rng.sample(free,2); d=delta_energy(p,i,j)
        if e+d<=m: p[i],p[j]=p[j],p[i]; e+=d
    return p,e
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
def run(n,fixed,M=400,rho=0.3,sweeps=4):
    free=[r for r in range(n) if r not in fixed]
    pop=[]
    for a in range(M):
        cols=[c for c in range(n) if c not in fixed.values()]; rng.shuffle(cols)
        p=[-1]*n
        for r,c in fixed.items(): p[r]=c
        for r,c in zip(free,cols): p[r]=c
        pop.append((p,energy(p),a))  # ancestor id = initial index
    ladder=[]; logZ=0; m=10**9
    while True:
        es=sorted(e for _,e,_ in pop); mnew=es[int(rho*M)-1]
        if mnew==m: mnew=m-1
        if mnew<0: mnew=0
        elite=[(p,e,a) for p,e,a in pop if e<=mnew]
        frac=len(elite)/M; logZ+=math.log(frac)
        anc=len(set(a for _,_,a in elite))
        ladder.append((mnew,round(frac,3),anc))
        if mnew==0: break
        pop=[]
        for i in range(M):
            p,e,a=elite[i%len(elite)]
            p,e=levelset_chain(list(p),e,mnew,sweeps*n,free); pop.append((p,e,a))
        m=mnew
    return ladder
res={}
for n in [10,14,18,22]:
    res[f"u{n}"]=run(n,{}); print("unconditioned",n,res[f"u{n}"],flush=True)
for n,k in [(14,3),(18,5)]:
    sol=find_solution(n); rows=rng.sample(range(n),k); fixed={r:sol[r] for r in rows}
    res[f"c{n}_{k}"]=run(n,fixed); print("conditioned",n,k,res[f"c{n}_{k}"],flush=True)
json.dump(res,open("genealogy.json","w"))
