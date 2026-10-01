from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

OUT=Path(__file__).resolve().parent/"assets"
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams["font.family"]="DejaVu Sans"

def chart(data,title,subtitle,out,support=None,resistance=None,labels=None,xlim=None):
    n=len(data); fig=plt.figure(figsize=(7.2,9.3),dpi=180)
    gs=fig.add_gridspec(8,1,height_ratios=[0.7,4,0.15,1.2,0.1,0.05,0.05,0.1])
    at=fig.add_subplot(gs[0]); at.axis("off")
    ax=fig.add_subplot(gs[1]); av=fig.add_subplot(gs[3],sharex=ax)
    for i,(o,h,l,c,v) in enumerate(data):
        ax.vlines(i,l,h,color="black",lw=1)
        fc="black" if c<o else "white"
        lo=min(o,c); ht=max(abs(c-o),0.12)
        if abs(c-o)<0.12: lo=(o+c)/2-ht/2
        ax.add_patch(Rectangle((i-.29,lo),.58,ht,fc=fc,ec="black",lw=1))
        av.bar(i,v,width=.58,color="0.65",edgecolor="black")
    ax.set_ylim(min(x[2] for x in data)-1,max(x[1] for x in data)+1)
    if resistance is not None:
        ax.axhline(resistance,ls="--",color="black",lw=.9)
        ax.text(n-1.2,resistance+.25,"Kháng cự",ha="right",fontsize=9)
    if support is not None:
        ax.axhline(support,ls="--",color="black",lw=.9)
        ax.text(n-1.2,support-.3,"Hỗ trợ",ha="right",va="top",fontsize=9)
    if labels:
        for i,lbl in labels.items():
            o,h,l,c,v=data[i]
            ax.annotate(lbl,xy=(i,h),xytext=(i,h+.7),ha="center",
                        arrowprops=dict(arrowstyle="-|>",lw=.8,color="black"),
                        fontsize=9,fontweight="bold")
    if xlim: ax.set_xlim(*xlim); av.set_xlim(*xlim)
    else: ax.set_xlim(-.7,n-.3)
    ax.grid(axis="y",color="0.86",lw=.6); av.grid(axis="y",color="0.90",lw=.5)
    ax.tick_params(axis="x",labelbottom=False); av.set_xticks([])
    ax.set_ylabel("Giá"); av.set_ylabel("Khối lượng")
    at.text(.5,.72,title,ha="center",va="center",fontsize=15,fontweight="bold")
    at.text(.5,.18,subtitle,ha="center",va="center",fontsize=9.5)
    fig.text(.5,.015,"Biểu đồ mô phỏng sư phạm — tối ưu cho màn hình e-ink",ha="center",fontsize=8)
    fig.subplots_adjust(top=.97,bottom=.05,left=.09,right=.97,hspace=.18)
    fig.savefig(OUT/out,bbox_inches="tight"); plt.close(fig)

sup=[]
vals=[88,90,92,94,95.5,96.8,97.9,98.8]; prev=87.5
for i,cl in enumerate(vals):
    o=prev+(0.3 if i%2==0 else -0.1); c=cl
    sup.append((o,max(o,c)+.8,min(o,c)-.6,c,[80,90,95,100,110,120,130,140][i])); prev=c
sup += [(99,100.2,97.9,98.6,180),(98.7,100.1,98.2,99.2,210),(99.1,100.05,98.6,99,230),
        (99,100.15,98.8,99.35,245),(99.3,100.1,99,99.55,260),(99.6,100.05,99.25,99.75,275),
        (99.8,101.8,99.55,101.4,300),(101.2,101.6,100.6,101.3,170),(101.4,103,101.2,102.7,250)]
chart(sup,"Absorption – Hấp thụ cung tại kháng cự","Effort tăng dần nhưng phản ứng giảm ngày càng nông.","absorption_supply_main.png",resistance=100,labels={8:"1",9:"2",10:"3",11:"4",12:"5",13:"6",14:"X"})
chart(sup,"Phóng to vùng 1–3","Effort tăng nhưng Result giảm.","absorption_supply_zoom_1.png",resistance=100,labels={8:"1",9:"2",10:"3"},xlim=(7.1,10.9))
chart(sup,"Phóng to vùng 4–6 và xác nhận","Phản ứng nông dần rồi breakout.","absorption_supply_zoom_2.png",resistance=100,labels={11:"4",12:"5",13:"6",14:"X"},xlim=(10.2,15.9))

dem=[]
vals=[102,100,98.5,97,95.5,94.6,93.7,92.8]; prev=103
for i,cl in enumerate(vals):
    o=prev+(-.3 if i%2==0 else .15); c=cl
    dem.append((o,max(o,c)+.6,min(o,c)-.8,c,[85,95,105,115,125,135,145,155][i])); prev=c
dem += [(92.4,93.6,90.9,91.8,185),(91.9,93.2,91.4,91.7,210),(91.8,92.8,91,91.45,225),
        (91.4,92.4,90.8,91.2,245),(91.25,92,90.6,91,260),(91.05,91.8,90.4,90.85,280),
        (90.8,91,88.6,89.2,305),(89.4,90.2,88.9,89.1,165),(89,89.3,87,87.4,250)]
chart(dem,"Absorption – Hấp thụ cầu tại hỗ trợ","Effort vẫn lớn nhưng lực hồi ngày càng kém.","absorption_demand_main.png",support=91,labels={8:"1",9:"2",10:"3",11:"4",12:"5",13:"6",14:"X"})
chart(dem,"Phóng to vùng 1–3","Có lực hồi nhưng không đi được xa.","absorption_demand_zoom_1.png",support=91,labels={8:"1",9:"2",10:"3"},xlim=(7.1,10.9))
chart(dem,"Phóng to vùng 4–6 và xác nhận","Rally yếu dần rồi breakdown.","absorption_demand_zoom_2.png",support=91,labels={11:"4",12:"5",13:"6",14:"X"},xlim=(10.2,15.9))

# richer 'realistic' chart for Kindle test
rng=np.random.default_rng(7)
N=92
price=[12.5]
for i in range(1,N):
    if i<18: drift=-0.025
    elif i<45: drift=0.035
    elif i<58: drift=0.12
    elif i<76: drift=0.005
    else: drift=0.045
    price.append(max(10,price[-1]+drift+rng.normal(0,.09)))
data=[]
for i,c in enumerate(price):
    o=price[i-1] if i else c+rng.normal(0,.05)
    h=max(o,c)+abs(rng.normal(.12,.05))
    l=min(o,c)-abs(rng.normal(.12,.05))
    v=80+abs(rng.normal(0,25))
    if i in [12,55,63,79]: v*=2.5
    data.append((o,h,l,c,v))
chart(data,"Ví dụ thực chiến mô phỏng","Xu hướng tăng, vùng co hẹp và điểm cần chờ xác nhận.","real_chart_full_grayscale.png")
chart(data,"Phóng to vùng ra quyết định","Giá co hẹp sau một nhịp tăng; theo dõi giá và khối lượng cùng lúc.","real_chart_zoom_price_volume.png",xlim=(52,91))
