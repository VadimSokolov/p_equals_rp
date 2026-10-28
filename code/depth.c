/* Shattering depth of a conditioned board. Usage: depth N mmax k seed boards
   For each of `boards` random boards with k fixed non attacking queens that
   have at least one completion: enumerate completions with S <= m for
   m = 0..mmax, BFS over swaps of free rows, report size, components,
   components with a completion, and the solution and shattering depths. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
static int N, K; static int fixedrow[16], fixedcol[16], isfixed[16], fixcol[16];
static uint64_t *keys; static int *energyv; static long cnt, cap;
static int x[16], used[16];
static void push(void){ uint64_t k=0; for(int i=0;i<N;i++) k=(k<<4)|x[i];
  if(cnt==cap){ cap*=2; keys=realloc(keys,cap*8); energyv=realloc(energyv,cap*4);} keys[cnt]=k; cnt++; }
static int energy_of(void){ int e=0; for(int i=0;i<N;i++) for(int j=i+1;j<N;j++) if(abs(x[i]-x[j])==j-i) e++; return e; }
static int M;
static void rec(int i,int conf){ if(i==N){ push(); return; }
  if(isfixed[i]){ /* count attacks of fixed queen with earlier rows */ int add=0; for(int j=0;j<i;j++) if(abs(x[j]-x[i])==i-j) add++; if(conf+add>M) return; rec(i+1,conf+add); return; }
  for(int c=0;c<N;c++){ if(used[c]) continue; int add=0; for(int j=0;j<i;j++) if(abs(x[j]-c)==i-j){ add++; if(conf+add>M) break; } if(conf+add>M) continue;
    x[i]=c; used[c]=1; rec(i+1,conf+add); used[c]=0; } }
static int cmpk(const void*a,const void*b){ uint64_t x=*(uint64_t*)a,y=*(uint64_t*)b; return x<y?-1:x>y; }
static long findkey(uint64_t k){ long lo=0,hi=cnt-1; while(lo<=hi){ long mid=(lo+hi)/2; if(keys[mid]==k) return mid; if(keys[mid]<k) lo=mid+1; else hi=mid-1; } return -1; }
int main(int argc,char**argv){ N=atoi(argv[1]); int mmax=atoi(argv[2]); K=atoi(argv[3]); srand(atoi(argv[4])); int boards=atoi(argv[5]);
  int done=0; int hist_ms[8]={0}, hist_mc[8]={0}; double ratio_sum=0; int ratio_n=0;
  while(done<boards){
    /* random board */
    memset(isfixed,0,sizeof isfixed); int rows[16],cols[16]; for(int i=0;i<N;i++){rows[i]=i;cols[i]=i;}
    for(int i=0;i<K;i++){ int r=i+rand()%(N-i); int t=rows[i];rows[i]=rows[r];rows[r]=t; r=i+rand()%(N-i); t=cols[i];cols[i]=cols[r];cols[r]=t; }
    int ok=1; for(int a=0;a<K;a++) for(int b=a+1;b<K;b++) if(abs(cols[a]-cols[b])==abs(rows[a]-rows[b])) ok=0; if(!ok) continue;
    for(int i=0;i<K;i++){ isfixed[rows[i]]=1; fixcol[rows[i]]=cols[i]; }
    int ms=-1, mc=-1; long n0=0; long sizes[8]={0};
    for(M=0;M<=mmax;M++){
      cap=1<<16; keys=malloc(cap*8); energyv=malloc(cap*4); cnt=0;
      memset(used,0,sizeof used); for(int i=0;i<N;i++) if(isfixed[i]){ x[i]=fixcol[i]; used[fixcol[i]]=1; }
      rec(0,0);
      qsort(keys,cnt,8,cmpk);
      for(long u=0;u<cnt;u++){ uint64_t k=keys[u]; for(int i=N-1;i>=0;i--){ x[i]=k&15; k>>=4; } energyv[u]=energy_of(); }
      long sols=0; for(long u=0;u<cnt;u++) if(energyv[u]==0) sols++;
      if(M==0){ n0=sols; if(n0==0) break; }
      /* BFS */
      unsigned char *seen=calloc(cnt,1); long *queue=malloc(cnt*sizeof(long)); long comps=0, withsol=0;
      for(long r0=0;r0<cnt;r0++){ if(seen[r0]) continue; long head=0,tail=0; queue[tail++]=r0; seen[r0]=1; long s=0;
        while(head<tail){ long u=queue[head++]; if(energyv[u]==0) s++; uint64_t k=keys[u]; for(int i=N-1;i>=0;i--){ x[i]=k&15; k>>=4; }
          for(int i=0;i<N;i++){ if(isfixed[i]) continue; for(int j=i+1;j<N;j++){ if(isfixed[j]) continue; int t=x[i];x[i]=x[j];x[j]=t; uint64_t kk=0; for(int q=0;q<N;q++) kk=(kk<<4)|x[q]; t=x[i];x[i]=x[j];x[j]=t;
            long v=findkey(kk); if(v>=0 && !seen[v]){ seen[v]=1; queue[tail++]=v; } } } }
        comps++; if(s>0) withsol++; }
      sizes[M]=cnt;
      if(ms<0 && withsol==1) ms=M; if(mc<0 && comps==1) mc=M;
      free(seen); free(queue); free(keys); free(energyv);
      if(mc>=0) break; }
    if(n0==0) continue;
    done++;
    printf("board %d fixed:",done); for(int i=0;i<K;i++) printf(" (%d,%d)",rows[i],cols[i]); printf(" N0=%ld ms=%d mc=%d sizes:",n0,ms,mc); for(int m=0;m<=mmax;m++) if(sizes[m]) printf(" %ld",sizes[m]);
    if(mc>=0){ printf(" ratio=%.3e",(double)n0/sizes[mc]); ratio_sum+=(double)n0/sizes[mc]; ratio_n++; }
    printf("\n"); fflush(stdout);
    if(ms>=0&&ms<8) hist_ms[ms]++; if(mc>=0&&mc<8) hist_mc[mc]++; else hist_mc[7]++; }
  printf("N=%d k=%d boards=%d ms_hist:",N,K,boards); for(int m=0;m<8;m++) printf(" %d",hist_ms[m]); printf(" mc_hist:"); for(int m=0;m<8;m++) printf(" %d",hist_mc[m]); printf(" mean_ratio=%.3e\n", ratio_n? ratio_sum/ratio_n:0.0);
  return 0; }
