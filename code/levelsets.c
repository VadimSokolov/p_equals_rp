/* Swap connectivity of the level sets {S <= m} of the N queens energy,
   for all m, by exhaustive enumeration of permutations (N <= 10).
   Output: for each m, number of components, size of the largest,
   whether all solutions lie in one component, and the number of
   components containing a solution. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int N; static long FACT[13];
static long rankp(const int *p){ /* Lehmer rank */
  long r=0; int used[16]={0};
  for(int i=0;i<N;i++){ int c=0; for(int k=0;k<p[i];k++) c+= !used[k]; r+= c*FACT[N-1-i]; used[p[i]]=1; }
  return r; }
static void unrank(long r,int *p){ int avail[16]; for(int i=0;i<N;i++) avail[i]=i; int na=N;
  for(int i=0;i<N;i++){ long f=FACT[N-1-i]; int c=r/f; r%=f; p[i]=avail[c]; for(int k=c;k<na-1;k++) avail[k]=avail[k+1]; na--; } }
static int energy(const int *p){ int e=0; for(int i=0;i<N;i++) for(int j=i+1;j<N;j++) if(abs(p[i]-p[j])==j-i) e++; return e; }
int main(int argc,char**argv){
  N=atoi(argv[1]); FACT[0]=1; for(int i=1;i<=12;i++) FACT[i]=FACT[i-1]*i;
  long M=FACT[N]; unsigned char *E=malloc(M); int p[16];
  int maxe=0; long *cnt=calloc(64,sizeof(long));
  for(long r=0;r<M;r++){ unrank(r,p); E[r]=energy(p); cnt[E[r]]++; if(E[r]>maxe) maxe=E[r]; }
  printf("N=%ld maxE=%d\n",(long)N,maxe);
  unsigned char *seen=malloc(M); long *queue=malloc(M*sizeof(long));
  for(int m=0;m<=maxe;m++){
    memset(seen,0,M); long comps=0,largest=0,withsol=0,largestsol=0,total=0;
    for(long r0=0;r0<M;r0++){ if(E[r0]>m||seen[r0]) continue;
      long head=0,tail=0; queue[tail++]=r0; seen[r0]=1; long size=0,sols=0;
      while(head<tail){ long u=queue[head++]; size++; unrank(u,p); if(E[u]==0) sols++;
        for(int i=0;i<N;i++) for(int j=i+1;j<N;j++){ int t=p[i]; p[i]=p[j]; p[j]=t; long v=rankp(p); t=p[i]; p[i]=p[j]; p[j]=t;
          if(E[v]<=m && !seen[v]){ seen[v]=1; queue[tail++]=v; } } }
      comps++; total+=size; if(size>largest) largest=size; if(sols>0) withsol++; if(sols>largestsol) largestsol=sols; }
    printf("m=%d size=%ld comps=%ld largest=%ld withsol=%ld largestsol=%ld sols=%ld\n",m,total,comps,largest,withsol,largestsol,cnt[0]); fflush(stdout);
    if(m>=2) break; }
  return 0; }
