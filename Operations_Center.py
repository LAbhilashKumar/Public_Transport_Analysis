import streamlit as st

st.set_page_config(
    page_title="Public Transport Delay Analysis",
    layout="wide"
)

st.write(" ")

st.markdown("""
<style>

/* ===== MAIN APP ===== */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #111827 50%,
        #1e1b4b 100%
    );
    color: #f8fafc;
}

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {
    background: #0b1120;
    border-right: 1px solid #312e81;
}

section[data-testid="stSidebar"]::before {
    content: "🚍 Route Analytics";
    display: block;
    padding: 22px 20px;
    font-size: 28px;
    font-weight: 700;
    color: white;
    border-bottom: 1px solid #312e81;
}

/* ===== TITLES ===== */
h1 {
    font-size: 52px !important;
    font-weight: 800 !important;
    color: white !important;
    text-align: center;
    margin-top: 40px;
}

h2, h3 {
    color: #c4b5fd !important;
}

/* ===== HERO BOX ===== */
.hero-box {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(139,92,246,0.25);
    border-radius: 24px;
    padding: 45px;
    margin-top: 30px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.25);
}

/* ===== CENTER TEXT ===== */
.center-text {
    text-align: center;
    font-size: 18px;
    color: #d1d5db;
    max-width: 950px;
    margin: auto;
    line-height: 1.8;
    padding-top: 20px;
}

/* ===== INFO BOX ===== */
div[data-testid="stAlert"] {
    border-radius: 14px;
    border: 1px solid rgba(139,92,246,0.25);
    background: rgba(255,255,255,0.04);
}

/* ===== METRIC CARDS ===== */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(139,92,246,0.35);
    backdrop-filter: blur(12px);
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.25);
    transition: all 0.3s ease;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-4px);
    border-color: #8b5cf6;
}

[data-testid="stMetricLabel"] {
    color: #d8b4fe !important;
    font-size: 15px !important;
}

[data-testid="stMetricValue"] {
    color: white !important;
    font-size: 32px !important;
    font-weight: 700 !important;
}

/* ===== DIVIDER ===== */
hr {
    border-color: rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# HERO SECTION
# ======================================================

st.markdown("""
<div class="hero-box">

<h1>Public Transport Delay Analysis</h1>

<p class="center-text">
Explore how traffic conditions, congestion levels, weather patterns,
and peak-hour operations affect public transport delays across routes and time periods.
</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# ======================================================
# USER INSIGHTS SECTION
# ======================================================

st.header("What You Can Discover")

col1, col2 = st.columns(2)

with col1:

    st.info("📍 Identify routes with frequent delays")

    st.info("🚦 Understand how congestion impacts travel time")

    st.info("⏱ Discover peak-hour delay patterns")

with col2:

    st.info("🌦 Analyze weather-related transport disruptions")

    st.info("📈 Compare delay behavior across different time periods")

    st.info("🚌 Explore operational performance trends across routes")

st.divider()

# ======================================================
# METRICS SECTION
# ======================================================

st.header("Operational Metrics")

m1, m2, m3, m4 = st.columns(4, gap="large")

with m1:
    st.metric("Total Records", "20K+")

with m2:
    st.metric("Analyzed Trips", "15K+")

with m3:
    st.metric("Average Delay", "7 mins")

with m4:
    st.metric("On-Time Performance", "89%")

st.write("")
st.write("")

st.caption("Public Transport Analytics Dashboard")
