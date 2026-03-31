import streamlit as st

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="MBAL Digital Transformation Progress",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# GOAL DATA
# ─────────────────────────────────────────────
GOALS = [
    {
        "num": "01",
        "title": "Digital-First Company",
        "subtitle": "Transform MBAL into a fully digital-first organization",
        "color": "#00E5A0",
        "icon": "◈",
        "progress": 68,
        "phase": "Scaling",
        "achieved": [
            "Enterprise BI platform live on Microsoft Fabric",
            "Power BI dashboards deployed across Finance, Sales & Procurement",
            "Axon Signage website 80% complete",
            "Digital branding guidelines rolled out group-wide",
            "GA4 analytics configured across web properties",
            "WhatsApp Business verified and operational",
        ],
        "in_motion": [
            "New Axon Full Profile buildout (7/11 milestones done)",
            "Axon Integrated Website in development",
            "IWantASafe.com platform in planning",
            "Malco Properties web platform scoped",
            "Service tariff digitization underway",
            "800 Axon phone integration initiated",
        ],
    },
    {
        "num": "02",
        "title": "AI & Automation",
        "subtitle": "Achieve 40%–60% operational efficiency through intelligent automation",
        "color": "#00BFFF",
        "icon": "⚡",
        "progress": 45,
        "phase": "Building",
        "achieved": [
            "Microsoft Fabric medallion architecture operational (Bronze → Silver → Gold)",
            "Automated data pipelines from Oracle Orion ERP",
            "EMX delivery logistics fully automated (9/9)",
            "Shopify delivery staffing automated (3/3)",
            "GallaBox WhatsApp chatbot flows live for customer engagement",
            "Procurement key handover letter generation automated",
        ],
        "in_motion": [
            "EMX API integration for end-to-end delivery automation",
            "Dashboard redesign for smarter decision-making",
            "Telegram AI BI bot in development (DeepSeek + GraphQL)",
            "Fabric GraphQL API enabling external data access",
            "ERP modernization evaluation completed (Odoo vs Orion)",
        ],
    },
    {
        "num": "03",
        "title": "Online Channel Enablement",
        "subtitle": "Activate and scale digital commerce across all group companies",
        "color": "#FF6B35",
        "icon": "◉",
        "progress": 52,
        "phase": "Expanding",
        "achieved": [
            "Shopify storefront live with payment gateway (Paymob)",
            "Amazon marketplace activated with first product batches sent",
            "Trendyol marketplace onboarding initiated",
            "eCom credit card processing enabled",
            "Product catalog digitized (PDF → structured data → listings)",
            "Partners' KPI framework completed (5/5)",
            "Brand registries advancing (Chubbsafes, Legamaster, Shinjin)",
        ],
        "in_motion": [
            "Amazon Universal Catalog integration",
            "Trendyol storefront activation",
            "IWantASafe.com digital channels launching",
            "Delivery logic being built into Shopify",
            "Malco Properties payment link enablement",
            "Multi-brand email outreach to channel partners completed",
        ],
    },
    {
        "num": "04",
        "title": "Central M Marketplace",
        "subtitle": "Build and launch the unified MBAL Group marketplace platform",
        "color": "#C084FC",
        "icon": "▣",
        "progress": 30,
        "phase": "Foundation",
        "achieved": [
            "Universal product catalog structure defined",
            "Partners' KPI & payment frequency framework established",
            "Brand registries initiated across key product lines",
            "Multi-marketplace strategy validated (Amazon, Trendyol, Shopify)",
            "Product photography & pack shots completed for first batch",
        ],
        "in_motion": [
            "One-Pager strategic brief in progress",
            "Amazon product details feeding into universal catalog",
            "Trendyol activation expanding the marketplace footprint",
            "Brands email follow-up outreach completed (3/3)",
            "Platform partner evaluation underway",
        ],
    },
]

PHASE_COLORS = {
    "Foundation": "#C084FC",
    "Building": "#00BFFF",
    "Expanding": "#FF6B35",
    "Scaling": "#00E5A0",
}

OVERALL_PROGRESS = 52
MILESTONES_DONE = 139
TOTAL_MILESTONES = 166
WORKSTREAMS = 9


# ─────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300;9..40,500;9..40,700&family=JetBrains+Mono:wght@400;600&display=swap');

.stApp { background: #0A0E17 !important; font-family: 'DM Sans', sans-serif; }
h1, h2, h3, p, span, div, label { color: #F0F0F0 !important; }
#MainMenu, footer, header { visibility: hidden; }
div[data-testid="stDecoration"] { display: none; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 1rem !important; max-width: 1400px; }

/* Stat box */
.stat-box {
    border-radius: 12px; padding: 14px 18px; text-align: center; display: inline-block;
}
.stat-num { font-size: 28px; font-weight: 700; font-family: 'JetBrains Mono', monospace; line-height: 1; }
.stat-label { font-size: 10px; font-weight: 600; letter-spacing: 1px; margin-top: 2px; }

/* Progress ring text */
.ring-pct { font-size: 32px; font-weight: 700; font-family: 'JetBrains Mono', monospace; }
.ring-label { font-size: 10px; color: rgba(255,255,255,0.4) !important; letter-spacing: 1px; text-transform: uppercase; }

/* Goal section */
.goal-section {
    background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px; padding: 24px; margin-bottom: 20px;
}
.goal-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px; }
.goal-num { font-size: 11px; font-family: 'JetBrains Mono', monospace; letter-spacing: 2px; }
.goal-title { font-size: 20px; font-weight: 700; margin: 4px 0 2px 0; }
.goal-sub { font-size: 12px; color: rgba(255,255,255,0.4) !important; }

/* Phase badge */
.phase-badge {
    padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: 600;
    letter-spacing: 0.5px; display: inline-block;
}

/* Progress bar */
.pbar-track { height: 6px; background: rgba(255,255,255,0.06); border-radius: 3px; }
.pbar-fill { height: 100%; border-radius: 3px; }

/* Checklist */
.check-title { font-size: 11px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 10px; }
.check-item {
    font-size: 12px; color: rgba(255,255,255,0.65) !important;
    margin-bottom: 5px; padding-left: 18px; position: relative; line-height: 1.5;
}
.check-done { color: rgba(255,255,255,0.7) !important; }
.check-active { color: rgba(255,255,255,0.5) !important; }

/* Panel */
.panel {
    background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px; padding: 18px; margin-bottom: 14px;
}
.panel-title {
    font-size: 11px; font-weight: 700; letter-spacing: 1px;
    text-transform: uppercase; color: rgba(255,255,255,0.5) !important; margin-bottom: 14px;
}

/* Phase row */
.phase-row { display: flex; align-items: center; margin-bottom: 10px; gap: 12px; }
.phase-dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }
.phase-line { height: 2px; flex: 1; border-radius: 1px; }
.phase-label { font-size: 11px; min-width: 80px; font-weight: 600; }
.phase-goal { font-size: 11px; color: rgba(255,255,255,0.4) !important; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.markdown(
    '<div style="font-size:10px;color:rgba(255,255,255,0.35);letter-spacing:3px;'
    "font-family:'JetBrains Mono',monospace;margin-bottom:4px;\">MBAL GROUP</div>",
    unsafe_allow_html=True,
)
st.markdown(
    '<h1 style="margin:0;font-size:30px;font-weight:700;">Digital Transformation Progress</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div style="font-size:12px;color:rgba(255,255,255,0.4);margin-top:2px;">Tracking strategic progress across 4 pillars</div>',
    unsafe_allow_html=True,
)
st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# TOP STATS ROW
# ─────────────────────────────────────────────
s1, s2, s3, s4 = st.columns(4, gap="small")

with s1:
    st.markdown(
        f"""<div class="stat-box" style="background:#00E5A010;border:1px solid #00E5A030;width:100%;">
            <div class="stat-num" style="color:#00E5A0;">{OVERALL_PROGRESS}%</div>
            <div class="stat-label" style="color:#00E5A0;">Overall Progress</div>
        </div>""", unsafe_allow_html=True)

with s2:
    st.markdown(
        f"""<div class="stat-box" style="background:#00BFFF10;border:1px solid #00BFFF30;width:100%;">
            <div class="stat-num" style="color:#00BFFF;">{MILESTONES_DONE}</div>
            <div class="stat-label" style="color:#00BFFF;">Milestones Delivered</div>
        </div>""", unsafe_allow_html=True)

with s3:
    st.markdown(
        f"""<div class="stat-box" style="background:#FF6B3510;border:1px solid #FF6B3530;width:100%;">
            <div class="stat-num" style="color:#FF6B35;">{WORKSTREAMS}</div>
            <div class="stat-label" style="color:#FF6B35;">Active Workstreams</div>
        </div>""", unsafe_allow_html=True)

with s4:
    st.markdown(
        f"""<div class="stat-box" style="background:#C084FC10;border:1px solid #C084FC30;width:100%;">
            <div class="stat-num" style="color:#C084FC;">4 / 4</div>
            <div class="stat-label" style="color:#C084FC;">Goals In Motion</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<div style='height:24px;'></div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# GOAL SECTIONS (2 per row)
# ─────────────────────────────────────────────
for row_start in range(0, 4, 2):
    cols = st.columns(2, gap="medium")
    for idx, col in enumerate(cols):
        g = GOALS[row_start + idx]
        pc = PHASE_COLORS.get(g["phase"], "#888")

        achieved_html = "".join(
            f'<div class="check-item check-done"><span style="position:absolute;left:0;color:{g["color"]};">✓</span>{a}</div>'
            for a in g["achieved"]
        )
        motion_html = "".join(
            f'<div class="check-item check-active"><span style="position:absolute;left:0;color:rgba(255,255,255,0.3);">○</span>{m}</div>'
            for m in g["in_motion"]
        )

        with col:
            st.markdown(
                f"""<div class="goal-section">
                    <div class="goal-header">
                        <div style="flex:1;">
                            <div class="goal-num" style="color:{g['color']};">GOAL {g['num']}</div>
                            <div class="goal-title">{g['icon']}  {g['title']}</div>
                            <div class="goal-sub">{g['subtitle']}</div>
                        </div>
                        <div style="text-align:right;">
                            <div style="font-size:32px;font-weight:700;color:{g['color']};font-family:'JetBrains Mono',monospace;line-height:1;">{g['progress']}%</div>
                            <div class="phase-badge" style="background:{pc}18;color:{pc};border:1px solid {pc}40;margin-top:6px;">{g['phase']}</div>
                        </div>
                    </div>
                    <div class="pbar-track" style="margin-bottom:20px;">
                        <div class="pbar-fill" style="width:{g['progress']}%;background:{g['color']};"></div>
                    </div>
                    <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;">
                        <div>
                            <div class="check-title" style="color:{g['color']};">✦ Achieved</div>
                            {achieved_html}
                        </div>
                        <div>
                            <div class="check-title" style="color:rgba(255,255,255,0.4);">○ In Motion</div>
                            {motion_html}
                        </div>
                    </div>
                </div>""",
                unsafe_allow_html=True,
            )

st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# BOTTOM ROW: Transformation Journey + Summary
# ─────────────────────────────────────────────
import streamlit.components.v1 as components

COMPONENT_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300;9..40,500;9..40,700&family=JetBrains+Mono:wght@400;600&display=swap');
body { margin:0; padding:0; background:transparent; font-family:'DM Sans',sans-serif; color:#F0F0F0; }
.panel { background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.06); border-radius:14px; padding:18px; }
.panel-title { font-size:11px; font-weight:700; letter-spacing:1px; text-transform:uppercase; color:rgba(255,255,255,0.5); margin-bottom:14px; }
.pbar-track { height:4px; background:rgba(255,255,255,0.06); border-radius:2px; margin-top:4px; }
.pbar-fill { height:100%; border-radius:2px; }
</style>
"""

b1, b2 = st.columns([3, 2], gap="medium")

with b1:
    phases_data = [
        {"label": "Foundation", "desc": "Infrastructure, tools & team setup", "done": True},
        {"label": "Building", "desc": "Automation pipelines & platform development", "done": True},
        {"label": "Expanding", "desc": "Multi-channel activation & scaling", "current": True},
        {"label": "Scaling", "desc": "Full digital operations across the group"},
    ]
    rows = ""
    for i, p in enumerate(phases_data):
        if p.get("done"):
            dot_bg = "#00E5A0"
            lbl_c = "#00E5A0"
            check = "✓"
        elif p.get("current"):
            dot_bg = "#FF6B35"
            lbl_c = "#FF6B35"
            check = "●"
        else:
            dot_bg = "rgba(255,255,255,0.12)"
            lbl_c = "rgba(255,255,255,0.3)"
            check = "○"
        line_bg = "#00E5A0" if p.get("done") else "rgba(255,255,255,0.08)"
        connector = f'<div style="height:20px;margin-left:4px;width:2px;background:{line_bg};"></div>' if i < 3 else ""
        glow = "box-shadow:0 0 8px #FF6B3580;" if p.get("current") else ""
        rows += f"""
        <div style="display:flex;align-items:flex-start;gap:14px;">
          <div style="display:flex;flex-direction:column;align-items:center;">
            <div style="width:10px;height:10px;border-radius:50%;background:{dot_bg};{glow}flex-shrink:0;margin-top:4px;"></div>
            {connector}
          </div>
          <div style="padding-bottom:8px;">
            <div style="font-size:13px;font-weight:700;color:{lbl_c};">
              <span style="color:{lbl_c};margin-right:6px;">{check}</span>{p['label']}
            </div>
            <div style="font-size:11px;color:rgba(255,255,255,0.35);">{p['desc']}</div>
          </div>
        </div>"""

    components.html(
        f"""{COMPONENT_CSS}
        <div class="panel">
            <div class="panel-title">Transformation Journey</div>
            {rows}
        </div>""",
        height=260,
    )

with b2:
    bars = ""
    for g in GOALS:
        bars += f"""
        <div style="margin-bottom:16px;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
            <span style="font-size:12px;color:rgba(255,255,255,0.6);">{g['icon']}  {g['title']}</span>
            <span style="font-size:13px;color:{g['color']};font-family:'JetBrains Mono',monospace;font-weight:700;">{g['progress']}%</span>
          </div>
          <div class="pbar-track"><div class="pbar-fill" style="width:{g['progress']}%;background:{g['color']};"></div></div>
          <div style="font-size:10px;color:rgba(255,255,255,0.3);margin-top:3px;">{g['phase']} phase · {len(g['achieved'])} milestones achieved</div>
        </div>"""

    components.html(
        f"""{COMPONENT_CSS}
        <div class="panel">
            <div class="panel-title">Goal Progress Summary</div>
            {bars}
        </div>""",
        height=260,
    )
