from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

OUT=Path(__file__).resolve().parent/"assets"
OUT.mkdir(parents=True,exist_ok=True)

# Kindle 11th gen: use high-resolution monochrome graphics.
# Up candles = hollow white body; Down candles = solid black body.
plt.rcParams["font.family"]="DejaVu Sans"
plt.rcParams["savefig.facecolor"]="white"

def chart(data,title,subtitle,out,support=None,resistance=None,labels=None,xlim=None,
          legend=True, volume_by_direction=True):
    n=len(data)
    # 1236 px wide at 300 dpi, close to Kindle Paperwhite 11th-gen screen width.
    fig=plt.figure(figsize=(4.12,5.50),dpi=300,facecolor="white")
    gs=fig.add_gridspec(8,1,height_ratios=[0.85,4.4,0.12,1.25,0.07,0.04,0.04,0.08])
    at=fig.add_subplot(gs[0]); at.axis("off")
    ax=fig.add_subplot(gs[1]); av=fig.add_subplot(gs[3],sharex=ax)

    # Scale candle width based on visible bar count so bodies stay legible.
    visible_n = (xlim[1]-xlim[0]) if xlim else n
    w = min(0.72, max(0.48, 22.0/max(visible_n,1)))

    for i,(o,h,l,c,v) in enumerate(data):
        up = c >= o
        body_face = "white" if up else "black"
        # Thicker wick/body for e-ink.
        ax.vlines(i,l,h,color="black",lw=1.25,zorder=2)
        lo=min(o,c)
        ht=max(abs(c-o),0.10)
        if abs(c-o)<0.10:
            lo=(o+c)/2-ht/2
        ax.add_patch(Rectangle((i-w/2,lo),w,ht,
                               facecolor=body_face,edgecolor="black",
                               linewidth=1.25,zorder=3))
        if volume_by_direction:
            vface="white" if up else "0.18"
        else:
            vface="0.70"
        av.bar(i,v,width=w,facecolor=vface,edgecolor="black",linewidth=0.8)

    yr=max(x[1] for x in data)-min(x[2] for x in data)
    ax.set_ylim(min(x[2] for x in data)-max(0.5,yr*.05),
                max(x[1] for x in data)+max(0.5,yr*.06))

    if resistance is not None:
        ax.axhline(resistance,ls="--",color="black",lw=1.0)
        ax.text((xlim[1]-0.3 if xlim else n-1.1),resistance+yr*.025,
                "Kháng cự",ha="right",fontsize=7.5)
    if support is not None:
        ax.axhline(support,ls="--",color="black",lw=1.0)
        ax.text((xlim[1]-0.3 if xlim else n-1.1),support-yr*.025,
                "Hỗ trợ",ha="right",va="top",fontsize=7.5)

    if labels:
        for i,lbl in labels.items():
            o,h,l,c,v=data[i]
            ax.annotate(lbl,xy=(i,h),xytext=(i,h+yr*.06),ha="center",
                        arrowprops=dict(arrowstyle="-|>",lw=.8,color="black"),
                        fontsize=8,fontweight="bold")

    if xlim:
        ax.set_xlim(*xlim); av.set_xlim(*xlim)
    else:
        ax.set_xlim(-.7,n-.3)

    # Very light grid: it should not compete with candles on e-ink.
    ax.grid(axis="y",color="0.90",lw=.45)
    av.grid(axis="y",color="0.92",lw=.4)
    ax.tick_params(axis="both",labelsize=7)
    av.tick_params(axis="y",labelsize=7)
    ax.tick_params(axis="x",labelbottom=False)
    av.set_xticks([])
    ax.set_ylabel("Giá",fontsize=7.5)
    av.set_ylabel("Khối lượng",fontsize=7.5)

    at.text(.5,.74,title,ha="center",va="center",fontsize=11.5,fontweight="bold")
    at.text(.5,.33,subtitle,ha="center",va="center",fontsize=7.3)
    if legend:
        at.text(.5,.04,"NẾN TĂNG = THÂN TRẮNG RỖNG    •    NẾN GIẢM = THÂN ĐEN ĐẶC",
                ha="center",va="bottom",fontsize=6.8,fontweight="bold")
    fig.subplots_adjust(top=.985,bottom=.055,left=.12,right=.985,hspace=.20)
    fig.savefig(OUT/out,bbox_inches="tight",dpi=300)
    plt.close(fig)

# --- Absorption of Supply ---
sup=[]
vals=[88,90,92,94,95.5,96.8,97.9,98.8]; prev=87.5
for i,cl in enumerate(vals):
    o=prev+(0.3 if i%2==0 else -0.1); c=cl
    sup.append((o,max(o,c)+.8,min(o,c)-.6,c,[80,90,95,100,110,120,130,140][i])); prev=c
sup += [(99,100.2,97.9,98.6,180),(98.7,100.1,98.2,99.2,210),(99.1,100.05,98.6,99,230),
        (99,100.15,98.8,99.35,245),(99.3,100.1,99,99.55,260),(99.6,100.05,99.25,99.75,275),
        (99.8,101.8,99.55,101.4,300),(101.2,101.6,100.6,101.3,170),(101.4,103,101.2,102.7,250)]
chart(sup,"Absorption – Hấp thụ cung tại kháng cự",
      "Effort tăng dần nhưng phản ứng giảm ngày càng nông.",
      "absorption_supply_main.png",resistance=100,
      labels={8:"1",9:"2",10:"3",11:"4",12:"5",13:"6",14:"X"})
chart(sup,"Phóng to vùng 1–3","Effort tăng nhưng Result giảm.",
      "absorption_supply_zoom_1.png",resistance=100,
      labels={8:"1",9:"2",10:"3"},xlim=(7.1,10.9))
chart(sup,"Phóng to vùng 4–6 và xác nhận","Phản ứng nông dần rồi breakout.",
      "absorption_supply_zoom_2.png",resistance=100,
      labels={11:"4",12:"5",13:"6",14:"X"},xlim=(10.2,15.9))

# --- Absorption of Demand ---
dem=[]
vals=[102,100,98.5,97,95.5,94.6,93.7,92.8]; prev=103
for i,cl in enumerate(vals):
    o=prev+(-.3 if i%2==0 else .15); c=cl
    dem.append((o,max(o,c)+.6,min(o,c)-.8,c,[85,95,105,115,125,135,145,155][i])); prev=c
dem += [(92.4,93.6,90.9,91.8,185),(91.9,93.2,91.4,91.7,210),(91.8,92.8,91,91.45,225),
        (91.4,92.4,90.8,91.2,245),(91.25,92,90.6,91,260),(91.05,91.8,90.4,90.85,280),
        (90.8,91,88.6,89.2,305),(89.4,90.2,88.9,89.1,165),(89,89.3,87,87.4,250)]
chart(dem,"Absorption – Hấp thụ cầu tại hỗ trợ",
      "Effort vẫn lớn nhưng lực hồi ngày càng kém.",
      "absorption_demand_main.png",support=91,
      labels={8:"1",9:"2",10:"3",11:"4",12:"5",13:"6",14:"X"})
chart(dem,"Phóng to vùng 1–3","Có lực hồi nhưng không đi được xa.",
      "absorption_demand_zoom_1.png",support=91,
      labels={8:"1",9:"2",10:"3"},xlim=(7.1,10.9))
chart(dem,"Phóng to vùng 4–6 và xác nhận","Rally yếu dần rồi breakdown.",
      "absorption_demand_zoom_2.png",support=91,
      labels={11:"4",12:"5",13:"6",14:"X"},xlim=(10.2,15.9))

# --- Practical simulation ---
# Use fewer bars than the first draft so hollow/solid bodies remain visibly different
# even when the overview is fitted to a Kindle 11th-gen portrait screen.
rng=np.random.default_rng(7)
N=64
price=[12.5]
for i in range(1,N):
    if i<12: drift=-0.035
    elif i<30: drift=0.045
    elif i<40: drift=0.13
    elif i<53: drift=0.002
    else: drift=0.055
    price.append(max(10,price[-1]+drift+rng.normal(0,.10)))

data=[]
for i,c in enumerate(price):
    o=price[i-1] if i else c+rng.normal(0,.06)
    h=max(o,c)+abs(rng.normal(.15,.045))
    l=min(o,c)-abs(rng.normal(.15,.045))
    v=80+abs(rng.normal(0,24))
    if i in [9,38,44,55]: v*=2.5
    data.append((o,h,l,c,v))

chart(data,"Ví dụ thực chiến mô phỏng",
      "Nến tăng rỗng, nến giảm đen; khối lượng dùng cùng quy ước.",
      "real_chart_full_grayscale.png",volume_by_direction=True)
chart(data,"Phóng to vùng ra quyết định",
      "Giá co hẹp sau một nhịp tăng — đọc giá và khối lượng cùng lúc.",
      "real_chart_zoom_price_volume.png",xlim=(34,63),volume_by_direction=True)
