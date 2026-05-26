import streamlit as st

st.set_page_config(page_title="About us",layout="wide")
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
    font-size: 42px !important;
    font-weight: 800 !important;
    color: white !important;
}

h2, h3 {
    color: #c4b5fd !important;
}

/* ===== METRIC CARDS ===== */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(139,92,246,0.35);

    backdrop-filter: blur(12px);

    padding: 20px;

    border-radius: 18px;

    box-shadow:
        0 8px 30px rgba(0,0,0,0.25);

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

/* ===== CHARTS ===== */
div[data-testid="stPlotlyChart"] {
    background: rgba(17,24,39,0.75);

    border: 1px solid rgba(139,92,246,0.2);

    border-radius: 18px;

    padding: 12px;

    margin-top: 10px;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.25);
}

/* ===== BUTTONS ===== */
.stButton > button {
    background: linear-gradient(
        135deg,
        #7c3aed,
        #8b5cf6
    );

    color: white;

    border: none;

    border-radius: 12px;

    padding: 10px 20px;

    font-weight: 600;
}

/* ===== INPUT BOX ===== */
.stTextInput input {
    background-color: #111827 !important;
    color: white !important;

    border: 1px solid #7c3aed !important;

    border-radius: 10px !important;
}

/* ===== MULTISELECT ===== */
[data-baseweb="select"] {
    background-color: #111827 !important;
}

[data-testid="stMultiSelect"] span[data-baseweb="tag"] {
    background-color: #7c3aed !important;
    color: white !important;
}

/* ===== DIVIDER ===== */
hr {
    border-color: rgba(255,255,255,0.08);
}

/* ===== DATAFRAME ===== */
[data-testid="stDataFrame"] {
    border-radius: 16px;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)

st.write("")
# st.title("About us page")


# st.header("Summary")
st.header("📌 About the Project")

# st.markdown("""
# The **Public Transport Delay Analysis System**
# is designed to analyze, monitor, and visualize
# delays in buses and trains using operational
# transport datasets.

# The platform transforms transport data into
# interactive analytics dashboards that help:

# - Analyze delay trends
# - Detect congestion patterns
# - Improve route efficiency
# - Support smarter travel planning
# - Generate AI-powered operational insights
# """)

# c1, c2, c3, c4 = st.columns(4)

# c1.metric("Routes", "20+")
# c2.metric("Trips", "20K+")
# c3.metric("Avg Delay", "7 mins")
# c4.metric("OTP", "89%")

# st.divider()
# st.header("📌 About the Project")

st.markdown("""
Public transport delays create daily frustration for
thousands of passengers. Long waiting times,
unexpected congestion, and inconsistent schedules
make travel planning difficult for students,
employees, and regular commuters.

The **Public Transport Delay Analysis System**
was developed to transform raw transport data into
meaningful insights that help both passengers and
transport organizations make smarter decisions.

Using data analytics, visualization dashboards,
and AI-generated insights, the platform analyzes:

- Route-wise delay patterns
- Congestion trends
- Seasonal impacts
- On-Time Performance (OTP)
- Travel reliability insights

The goal is not just to display transport data —
but to help users understand *why* delays happen
and how they can make better travel decisions.
""")

st.divider()

# ======================================================
# PASSENGER POV
# ======================================================

st.subheader("🚍 How It Helps Passengers")


st.markdown("""
Many people use public transport every day for
college, work, shopping, and other daily activities.
But delays and traffic congestion can make travel
stressful and unpredictable.

Our system helps passengers better understand
transport delays and travel patterns so they can
plan their journeys more easily.

### How Users Benefit:
- Find routes that are usually delayed
- Know which timings are more crowded
- Choose better travel timings
- Reduce long waiting times
- Travel with better planning and awareness
- Get simple AI-generated travel insights

### Example:
Imagine a student going to college every day.

Sometimes the bus may arrive late because of
heavy traffic or congestion during peak hours.

Using our platform, the student can understand:
- which routes are often delayed,
- what time congestion is highest,
- and which timings are more reliable for travel.

This helps passengers save time and avoid
unnecessary waiting.
""")

st.divider()

# ======================================================
# AUTHORITY POV
# ======================================================

st.subheader("🏢 How It Helps Transport Organizations")

st.markdown("""
Transport organizations handle large volumes of
operational data every day, but identifying hidden
delay patterns manually can be difficult.

Our platform helps authorities convert transport data
into actionable operational insights.

### Key Benefits for Authorities:
- Detect routes with repeated delays
- Analyze congestion hotspots
- Monitor route performance
- Study seasonal delay behavior
- Improve scheduling efficiency
- Support data-driven planning

The system enables organizations to make informed
decisions that can improve operational performance
and passenger experience.
""")


st.divider()
