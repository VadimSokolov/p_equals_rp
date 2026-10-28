import numpy as np, math, json
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
pages=251; spine=pages*0.002252; bleed=0.125; W=2*(6+bleed)+spine; H=9+2*bleed
fig=plt.figure(figsize=(W,H),dpi=300)
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,W); ax.set_ylim(0,H); ax.axis('off')
bg='#0b1a2e'; accent='#e8c547'; ink='#f2efe6'
ax.add_patch(Rectangle((0,0),W,H,color=bg))
# front cover region
fx0=bleed+6+spine
# chessboard with 8 queens solution, lower part of front
sol=[5,3,6,0,7,1,4,2]  # rows bottom to top columns
bx=fx0+0.55; by=bleed+1.05; cell=0.40
for r in range(8):
    for c in range(8):
        col='#1f3a5f' if (r+c)%2==0 else '#dfe6ee'
        ax.add_patch(Rectangle((bx+c*cell,by+r*cell),cell,cell,color=col,lw=0))
for r,c in enumerate(sol):
    ax.text(bx+c*cell+cell/2,by+r*cell+cell/2,'♛',ha='center',va='center',fontsize=17,color=accent if (r+c)%2==0 else '#0b1a2e',fontname='DejaVu Sans')
ax.add_patch(Rectangle((bx,by),8*cell,8*cell,fill=False,ec=accent,lw=2))
# staircase (Lorenz quantile) drawn to the right of board on front, as a glowing step function
dos=json.load(open('dos.json'))['8']; d={int(k):v for k,v in dos.items()}; tot=sum(d.values())
ss=sorted(d); u=0; xs=[]; ys=[]
sx=bx+8*cell+0.4; sw=6-0.55-8*cell-0.4-0.5; sy=by; sh=8*cell
for sdx in ss:
    w=d[sdx]/tot
    xs+= [sx+u*sw, sx+(u+w)*sw]; ys+=[sy+sh*math.exp(-sdx/6)]*2; u+=w
ax.plot(xs,ys,color=accent,lw=2.5)
ax.fill_between(xs,sy,ys,color=accent,alpha=0.15)
ax.text(sx+sw/2,sy-0.3,'$Z=\\int_0^1 \\Lambda(s)\\,ds$',ha='center',va='top',fontsize=12,color=ink)
# title
ax.text(fx0+3,H-bleed-1.3,'P = RP',ha='center',va='center',fontsize=64,color=ink,fontweight='bold')
ax.text(fx0+3,H-bleed-2.35,'A Monte Carlo Program for P versus NP',ha='center',va='center',fontsize=19,color=accent,style='italic')
ax.plot([fx0+0.9,fx0+5.1],[H-bleed-2.85,H-bleed-2.85],color=accent,lw=1)
ax.text(fx0+3,H-bleed-3.3,'Nick Polson   ·   Vadim Sokolov',ha='center',va='center',fontsize=20,color=ink)
ax.text(fx0+3,H-bleed-3.85,'Vertical likelihood, counting N queens,\nand the complexity of randomness',ha='center',va='center',fontsize=12,color=ink,alpha=0.85)
# spine
sx0=bleed+6
ax.text(sx0+spine/2,H/2,'P = RP     Polson and Sokolov',rotation=270,ha='center',va='center',fontsize=14,color=ink)
# back cover
bx0=bleed
blurb=("Gauss asked how many ways N queens can be placed on an N by N board so that no two attack. "
"The question looks like a puzzle. It is a window on the central problem of computer science. "
"Counting the queens is #P complete, completing a board is NP complete, and every Monte Carlo method ever "
"proposed for such problems is, in the end, a walk down a single staircase on the unit interval: the quantile "
"function of the likelihood, the Lorenz curve of the count.\n\n"
"This book sets out that observation as a program. It proves that the question whether NP = RP is exactly the "
"question whether a swap chain on a chessboard mixes in polynomial time; it restates P = RP as the problem of "
"hitting a dense level set without a coin; it gives Yakowitz type bounds, higher order and stratified rules, and "
"generative Bayesian computation as the practical machinery; and it reports experiments and exact computations on the "
"queens, including the giant component of solutions and the finite size correction to Simkin's constant.\n\n"
"From Hilbert and Turing through Shannon and von Neumann to Jerrum, Sinclair and Impagliazzo, the authors trace "
"what is known, state what is conjectured, and leave the reader at the exact place where the next theorem must be proved.")
import textwrap
y=H-bleed-1.0
for para in blurb.split("\n\n"):
    for line in textwrap.wrap(para,70):
        ax.text(bx0+0.7,y,line,ha='left',va='top',fontsize=10,color=ink); y-=0.23
    y-=0.2
ax.text(bx0+0.7,bleed+1.75,'Nick Polson is the Robert Law Jr. Professor of Econometrics and Statistics\nat the University of Chicago Booth School of Business.\nVadim Sokolov is Associate Professor of Operations Research\nat George Mason University.',ha='left',va='bottom',fontsize=10,color=accent)
# barcode placeholder box (KDP adds its own barcode at lower right of back)
ax.add_patch(Rectangle((bx0+6-0.25-2.0,bleed+0.25),2.0,1.2,color='white'))
fig.savefig('cover_wrap.pdf'); fig.savefig('cover_wrap.png',dpi=120)
print(W,H,spine)
