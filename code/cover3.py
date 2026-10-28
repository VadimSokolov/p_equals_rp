import numpy as np, math, json, textwrap, sys
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle
from matplotlib.collections import PolyCollection
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patheffects as pe
PAGES=337
if len(sys.argv)>1: PAGES=int(sys.argv[1])
TW,TH=7.0,10.0; k=TW/6; kv=TH/9
spine=PAGES*0.002252; bleed=0.125; W=2*(TW+bleed)+spine; H=TH+2*bleed
fig=plt.figure(figsize=(W,H),dpi=300)
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,W); ax.set_ylim(0,H); ax.axis('off')
# background: vertical gradient navy to near black
cm=LinearSegmentedColormap.from_list('bg',['#050b16','#0e2240','#132d52'])
NS=500; ee=np.linspace(0,H,NS+1)
ax.add_collection(PolyCollection([[(0,ee[i]),(W,ee[i]),(W,ee[i+1]+0.004),(0,ee[i+1]+0.004)] for i in range(NS)],facecolors=[cm((i+.5)/NS) for i in range(NS)],edgecolors='none',linewidths=0,zorder=0))
gold='#e4b94a'; ink='#f3efe4'
fx0=bleed+TW+spine
# perspective board
def persp(c,r,n=8):
    # map board coords (c,r) in [0,n] to page; bottom edge wide, top narrow
    cx=fx0+2.05*k; base_y=bleed+1.75*kv; side=3.4*k
    return (cx-side/2+side*(c/n), base_y+side*(r/n))
light='#e9e2d0'; dark='#2b4a73'
polys=[]; cols=[]
for r in range(8):
    for c in range(8):
        quad=[persp(c,r),persp(c+1,r),persp(c+1,r+1),persp(c,r+1)]
        polys.append(quad); cols.append(light if (r+c)%2 else dark)
ax.add_collection(PolyCollection(polys,facecolors=cols,edgecolors='#0a1526',linewidths=0.45,zorder=2))
# board rim
rim=[persp(0,0),persp(8,0),persp(8,8),persp(0,8)]
ax.add_patch(Polygon(rim,closed=True,fill=False,ec=gold,lw=2.2,zorder=3))
# queens: glyph with shadow and glow, scaled by depth
sol=[5,3,6,0,7,1,4,2]
for r,c in enumerate(sol):
    x,y=persp(c+0.5,r+0.5)
    t=ax.text(x,y-0.01,'\u265B',ha='center',va='center',fontsize=30*k,color='#f6f1e3',fontname='DejaVu Sans',zorder=5)
    t.set_path_effects([pe.withStroke(linewidth=1.1,foreground='#101a2c')])
# staircase panel beside the board
dos=json.load(open('dos.json'))['8']; d={int(k):v for k,v in dos.items()}; tot=sum(d.values())
sx=fx0+4.2*k; sw=1.45*k; sy=bleed+1.75*kv; sh=3.4*k; u=0; xs=[]; ys=[]
for sdx in sorted(d):
    w=d[sdx]/tot; xs+=[sx+u*sw,sx+(u+w)*sw]; ys+=[sy+sh*math.exp(-sdx/5)]*2; u+=w
ax.plot(xs,ys,color=gold,lw=2,zorder=6); ax.fill_between(xs,sy,ys,color=gold,alpha=0.32,zorder=5)
ax.plot([sx,sx+sw],[sy,sy],color=gold,lw=0.8,zorder=6); ax.plot([sx,sx],[sy,sy+sh],color=gold,lw=0.8,zorder=6)
ax.text(sx+sw/2,sy+sh+0.12,'$\\Lambda(s)$',ha='center',va='bottom',fontsize=11*k,color=ink,zorder=6)
ax.text(sx+sw/2,sy-0.12,'$Z=\\int_0^1\\Lambda(s)\\,ds$',ha='center',va='top',fontsize=9*k,color=ink,zorder=6)
ax.text(sx,sy-0.36,'$0$',ha='center',va='top',fontsize=8*k,color=ink,zorder=6); ax.text(sx+sw,sy-0.36,'$1$',ha='center',va='top',fontsize=8*k,color=ink,zorder=6)
# title block
ax.text(fx0+3.5,H-bleed-1.15*kv,'P = RP',ha='center',va='center',fontsize=66*k,color=ink,family='serif',fontweight='bold',zorder=6)
ax.text(fx0+3.5,H-bleed-2.15*kv,'A Monte Carlo Program\nfor P versus NP',ha='center',va='center',fontsize=19*k,color=gold,family='serif',style='italic',linespacing=1.15,zorder=6)
ax.plot([fx0+3.5-1.9*k,fx0+3.5+1.9*k],[H-bleed-2.78*kv]*2,color=gold,lw=1.2,zorder=6)
ax.text(fx0+3.5,H-bleed-3.25*kv,'Vertical likelihood, counting N queens,\nand the complexity of randomness',ha='center',va='center',fontsize=11*k,color=ink,alpha=0.8,family='serif',zorder=6)
ax.text(fx0+3.5,bleed+0.95*kv,'Nick Polson  \u00b7  Vadim Sokolov',ha='center',va='center',fontsize=19*k,color=ink,family='serif',zorder=6)
# spine
sx0=bleed+TW
ax.text(sx0+spine/2,H/2+0.3*kv,'P = RP',rotation=270,ha='center',va='center',fontsize=15,color=ink,family='serif',fontweight='bold')
ax.text(sx0+spine/2,H/2-2.6*kv,'Polson and Sokolov',rotation=270,ha='center',va='center',fontsize=11,color=gold,family='serif')
# back cover
bx0=bleed
blurb=("In 1850 Franz Nauck asked how many ways N queens can be placed on an N by N board so that no two attack, generalizing the eight queens question that Gauss had taken up. The puzzle is a window on the central problem of computer science. Completing a partial board is NP complete, counting its completions is #P complete, and every Monte Carlo method proposed for such counts comes down to a walk along a single staircase on the unit interval: the quantile function of the likelihood, whose integral is the Lorenz curve identity behind nested sampling and vertical likelihood.",
"This book sets out that observation as a program and marks its gaps. It proves that NP = RP is equivalent to polynomial time sampling and approximate counting of queens completions, and states as a conjecture when a swap chain on the energy levels mixes fast enough to deliver them; it restates promise RP = promise P, which implies P = RP, as the known hitting set problem on the quantile axis, which it does not claim to solve; it gives Yakowitz type bounds, higher order and stratified rules, and generative Bayesian computation as the machinery; and it reports exact computations on the queens: the density of states, the giant component of solutions, its persistence on conditioned boards, and the shattering depth of the bottom level sets.",
"From Hilbert and Turing through Shannon and von Neumann to Jerrum, Sinclair and Impagliazzo, the authors trace what is known, state what is conjectured, and leave the reader at the exact place where the next theorem must be proved.")
y=H-bleed-0.7
L=bx0+0.55; R=bx0+TW-0.55
for para in blurb:
    for line in textwrap.wrap(para,76):
        ax.text(L,y,line,ha='left',va='top',fontsize=10.4,color=ink,family='serif'); y-=0.24
    y-=0.18
ax.plot([L,R],[y-0.05,y-0.05],color=gold,lw=0.8)
ax.text(L,y-0.25,'Nick Polson is the Robert Law Jr. Professor of Econometrics and Statistics\nat the University of Chicago Booth School of Business.\nVadim Sokolov is Associate Professor of Operations Research\nat George Mason University.',ha='left',va='top',fontsize=9.5,color=gold,family='serif',linespacing=1.3)
fig.savefig('../cover/cover_wrap.pdf'); fig.savefig('../cover/cover_wrap.png',dpi=150)
