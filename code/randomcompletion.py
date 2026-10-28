import json, random, time
exec(open("conditioned.py").read().split("res={}")[0])
rng=random.Random(99)
def random_partial(n,k):
    # place k queens on random rows/columns with no two attacking, by random greedy with restarts
    for _ in range(1000):
        rows=rng.sample(range(n),k); cols=list(range(n)); rng.shuffle(cols); placed={}
        ok=True
        for r in rows:
            found=False
            for c in cols:
                if c in placed.values(): continue
                if any(abs(c-pc)==abs(r-pr) for pr,pc in placed.items()): continue
                placed[r]=c; found=True; break
            if not found: ok=False; break
        if ok: return placed
    return None
res={}
n=12
for k in [1,2,3,4,5,6,7]:
    rows=[]; t0=time.time()
    for inst in range(30):
        fixed=random_partial(n,k)
        if fixed is None: continue
        free=[r for r in range(n) if r not in fixed]
        states=enum_completions_le1(n,fixed)
        a=analyse(n,states,free) if states else dict(N0=0,N1=0,comps_with_sol=0,largest_sol=0)
        rows.append(a)
    sat=[r for r in rows if r['N0']>0]
    frac=[r['largest_sol']/r['N0'] for r in sat]
    res[k]=dict(inst=len(rows),satisfiable=len(sat),meanN0=sum(r['N0'] for r in sat)/max(1,len(sat)),meancomps=sum(r['comps_with_sol'] for r in sat)/max(1,len(sat)),giant_mean=sum(frac)/max(1,len(frac)),giant_min=min(frac) if frac else None,
               multi=sum(1 for r in sat if r['comps_with_sol']>1))
    print(k,res[k],round(time.time()-t0),flush=True)
json.dump(res,open("randomcompletion.json","w"))
