import json,time,random
exec(open("conditioned.py").read().split("res={}")[0])
rng=random.Random(5)
res={}
for n,k,ninst in [(14,2,8),(15,3,8),(16,4,6),(17,5,6)]:
    rows=[]; t0=time.time()
    for inst in range(ninst):
        sol=find_solution(n); fixrows=rng.sample(range(n),k); fixed={r:sol[r] for r in fixrows}
        free=[r for r in range(n) if r not in fixed]
        states=enum_completions_le1(n,fixed); a=analyse(n,states,free); rows.append(a)
        if time.time()-t0>400: break
    res[f"{n}_{k}"]=rows
    frac=[r['largest_sol']/r['N0'] for r in rows if r['N0']>0]
    print(n,k,"inst",len(rows),"mean N0",round(sum(r['N0'] for r in rows)/len(rows)),"mean N1",round(sum(r['N1'] for r in rows)/len(rows)),"mean comps",round(sum(r['comps_with_sol'] for r in rows)/len(rows),2),"mean giant",round(sum(frac)/len(frac),3),"min giant",round(min(frac),3),"secs",round(time.time()-t0),flush=True)
json.dump(res,open("conditioned2.json","w"))
