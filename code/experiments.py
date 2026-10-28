import math, json, random, itertools
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
rng=random.Random(1)

def energy(p):
    n=len(p); c=0
    for i in range(n):
        for j in range(i+1,n):
            if abs(p[i]-p[j])==j-i: c+=1
    return c
def delta_energy(p,i,j):
    # energy change from swapping positions i,j
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

def levelset_chain(p,e,m,steps):
    """swap Metropolis chain uniform on {S<=m}"""
    n=len(p)
    for _ in range(steps):
        i,j=rng.sample(range(n),2)
        d=delta_energy(p,i,j)
        if e+d<=m:
            p[i],p[j]=p[j],p[i]; e+=d
    return p,e

def split_count(n,rho=0.3,M=400,sweeps=4):
    # product estimator with quantile ladder
    pop=[]
    for _ in range(M):
        p=list(range(n)); rng.shuffle(p); pop.append((p,energy(p)))
    logZ=0.0; m=10**9; ladder=[]
    while True:
        es=sorted(e for _,e in pop)
        k=int(rho*M)
        mnew=es[k-1]
        if mnew==m: mnew=m-1
        if mnew<0: mnew=0
        frac=sum(1 for e in es if e<=mnew)/M
        logZ+=math.log(frac); ladder.append((mnew,frac))
        if mnew==0: break
        elite=[(list(p),e) for p,e in pop if e<=mnew]
        pop=[]
        for i in range(M):
            p,e=elite[i%len(elite)]
            p,e=levelset_chain(list(p),e,mnew,sweeps*n)
            pop.append((p,e))
        m=mnew
    return logZ,ladder

sol={4:2,5:10,6:4,7:40,8:92,9:352,10:724,11:2680,12:14200,13:73712,14:365596,15:2279184,16:14772512}
results={}
for n in [8,10,12,14,16]:
    ests=[]
    for rep in range(10):
        logZ,ladder=split_count(n)
        ests.append(math.exp(logZ)*math.factorial(n))
    ests=np.array(ests)
    results[n]=dict(mean=float(ests.mean()),sd=float(ests.std()),exact=sol[n],ladder=ladder,
                    rel=float(ests.mean()/sol[n]),cv=float(ests.std()/ests.mean()))
    print(n, results[n]['mean'], results[n]['sd'], sol[n], results[n]['rel'], len(ladder))
json.dump(results,open("split_results.json","w"))

# figure: estimates vs exact
fig,ax=plt.subplots(figsize=(6,3.4))
ns=sorted(results)
ax.errorbar(ns,[results[n]['mean'] for n in ns],yerr=[results[n]['sd'] for n in ns],fmt='o',color='#c0392b',capsize=3,label='split sampling estimate (10 runs)')
ax.plot(ns,[sol[n] for n in ns],'k-',label='exact $Q(N)$')
ax.set_yscale('log'); ax.set_xlabel('$N$'); ax.set_ylabel('$Q(N)$'); ax.legend(fontsize=8)
ax.set_title('Vertical ladder estimates of $Q(N)$')
plt.tight_layout(); plt.savefig('fig_split.pdf')

# figure: ladder for n=14, log Z_m vs level
fig,ax=plt.subplots(figsize=(6,3.4))
for n in [10,14,16]:
    lad=results[n]['ladder']
    ms=[l[0] for l in lad]; cum=np.cumsum([math.log(l[1]) for l in lad])
    ax.plot(ms,cum,'o-',label=f'$N={n}$')
ax.set_xlabel('level $m$ (attacking pairs)'); ax.set_ylabel('$\\log \\hat Z_m$')
ax.set_title('The vertical ladder: estimated $\\log Z_m$ by level')
ax.legend(fontsize=8); plt.tight_layout(); plt.savefig('fig_ladder.pdf')

# Wang Landau density of states for n=10 vs exact
n=10
exact={}
for p in itertools.permutations(range(n)):
    e=energy(p); exact[e]=exact.get(e,0)+1
K=max(exact)
logg=np.zeros(K+1); H=np.zeros(K+1); lf=1.0
p=list(range(n)); rng.shuffle(p); e=energy(p)
it=0
while lf>1e-6 and it<60:
    H[:]=0
    for _ in range(20000*(it+1)):
        i,j=rng.sample(range(n),2); d=delta_energy(p,i,j); e2=e+d
        if e2<=K and math.log(rng.random())< logg[e]-logg[e2]:
            p[i],p[j]=p[j],p[i]; e=e2
        logg[e]+=lf; H[e]+=1
    visited=H>0
    if H[visited].min()>0.8*H[visited].mean():
        lf/=2; it+=1
    it+=0
levels=sorted(exact)
est=np.exp(logg-logg.max()); est=est/est.sum()*math.factorial(n)
fig,ax=plt.subplots(figsize=(6,3.4))
ax.semilogy(levels,[exact[l] for l in levels],'ko-',label='exact $N(s)$')
ax.semilogy(levels,[est[l] for l in levels],'rs--',label='Wang Landau estimate')
ax.set_xlabel('energy $s$'); ax.set_ylabel('$N(s)$'); ax.set_title('Density of states, $N=10$'); ax.legend(fontsize=8)
plt.tight_layout(); plt.savefig('fig_wl10.pdf')
print("WL N(0) est",est[0],"exact",exact[0],"levels",len(levels))
json.dump({"exact":{str(k):v for k,v in exact.items()},"est":{str(l):float(est[l]) for l in levels}},open("wl10.json","w"))
