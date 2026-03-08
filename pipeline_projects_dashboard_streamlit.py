import streamlit as st
import pandas as pd
import altair as alt
from datetime import date

st.set_page_config(
    page_title="Leads & Opportunities",
    page_icon="📌",
    layout="wide",
    initial_sidebar_state="expanded",
)

TRACKER_UPDATED = pd.Timestamp("2026-02-24")
DEFAULT_AS_OF = date(2026, 3, 8)


@st.cache_data
def create_seed_data() -> pd.DataFrame:
    records = [
        {
            "Opportunity": "Amref - resubmitted",
            "Category": "In Process",
            "Status": "Through to next round",
            "Lead": "Go",
            "Partner / Sponsor": "Amref",
            "Focus Area": "General",
            "Submission Date": "2026-01-09",
            "Deadline": "2026-02-28",
            "Stage": "In Process",
            "Funding Amount": 50000,
            "Funding Currency": "USD",
            "Notes": "Through to next round.",
        },
        {
            "Opportunity": "EDCTP Global collaboration action",
            "Category": "In Process",
            "Status": "In process",
            "Lead": "FV",
            "Partner / Sponsor": "EDCTP / Utrecht / Heidelberg / Amsterdam",
            "Focus Area": "HIV / Comorbidity",
            "Submission Date": None,
            "Deadline": "2026-03-04",
            "Stage": "Stage 1 Submission",
            "Funding Amount": 5000000,
            "Funding Currency": "EUR",
            "Notes": "Two-stage application.",
        },
        {
            "Opportunity": "Three other EDCTP opportunities",
            "Category": "In Process",
            "Status": "In process",
            "Lead": "Various",
            "Partner / Sponsor": "EDCTP",
            "Focus Area": "HIV / Cannabis / Comorbidity",
            "Submission Date": None,
            "Deadline": "2026-03-04",
            "Stage": "In Process",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Cannabis, HIV cure, comorbidity.",
        },
        {
            "Opportunity": "NIH R21/33: RISE",
            "Category": "In Process",
            "Status": "Due soon",
            "Lead": "Nicola Bulled / Wits",
            "Partner / Sponsor": "NIH / UMass",
            "Focus Area": "HIV / Comorbidity",
            "Submission Date": None,
            "Deadline": "2026-03-15",
            "Stage": "Proposal Development",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Low-resource urban communities in South Africa.",
        },
        {
            "Opportunity": "Wellcome Discovery 2",
            "Category": "In Process",
            "Status": "Review discussion ongoing",
            "Lead": "FV / Jen / Suman",
            "Partner / Sponsor": "Wellcome",
            "Focus Area": "Research",
            "Submission Date": None,
            "Deadline": "2026-03-31",
            "Stage": "Review / Rework",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Review meeting completed.",
        },
        {
            "Opportunity": "Wellcome Discovery 1 Reloaded",
            "Category": "In Process",
            "Status": "Concept submitted",
            "Lead": "FV / Jenn / Holly",
            "Partner / Sponsor": "Wellcome",
            "Focus Area": "Research",
            "Submission Date": None,
            "Deadline": "2026-07-31",
            "Stage": "Concept / Reapply",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "July 2026 target round.",
        },
        {
            "Opportunity": "Wellcome Clinical Trials",
            "Category": "In Process",
            "Status": "Call expected",
            "Lead": "FV",
            "Partner / Sponsor": "Wellcome",
            "Focus Area": "Clinical Trials",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "Watchlist",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Possible generic Sema study.",
        },
        {
            "Opportunity": "CHAI Len/CAB switch/naive",
            "Category": "In Process",
            "Status": "Concept circulated",
            "Lead": "FV",
            "Partner / Sponsor": "CHAI / Gates",
            "Focus Area": "Len / HIV",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "Concept",
            "Funding Amount": 3000000,
            "Funding Currency": "USD",
            "Notes": "Additional $2m may be needed.",
        },
        {
            "Opportunity": "Novo obesity trials opportunity",
            "Category": "In Process",
            "Status": "Concept to be written",
            "Lead": "Tarryn / Alison",
            "Partner / Sponsor": "Novo",
            "Focus Area": "Obesity",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "Concept",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Investigator-led studies.",
        },
        {
            "Opportunity": "Chinese Pharmaceutical",
            "Category": "In Process",
            "Status": "Unfunded for now",
            "Lead": "Francois / Simiso",
            "Partner / Sponsor": "Chinese Pharmaceutical",
            "Focus Area": "Pharma",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "Early Discussion",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Roger Bedimo wants to chat.",
        },
        {
            "Opportunity": "London Growth Capital / Baby Trump",
            "Category": "In Process",
            "Status": "Monitoring",
            "Lead": "Nkuli",
            "Partner / Sponsor": "London Growth Capital",
            "Focus Area": "Sepsis",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "Watchlist",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Probably not a fit.",
        },
        {
            "Opportunity": "Merck CRO / Oncology HIV study",
            "Category": "In Process",
            "Status": "Looking into it",
            "Lead": "Nkuli",
            "Partner / Sponsor": "Merck",
            "Focus Area": "Oncology / HIV",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "Early Review",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Review underway.",
        },
        {
            "Opportunity": "Eli Lilly diabetes and obesity projects",
            "Category": "In Process",
            "Status": "Follow-up required",
            "Lead": "Nkuli",
            "Partner / Sponsor": "Eli Lilly",
            "Focus Area": "Diabetes / Obesity",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "Follow-up",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Further viability check needed.",
        },
        {
            "Opportunity": "Sema/Cagril Pharma study",
            "Category": "In Process",
            "Status": "Contract coming",
            "Lead": "Simiso",
            "Partner / Sponsor": "Pharma",
            "Focus Area": "Sema / Cagril",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "Contracting",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "15–20 participants.",
        },
        {
            "Opportunity": "FHI 360 long-acting prevention",
            "Category": "In Process",
            "Status": "Follow-up needed",
            "Lead": "Francois / Hally / Chris",
            "Partner / Sponsor": "FHI 360",
            "Focus Area": "Prevention",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "Follow-up",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Meeting follow-up required.",
        },
        {
            "Opportunity": "EDCTP - PK, Reg Ethics capacity",
            "Category": "In Process",
            "Status": "Likely August submission",
            "Lead": "Nkuli",
            "Partner / Sponsor": "EDCTP / NEPAD",
            "Focus Area": "Capacity Building",
            "Submission Date": None,
            "Deadline": "2026-08-15",
            "Stage": "Planning",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "1-stage application.",
        },
        {
            "Opportunity": "Phoenix group quotes",
            "Category": "In Process",
            "Status": "None presently",
            "Lead": "Mo",
            "Partner / Sponsor": "Phoenix Group",
            "Focus Area": "Quotes",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "Dormant",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Discuss with Mo.",
        },
        {
            "Opportunity": "University of British Columbia - small application",
            "Category": "In Process",
            "Status": "Submitted on our behalf",
            "Lead": "Nkuli / Jamie Forrest",
            "Partner / Sponsor": "University of British Columbia",
            "Focus Area": "Academic",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "Submitted",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Small application.",
        },
        {
            "Opportunity": "MISP - opti dor",
            "Category": "In Process",
            "Status": "In process",
            "Lead": "Unknown",
            "Partner / Sponsor": "MISP",
            "Focus Area": "MISP",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "In Process",
            "Funding Amount": 1000000,
            "Funding Currency": "USD",
            "Notes": "Approx $1m.",
        },
        {
            "Opportunity": "Gates Grand Challenges - AI decision support",
            "Category": "New Opportunity",
            "Status": "For consideration",
            "Lead": "TBD",
            "Partner / Sponsor": "Gates",
            "Focus Area": "AI / Primary Care",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "New Opportunity",
            "Funding Amount": 3000000,
            "Funding Currency": "USD",
            "Notes": "Pathway A and B available.",
        },
        {
            "Opportunity": "Leeds-Wits Horizons platform",
            "Category": "New Opportunity",
            "Status": "For consideration",
            "Lead": "TBD",
            "Partner / Sponsor": "Leeds-Wits",
            "Focus Area": "Climate and Health",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "New Opportunity",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Three small opportunities.",
        },
        {
            "Opportunity": "GACD 11th funding round - Joint Process",
            "Category": "New Opportunity",
            "Status": "Suggested go",
            "Lead": "Sam",
            "Partner / Sponsor": "GACD",
            "Focus Area": "Multisectoral approaches",
            "Submission Date": None,
            "Deadline": "2026-06-17",
            "Stage": "New Opportunity",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Use Healthy Jozi phase 1 learnings.",
        },
        {
            "Opportunity": "UK MRC partnership grant",
            "Category": "New Opportunity",
            "Status": "Co-lead only",
            "Lead": "TBD",
            "Partner / Sponsor": "UK MRC",
            "Focus Area": "Research Grant",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "New Opportunity",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Rolling submission.",
        },
        {
            "Opportunity": "UK MRC research grant",
            "Category": "New Opportunity",
            "Status": "Co-lead only",
            "Lead": "TBD",
            "Partner / Sponsor": "UK MRC",
            "Focus Area": "Research Grant",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "New Opportunity",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Rolling submission.",
        },
        {
            "Opportunity": "PATH opportunities with Kim",
            "Category": "New Opportunity",
            "Status": "Email discussion",
            "Lead": "Mo",
            "Partner / Sponsor": "PATH",
            "Focus Area": "Len / Dx / Pharmacy Health",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "New Opportunity",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Discussion ongoing.",
        },
        {
            "Opportunity": "5FC - Jeremy Nel",
            "Category": "New Opportunity",
            "Status": "Explore as EzCRO",
            "Lead": "Nkuli",
            "Partner / Sponsor": "5FC",
            "Focus Area": "EzCRO",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "New Opportunity",
            "Funding Amount": 300000,
            "Funding Currency": "ZAR",
            "Notes": "R300,000 opportunity.",
        },
        {
            "Opportunity": "PICASSO 2 for Len",
            "Category": "New Opportunity",
            "Status": "For consideration",
            "Lead": "Francois / Simiso",
            "Partner / Sponsor": "PICASSO 2",
            "Focus Area": "Len",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "New Opportunity",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "For Len.",
        },
        {
            "Opportunity": "GES Labs cannabis work",
            "Category": "New Opportunity",
            "Status": "Next step call",
            "Lead": "TBD",
            "Partner / Sponsor": "GES Labs",
            "Focus Area": "Cannabis",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "New Opportunity",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Call with Peter Nel and team.",
        },
        {
            "Opportunity": "Wellcome early career award",
            "Category": "Submitted - Awaiting Decision",
            "Status": "Awaiting decision",
            "Lead": "Spha",
            "Partner / Sponsor": "Wellcome",
            "Focus Area": "Early Career",
            "Submission Date": "2026-02-16",
            "Deadline": None,
            "Stage": "Submitted",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Awaiting decision.",
        },
        {
            "Opportunity": "Multiplex/Diagnostics Unitaid",
            "Category": "Submitted - Awaiting Decision",
            "Status": "Submitted",
            "Lead": "Ezintsha / PSI",
            "Partner / Sponsor": "Unitaid",
            "Focus Area": "Diagnostics",
            "Submission Date": "2026-01-29",
            "Deadline": None,
            "Stage": "Submitted",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Ezintsha prime, PSI support.",
        },
        {
            "Opportunity": "BioEquivalence Morphine Sulphate Oral products",
            "Category": "Submitted - Awaiting Decision",
            "Status": "Budget submitted",
            "Lead": "TBD",
            "Partner / Sponsor": "Unknown",
            "Focus Area": "Bioequivalence",
            "Submission Date": "2026-01-19",
            "Deadline": None,
            "Stage": "Submitted",
            "Funding Amount": 500000,
            "Funding Currency": "USD",
            "Notes": "Approx $500,000.",
        },
        {
            "Opportunity": "Merck MISP Sleep",
            "Category": "Submitted - Awaiting Decision",
            "Status": "Review comments addressed",
            "Lead": "Tarryn",
            "Partner / Sponsor": "Merck",
            "Focus Area": "Sleep",
            "Submission Date": "2025-11-17",
            "Deadline": None,
            "Stage": "Submitted",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Reviewer comments addressed.",
        },
        {
            "Opportunity": "Open Society Foundations - IMITHI concept",
            "Category": "Submitted - Awaiting Decision",
            "Status": "Waiting on OSF",
            "Lead": "Nkuli",
            "Partner / Sponsor": "Open Society Foundations",
            "Focus Area": "IMITHI",
            "Submission Date": "2025-10-15",
            "Deadline": None,
            "Stage": "Submitted",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Tricky sell.",
        },
        {
            "Opportunity": "SA MRC SIR grant - iHEART follow up",
            "Category": "Submitted - Awaiting Decision",
            "Status": "Awaiting decision",
            "Lead": "Spha",
            "Partner / Sponsor": "SA MRC",
            "Focus Area": "iHEART",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "Submitted",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Follow up.",
        },
        {
            "Opportunity": "University of British Columbia - small application",
            "Category": "Submitted - Awaiting Decision",
            "Status": "Submitted on our behalf",
            "Lead": "Jamie Forrest",
            "Partner / Sponsor": "University of British Columbia",
            "Focus Area": "Academic",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "Submitted",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Small application.",
        },
        {
            "Opportunity": "Talisman 2/IMPRESS",
            "Category": "Recent Decision",
            "Status": "Not successful",
            "Lead": "Sam",
            "Partner / Sponsor": "Unknown",
            "Focus Area": "Research",
            "Submission Date": "2025-09-16",
            "Deadline": None,
            "Stage": "Decision",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Not successful.",
        },
        {
            "Opportunity": "HERO vaccine work",
            "Category": "Recent Decision",
            "Status": "Cancelled",
            "Lead": "Simiso",
            "Partner / Sponsor": "NIH",
            "Focus Area": "Vaccine",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "Decision",
            "Funding Amount": 20000,
            "Funding Currency": "USD",
            "Notes": "Funding withdrawn.",
        },
        {
            "Opportunity": "COMBAT Trial",
            "Category": "Recent Decision",
            "Status": "Not successful",
            "Lead": "Unknown",
            "Partner / Sponsor": "Unknown",
            "Focus Area": "Clinical Trial",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "Decision",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Not successful.",
        },
        {
            "Opportunity": "Gilead INCLUSION",
            "Category": "Recent Decision",
            "Status": "No go",
            "Lead": "PSI",
            "Partner / Sponsor": "Gilead",
            "Focus Area": "Inclusion",
            "Submission Date": "2026-01-30",
            "Deadline": None,
            "Stage": "Decision",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "Budget small, drug unavailable.",
        },
        {
            "Opportunity": "ANRS",
            "Category": "Recent Decision",
            "Status": "Not successful",
            "Lead": "FV / Tarryn",
            "Partner / Sponsor": "ANRS",
            "Focus Area": "Research",
            "Submission Date": "2025-09-15",
            "Deadline": None,
            "Stage": "Decision",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "To discuss.",
        },
        {
            "Opportunity": "HBNU Fogarty Global Health Fellowship",
            "Category": "Recent Decision",
            "Status": "Not successful",
            "Lead": "Spha / Sam",
            "Partner / Sponsor": "Fogarty",
            "Focus Area": "Global Health Fellowship",
            "Submission Date": None,
            "Deadline": None,
            "Stage": "Decision",
            "Funding Amount": None,
            "Funding Currency": "Unknown",
            "Notes": "May repurpose concept.",
        },
    ]

    df = pd.DataFrame(records)
    df["Submission Date"] = pd.to_datetime(df["Submission Date"], errors="coerce")
    df["Deadline"] = pd.to_datetime(df["Deadline"], errors="coerce")
    df["Funding Amount"] = pd.to_numeric(df["Funding Amount"], errors="coerce")
    return df


def fmt_money(amount: float, currency: str) -> str:
    if pd.isna(amount):
        return "Not stated"
    symbol = {"USD": "$", "EUR": "€", "ZAR": "R"}.get(currency, "")
    if amount >= 1_000_000:
        return f"{symbol}{amount / 1_000_000:.1f}M"
    if amount >= 1_000:
        return f"{symbol}{amount / 1_000:.0f}K"
    return f"{symbol}{amount:,.0f}"


def status_tone(status: str) -> str:
    s = str(status).lower()
    if any(x in s for x in ["cancel", "not successful", "no go", "overdue"]):
        return "negative"
    if any(x in s for x in ["await", "follow", "review", "discussion", "looking", "due soon"]):
        return "warning"
    if any(x in s for x in ["submitted", "through", "concept", "in process", "suggested go", "contract"]):
        return "positive"
    return "neutral"


def deadline_tone(days):
    if pd.isna(days):
        return "neutral"
    if days < 0:
        return "negative"
    if days <= 7:
        return "negative"
    if days <= 30:
        return "warning"
    return "positive"


def badge(text: str, tone: str = "neutral") -> str:
    colors = {
        "positive": ("#DCFCE7", "#166534"),
        "warning": ("#FEF3C7", "#92400E"),
        "negative": ("#FEE2E2", "#991B1B"),
        "neutral": ("#E2E8F0", "#334155"),
        "brand": ("#DBEAFE", "#1D4ED8"),
    }
    bg, fg = colors.get(tone, colors["neutral"])
    return (
        f"<span style='display:inline-block;padding:4px 10px;border-radius:999px;"
        f"background:{bg};color:{fg};font-size:12px;font-weight:700;'>{text}</span>"
    )


def add_display_columns(df: pd.DataFrame, as_of_ts: pd.Timestamp) -> pd.DataFrame:
    out = df.copy()
    out["Days to Deadline"] = (out["Deadline"] - as_of_ts).dt.days
    out["Funding Display"] = out.apply(
        lambda r: fmt_money(r["Funding Amount"], r["Funding Currency"]), axis=1
    )
    out["Deadline Status"] = out["Days to Deadline"].apply(
        lambda x: "No deadline"
        if pd.isna(x)
        else "Overdue"
        if x < 0
        else "Due in 7 days"
        if x <= 7
        else "Due in 30 days"
        if x <= 30
        else "Future"
    )
    out["Status Tone"] = out["Status"].apply(status_tone)
    out["Deadline Tone"] = out["Days to Deadline"].apply(deadline_tone)
    return out


st.markdown(
    """
    <style>
    :root {
        --line: #E6EBF4;
        --shadow: 0 10px 28px rgba(15, 23, 42, 0.06);
    }
    .stApp {
        background: radial-gradient(circle at top left, #f8fbff 0%, #f6f8fc 35%, #f6f8fc 100%);
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 1480px;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
        border-right: 1px solid rgba(255,255,255,0.06);
    }
    [data-testid="stSidebar"] * {
        color: #f8fafc !important;
    }
    .hero {
        padding: 22px 24px;
        border-radius: 24px;
        background: linear-gradient(135deg, #0f172a 0%, #1d4ed8 55%, #14b8a6 100%);
        color: white;
        box-shadow: 0 18px 40px rgba(29, 78, 216, 0.18);
        margin-bottom: 1rem;
    }
    .hero h1 {
        margin: 0;
        font-size: 2rem;
        line-height: 1.1;
        color: white;
    }
    .hero p {
        margin: 8px 0 0 0;
        color: rgba(255,255,255,0.88);
        max-width: 780px;
    }
    .card {
        background: white;
        border: 1px solid var(--line);
        border-radius: 22px;
        padding: 18px;
        box-shadow: var(--shadow);
    }
    .mini-card {
        background: linear-gradient(180deg, #ffffff 0%, #fbfdff 100%);
        border: 1px solid var(--line);
        border-radius: 20px;
        padding: 16px;
        box-shadow: var(--shadow);
        min-height: 150px;
    }
    .section-title {
        font-size: 1.05rem;
        font-weight: 800;
        margin-bottom: 8px;
        color: #0f172a;
    }
    .toolbar-note {
        color: #64748b;
        font-size: 0.9rem;
        padding-top: 8px;
    }
    div[data-testid="stMetric"] {
        background: linear-gradient(180deg, #ffffff 0%, #fbfdff 100%);
        border: 1px solid var(--line);
        border-radius: 20px;
        padding: 14px;
        box-shadow: var(--shadow);
    }
    div[data-testid="stMetricLabel"] {
        font-weight: 700;
        color: #334155;
    }
    div[data-testid="stDataFrame"] {
        border: 1px solid var(--line);
        border-radius: 18px;
        overflow: hidden;
        box-shadow: var(--shadow);
    }
    .quick-list-item {
        padding: 10px 0;
        border-bottom: 1px solid #eef2f7;
    }
    .quick-list-item:last-child {
        border-bottom: none;
    }
    .quick-title {
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 2px;
    }
    .quick-meta {
        color: #64748b;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <div style="display:flex;justify-content:space-between;gap:18px;align-items:flex-start;flex-wrap:wrap;">
            <div>
                <h1>Leads & Opportunities</h1>
                <p>Executive portfolio view for funding pipeline, sponsors, deadlines, and follow-up actions.</p>
            </div>
            <div style="text-align:right;min-width:220px;">
                <div style="font-size:12px;letter-spacing:0.08em;text-transform:uppercase;opacity:0.75;">Tracker updated</div>
                <div style="font-size:1.1rem;font-weight:800;">24 Feb 2026</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

toolbar_left, toolbar_mid, toolbar_right, toolbar_date = st.columns([1.1, 1.8, 1.1, 1.1])
with toolbar_left:
    view_mode = st.selectbox("View", ["Executive", "Detailed"], index=0)
with toolbar_mid:
    search = st.text_input("Search", placeholder="Opportunity, sponsor, lead, focus area")
with toolbar_right:
    sort_mode = st.selectbox("Sort", ["Deadline", "Funding", "Category", "Lead"], index=0)
with toolbar_date:
    as_of_date = st.date_input("As of date", value=DEFAULT_AS_OF)

as_of_ts = pd.Timestamp(as_of_date)
st.caption(f"As of date: {as_of_ts.date()} | Tracker last updated: {TRACKER_UPDATED.date()}")

st.sidebar.title("Portfolio Filters")
source = st.sidebar.radio("Data source", ["Seeded February 2026 data", "Upload CSV"], index=0)

if source == "Upload CSV":
    uploaded = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    if uploaded is not None:
        df = pd.read_csv(uploaded)
        for col in ["Submission Date", "Deadline"]:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors="coerce")
        if "Funding Amount" in df.columns:
            df["Funding Amount"] = pd.to_numeric(df["Funding Amount"], errors="coerce")
        else:
            df["Funding Amount"] = pd.NA
        if "Funding Currency" not in df.columns:
            df["Funding Currency"] = "Unknown"
        if "Notes" not in df.columns:
            df["Notes"] = ""
    else:
        st.info("No file uploaded yet. Seeded data is displayed.")
        df = create_seed_data()
else:
    df = create_seed_data()

df = add_display_columns(df, as_of_ts)

category_options = sorted(df["Category"].dropna().unique().tolist())
focus_options = sorted(df["Focus Area"].dropna().unique().tolist())
lead_options = sorted(df["Lead"].dropna().unique().tolist())
status_options = sorted(df["Status"].dropna().unique().tolist())
partner_options = sorted(df["Partner / Sponsor"].dropna().unique().tolist())

selected_categories = st.sidebar.multiselect("Category", category_options, default=category_options)
selected_focus = st.sidebar.multiselect("Focus Area", focus_options, default=focus_options)
selected_leads = st.sidebar.multiselect("Lead", lead_options, default=lead_options)
selected_status = st.sidebar.multiselect("Status", status_options, default=status_options)
selected_partners = st.sidebar.multiselect("Sponsor / Partner", partner_options, default=partner_options)
show_deadline_only = st.sidebar.checkbox("Only rows with deadlines")
show_known_funding = st.sidebar.checkbox("Only rows with funding values")

filtered = df[
    df["Category"].isin(selected_categories)
    & df["Focus Area"].isin(selected_focus)
    & df["Lead"].isin(selected_leads)
    & df["Status"].isin(selected_status)
    & df["Partner / Sponsor"].isin(selected_partners)
].copy()

if show_deadline_only:
    filtered = filtered[filtered["Deadline"].notna()].copy()

if show_known_funding:
    filtered = filtered[filtered["Funding Amount"].notna()].copy()

if search:
    q = search.strip().lower()
    filtered = filtered[
        filtered[["Opportunity", "Partner / Sponsor", "Lead", "Focus Area", "Notes"]]
        .fillna("")
        .apply(lambda col: col.str.lower().str.contains(q, regex=False))
        .any(axis=1)
    ].copy()

if sort_mode == "Deadline":
    filtered = filtered.sort_values(["Deadline", "Funding Amount"], ascending=[True, False], na_position="last")
elif sort_mode == "Funding":
    filtered = filtered.sort_values("Funding Amount", ascending=False, na_position="last")
elif sort_mode == "Category":
    filtered = filtered.sort_values(["Category", "Deadline"], ascending=[True, True], na_position="last")
elif sort_mode == "Lead":
    filtered = filtered.sort_values(["Lead", "Deadline"], ascending=[True, True], na_position="last")

total_opps = len(filtered)
in_process = int((filtered["Category"] == "In Process").sum())
new_opps = int((filtered["Category"] == "New Opportunity").sum())
awaiting = int((filtered["Category"] == "Submitted - Awaiting Decision").sum())
recent_decisions = int((filtered["Category"] == "Recent Decision").sum())
critical_7 = int(filtered["Days to Deadline"].between(0, 7, inclusive="both").sum())
due_30 = int(filtered["Days to Deadline"].between(0, 30, inclusive="both").sum())
known_funding = filtered["Funding Amount"].sum(min_count=1)

k1, k2, k3, k4, k5, k6 = st.columns(6)
k1.metric("Total", total_opps)
k2.metric("In Process", in_process)
k3.metric("New", new_opps)
k4.metric("Awaiting", awaiting)
k5.metric("Due in 7 Days", critical_7)
k6.metric("Due in 30 Days", due_30)

if pd.notna(known_funding):
    st.caption(f"Known funding in current view: {fmt_money(known_funding, 'USD')}+ across mixed currencies")

upcoming = filtered[filtered["Days to Deadline"] >= 0].sort_values("Deadline")
next_deadline_card = "None in current view"
if not upcoming.empty:
    next_item = upcoming.iloc[0]
    next_deadline_card = (
        f"{next_item['Opportunity']} · {next_item['Deadline'].date()} · "
        f"{int(next_item['Days to Deadline'])} days left"
    )

overdue_count = int((filtered["Days to Deadline"] < 0).sum())
safe_count = int((filtered["Days to Deadline"] > 30).sum())
active_sponsors = filtered["Partner / Sponsor"].nunique()

exec_left, exec_mid, exec_right = st.columns([1.2, 1, 1])
with exec_left:
    st.markdown(
        f"""
        <div class="card">
            <div class="section-title">Next deadline</div>
            <div style="font-size:1.05rem;font-weight:800;color:#0f172a;line-height:1.35;">{next_deadline_card}</div>
            <div class="toolbar-note">Calculated from the selected as-of date.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with exec_mid:
    st.markdown(
        f"""
        <div class="card">
            <div class="section-title">Urgency</div>
            <div style="display:flex;flex-direction:column;gap:8px;">
                <div style="display:flex;justify-content:space-between;align-items:center;"><span>Overdue</span><span>{badge(str(overdue_count), 'negative')}</span></div>
                <div style="display:flex;justify-content:space-between;align-items:center;"><span>Due in 7 days</span><span>{badge(str(critical_7), 'negative' if critical_7 else 'positive')}</span></div>
                <div style="display:flex;justify-content:space-between;align-items:center;"><span>Due in 30 days</span><span>{badge(str(due_30), 'warning' if due_30 else 'positive')}</span></div>
                <div style="display:flex;justify-content:space-between;align-items:center;"><span>Safe</span><span>{badge(str(safe_count), 'positive')}</span></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with exec_right:
    st.markdown(
        f"""
        <div class="card">
            <div class="section-title">Sponsor coverage</div>
            <div style="display:flex;justify-content:space-between;align-items:center;gap:10px;">
                <div style="font-size:2rem;font-weight:900;color:#0F62FE;">{active_sponsors}</div>
                <div>{badge('Active sponsors', 'brand')}</div>
            </div>
            <div class="toolbar-note">Unique sponsors or partners in current filters.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

quick1, quick2, quick3 = st.columns(3)

with quick1:
    high_value = filtered[filtered["Funding Amount"].notna()].sort_values("Funding Amount", ascending=False).head(5)
    items = "".join(
        [
            f"<div class='quick-list-item'><div class='quick-title'>{r['Opportunity']}</div>"
            f"<div class='quick-meta'>{r['Funding Display']}</div></div>"
            for _, r in high_value.iterrows()
        ]
    ) or "<div class='quick-meta'>No funding values.</div>"
    st.markdown(f"<div class='mini-card'><div class='section-title'>Top value</div>{items}</div>", unsafe_allow_html=True)

with quick2:
    urgent = filtered[filtered["Days to Deadline"].between(0, 30, inclusive="both")].sort_values("Deadline").head(5)
    items = "".join(
        [
            f"<div class='quick-list-item'><div class='quick-title'>{r['Opportunity']}</div>"
            f"<div class='quick-meta'>{int(r['Days to Deadline'])} days · {r['Deadline'].date()}</div></div>"
            for _, r in urgent.iterrows()
        ]
    ) or "<div class='quick-meta'>No urgent deadlines.</div>"
    st.markdown(f"<div class='mini-card'><div class='section-title'>Due soon</div>{items}</div>", unsafe_allow_html=True)

with quick3:
    action_needed = filtered[
        filtered["Status"].str.contains("follow|review|discussion|looking|awaiting|tricky", case=False, na=False)
    ].head(5)
    items = "".join(
        [
            f"<div class='quick-list-item'><div class='quick-title'>{r['Opportunity']}</div>"
            f"<div class='quick-meta'>{r['Status']}</div></div>"
            for _, r in action_needed.iterrows()
        ]
    ) or "<div class='quick-meta'>No flagged actions.</div>"
    st.markdown(f"<div class='mini-card'><div class='section-title'>Action list</div>{items}</div>", unsafe_allow_html=True)


def styled_bar(data, y_field, x_field, title, color="#0F62FE", height=300):
    base = alt.Chart(data).encode(
        y=alt.Y(f"{y_field}:N", sort="-x", title=None),
        x=alt.X(f"{x_field}:Q", title=None),
        tooltip=[y_field, x_field],
    )
    bars = base.mark_bar(cornerRadiusTopRight=8, cornerRadiusBottomRight=8, color=color)
    labels = base.mark_text(
        align="left", baseline="middle", dx=6, fontWeight="bold", color="#0f172a"
    ).encode(text=f"{x_field}:Q")
    return (bars + labels).properties(title=title, height=height)


def styled_column(data, x_field, y_field, title, color="#14B8A6", height=320):
    base = alt.Chart(data).encode(
        x=alt.X(f"{x_field}:N", sort=None, title=None),
        y=alt.Y(f"{y_field}:Q", title=None),
        tooltip=[x_field, y_field],
    )
    bars = base.mark_bar(cornerRadiusTopLeft=8, cornerRadiusTopRight=8, color=color)
    labels = base.mark_text(dy=-10, fontWeight="bold", color="#0f172a").encode(text=f"{y_field}:Q")
    return (bars + labels).properties(title=title, height=height)


def category_color_scale():
    return alt.Scale(
        domain=[
            "In Process",
            "New Opportunity",
            "Submitted - Awaiting Decision",
            "Recent Decision",
        ],
        range=["#2563EB", "#14B8A6", "#F59E0B", "#DC2626"],
    )


st.markdown("### Portfolio analytics")

tab1, tab2, tab3 = st.tabs(["Overview", "Deadlines", "Portfolio"])

with tab1:
    chart1, chart2 = st.columns(2)

    with chart1:
        cat_df = filtered.groupby("Category", as_index=False).size().rename(columns={"size": "Count"})
        cat_chart = alt.Chart(cat_df).mark_bar(cornerRadiusTopRight=8, cornerRadiusBottomRight=8).encode(
            y=alt.Y("Category:N", sort="-x", title=None),
            x=alt.X("Count:Q", title=None),
            color=alt.Color("Category:N", scale=category_color_scale(), legend=None),
            tooltip=["Category", "Count"],
        )
        cat_text = alt.Chart(cat_df).mark_text(align="left", baseline="middle", dx=6, fontWeight="bold").encode(
            y=alt.Y("Category:N", sort="-x", title=None),
            x=alt.X("Count:Q", title=None),
            text="Count:Q",
        )
        st.altair_chart((cat_chart + cat_text).properties(title="By category", height=290), width="stretch")

    with chart2:
        focus_df = (
            filtered.groupby("Focus Area", as_index=False)
            .size()
            .rename(columns={"size": "Count"})
            .sort_values("Count", ascending=False)
            .head(10)
        )
        st.altair_chart(
            styled_bar(focus_df, "Focus Area", "Count", "Top focus areas", color="#14B8A6", height=290),
            width="stretch",
        )

    chart3, chart4 = st.columns(2)

    with chart3:
        sponsor_df = (
            filtered.groupby("Partner / Sponsor", as_index=False)
            .size()
            .rename(columns={"size": "Count"})
            .sort_values("Count", ascending=False)
            .head(10)
        )
        st.altair_chart(
            styled_bar(sponsor_df, "Partner / Sponsor", "Count", "Top sponsors / partners", color="#0F62FE", height=330),
            width="stretch",
        )

    with chart4:
        lead_df = (
            filtered.groupby("Lead", as_index=False)
            .size()
            .rename(columns={"size": "Count"})
            .sort_values("Count", ascending=False)
            .head(10)
        )
        st.altair_chart(
            styled_bar(lead_df, "Lead", "Count", "Top leads", color="#7C3AED", height=330),
            width="stretch",
        )

with tab2:
    upcoming_cols = [
        "Opportunity",
        "Category",
        "Lead",
        "Partner / Sponsor",
        "Deadline",
        "Days to Deadline",
        "Funding Display",
        "Status",
    ]
    deadline_df = filtered[filtered["Deadline"].notna()].copy()
    left_dead, right_dead = st.columns([1.2, 1])

    with left_dead:
        if not deadline_df.empty:
            deadline_summary = (
                deadline_df.groupby(deadline_df["Deadline"].dt.strftime("%d %b %Y"), as_index=False)
                .size()
                .rename(columns={"size": "Count"})
            )
            deadline_summary = deadline_summary.rename(columns={deadline_summary.columns[0]: "Deadline Label"})
            st.altair_chart(
                styled_column(deadline_summary, "Deadline Label", "Count", "Deadline volume", color="#F59E0B", height=330),
                width="stretch",
            )
        else:
            st.info("No deadline data.")

    with right_dead:
        st.markdown("#### Deadline list")
        if not upcoming.empty:
            deadline_view = upcoming[upcoming_cols].copy()
            st.dataframe(deadline_view, width="stretch", hide_index=True)
        else:
            st.info("No upcoming deadlines.")

with tab3:
    st.markdown("#### Portfolio table")

    detail_cols = [
        "Opportunity",
        "Category",
        "Stage",
        "Status",
        "Lead",
        "Partner / Sponsor",
        "Focus Area",
        "Submission Date",
        "Deadline",
        "Days to Deadline",
        "Funding Display",
        "Notes",
    ]
    display_df = filtered[detail_cols].copy()
    st.dataframe(display_df, width="stretch", hide_index=True)

    st.markdown("#### Opportunity detail")
    chosen = st.selectbox("Open opportunity", ["Select an opportunity"] + filtered["Opportunity"].tolist())
    if chosen != "Select an opportunity":
        row = filtered[filtered["Opportunity"] == chosen].iloc[0]
        d1, d2 = st.columns([1, 1])

        with d1:
            st.markdown(f"### {row['Opportunity']}")
            st.markdown(
                f"{badge(row['Category'], 'brand')} "
                f"{badge(row['Status'], row['Status Tone'])} "
                f"{badge(row['Deadline Status'], row['Deadline Tone'])}",
                unsafe_allow_html=True,
            )
            st.write(f"**Lead:** {row['Lead']}")
            st.write(f"**Partner / Sponsor:** {row['Partner / Sponsor']}")
            st.write(f"**Focus Area:** {row['Focus Area']}")
            st.write(f"**Stage:** {row['Stage']}")

        with d2:
            st.write(f"**Submission Date:** {row['Submission Date']}")
            st.write(f"**Deadline:** {row['Deadline']}")
            st.write(f"**Days to Deadline:** {row['Days to Deadline']}")
            st.write(f"**Funding:** {row['Funding Display']}")
            st.write(f"**Notes:** {row['Notes']}")

st.markdown("### Export")
export_df = filtered.copy()
export_df["Submission Date"] = export_df["Submission Date"].astype(str)
export_df["Deadline"] = export_df["Deadline"].astype(str)
csv = export_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download current view",
    data=csv,
    file_name="leads_opportunities_dashboard_export.csv",
    mime="text/csv",
)

with st.expander("How to connect this to a live tracker"):
    st.markdown(
        """
Use a CSV or Excel export with columns similar to:
- Opportunity
- Category
- Status
- Lead
- Partner / Sponsor
- Focus Area
- Submission Date
- Deadline
- Funding Amount
- Funding Currency
- Notes

This app can be connected to a live source such as SharePoint, OneDrive, SQL, or a scheduled export.
"""
    )