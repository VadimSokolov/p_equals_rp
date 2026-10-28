import numpy as np, math, json, textwrap
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle
from matplotlib.collections import PolyCollection
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patheffects as pe
pages=405; spine=pages*0.002252; bleed=0.125; W=2*(6+bleed)+spine; H=9+2*bleed
fig=plt.figure(figsize=(W,H),dpi=300)
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,W); ax.set_ylim(0,H); ax.axis('off')
# background: vertical gradient navy to near black
grad=np.linspace(0,1,400)[:,None]*np.ones((1,10))
cm=LinearSegmentedColormap.from_list('bg',['#050b16','#0e2240','#132d52'])
ax.imshow(grad,extent=[0,W,0,H],aspect='auto',cmap=cm,zorder=0,origin='lower')
gold='#e4b94a'; ink='#f3efe4'
fx0=bleed+6+spine
# perspective board
def persp(c,r,n=8):
    # map board coords (c,r) in [0,n] to page; bottom edge wide, top narrow
    cx=fx0+2.05; base_y=bleed+1.65; side=3.4
    return (cx-side/2+side*(c/n), base_y+side*(r/n))
light='#e9e2d0'; dark='#2b4a73'
polys=[]; cols=[]
for r in range(8):
    for c in range(8):
        quad=[persp(c,r),persp(c+1,r),persp(c+1,r+1),persp(c,r+1)]
        polys.append(quad); cols.append(light if (r+c)%2 else dark)
ax.add_collection(PolyCollection(polys,facecolors=cols,edgecolors='#0a1526',linewidths=0.4,zorder=2))
# board rim
rim=[persp(0,0),persp(8,0),persp(8,8),persp(0,8)]
ax.add_patch(Polygon(rim,closed=True,fill=False,ec=gold,lw=2.2,zorder=3))
# queens: glyph with shadow and glow, scaled by depth
sol=[5,3,6,0,7,1,4,2]
for r,c in enumerate(sol):
    x,y=persp(c+0.5,r+0.5)
    t=ax.text(x,y-0.01,'\u265B',ha='center',va='center',fontsize=30,color='#f6f1e3',fontname='DejaVu Sans',zorder=5)
    t.set_path_effects([pe.withStroke(linewidth=1.1,foreground='#101a2c')])
# staircase panel beside the board
dos=json.load(open('dos.json'))['8']; d={int(k):v for k,v in dos.items()}; tot=sum(d.values())
sx=fx0+4.2; sw=1.45; sy=bleed+1.65; sh=3.4; u=0; xs=[]; ys=[]
for sdx in sorted(d):
    w=d[sdx]/tot; xs+=[sx+u*sw,sx+(u+w)*sw]; ys+=[sy+sh*math.exp(-sdx/5)]*2; u+=w
ax.plot(xs,ys,color=gold,lw=2,zorder=6); ax.fill_between(xs,sy,ys,color=gold,alpha=0.32,zorder=5)
ax.plot([sx,sx+sw],[sy,sy],color=gold,lw=0.8,zorder=6); ax.plot([sx,sx],[sy,sy+sh],color=gold,lw=0.8,zorder=6)
ax.text(sx+sw/2,sy+sh+0.12,'$\\Lambda(s)$',ha='center',va='bottom',fontsize=11,color=ink,zorder=6)
ax.text(sx+sw/2,sy-0.12,'$Z=\\int_0^1\\Lambda(s)\\,ds$',ha='center',va='top',fontsize=9,color=ink,zorder=6)
ax.text(sx,sy-0.36,'$0$',ha='center',va='top',fontsize=8,color=ink,zorder=6); ax.text(sx+sw,sy-0.36,'$1$',ha='center',va='top',fontsize=8,color=ink,zorder=6)
# title block
ax.text(fx0+3,H-bleed-1.15,'P = RP',ha='center',va='center',fontsize=66,color=ink,family='serif',fontweight='bold',zorder=6)
ax.text(fx0+3,H-bleed-2.15,'A Monte Carlo Program\nfor P versus NP',ha='center',va='center',fontsize=19,color=gold,family='serif',style='italic',linespacing=1.15,zorder=6)
ax.plot([fx0+1.1,fx0+4.9],[H-bleed-2.78,H-bleed-2.78],color=gold,lw=1.2,zorder=6)
ax.text(fx0+3,H-bleed-3.25,'Vertical likelihood, counting N queens,\nand the complexity of randomness',ha='center',va='center',fontsize=11,color=ink,alpha=0.8,family='serif',zorder=6)
ax.text(fx0+3,bleed+1.0,'Nick Polson  \u00b7  Vadim Sokolov',ha='center',va='center',fontsize=19,color=ink,family='serif',zorder=6)
# spine
sx0=bleed+6
ax.text(sx0+spine/2,H/2+0.3,'P = RP',rotation=270,ha='center',va='center',fontsize=15,color=ink,family='serif',fontweight='bold')
ax.text(sx0+spine/2,H/2-2.6,'Polson and Sokolov',rotation=270,ha='center',va='center',fontsize=11,color=gold,family='serif')
# back cover
bx0=bleed
blurb=("Gauss asked how many ways N queens can be placed on an N by N board so that no two attack. The question looks like a puzzle. It is a window on the central problem of computer science. Counting the queens is #P complete, completing a board is NP complete, and every Monte Carlo method ever proposed for such problems is, in the end, a walk down a single staircase on the unit interval: the quantile function of the likelihood, the Lorenz curve of the count.",
"This book sets out that observation as a program. It proves that the question whether NP = RP is exactly the question whether a swap chain on a chessboard mixes in polynomial time; it restates P = RP as the problem of hitting a dense level set without a coin; it gives Yakowitz type bounds, higher order and stratified rules, and generative Bayesian computation as the practical machinery; and it reports experiments and exact computations on the queens, including the giant component of solutions, its persistence on conditioned boards, and the finite size correction to Simkin's constant.",
"From Hilbert and Turing through Shannon and von Neumann to Jerrum, Sinclair and Impagliazzo, the authors trace what is known, state what is conjectured, and leave the reader at the exact place where the next theorem must be proved.")
y=H-bleed-0.95
for para in blurb:
    for line in textwrap.wrap(para,66):
        ax.text(bx0+0.65,y,line,ha='left',va='top',fontsize=10.2,color=ink,family='serif'); y-=0.235
    y-=0.18
ax.plot([bx0+0.65,bx0+5.35],[y-0.05,y-0.05],color=gold,lw=0.8)
ax.text(bx0+0.65,y-0.25,'Nick Polson is the Robert Law Jr. Professor of Econometrics and Statistics\nat the University of Chicago Booth School of Business.\nVadim Sokolov is Associate Professor of Operations Research\nat George Mason University.',ha='left',va='top',fontsize=9.5,color=gold,family='serif',linespacing=1.3)
ax.add_patch(Rectangle((bx0+6-0.25-2.0,bleed+0.25),2.0,1.2,color='white'))
fig.savefig('cover_wrap.pdf'); fig.savefig('cover_wrap.png',dpi=110)
im=plt.imread('cover_wrap.png')
