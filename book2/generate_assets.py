from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

OUT=Path(__file__).resolve().parent/"assets"
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams["font.family"]="DejaVu Sans"
plt.rcParams["savefig.facecolor"]="white"

def chart(data,title,subtitle,out,support=None,resistance=None,labels=None,xlim=None):
    n=len(data)
    fig=plt.figure(figsize=(4.12,5.50),dpi=300,facecolor="white")
    gs=fig.add_gridspec(8,1,height_ratios=[0.82,4.4,0.12,1.25,0.07,0.04,0.04,0.08])
    at=fig.add_subplot(gs[0]); at.axis("off")
    ax=fig.add_subplot(gs[1]); av=fig.add_subplot(gs[3],sharex=ax)
    visible_n=(xlim[1]-xlim[0]) if xlim else n
    w=min(.72,max(.48,22/max(visible_n,1)))
    for i,(o,h,l,c,v) in enumerate(data):
        up=c>=o
        ax.vlines(i,l,h,color="black",lw=1.25,zorder=2)
        lo=min(o,c); ht=max(abs(c-o),.10)
        if abs(c-o)<.10: lo=(o+c)/2-ht/2
        ax.add_patch(Rectangle((i-w/2,lo),w,ht,
            facecolor=("white" if up else "black"),
            edgecolor="black",linewidth=1.25,zorder=3))
        av.bar(i,v,width=w,facecolor=("white" if up else "0.18"),
               edgecolor="black",linewidth=.8)
    yr=max(x[1] for x in data)-min(x[2] for x in data)
    ax.set_ylim(min(x[2] for x in data)-max(.35,yr*.06),
                max(x[1] for x in data)+max(.35,yr*.07))
    if support is not None:
        ax.axhline(support,ls="--",color="black",lw=1)
        ax.text((xlim[1]-.2 if xlim else n-1),support-yr*.025,"Hỗ trợ",ha="right",va="top",fontsize=7.3)
    if resistance is not None:
        ax.axhline(resistance,ls="--",color="black",lw=1)
        ax.text((xlim[1]-.2 if xlim else n-1),resistance+yr*.025,"Kháng cự",ha="right",va="bottom",fontsize=7.3)
    if labels:
        for i,lbl in labels.items():
            o,h,l,c,v=data[i]
            ax.annotate(lbl,xy=(i,h),xytext=(i,h+yr*.07),ha="center",
                arrowprops=dict(arrowstyle="-|>",lw=.8,color="black"),
                fontsize=7.5,fontweight="bold")
    if xlim: ax.set_xlim(*xlim); av.set_xlim(*xlim)
    else: ax.set_xlim(-.7,n-.3)
    ax.grid(axis="y",color="0.90",lw=.45)
    av.grid(axis="y",color="0.92",lw=.4)
    ax.tick_params(axis="x",labelbottom=False)
    ax.tick_params(axis="y",labelsize=6.8)
    av.tick_params(axis="y",labelsize=6.8)
    av.set_xticks([])
    ax.set_ylabel("Giá",fontsize=7.4); av.set_ylabel("Khối lượng",fontsize=7.4)
    at.text(.5,.76,title,ha="center",va="center",fontsize=11.2,fontweight="bold")
    at.text(.5,.34,subtitle,ha="center",va="center",fontsize=7.2)
    at.text(.5,.04,"NẾN TĂNG = THÂN TRẮNG RỖNG    •    NẾN GIẢM = THÂN ĐEN ĐẶC",
            ha="center",va="bottom",fontsize=6.5,fontweight="bold")
    fig.subplots_adjust(top=.985,bottom=.055,left=.12,right=.985,hspace=.20)
    fig.savefig(OUT/out,bbox_inches="tight",dpi=300)
    plt.close(fig)

# No Supply after Strength
ns=[
(15.0,15.3,14.8,15.2,120),(15.2,15.6,15.1,15.5,150),(15.5,15.9,15.4,15.8,180),
(15.8,16.2,15.7,16.1,210),(16.1,16.4,16.0,16.3,190),
(16.3,16.35,16.05,16.12,110),(16.12,16.18,15.98,16.05,72),(16.05,16.10,15.96,16.02,58),
(16.02,16.38,15.99,16.34,165),(16.34,16.62,16.28,16.58,210),(16.58,16.9,16.52,16.82,235)
]
chart(ns,"No Supply trong pullback sau Strength","Volume giảm dần khi giá lùi; Demand quay lại sau đó.",
      "ch02_no_supply_overview.png",support=16.0,labels={7:"NS?",8:"XÁC NHẬN"})
chart(ns,"Phóng to No Supply candidate","Spread hẹp + volume thấp + hỗ trợ giữ; bar sau xác nhận.",
      "ch02_no_supply_zoom.png",support=16.0,labels={6:"1",7:"NS?",8:"X"},xlim=(5.2,9.5))

# No Demand after Weakness
nd=[
(18.2,18.3,17.8,17.9,210),(17.9,18.0,17.5,17.6,230),(17.6,17.7,17.2,17.3,250),
(17.3,17.45,17.05,17.12,270),(17.12,17.3,17.0,17.25,160),
(17.25,17.48,17.2,17.42,95),(17.42,17.58,17.37,17.50,72),(17.50,17.60,17.43,17.52,60),
(17.52,17.55,17.15,17.22,190),(17.22,17.28,16.88,16.95,240),(16.95,17.02,16.62,16.70,260)
]
chart(nd,"No Demand sau Weakness","Nhịp hồi volume thấp không lấy lại được kháng cự; Supply quay lại.",
      "ch02_no_demand_overview.png",resistance=17.6,labels={7:"ND?",8:"XÁC NHẬN"})
chart(nd,"Phóng to No Demand candidate","Effort mua thấp, Result tăng nhỏ; bar giảm sau đó xác nhận.",
      "ch02_no_demand_zoom.png",resistance=17.6,labels={6:"1",7:"ND?",8:"X"},xlim=(5.2,9.5))


# --- Chapter 03: Spring / Shakeout / Test ---
spring=[
(14.8,15.0,14.5,14.65,150),(14.65,14.9,14.4,14.55,145),(14.55,14.8,14.35,14.6,138),
(14.6,14.85,14.4,14.72,132),(14.72,14.95,14.5,14.58,128),(14.58,14.7,14.1,14.25,190),
(14.25,14.72,14.05,14.62,225),(14.62,14.78,14.36,14.48,105),(14.48,14.66,14.38,14.57,72),
(14.57,14.98,14.52,14.9,165),(14.9,15.2,14.85,15.12,205)
]
chart(spring,"Spring candidate và Test","Xuyên hỗ trợ, quay lại Range; Test sau đó có volume thấp.",
      "ch03_spring_overview.png",support=14.4,labels={5:"XUYÊN",6:"QUAY LẠI",8:"TEST",9:"DEMAND"})
chart(spring,"Phóng to Spring → Test","Rejection giá thấp rồi Test với Effort bán thấp.",
      "ch03_spring_zoom.png",support=14.4,labels={5:"1",6:"2",8:"TEST",9:"X"},xlim=(4.3,10.1))

# --- Chapter 04: SOS / Retest / LPS ---
sos=[
(16.0,16.2,15.8,16.1,125),(16.1,16.35,16.0,16.28,145),(16.28,16.5,16.2,16.42,160),
(16.42,16.65,16.35,16.55,155),(16.55,16.7,16.4,16.48,135),(16.48,16.72,16.42,16.66,150),
(16.66,17.05,16.62,16.98,245),(16.98,17.22,16.9,17.15,260),
(17.15,17.2,16.92,17.02,118),(17.02,17.08,16.88,16.98,82),(16.98,17.08,16.91,17.03,70),
(17.03,17.38,17.0,17.32,205),(17.32,17.62,17.25,17.56,240)
]
chart(sos,"SOS → Retest → LPS","Breakout giữ trên cản, pullback volume thấp, Demand quay lại.",
      "ch04_sos_lps_overview.png",resistance=16.7,labels={6:"SOS",9:"LPS?",11:"DEMAND"})
chart(sos,"Phóng to breakout và retest","Acceptance phía trên cản; retest volume giảm cho điểm vào đẹp hơn.",
      "ch04_sos_lps_zoom.png",resistance=16.7,labels={6:"SOS",8:"1",9:"LPS?",10:"2",11:"X"},xlim=(5.0,12.5))


# --- Chapter 05: Markup pullback / Buying Climax ---
mk=[
(18.0,18.3,17.9,18.25,150),(18.25,18.6,18.2,18.55,175),(18.55,18.9,18.5,18.82,190),
(18.82,19.1,18.75,19.02,205),(19.02,19.08,18.8,18.88,135),(18.88,18.93,18.72,18.80,98),
(18.80,18.86,18.68,18.76,72),(18.76,19.12,18.73,19.08,180),(19.08,19.38,19.02,19.31,205),
(19.31,19.68,19.25,19.62,225)
]
chart(mk,"Markup và pullback lành mạnh","Nhịp lùi hẹp, volume giảm; Demand quay lại sau đó.",
      "ch05_markup_overview.png",support=18.7,labels={6:"PULLBACK",7:"DEMAND"})
chart(mk,"Phóng to pullback","Effort bán giảm, hỗ trợ giữ, rồi Demand mở rộng Result.",
      "ch05_markup_zoom.png",support=18.7,labels={4:"1",5:"2",6:"3",7:"X"},xlim=(3.5,8.5))

bc=[
(20.0,20.4,19.9,20.35,180),(20.35,20.8,20.3,20.72,210),(20.72,21.15,20.68,21.08,235),
(21.08,21.6,21.0,21.52,260),(21.52,22.25,21.45,22.12,410),
(22.12,22.32,21.86,22.00,390),(22.00,22.10,21.58,21.68,345),(21.68,21.84,21.30,21.42,300),
(21.42,21.65,21.28,21.55,210)
]
chart(bc,"Buying Climax candidate","Effort tăng vọt cuối nhịp tăng; cần xem Result và phản ứng sau.",
      "ch05_bc_overview.png",labels={4:"BC?",5:"PHẢN ỨNG"})
chart(bc,"Phóng to Buying Climax candidate","Volume rất lớn nhưng giá bắt đầu khó tiến xa.",
      "ch05_bc_zoom.png",labels={4:"BC?",5:"1",6:"2"},xlim=(3.2,7.8))

# --- Chapter 06: decision-process diagrams ---
def save_flow(title, rows, out):
    fig,ax=plt.subplots(figsize=(4.12,5.50),dpi=300,facecolor="white")
    ax.axis("off")
    ax.set_xlim(0,1); ax.set_ylim(0,1)
    y=.92
    ax.text(.5,.965,title,ha="center",va="top",fontsize=11.5,fontweight="bold")
    for idx,(label,desc) in enumerate(rows,1):
        h=.095
        rect=Rectangle((.08,y-h),.84,h,facecolor="white",edgecolor="black",linewidth=1.2)
        ax.add_patch(rect)
        ax.text(.12,y-h/2,f"{idx}. {label}",ha="left",va="center",fontsize=8,fontweight="bold")
        ax.text(.88,y-h/2,desc,ha="right",va="center",fontsize=7.1)
        if idx<len(rows):
            ax.annotate("",xy=(.5,y-h-.028),xytext=(.5,y-h-.002),
                        arrowprops=dict(arrowstyle="-|>",lw=1,color="black"))
        y-=.112
    fig.subplots_adjust(left=.02,right=.98,top=.99,bottom=.02)
    fig.savefig(OUT/out,bbox_inches="tight",dpi=300)
    plt.close(fig)

save_flow("Quy trình đọc Wyckoff/VSA",[
("Bối cảnh","Thị trường chung"),
("Cổ phiếu","Xu hướng • cấu trúc"),
("Pha Wyckoff","A/M/D/Md"),
("Vị trí","Range • breakout • retest"),
("Price + Volume","Spread • Close • Wick"),
("Effort/Result","Nỗ lực vs kết quả"),
("Supply/Demand","Bên nào mất hiệu quả?"),
("Kịch bản","Xác nhận • vô hiệu")
],"ch06_decision_overview.png")

save_flow("Nhánh Breakout / Retest",[
("Tiếp cận kháng cự","Đọc Supply"),
("Breakout","Có Result?"),
("Acceptance","Giữ trên vùng cản"),
("Retest","Volume giảm?"),
("Demand quay lại","Continuation")
],"ch06_decision_breakout.png")

save_flow("Nhánh Spring / Breakdown",[
("Tiếp cận hỗ trợ","Đọc Demand"),
("Xuyên hỗ trợ","Candidate"),
("Quay lại Range?","Rejection"),
("Test","Effort bán giảm?"),
("Ở dưới hỗ trợ?","Acceptance thấp")
],"ch06_decision_spring.png")
