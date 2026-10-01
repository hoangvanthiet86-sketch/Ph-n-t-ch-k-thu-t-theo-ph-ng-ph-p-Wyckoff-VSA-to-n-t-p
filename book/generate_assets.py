import os, numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import rcParams
OUT=os.path.join(os.path.dirname(__file__),"assets"); os.makedirs(OUT,exist_ok=True)
rcParams["font.family"]="DejaVu Sans"; NOTE="Sơ đồ mô phỏng sư phạm — không phải dữ liệu thị trường thực"
def candle(ax,x,o,h,l,c,w=.58):
    ax.plot([x,x],[l,h],color="black",lw=1.15)
    ax.add_patch(Rectangle((x-w/2,min(o,c)),w,max(abs(c-o),.06),facecolor="white" if c>=o else ".15",edgecolor="black",lw=1.15))
def style(ax,t=""):
    ax.spines[["top","right"]].set_visible(False); ax.grid(axis="y",ls=":",lw=.5,color=".75"); ax.tick_params(labelsize=8)
    if t: ax.set_title(t,fontsize=11,fontweight="bold",pad=7)
def vols(ax,v):
    ax.bar(range(len(v)),v,width=.6,facecolor=".7",edgecolor="black",lw=.75); ax.set_ylim(0,max(v)*1.28); ax.set_ylabel("Volume",fontsize=8); ax.set_xticks([]); ax.spines[["top","right"]].set_visible(False)
def series(ax,oh,t="",level=None,labels=None):
    for i,z in enumerate(oh): candle(ax,i,*z)
    if level:
        y,txt=level; ax.axhline(y,ls="--",color="black",lw=1); ax.text(len(oh)-.2,y,txt,ha="right",va="bottom",fontsize=8,backgroundcolor="white")
    if labels:
        for i,txt in labels: ax.text(i,oh[i][1]+.2,txt,ha="center",fontsize=8,fontweight="bold")
    style(ax,t); ax.set_xlim(-.7,len(oh)-.2); ax.set_xticks([])
def save(fig,n):
    fig.text(.5,.008,NOTE,ha="center",fontsize=6.8,color=".35"); fig.savefig(os.path.join(OUT,n),dpi=170,bbox_inches="tight",facecolor="white"); plt.close(fig)
def pv(name,oh,v,title,level=None,labels=None):
    f=plt.figure(figsize=(6,5.3));g=f.add_gridspec(2,1,height_ratios=[3,.9],hspace=.05)
    a=f.add_subplot(g[0]);series(a,oh,title,level,labels); b=f.add_subplot(g[1]);vols(b,v);save(f,name)

# cover
f,a=plt.subplots(figsize=(6,8));a.axis("off");a.text(.5,.82,"WYCKOFF / VSA",ha="center",fontsize=30,fontweight="bold");a.text(.5,.73,"ĐỌC HÀNH VI GIÁ VÀ KHỐI LƯỢNG",ha="center",fontsize=15,fontweight="bold");a.text(.5,.66,"Từ bối cảnh → cung cầu → xác nhận → hành động",ha="center",fontsize=11)
p=np.array([[.08,.35],[.18,.25],[.28,.28],[.37,.27],[.46,.48],[.56,.60],[.66,.58],[.74,.62],[.84,.38],[.92,.25]]);a.plot(p[:,0],p[:,1],color="black",lw=3);a.add_patch(Rectangle((.20,.19),.20,.14,fill=False,lw=2));a.add_patch(Rectangle((.62,.52),.16,.14,fill=False,lw=2));a.text(.30,.16,"TÍCH LŨY",ha="center",fontsize=10,fontweight="bold");a.text(.70,.69,"PHÂN PHỐI",ha="center",fontsize=10,fontweight="bold");a.text(.50,.42,"MARKUP",ha="center",fontsize=9);a.text(.86,.33,"MARKDOWN",ha="center",fontsize=9);a.text(.5,.08,"Giáo trình học và thực hành — tối ưu cho Kindle 3",ha="center",fontsize=10);f.savefig(os.path.join(OUT,"cover.png"),dpi=170,bbox_inches="tight",facecolor="white");plt.close(f)

# 3.1
f,a=plt.subplots(figsize=(6,6));a.set_xlim(-1,4);a.set_ylim(0,12);a.axis("off");candle(a,.6,3.5,10,2,8.2,1);candle(a,2.7,8.5,10.3,2.2,4,1);a.text(.6,11,"Nến tăng",ha="center",fontsize=13,fontweight="bold");a.text(2.7,11,"Nến giảm",ha="center",fontsize=13,fontweight="bold")
for txt,xy,tx in [("High",(.6,10),(-.5,10)),("Low",(.6,2),(-.5,1.2)),("Close",(.6,8.2),(-.6,7.5)),("Open",(.6,3.5),(-.6,4.4)),("Open",(2.7,8.5),(3.65,9.2)),("Close",(2.7,4),(3.65,3.3))]: a.annotate(txt,xy=xy,xytext=tx,arrowprops=dict(arrowstyle="->"),fontsize=10)
a.plot([1.35,1.35],[2,10],color="black");a.plot([1.25,1.45],[2,2],color="black");a.plot([1.25,1.45],[10,10],color="black");a.text(1.52,6,"Spread\n= High − Low",va="center",fontsize=10);save(f,"fig-03-01-candle-anatomy.png")
# 3.2
f,a=plt.subplots(figsize=(6,5));a.set_xlim(-.7,5.7);a.set_ylim(0,11);style(a,"Cùng hướng tăng — Result khác nhau")
for v in [(0,2,9.5,1.5,9),(2,2.2,9.8,1.7,5.4),(4,4,6.5,3.5,5.8)]: candle(a,*v,w=.85)
a.text(0,.8,"A\nSpread rộng\nClose gần High",ha="center",fontsize=9);a.text(2,.8,"B\nSpread rộng\nRâu trên dài",ha="center",fontsize=9);a.text(4,.8,"C\nSpread hẹp",ha="center",fontsize=9);a.set_xticks([]);save(f,"fig-03-02-spread-close.png")
# 4.1
f=plt.figure(figsize=(6,8));g=f.add_gridspec(6,1,height_ratios=[2,.8,2,.8,2,.8],hspace=.18)
cases=[([(5,6.2,4.8,6),(6,7.8,5.8,7.6),(7.6,9.5,7.4,9.2)],[3,5,8],"A — Spread mở rộng, Volume tăng"),([(5,6.5,4.7,6.2),(6.2,8.8,6,8.3),(8.3,10,7.6,8.6)],[4,8,14],"B — Volume cực lớn, Result bắt đầu kém"),([(5,5.8,4.7,5.5),(5.5,6.2,5.2,6),(6,7.1,5.8,6.9)],[5,3,2.5],"C — Giá tiến với Volume vừa/thấp")]
for k,(oh,v,t) in enumerate(cases):
    a=f.add_subplot(g[k*2]);series(a,oh,t);b=f.add_subplot(g[k*2+1]);vols(b,v)
save(f,"fig-04-01-volume-cases.png")
pv("fig-04-02-high-volume-narrow-spread.png",[(5,6,4.8,5.7),(5.7,6.5,5.4,6.2),(6.2,7,5.9,6.35),(6.35,6.8,6,6.15)],[3,5,13,11],"Volume lớn + Spread hẹp: lực đối ứng đáng chú ý")
# 5.1
f,a=plt.subplots(figsize=(6,6));a.axis("off");a.set_xlim(0,10);a.set_ylim(0,10);a.plot([5,5],[1,9],c="black");a.plot([1,9],[5,5],c="black");a.text(5,9.5,"RESULT",ha="center",fontsize=14,fontweight="bold");a.text(.35,5,"EFFORT",rotation=90,va="center",fontsize=14,fontweight="bold")
for x,y,t in [(3,8,"Effort thấp\nResult lớn\n→ ít cản"),(7,8,"Effort lớn\nResult lớn\n→ hiệu quả"),(3,3,"Effort thấp\nResult thấp\n→ ít hoạt động"),(7,3,"Effort lớn\nResult thấp\n→ lực đối ứng")]: a.text(x,y,t,ha="center",va="center",fontsize=10)
save(f,"fig-05-01-effort-result-matrix.png")
# 7
prices=[5,6,7.8,7,5.5,4.8,5.6,7.4,8,7.1,5.3,4.6,5.4,7.5,8.3,7.7];oh=[]
for i,p in enumerate(prices): o=p+(.18 if i%2 else -.15);c=p+(.18 if i%3 else -.12);oh.append((o,max(o,c)+.45,min(o,c)-.45,c))
pv("fig-07-01-trading-range.png",oh,[7,6,5,4,6,7,5,4,5,6,7,8,5,4,5,4],"Trading Range: vị trí quan trọng",None)
# 8-14
pv("fig-08-01-sc-ar-st.png",[(9.4,9.8,8.8,9),(9,9.2,7.8,8),(8,8.2,6,6.3),(6.3,8,6.1,7.7),(7.7,8.2,6.9,7.1),(7.1,7.4,6.2,6.6),(6.6,7.1,6.35,6.9),(6.9,7.8,6.7,7.5)],[5,7,14,9,6,7,4,5],"SC → AR → ST",None,[(2,"SC"),(3,"AR"),(5,"ST")])
pv("fig-09-01-spring-test.png",[(6.8,7.5,6.5,7.2),(7.2,7.6,6.8,7),(7,7.2,6.3,6.5),(6.5,6.8,5.5,6.65),(6.65,7.4,6.5,7.25),(7.25,7.5,6.7,6.9),(6.9,7.1,6.55,6.95),(6.95,7.8,6.8,7.65)],[5,4,6,10,8,5,3,7],"Spring candidate → Test → Demand",(6.2,"Vùng hỗ trợ"),[(3,"Spring?"),(6,"Test")])
pv("fig-10-01-sos-lps.png",[(6.5,7,6.3,6.8),(6.8,7.4,6.6,7.2),(7.2,8.6,7.1,8.4),(8.4,9.4,8.2,9.2),(9.2,9.3,8.5,8.7),(8.7,8.9,8.45,8.65),(8.65,9.6,8.6,9.45)],[4,5,9,8,5,3,7],"SOS → LPS → tiếp diễn",(8,"Kháng cự cũ / hỗ trợ mới"),[(2,"SOS"),(5,"LPS")])
pv("fig-12-01-distribution-start.png",[(6,6.8,5.8,6.6),(6.6,7.7,6.4,7.5),(7.5,9,7.3,8.7),(8.7,9.2,7.4,7.7),(7.7,8.5,7.5,8.2),(8.2,8.9,7.7,8),(8,8.7,7.6,8.4)],[5,8,14,10,7,8,7],"PSY → BC candidate → AR → ST",None,[(1,"PSY"),(2,"BC?"),(3,"AR"),(5,"ST")])
pv("fig-13-01-utad.png",[(7.8,8.4,7.5,8.2),(8.2,8.8,7.9,8.5),(8.5,9.1,8.1,8.7),(8.7,9.9,8.5,8.9),(8.9,9.1,7.8,8),(8,8.4,7.5,7.7)],[5,5,6,11,10,8],"Vượt kháng cự nhưng bị từ chối",(9,"Kháng cự"),[(3,"UT/UTAD?")])
pv("fig-14-01-sow-lpsy.png",[(8.5,8.8,8,8.2),(8.2,8.4,7,7.2),(7.2,7.4,6.5,6.7),(6.7,7.4,6.6,7.2),(7.2,7.6,7,7.3),(7.3,7.4,6.2,6.4)],[5,9,8,4,3,8],"SOW → rally yếu → LPSY",(7.8,"Hỗ trợ cũ / kháng cự mới"),[(1,"SOW"),(4,"LPSY")])
# phase plots
for n,t,y in [("fig-15-01-accumulation-phases.png","Accumulation — Phase A → E",[10,9,7,5.8,7.5,6.2,5.9,6.7,7.1,6.1,5.5,6.4,7,6.6,7.4,8.2,7.8,8.8,9.7,10.4,11.1]),("fig-16-01-distribution-phases.png","Distribution — Phase A → E",[5,6,8,10.3,8.8,9.6,9.1,9.8,9,9.6,9.2,10,9.4,8.9,8.3,7.7,8.1,7.2,6.3,5.5,4.8])]:
    f,a=plt.subplots(figsize=(6,5));x=np.arange(len(y));a.plot(x,y,c="black",lw=2);style(a,t)
    for u,v,q in [(0,4,"A"),(4,11,"B"),(11,14,"C"),(14,18,"D"),(18,20,"E")]: a.axvspan(u,v,facecolor=".93",edgecolor="none");a.text((u+v)/2,max(y)+.7,"Phase "+q,ha="center",fontsize=8,fontweight="bold")
    a.set_xticks([]);save(f,n)
# full cycle
f,a=plt.subplots(figsize=(6,5));y=np.array([12,11,10,9,8,7,6.4,6.1,6.6,6.3,6.7,7.2,7.9,8.7,9.7,10.8,12,13.2,14,14.6,14.3,14.7,14.1,14.5,13.8,12.9,11.8,10.6,9.5,8.4,7.4]);a.plot(np.arange(len(y)),y,c="black",lw=2);style(a,"Một chu kỳ hoàn chỉnh")
for u,v,t in [(0,6,"Markdown"),(6,11,"Accumulation"),(11,20,"Markup"),(20,24,"Distribution"),(24,30,"Markdown")]: a.axvspan(u,v,facecolor=".93",edgecolor="none");a.text((u+v)/2,15.2,t,ha="center",fontsize=8,fontweight="bold")
a.set_ylim(5,16);a.set_xticks([]);save(f,"fig-17-01-full-cycle.png")
# paired panels helper
def pair(name,top,bot,topv,botv,t1,t2,lev1=None,lev2=None):
    f=plt.figure(figsize=(6,8.4));g=f.add_gridspec(4,1,height_ratios=[2.6,.7,2.6,.7],hspace=.42)
    a=f.add_subplot(g[0]);series(a,top,t1,lev1);v=f.add_subplot(g[1]);vols(v,topv);a=f.add_subplot(g[2]);series(a,bot,t2,lev2);v=f.add_subplot(g[3]);vols(v,botv);save(f,name)
pair("fig-18-01-no-supply-no-demand.png",[(6,7,5.8,6.8),(6.8,7.8,6.6,7.6),(7.6,7.7,7.1,7.25),(7.25,7.4,7,7.2),(7.2,8,7.1,7.8)],[(8,8.2,7.2,7.4),(7.4,7.6,6.6,6.8),(6.8,7.1,6.6,6.95),(6.95,7.2,6.8,7.05),(7.05,7.1,6.2,6.35)],[5,8,4,2,7],[8,7,3,2,7],"A — Sau Strength: pullback hẹp, volume thấp","B — Sau Weakness: rally hẹp, volume thấp")
pair("fig-20-01-absorption-pair.png",[(6,7,5.8,6.8),(6.8,7.8,6.5,7.2),(7.2,7.9,6.9,7.4),(7.4,8,7.2,7.55),(7.55,8.8,7.5,8.6)],[(8.5,8.8,7.8,8),(8,8.4,7.4,7.9),(7.9,8.2,7.2,7.6),(7.6,7.9,7,7.35),(7.35,7.5,6.2,6.4)],[5,8,10,12,9],[5,8,10,12,9],"Hấp thụ Supply: phản ứng giảm ngày càng nông","Hấp thụ Demand: rally ngày càng kém",(8,"Resistance"),(7,"Support"))
# comparison diagrams
def comp(name,lttl,rttl,lpts,rpts,ltext,rtext,level=False):
    f,a=plt.subplots(figsize=(6,6));a.axis("off");a.set_xlim(0,10);a.set_ylim(0,10);a.text(2.5,9.2,lttl,ha="center",fontsize=11,fontweight="bold");a.text(7.5,9.2,rttl,ha="center",fontsize=11,fontweight="bold")
    if level: a.plot([.5,4.5],[5,5],ls="--",c="black");a.plot([5.5,9.5],[5,5],ls="--",c="black")
    a.plot(*zip(*lpts),c="black",lw=2);a.plot(*zip(*rpts),c="black",lw=2);a.text(2.5,2.1,ltext,ha="center",fontsize=9);a.text(7.5,2.1,rtext,ha="center",fontsize=9);save(f,name)
comp("fig-22-01-reaccum-vs-distribution.png","RE-ACCUMULATION","DISTRIBUTION",[(.8,4),(1.5,6),(2.2,5),(3,6.6),(3.7,5.8),(4.3,7.1)],[(5.5,7),(6.2,5.8),(6.9,6.5),(7.6,5.2),(8.3,5.8),(9.1,4.4)],"Pullback nông dần\nSupply mất hiệu quả","Rally yếu dần\nDemand mất hiệu quả")
comp("fig-23-01-spring-vs-breakdown.png","SPRING CANDIDATE","BREAKDOWN",[(.7,6),(1.5,5.4),(2.3,4.4),(3,5.3),(3.5,5.8),(4.2,6.4)],[(5.7,6),(6.5,5.3),(7.2,4.6),(8,4.2),(8.8,4),(9.3,3.6)],"Phá dưới → bị từ chối\n→ quay lại Range","Phá dưới → được chấp nhận",True)
comp("fig-24-01-breakout-vs-utad.png","BREAKOUT THẬT","UT / UTAD",[(.7,4.2),(1.5,4.8),(2.2,5.4),(3,6),(3.7,5.7),(4.3,6.5)],[(5.7,4.2),(6.5,4.8),(7.2,5.8),(8,5.2),(8.7,4.6),(9.3,4.2)],"Vượt → giữ trên\n→ retest thành support","Vượt → bị từ chối\n→ quay lại Range",True)
comp("fig-25-01-sos-vs-bc.png","SOS","BUYING CLIMAX?",[(.7,3.8),(1.5,4),(2.3,4.2),(3,5.5),(3.8,6.2),(4.3,6.8)],[(5.7,3),(6.5,4),(7.3,5.2),(8,6.5),(8.6,8.2),(9.2,8.4)],"Sau nền\nStrength được chấp nhận","Sau Markup kéo dài\ncần xem follow-through")
comp("fig-26-01-lps-vs-lpsy.png","LPS","LPSY",[(.7,4),(1.6,6),(2.4,5.4),(3.2,5.2),(4.2,6.7)],[(5.7,6.5),(6.6,4.5),(7.4,5.2),(8.2,5.5),(9.2,4)],"Sau SOS\nSupply phản công yếu","Sau SOW\nDemand phản công yếu")
# entry and exit
f,a=plt.subplots(figsize=(6,5));x=np.arange(10);y=np.array([5,4.7,4.4,4.9,5.4,6.5,7.4,6.8,6.9,7.8]);a.plot(x,y,c="black",lw=2);style(a,"Ba cấp độ điểm vào");a.axhline(6.2,ls="--",c="black");a.annotate("1. Sớm",xy=(3,4.9),xytext=(1,6),arrowprops=dict(arrowstyle="->"));a.annotate("2. Xác nhận",xy=(5,6.5),xytext=(4.1,8),arrowprops=dict(arrowstyle="->"));a.annotate("3. Cân bằng",xy=(7,6.8),xytext=(7.2,5.2),arrowprops=dict(arrowstyle="->"));a.set_xticks([]);save(f,"fig-28-01-entry-levels.png")
f,a=plt.subplots(figsize=(6,5));x=np.arange(11);y=np.array([5,6,7,8,9,9.8,9.5,8.9,8,8.4,7.2]);a.plot(x,y,c="black",lw=2);style(a,"Cảnh báo → bằng chứng → xác nhận");a.annotate("BC candidate",xy=(5,9.8),xytext=(3.3,10.8),arrowprops=dict(arrowstyle="->"));a.annotate("SOW",xy=(8,8),xytext=(6.1,6.7),arrowprops=dict(arrowstyle="->"));a.annotate("LPSY",xy=(9,8.4),xytext=(8.3,10.4),arrowprops=dict(arrowstyle="->"));a.set_xticks([]);save(f,"fig-31-01-exit-management.png")
# exercises
f,a=plt.subplots(figsize=(6,5));a.set_xlim(-.8,6);a.set_ylim(0,11);style(a,"Bài tập: chỉ mô tả nến — chưa gắn nhãn")
for v in [(0,2,8,1,7.4),(1,7.5,9.6,3.5,5),(2,5,6.2,4.4,5.7),(3,6,9.8,5.8,6.8),(4,7,7.5,2.5,6.7),(5,6.5,7,2.3,2.8)]: candle(a,*v,w=.72)
for i,ch in enumerate("ABCDEF"): a.text(i,.45,ch,ha="center",fontweight="bold")
a.set_xticks([]);save(f,"fig-34-01-six-candles-exercise.png")
prices=[6,7.5,8.1,7,5.2,4.6,5.1,7.2,8.3,7.4,5.1,4.3,5.5,7.5,8.6,8,6.8];oh=[]
for i,p in enumerate(prices): o=p+(.18 if i%2 else -.15);c=p+(.12 if i%3 else -.18);oh.append((o,max(o,c)+.4,min(o,c)-.45,c))
pv("fig-36-01-range-exercise.png",oh,[5,6,7,5,9,12,6,5,7,6,8,10,6,5,8,6,5],"Bài tập Trading Range — không có nhãn đáp án")
print("Generated",len(os.listdir(OUT)),"assets")