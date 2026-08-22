import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import base64

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Study Smart Tuition Centre | Management Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CORPORATE DESIGN SYSTEM & CSS
# =========================================================

st.markdown(
    """
    <style>
    
    /* Global Typography & Background */
    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    }

    .stApp {
        background-color: #F8FAFC;
        color: #0F172A;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        max-width: 1560px;
    }

    /* ---------------- SIDEBAR (Corporate Slate/Navy) ---------------- */

    [data-testid="stSidebar"] {
        background-color: #0F172A !important;
        border-right: 1px solid #1E293B;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 0.15rem;
    }

    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        gap: 0.4rem !important;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: #F1F5F9 !important;
    }

    .brand-wrap {
        margin: 2px 8px 6px 8px;
        padding: 5px 7px;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(2, 6, 23, 0.14);
        overflow: hidden;
    }

    .brand-logo {
        width: 100%;
        max-height: 118px;
        display: block;
        object-fit: contain;
        margin: 0 auto;
    }

    .brand-subtitle {
        margin: 6px 10px 12px 10px;
        font-size: 9px;
        letter-spacing: 1.9px;
        font-weight: 800;
        color: #94A3B8;
        text-transform: uppercase;
        text-align: left;
    }

    .side-section {
        margin-top: 8px;
        margin-bottom: 5px;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 1.5px;
        color: #64748B;
        text-transform: uppercase;
    }

    [data-testid="stSidebar"] hr {
        margin: 0.8rem 0 !important;
        border-color: #1E293B !important;
    }

    /* Radio navigation */
    [data-testid="stSidebar"] [data-testid="stRadio"] > label {
        display: none !important;
    }

    [data-testid="stSidebar"] [role="radiogroup"] {
        gap: 0.25rem !important;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label {
        padding: 0.5rem 0.75rem !important;
        border-radius: 8px !important;
        transition: all 0.15s ease-in-out !important;
        border: 1px solid transparent;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label:hover {
        background: #1E293B !important;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label[data-checked="true"] {
        background: #1E3A8A !important;
        border-color: #3B82F6 !important;
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] span,
    [data-testid="stSidebar"] [data-testid="stRadio"] p {
        color: #F8FAFC !important;
        -webkit-text-fill-color: #F8FAFC !important;
        font-weight: 500 !important;
        font-size: 13px !important;
    }

    /* Selectboxes */
    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        min-height: 40px !important;
        border-radius: 8px !important;
        background: #1E293B !important;
        border: 1px solid #334155 !important;
        color: #F8FAFC !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] span,
    [data-testid="stSidebar"] [data-baseweb="select"] input {
        color: #F8FAFC !important;
        -webkit-text-fill-color: #F8FAFC !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] svg {
        fill: #94A3B8 !important;
    }

    div[role="listbox"] {
        background: #1E293B !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
    }

    div[role="option"], li[role="option"] {
        background: #1E293B !important;
        color: #F8FAFC !important;
        -webkit-text-fill-color: #F8FAFC !important;
    }

    div[role="option"]:hover, li[role="option"]:hover {
        background: #334155 !important;
    }

    /* Buttons */
    [data-testid="stSidebar"] .stButton > button {
        width: 100%;
        min-height: 38px;
        border-radius: 8px;
        color: #F8FAFC;
        background: #1E293B;
        border: 1px solid #334155;
        font-weight: 600;
        font-size: 13px;
        transition: all 0.15s ease;
    }

    [data-testid="stSidebar"] .stButton > button:hover {
        background: #334155;
        border-color: #475569;
    }

    /* ---------------- CORPORATE HERO & CARDS ---------------- */

    .hero {
        padding: 32px 36px;
        border-radius: 16px;
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #1E3A8A 100%);
        border: 1px solid #334155;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.2);
        margin-bottom: 24px;
    }

    .hero-kicker {
        color: #60A5FA;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 2px;
        margin-bottom: 8px;
        text-transform: uppercase;
    }

    .hero-title {
        color: #FFFFFF;
        font-size: 32px;
        font-weight: 800;
        letter-spacing: -0.6px;
        margin: 0;
    }

    .hero-sub {
        color: #94A3B8;
        font-size: 14px;
        margin-top: 10px;
        max-width: 760px;
        line-height: 1.6;
    }

    .home-section-title {
        margin-top: 24px;
        margin-bottom: 12px;
        color: #0F172A;
        font-size: 18px;
        font-weight: 700;
        letter-spacing: -0.3px;
    }

    .role-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
        min-height: 155px;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
        transition: all 0.2s ease-in-out;
        border-top: 3px solid #2563EB;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .role-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
        border-color: #CBD5E1;
        border-top-color: #1D4ED8;
    }

    .role-icon {
        font-size: 22px;
        margin-bottom: 8px;
    }

    .role-title {
        color: #0F172A;
        font-size: 15px;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .role-desc {
        color: #64748B;
        font-size: 12px;
        line-height: 1.5;
    }


    .top-meta {
        display:flex;
        justify-content:space-between;
        align-items:center;
        margin-bottom:10px;
        font-size:11px;
        color:#64748B;
    }

    .top-meta strong {
        color:#0F172A;
        font-weight:700;
    }

    /* ---------------- DASHBOARD HEADER & KPIs ---------------- */

    .dashboard-badge {
        display: inline-flex;
        align-items: center;
        padding: 4px 10px;
        border-radius: 6px;
        background: #EFF6FF;
        border: 1px solid #DBEAFE;
        color: #1E40AF;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.8px;
        margin-bottom: 10px;
        text-transform: uppercase;
    }

    .dashboard-title {
        font-size: 26px;
        font-weight: 800;
        color: #0F172A;
        letter-spacing: -0.5px;
        margin-bottom: 4px;
    }

    .dashboard-subtitle {
        color: #64748B;
        font-size: 14px;
        margin-bottom: 16px;
    }

    .context-bar {
        margin-bottom: 20px;
        padding: 10px 16px;
        border-radius: 10px;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        color: #475569;
        font-size: 12px;
        display: flex;
        gap: 16px;
        align-items: center;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.03);
    }

    .context-item {
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .context-label {
        color: #94A3B8;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 10px;
        letter-spacing: 0.5px;
    }

    .context-value {
        color: #0F172A;
        font-weight: 700;
    }

    /* Custom KPI Container */
    .kpi-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 18px 20px;
        box-shadow: 0 4px 12px rgba(15,23,42,0.045);
        transition: all 0.18s ease-in-out;
        border-left: 4px solid #2563EB;
        margin-bottom: 12px;
        min-height: 126px;
        height: 126px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-sizing: border-box;
    }

    .kpi-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 22px rgba(15,23,42,0.08);
        border-color: #CBD5E1;
    }

    .kpi-label {
        font-size: 11px;
        font-weight: 700;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.55px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .kpi-value {
        font-size: 24px;
        font-weight: 800;
        color: #0F172A;
        margin-top: 4px;
        letter-spacing: -0.5px;
    }

    .kpi-subtext {
        font-size: 11px;
        color: #94A3B8;
        margin-top: 4px;
        font-weight: 500;
    }

    /* Plotly Wrappers */
    div[data-testid="stPlotlyChart"] {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 14px 14px 10px 14px;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.04);
        transition: all 0.15s ease;
    }

    div[data-testid="stPlotlyChart"]:hover {
        border-color: #CBD5E1;
    }


    /* Plotly text safety for deployed light theme */
    div[data-testid="stPlotlyChart"] {
        color: #0F172A !important;
    }


    /* Finance legends: rendered as HTML instead of Plotly for cloud-safe visibility */
    .finance-legend {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 18px;
        margin: 2px 0 10px 2px;
        color: #334155 !important;
        font-size: 12px;
        font-weight: 600;
    }

    .finance-legend-item {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        color: #334155 !important;
    }

    .finance-legend-dot {
        width: 11px;
        height: 11px;
        border-radius: 2px;
        display: inline-block;
        flex: 0 0 11px;
    }

    .finance-legend-dot.collected { background: #10B981; }
    .finance-legend-dot.outstanding { background: #EF4444; }
    .finance-legend-dot.paid { background: #10B981; }
    .finance-legend-dot.overdue { background: #F59E0B; }
    .finance-legend-dot.revenue { background: #2563EB; }
    .finance-legend-dot.branch-outstanding { background: #F59E0B; }


    /* Data Table & Expanders */
    [data-testid="stExpander"] {
        background: #FFFFFF;
        border: 1px solid #E2E8F0 !important;
        border-radius: 10px !important;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.03);
    }

    [data-testid="stDataFrame"] {
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        overflow: hidden;
    }

    .stDownloadButton > button {
        background: #2563EB;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        font-size: 13px;
        box-shadow: 0 1px 3px 0 rgba(37, 99, 235, 0.2);
        transition: all 0.15s ease;
    }

    .stDownloadButton > button:hover {
        background: #1D4ED8;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.3);
    }

    hr {
        border: none;
        border-top: 1px solid #E2E8F0;
        margin: 1.5rem 0;
    }

    /* System Status Widget */
    .system-card {
        margin-top: 12px;
        padding: 12px;
        border-radius: 8px;
        background: #1E293B;
        border: 1px solid #334155;
    }

    .system-label {
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 1.2px;
        color: #64748B;
        text-transform: uppercase;
        margin-bottom: 6px;
    }

    .system-status-row {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .status-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #10B981;
        box-shadow: 0 0 8px rgba(16, 185, 129, 0.5);
    }

    .system-status-text {
        color: #F1F5F9;
        font-size: 12px;
        font-weight: 600;
    }

    .system-name {
        color: #94A3B8;
        font-size: 11px;
        margin-top: 4px;
    }

    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# DATA LOADER
# =========================================================

@st.cache_data
def load_data():
    file_path = "StudySmart_DummyDataset.xlsx"

    data = {
        "students": pd.read_excel(file_path, sheet_name="Students"),
        "tutors": pd.read_excel(file_path, sheet_name="Tutors"),
        "courses": pd.read_excel(file_path, sheet_name="Courses"),
        "branches": pd.read_excel(file_path, sheet_name="Branches"),
        "enrolments": pd.read_excel(file_path, sheet_name="Enrolments"),
        "payments": pd.read_excel(file_path, sheet_name="Payments"),
        "attendance": pd.read_excel(file_path, sheet_name="Attendance"),
        "exam_scores": pd.read_excel(file_path, sheet_name="Exam Scores"),
        "inventory": pd.read_excel(file_path, sheet_name="Inventory"),
        "marketing": pd.read_excel(file_path, sheet_name="Marketing"),
        "online_sessions": pd.read_excel(file_path, sheet_name="Online Sessions")
    }

    data["students"]["RegistrationDate"] = pd.to_datetime(
        data["students"]["RegistrationDate"], errors="coerce"
    )
    data["enrolments"]["EnrolmentDate"] = pd.to_datetime(
        data["enrolments"]["EnrolmentDate"], errors="coerce"
    )
    data["payments"]["BillingMonth"] = pd.to_datetime(
        data["payments"]["BillingMonth"], errors="coerce"
    )
    data["payments"]["PaymentDate"] = pd.to_datetime(
        data["payments"]["PaymentDate"], errors="coerce"
    )
    data["attendance"]["SessionDate"] = pd.to_datetime(
        data["attendance"]["SessionDate"], errors="coerce"
    )
    data["exam_scores"]["AssessmentDate"] = pd.to_datetime(
        data["exam_scores"]["AssessmentDate"], errors="coerce"
    )
    data["online_sessions"]["SessionDate"] = pd.to_datetime(
        data["online_sessions"]["SessionDate"], errors="coerce"
    )

    return data


D = load_data()

students = D["students"]
tutors = D["tutors"]
courses = D["courses"]
branches = D["branches"]
enrolments = D["enrolments"]
payments = D["payments"]
attendance = D["attendance"]
exam_scores = D["exam_scores"]
inventory = D["inventory"]
marketing = D["marketing"]
online_sessions = D["online_sessions"]

branch_map = dict(zip(branches["BranchID"], branches["BranchName"]))
course_map = dict(zip(courses["CourseID"], courses["CourseName"]))
subject_map = dict(zip(courses["CourseID"], courses["Subject"]))
tutor_map = dict(zip(tutors["TutorID"], tutors["TutorName"]))

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "branch_filter" not in st.session_state:
    st.session_state.branch_filter = "All Branches"

if "subject_filter" not in st.session_state:
    st.session_state.subject_filter = "All Subjects"

if "month_filter" not in st.session_state:
    st.session_state.month_filter = "All Months"

# =========================================================
# UI & PLOTLY HELPERS
# =========================================================

# Corporate Palette
CORPORATE_PALETTE = ["#2563EB", "#0EA5E9", "#6366F1", "#8B5CF6", "#0284C7", "#3B82F6"]

def render_kpi(label, value, accent="#2563EB", subtext=None):
    subtext_html = f'<div class="kpi-subtext">{subtext}</div>' if subtext else ''
    st.markdown(
        f"""
        <div class="kpi-card" style="border-left-color: {accent};">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            {subtext_html}
        </div>
        """,
        unsafe_allow_html=True
    )


def modern_chart(fig, height=360, show_legend=True):
    """Apply a deployment-safe corporate Plotly theme."""
    fig.update_layout(
        height=height,
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(
            family="Segoe UI, Arial, sans-serif",
            color="#475569",
            size=12
        ),
        margin=dict(l=18, r=18, t=54, b=56),
        hoverlabel=dict(
            bgcolor="#0F172A",
            font_size=12,
            font_color="#FFFFFF",
            font_family="Segoe UI"
        ),
        colorway=CORPORATE_PALETTE,
        showlegend=show_legend
    )

    # Never create an empty title object that can render as 'undefined'
    title_text = ""
    try:
        raw_title = fig.layout.title.text
        if isinstance(raw_title, str):
            title_text = raw_title.strip()
    except Exception:
        title_text = ""

    if title_text:
        fig.update_layout(
            title=dict(
                text=title_text,
                font=dict(size=15, color="#0F172A", family="Segoe UI"),
                x=0.02,
                xanchor="left",
                y=0.97,
                yanchor="top"
            )
        )
    else:
        fig.update_layout(title_text="")

    if show_legend:
        fig.update_layout(
            legend=dict(
                title=None,
                orientation="h",
                yanchor="top",
                y=-0.12,
                xanchor="left",
                x=0,
                font=dict(size=11, color="#475569"),
                bgcolor="rgba(0,0,0,0)"
            )
        )

    try:
        fig.update_xaxes(
            showgrid=False,
            zeroline=False,
            linecolor="#E2E8F0",
            tickfont=dict(color="#64748B", size=11),
            title_font=dict(color="#64748B", size=11)
        )
        fig.update_yaxes(
            gridcolor="#F1F5F9",
            zeroline=False,
            linecolor="#E2E8F0",
            tickfont=dict(color="#64748B", size=11),
            title_font=dict(color="#64748B", size=11)
        )
    except Exception:
        pass

    return fig


def dashboard_header(title, subtitle):
    st.markdown(
        """
        <div class="top-meta">
            <span><strong>Study Smart Tuition Centre</strong></span>
            <span>Management View</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="dashboard-badge">STUDY SMART TUITION CENTRE</div>',
        unsafe_allow_html=True
    )
    st.markdown(f'<div class="dashboard-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="dashboard-subtitle">{subtitle}</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="context-bar">
            <div class="context-item">
                <span class="context-label">Branch:</span>
                <span class="context-value">{selected_branch}</span>
            </div>
            <span>•</span>
            <div class="context-item">
                <span class="context-label">Subject:</span>
                <span class="context-value">{selected_subject}</span>
            </div>
            <span>•</span>
            <div class="context-item">
                <span class="context-label">Month:</span>
                <span class="context-value">{selected_month}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def set_page(page_name):
    st.session_state.page = page_name
    st.rerun()


# =========================================================
# SIDEBAR
# =========================================================

with open("study_smart_logo_new.png", "rb") as logo_file:
    logo_base64 = base64.b64encode(logo_file.read()).decode()

st.sidebar.markdown(
    f"""
    <div class="brand-wrap">
        <img class="brand-logo"
             src="data:image/png;base64,{logo_base64}"
             alt="Study Smart Tuition Centre">
    </div>
    <div class="brand-subtitle">Management Portal</div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown('<div class="side-section">NAVIGATION</div>', unsafe_allow_html=True)

menu_options = [
    "Home",
    "Executive Management",
    "Academic Manager",
    "Finance Manager",
    "Branch Manager",
    "Marketing Manager"
]

default_index = menu_options.index(
    st.session_state.page if st.session_state.page in menu_options else "Home"
)

selected_page = st.sidebar.radio(
    "Navigation",
    menu_options,
    index=default_index,
    label_visibility="collapsed"
)

if selected_page != st.session_state.page:
    st.session_state.page = selected_page

# Filters display when navigating dashboards
if st.session_state.page != "Home":
    st.sidebar.markdown('<div class="side-section">FILTERS</div>', unsafe_allow_html=True)

    branch_options = ["All Branches"] + sorted(
        branches["BranchName"].dropna().unique().tolist()
    )
    subject_options = ["All Subjects"] + sorted(
        courses["Subject"].dropna().unique().tolist()
    )
    month_options = ["All Months"] + sorted(
        payments["BillingMonth"]
        .dropna()
        .dt.strftime("%Y-%m")
        .unique()
        .tolist()
    )

    selected_branch = st.sidebar.selectbox(
        "Branch",
        branch_options,
        index=branch_options.index(st.session_state.branch_filter)
        if st.session_state.branch_filter in branch_options else 0
    )
    st.session_state.branch_filter = selected_branch

    selected_subject = st.sidebar.selectbox(
        "Subject",
        subject_options,
        index=subject_options.index(st.session_state.subject_filter)
        if st.session_state.subject_filter in subject_options else 0
    )
    st.session_state.subject_filter = selected_subject

    selected_month = st.sidebar.selectbox(
        "Month",
        month_options,
        index=month_options.index(st.session_state.month_filter)
        if st.session_state.month_filter in month_options else 0
    )
    st.session_state.month_filter = selected_month

    st.sidebar.markdown('<div class="side-section">ACTIONS</div>', unsafe_allow_html=True)

    if st.sidebar.button("↻ Reset Filters", use_container_width=True):
        st.session_state.branch_filter = "All Branches"
        st.session_state.subject_filter = "All Subjects"
        st.session_state.month_filter = "All Months"
        st.rerun()

    st.sidebar.markdown(
        """
        <div class="system-card">
            <div class="system-label">System</div>
            <div class="system-status-row">
                <span class="status-dot"></span>
                <span class="system-status-text">Connected</span>
            </div>
            <div class="system-name">Study Smart Management Portal</div>
        </div>
        """,
        unsafe_allow_html=True
    )

else:
    selected_branch = "All Branches"
    selected_subject = "All Subjects"
    selected_month = "All Months"

# =========================================================
# FILTER DATA ENGINE
# =========================================================

filtered_students = students.copy()
filtered_tutors = tutors.copy()
filtered_courses = courses.copy()
filtered_enrolments = enrolments.copy()
filtered_payments = payments.copy()
filtered_attendance = attendance.copy()
filtered_scores = exam_scores.copy()
filtered_inventory = inventory.copy()
filtered_online = online_sessions.copy()

selected_branch_id = None
selected_course_ids = courses["CourseID"].tolist()

if selected_branch != "All Branches":
    selected_branch_id = branches.loc[
        branches["BranchName"] == selected_branch,
        "BranchID"
    ].iloc[0]

    filtered_students = filtered_students[filtered_students["BranchID"] == selected_branch_id]
    filtered_tutors = filtered_tutors[filtered_tutors["BranchID"] == selected_branch_id]
    filtered_enrolments = filtered_enrolments[filtered_enrolments["BranchID"] == selected_branch_id]
    filtered_payments = filtered_payments[filtered_payments["BranchID"] == selected_branch_id]
    filtered_attendance = filtered_attendance[filtered_attendance["BranchID"] == selected_branch_id]
    filtered_scores = filtered_scores[filtered_scores["BranchID"] == selected_branch_id]
    filtered_inventory = filtered_inventory[filtered_inventory["BranchID"] == selected_branch_id]
    filtered_online = filtered_online[filtered_online["BranchID"] == selected_branch_id]

if selected_subject != "All Subjects":
    selected_course_ids = courses.loc[
        courses["Subject"] == selected_subject,
        "CourseID"
    ].tolist()

    filtered_courses = filtered_courses[filtered_courses["CourseID"].isin(selected_course_ids)]
    filtered_enrolments = filtered_enrolments[filtered_enrolments["CourseID"].isin(selected_course_ids)]
    filtered_payments = filtered_payments[filtered_payments["CourseID"].isin(selected_course_ids)]
    filtered_attendance = filtered_attendance[filtered_attendance["CourseID"].isin(selected_course_ids)]
    filtered_scores = filtered_scores[filtered_scores["CourseID"].isin(selected_course_ids)]
    filtered_online = filtered_online[filtered_online["CourseID"].isin(selected_course_ids)]

if selected_month != "All Months":
    filtered_payments = filtered_payments[
        filtered_payments["BillingMonth"].dt.strftime("%Y-%m") == selected_month
    ]
    filtered_attendance = filtered_attendance[
        filtered_attendance["SessionDate"].dt.strftime("%Y-%m") == selected_month
    ]
    filtered_enrolments = filtered_enrolments[
        filtered_enrolments["EnrolmentDate"].dt.strftime("%Y-%m") == selected_month
    ]
    filtered_online = filtered_online[
        filtered_online["SessionDate"].dt.strftime("%Y-%m") == selected_month
    ]

if selected_subject != "All Subjects" or selected_month != "All Months":
    valid_student_ids = filtered_enrolments["StudentID"].dropna().unique()
    valid_tutor_ids = filtered_enrolments["TutorID"].dropna().unique()

    filtered_students = filtered_students[filtered_students["StudentID"].isin(valid_student_ids)]
    filtered_tutors = filtered_tutors[filtered_tutors["TutorID"].isin(valid_tutor_ids)]

# =========================================================
# PAGE 1: HOME
# =========================================================

if st.session_state.page == "Home":

    st.markdown(
        """
        <div class="hero">
            <div class="hero-kicker">Study Smart Tuition Centre</div>
            <div class="hero-title">Study Smart Management Portal</div>
            <div class="hero-sub">
                Supporting quality education through clear visibility of academic, operational, financial and student performance across Study Smart Tuition Centre.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    total_students_home = students["StudentID"].nunique()
    total_revenue_home = payments["PaidAmountRM"].sum()
    attendance_home = attendance["Present"].mean() * 100
    total_branches_home = branches["BranchID"].nunique()
    total_tutors_home = tutors["TutorID"].nunique()
    total_courses_home = courses["CourseID"].nunique()

    c1, c2, c3, c4, c5, c6 = st.columns(6)
    with c1:
        render_kpi("Active Students", f"{total_students_home:,}", "#2563EB")
    with c2:
        render_kpi("Revenue", f"RM {total_revenue_home/1e3:,.1f}k", "#0EA5E9")
    with c3:
        render_kpi("Attendance", f"{attendance_home:.1f}%", "#10B981")
    with c4:
        render_kpi("Branches", f"{total_branches_home}", "#6366F1")
    with c5:
        render_kpi("Tutors", f"{total_tutors_home}", "#8B5CF6")
    with c6:
        render_kpi("Courses", f"{total_courses_home}", "#F59E0B")

    st.markdown('<div class="home-section-title">About Study Smart</div>', unsafe_allow_html=True)

    about_col, services_col = st.columns(2)

    with about_col:
        st.markdown(
            """
            <div class="role-card" style="border-top-color:#2563EB;">
                <div>
                    <div class="role-title">Who We Are</div>
                    <div class="role-desc">
                        Study Smart Tuition Centre is a multi-branch education provider committed to
                        helping students strengthen academic foundations, improve learning confidence,
                        and achieve consistent progress through structured tuition programmes.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with services_col:
        st.markdown(
            """
            <div class="role-card" style="border-top-color:#10B981;">
                <div>
                    <div class="role-title">Our Services</div>
                    <div class="role-desc">
                        Physical tuition classes, online learning, exam preparation, homework support,
                        student progress monitoring, and academic consultation.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="home-section-title">Management Dashboards</div>', unsafe_allow_html=True)


    r1c1, r1c2, r1c3 = st.columns(3)

    with r1c1:
        st.markdown(
            """
            <div class="role-card">
                <div>
                    <div class="role-icon">👔</div>
                    <div class="role-title">Executive Management</div>
                    <div class="role-desc">
                        Macro organization KPIs, high-level revenue trends, overall attendance, and branch performance summaries.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write("")
        if st.button("Open Executive View →", key="btn_exec", use_container_width=True):
            set_page("Executive Management")

    with r1c2:
        st.markdown(
            """
            <div class="role-card" style="border-top-color: #0EA5E9;">
                <div>
                    <div class="role-icon">🎓</div>
                    <div class="role-title">Academic Manager</div>
                    <div class="role-desc">
                        Academic outcomes, exam distributions, tutor efficiency scores, and student intervention tracking.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write("")
        if st.button("Open Academic View →", key="btn_acad", use_container_width=True):
            set_page("Academic Manager")

    with r1c3:
        st.markdown(
            """
            <div class="role-card" style="border-top-color: #10B981;">
                <div>
                    <div class="role-icon">💰</div>
                    <div class="role-title">Finance Manager</div>
                    <div class="role-desc">
                        Collection performance, fee aging analysis, outstanding balances, and branch financial health.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write("")
        if st.button("Open Finance View →", key="btn_fin", use_container_width=True):
            set_page("Finance Manager")

    st.write("")
    r2c1, r2c2, r2c3 = st.columns(3)

    with r2c1:
        st.markdown(
            """
            <div class="role-card" style="border-top-color: #6366F1;">
                <div>
                    <div class="role-icon">🏢</div>
                    <div class="role-title">Branch Manager</div>
                    <div class="role-desc">
                        Location-specific operations, course enrollment demand, local inventory, and tutor allocation.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write("")
        if st.button("Open Branch View →", key="btn_branch", use_container_width=True):
            set_page("Branch Manager")

    with r2c2:
        st.markdown(
            """
            <div class="role-card" style="border-top-color: #8B5CF6;">
                <div>
                    <div class="role-icon">📈</div>
                    <div class="role-title">Marketing Manager</div>
                    <div class="role-desc">
                        Campaign conversion metrics, student acquisition costs (CAC), channel yields, and funnel efficiency.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write("")
        if st.button("Open Marketing View →", key="btn_mkt", use_container_width=True):
            set_page("Marketing Manager")

    with r2c3:
        st.markdown(
            """
            <div class="role-card" style="border-top-color: #64748B;">
                <div>
                    <div class="role-icon">🗄️</div>
                    <div class="role-title">Integrated Data</div>
                    <div class="role-desc">
                        Integrated operational data supporting consistent reporting and management visibility across Study Smart Tuition Centre.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write("")
        st.button("System Operational ✓", disabled=True, use_container_width=True)

# =========================================================
# PAGE 2: EXECUTIVE MANAGEMENT
# =========================================================

elif st.session_state.page == "Executive Management":

    dashboard_header(
        "Executive Performance Overview",
        "High-level enterprise summary and operational monitoring"
    )

    total_students = filtered_students["StudentID"].nunique()
    total_enrolments = filtered_enrolments["EnrolmentID"].nunique()
    attendance_rate = (
        filtered_attendance["Present"].mean() * 100
        if not filtered_attendance.empty else 0
    )
    total_revenue = filtered_payments["PaidAmountRM"].sum()
    outstanding_fees = filtered_payments["OutstandingAmountRM"].sum()
    active_tutors = filtered_tutors["TutorID"].nunique()

    k1, k2, k3, k4, k5, k6 = st.columns(6)
    with k1:
        render_kpi("Students", f"{total_students:,}", "#2563EB")
    with k2:
        render_kpi("Enrolments", f"{total_enrolments:,}", "#0EA5E9")
    with k3:
        render_kpi("Attendance", f"{attendance_rate:.1f}%", "#10B981")
    with k4:
        render_kpi("Revenue", f"RM {total_revenue:,.0f}", "#2563EB")
    with k5:
        render_kpi("Outstanding", f"RM {outstanding_fees:,.0f}", "#EF4444")
    with k6:
        render_kpi("Tutor Staff", f"{active_tutors:,}", "#8B5CF6")

    st.markdown("---")

    col1, col2 = st.columns([1.6, 1])

    with col1:
        rev = payments.copy()
        if selected_branch_id is not None:
            rev = rev[rev["BranchID"] == selected_branch_id]
        if selected_subject != "All Subjects":
            rev = rev[rev["CourseID"].isin(selected_course_ids)]

        rev["Month"] = rev["BillingMonth"].dt.strftime("%b")
        revenue_monthly = (
            rev.groupby("Month")["PaidAmountRM"]
            .sum()
            .reindex(["Jan", "Feb", "Mar", "Apr", "May"])
            .fillna(0)
            .reset_index()
        )

        fig = px.area(
            revenue_monthly,
            x="Month",
            y="PaidAmountRM",
            markers=True,
            title="Revenue Trend"
        )
        fig.update_traces(
            fillcolor="rgba(37, 99, 235, 0.12)",
            line=dict(color="#2563EB", width=2.5)
        )
        fig.update_layout(xaxis_title="", yaxis_title="Revenue (RM)", hovermode="x unified")
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    with col2:
        st.markdown("#### Attendance Performance")
        st.caption("Overall attendance benchmark for the selected view.")

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=attendance_rate,
                number={"suffix": "%", "font": {"size": 28, "color": "#0F172A"}},
                gauge={
                    "axis": {
                        "range": [0, 100],
                        "tickcolor": "#64748B",
                        "tickfont": {"color": "#64748B"}
                    },
                    "bar": {"color": "#2563EB"},
                    "steps": [
                        {"range": [0, 75], "color": "#FEE2E2"},
                        {"range": [75, 88], "color": "#FEF3C7"},
                        {"range": [88, 100], "color": "#D1FAE5"}
                    ]
                }
            )
        )
        fig.update_layout(
            height=330,
            paper_bgcolor="#FFFFFF",
            margin=dict(l=18, r=18, t=10, b=18),
            showlegend=False,
            font=dict(family="Segoe UI, Arial, sans-serif", color="#475569")
        )
        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )

    col3, col4 = st.columns(2)

    with col3:
        branch_students = (
            enrolments.groupby("BranchID")["StudentID"]
            .nunique()
            .reset_index(name="Students")
        )
        branch_students["Branch"] = branch_students["BranchID"].map(branch_map)

        fig = px.bar(
            branch_students.sort_values("Students"),
            x="Students",
            y="Branch",
            orientation="h",
            title="Students by Branch",
            color_discrete_sequence=["#2563EB"]
        )
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    with col4:
        course_popularity = (
            filtered_enrolments.groupby("CourseID")["StudentID"]
            .nunique()
            .reset_index(name="Students")
        )
        course_popularity["Course"] = course_popularity["CourseID"].map(course_map)
        course_popularity = (
            course_popularity.sort_values("Students", ascending=False).head(7)
        )

        fig = px.bar(
            course_popularity,
            x="Students",
            y="Course",
            orientation="h",
            title="Course Popularity",
            color_discrete_sequence=["#0EA5E9"]
        )
        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# =========================================================
# PAGE 3: ACADEMIC MANAGER
# =========================================================

elif st.session_state.page == "Academic Manager":

    dashboard_header(
        "Academic Performance Centre",
        "Monitoring student outcomes, assessment scoring, and faculty performance"
    )

    avg_score = filtered_scores["Score"].mean() if not filtered_scores.empty else 0
    attendance_rate = (
        filtered_attendance["Present"].mean() * 100
        if not filtered_attendance.empty else 0
    )
    active_courses = filtered_enrolments["CourseID"].nunique()
    active_tutors = filtered_tutors["TutorID"].nunique()

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        render_kpi("Average Exam Score", f"{avg_score:.1f}%", "#2563EB")
    with k2:
        render_kpi("Attendance Rate", f"{attendance_rate:.1f}%", "#10B981")
    with k3:
        render_kpi("Courses", f"{active_courses}", "#0EA5E9")
    with k4:
        render_kpi("Active Tutors", f"{active_tutors}", "#8B5CF6")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        subject_scores = filtered_scores.copy()
        subject_scores["Subject"] = subject_scores["CourseID"].map(subject_map)
        subject_scores = (
            subject_scores.groupby("Subject")["Score"]
            .mean()
            .reset_index()
        )

        fig = px.bar(
            subject_scores,
            x="Subject",
            y="Score",
            text_auto=".1f",
            title="Academic Performance by Subject",
            color_discrete_sequence=["#2563EB"]
        )
        fig.update_yaxes(range=[0, 100])
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    with col2:
        tutor_perf = (
            filtered_scores.groupby("TutorID")["Score"]
            .mean()
            .reset_index()
        )
        tutor_perf["Tutor"] = tutor_perf["TutorID"].map(tutor_map)
        tutor_perf = tutor_perf.sort_values("Score", ascending=False).head(10)

        fig = px.bar(
            tutor_perf.sort_values("Score"),
            x="Score",
            y="Tutor",
            orientation="h",
            title="Tutor Performance",
            text="Score",
            color_discrete_sequence=["#6366F1"]
        )
        fig.update_xaxes(range=[0, 100])
        fig.update_traces(texttemplate="%{text:.1f}", textposition="outside")
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    col3, col4 = st.columns(2)

    with col3:
        att = attendance.copy()
        if selected_branch_id is not None:
            att = att[att["BranchID"] == selected_branch_id]
        if selected_subject != "All Subjects":
            att = att[att["CourseID"].isin(selected_course_ids)]

        att["Month"] = att["SessionDate"].dt.strftime("%b")
        trend = (
            att.groupby("Month")["Present"]
            .mean()
            .mul(100)
            .reindex(["Jan", "Feb", "Mar", "Apr", "May"])
            .reset_index(name="AttendanceRate")
        )

        fig = px.line(
            trend,
            x="Month",
            y="AttendanceRate",
            markers=True,
            title="Attendance Trend",
            color_discrete_sequence=["#10B981"]
        )
        fig.update_yaxes(range=[70, 100], ticksuffix="%")
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    with col4:
        learning_mode = (
            filtered_attendance.groupby("Mode")
            .size()
            .reset_index(name="Sessions")
        )

        st.markdown("#### Learning Delivery Mode")
        st.caption("Distribution of physical and online learning sessions.")

        fig = px.pie(
            learning_mode,
            names="Mode",
            values="Sessions",
            hole=0.62,
            color_discrete_sequence=["#2563EB", "#0EA5E9"]
        )

        fig = modern_chart(fig, height=360)
        fig.update_layout(
            title_text="",
            margin=dict(l=10, r=10, t=12, b=76),
            legend=dict(
                title=None,
                orientation="h",
                yanchor="top",
                y=-0.08,
                xanchor="center",
                x=0.5,
                font=dict(size=11, color="#475569"),
                bgcolor="rgba(255,255,255,0)"
            )
        )
        fig.update_traces(
            textposition="inside",
            textinfo="percent",
            textfont=dict(color="#0F172A", size=12),
            hovertemplate="<b>%{label}</b><br>Sessions: %{value}<br>Share: %{percent}<extra></extra>"
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )

    with st.expander("🔎 Academic Support Needs (Scores Below 60%)"):
        low_scores = filtered_scores[filtered_scores["Score"] < 60].copy()
        low_scores = low_scores.merge(
            students[["StudentID", "StudentName", "Level"]],
            on="StudentID",
            how="left"
        )
        low_scores["Course"] = low_scores["CourseID"].map(course_map)

        st.dataframe(
            low_scores[
                ["StudentID", "StudentName", "Level", "Course", "Score"]
            ].sort_values("Score"),
            use_container_width=True
        )

# =========================================================
# PAGE 4: FINANCE MANAGER
# =========================================================

elif st.session_state.page == "Finance Manager":

    dashboard_header(
        "Financial Performance Centre",
        "Revenue tracking, receivables aging, and billing efficiency"
    )

    net_billed = (
        filtered_payments["BilledAmountRM"].sum()
        - filtered_payments["DiscountAmountRM"].sum()
    )
    collected = filtered_payments["PaidAmountRM"].sum()
    outstanding = filtered_payments["OutstandingAmountRM"].sum()
    collection_rate = collected / net_billed * 100 if net_billed > 0 else 0

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        render_kpi("Net Billed Amount", f"RM {net_billed:,.0f}", "#2563EB")
    with k2:
        render_kpi("Total Revenue Collected", f"RM {collected:,.0f}", "#10B981")
    with k3:
        render_kpi("Outstanding Receivables", f"RM {outstanding:,.0f}", "#EF4444")
    with k4:
        render_kpi("Collection Rate", f"{collection_rate:.1f}%", "#0EA5E9")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        fin = payments.copy()
        if selected_branch_id is not None:
            fin = fin[fin["BranchID"] == selected_branch_id]
        if selected_subject != "All Subjects":
            fin = fin[fin["CourseID"].isin(selected_course_ids)]

        fin["Month"] = fin["BillingMonth"].dt.strftime("%b")
        monthly_finance = (
            fin.groupby("Month")
            .agg(
                Collected=("PaidAmountRM", "sum"),
                Outstanding=("OutstandingAmountRM", "sum")
            )
            .reindex(["Jan", "Feb", "Mar", "Apr", "May"])
            .fillna(0)
            .reset_index()
        )

        st.markdown("#### Monthly Cash Collection")
        st.caption("Collected fees compared with outstanding balances by month.")
        st.markdown(
            """
            <div class="finance-legend">
                <span class="finance-legend-item">
                    <span class="finance-legend-dot collected"></span>Collected
                </span>
                <span class="finance-legend-item">
                    <span class="finance-legend-dot outstanding"></span>Outstanding
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

        fig = px.bar(
            monthly_finance,
            x="Month",
            y=["Collected", "Outstanding"],
            barmode="group",
            color_discrete_sequence=["#10B981", "#EF4444"]
        )

        fig = modern_chart(fig, height=340, show_legend=False)
        fig.update_layout(
            title_text="",
            margin=dict(l=18, r=18, t=8, b=45),
            showlegend=False,
            xaxis_title="Month",
            yaxis_title="Amount (RM)"
        )
        fig.update_xaxes(
            tickfont=dict(color="#475569", size=11),
            title_font=dict(color="#475569", size=12)
        )
        fig.update_yaxes(
            tickfont=dict(color="#475569", size=11),
            title_font=dict(color="#475569", size=12),
            gridcolor="#E2E8F0"
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )

    with col2:
        payment_status = (
            filtered_payments.groupby("PaymentStatus")
            .size()
            .reset_index(name="Transactions")
        )

        st.markdown("#### Payment Settlement Status")
        st.caption("Distribution of paid, outstanding and overdue payment records.")
        st.markdown(
            """
            <div class="finance-legend">
                <span class="finance-legend-item">
                    <span class="finance-legend-dot paid"></span>Paid
                </span>
                <span class="finance-legend-item">
                    <span class="finance-legend-dot overdue"></span>Overdue
                </span>
                <span class="finance-legend-item">
                    <span class="finance-legend-dot outstanding"></span>Outstanding
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

        fig = px.pie(
            payment_status,
            names="PaymentStatus",
            values="Transactions",
            hole=0.62,
            color_discrete_sequence=["#10B981", "#F59E0B", "#EF4444"]
        )

        fig = modern_chart(fig, height=340, show_legend=False)
        fig.update_layout(
            title_text="",
            margin=dict(l=10, r=10, t=4, b=10),
            showlegend=False
        )
        fig.update_traces(
            textposition="inside",
            textinfo="percent",
            textfont=dict(color="#0F172A", size=12),
            hovertemplate="<b>%{label}</b><br>Transactions: %{value}<br>Share: %{percent}<extra></extra>"
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )

    finance_branch = (
        payments.groupby("BranchID")
        .agg(
            Revenue=("PaidAmountRM", "sum"),
            Outstanding=("OutstandingAmountRM", "sum")
        )
        .reset_index()
    )
    finance_branch["Branch"] = finance_branch["BranchID"].map(branch_map)

    st.markdown("#### Financial Performance by Branch")
    st.caption("Compare collected revenue and outstanding balances across branches.")
    st.markdown(
        """
        <div class="finance-legend">
            <span class="finance-legend-item">
                <span class="finance-legend-dot revenue"></span>Revenue
            </span>
            <span class="finance-legend-item">
                <span class="finance-legend-dot branch-outstanding"></span>Outstanding
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

    fig = px.bar(
        finance_branch,
        x="Branch",
        y=["Revenue", "Outstanding"],
        barmode="group",
        color_discrete_sequence=["#2563EB", "#F59E0B"]
    )

    fig = modern_chart(fig, height=390, show_legend=False)
    fig.update_layout(
        title_text="",
        margin=dict(l=18, r=18, t=8, b=52),
        showlegend=False,
        xaxis_title="Branch",
        yaxis_title="Amount (RM)"
    )
    fig.update_xaxes(
        tickfont=dict(color="#475569", size=11),
        title_font=dict(color="#475569", size=12)
    )
    fig.update_yaxes(
        tickfont=dict(color="#475569", size=11),
        title_font=dict(color="#475569", size=12),
        gridcolor="#E2E8F0"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

    with st.expander("🔎 Outstanding Receivables Detail Register"):
        outstanding_records = (
            filtered_payments[
                filtered_payments["OutstandingAmountRM"] > 0
            ]
            .merge(
                students[["StudentID", "StudentName"]],
                on="StudentID",
                how="left"
            )
        )

        st.dataframe(
            outstanding_records[
                [
                    "PaymentID",
                    "StudentName",
                    "BillingMonth",
                    "BilledAmountRM",
                    "PaidAmountRM",
                    "OutstandingAmountRM",
                    "PaymentStatus"
                ]
            ].sort_values("OutstandingAmountRM", ascending=False),
            use_container_width=True
        )

# =========================================================
# PAGE 5: BRANCH MANAGER
# =========================================================

elif st.session_state.page == "Branch Manager":

    dashboard_header(
        "Branch Operations Centre",
        "Branch performance, course utilization, and resource readiness"
    )

    if selected_branch == "All Branches":
        st.info("💡 Select a specific branch in the sidebar filters for detailed local operational analysis.")

    branch_students = filtered_students["StudentID"].nunique()
    branch_tutors = filtered_tutors["TutorID"].nunique()
    branch_attendance = (
        filtered_attendance["Present"].mean() * 100
        if not filtered_attendance.empty else 0
    )
    branch_revenue = filtered_payments["PaidAmountRM"].sum()

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        render_kpi("Branch Students", f"{branch_students:,}", "#2563EB")
    with k2:
        render_kpi("Active Tutors", f"{branch_tutors:,}", "#8B5CF6")
    with k3:
        render_kpi("Attendance Rate", f"{branch_attendance:.1f}%", "#10B981")
    with k4:
        render_kpi("Branch Revenue", f"RM {branch_revenue:,.0f}", "#0EA5E9")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        branch_courses = (
            filtered_enrolments.groupby("CourseID")["StudentID"]
            .nunique()
            .reset_index(name="Students")
        )
        branch_courses["Course"] = branch_courses["CourseID"].map(course_map)
        branch_courses = (
            branch_courses.sort_values("Students", ascending=False).head(10)
        )

        fig = px.bar(
            branch_courses.sort_values("Students"),
            x="Students",
            y="Course",
            orientation="h",
            title="Course Demand",
            color_discrete_sequence=["#2563EB"]
        )
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    with col2:
        fig = px.bar(
            filtered_inventory,
            x="ItemCategory",
            y="ClosingQty",
            color="StockStatus",
            title="Inventory Status",
            color_discrete_sequence=["#10B981", "#EF4444", "#F59E0B"]
        )
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    branch_comparison = (
        enrolments.groupby("BranchID")["StudentID"]
        .nunique()
        .reset_index(name="Students")
    )
    branch_comparison["Branch"] = branch_comparison["BranchID"].map(branch_map)

    fig = px.bar(
        branch_comparison,
        x="Branch",
        y="Students",
        title="Student Distribution Across Branches",
        color_discrete_sequence=["#0EA5E9"]
    )
    fig = modern_chart(fig, height=380)
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# =========================================================
# PAGE 6: MARKETING MANAGER
# =========================================================

elif st.session_state.page == "Marketing Manager":

    dashboard_header(
        "Marketing Performance Centre",
        "Campaign efficiency, student acquisition costs, and channel returns"
    )

    total_leads = marketing["Leads"].sum()
    marketing_enrolments = marketing["Enrolments"].sum()
    total_spend = marketing["SpendRM"].sum()
    conversion_rate = (
        marketing_enrolments / total_leads * 100
        if total_leads > 0 else 0
    )
    average_cpa = (
        total_spend / marketing_enrolments
        if marketing_enrolments > 0 else 0
    )

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        render_kpi("Total Marketing Leads", f"{total_leads:,}", "#2563EB")
    with k2:
        render_kpi("Conversions", f"{marketing_enrolments:,}", "#10B981")
    with k3:
        render_kpi("Conversion Rate", f"{conversion_rate:.1f}%", "#0EA5E9")
    with k4:
        render_kpi("Avg Cost / Acquisition", f"RM {average_cpa:,.0f}", "#8B5CF6")

    st.markdown("---")

    col1, col2 = st.columns([1.1, 0.9])

    with col1:
        campaign_data = marketing.sort_values("Enrolments", ascending=True)

        fig = px.bar(
            campaign_data,
            x="Enrolments",
            y="CampaignName",
            orientation="h",
            color="Channel",
            title="Enrolments by Campaign",
            color_discrete_sequence=CORPORATE_PALETTE
        )
        fig.update_yaxes(categoryorder="total ascending")
        fig = modern_chart(fig, height=380)
        fig.update_layout(showlegend=False)
        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )

    with col2:
        fig = px.scatter(
            marketing,
            x="SpendRM",
            y="Enrolments",
            size="Leads",
            color="Channel",
            title="Campaign Spend vs Enrolments",
            hover_name="CampaignName",
            color_discrete_sequence=CORPORATE_PALETTE
        )
        fig.update_traces(
            marker=dict(line=dict(width=1, color="#FFFFFF"), opacity=0.9)
        )
        fig = modern_chart(fig, height=380)
        fig.update_layout(showlegend=False)
        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )

    st.markdown("#### Student Acquisition Sources")

    acquisition = (
        students.groupby("AcquisitionSource")
        .size()
        .reset_index(name="Students")
        .sort_values("Students", ascending=False)
    )

    fig = px.bar(
        acquisition,
        x="AcquisitionSource",
        y="Students",
        color_discrete_sequence=["#2563EB"]
    )
    fig = modern_chart(fig, height=340)
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# =========================================================
# DATA EXPORT & FOOTER
# =========================================================

if st.session_state.page != "Home":
    st.markdown("---")
    c_left, c_right = st.columns([3, 1])

    with c_left:
        st.markdown("### 📥 Export Analytical Dataset")
        st.caption("Download the currently filtered dataset in CSV format for executive reporting.")

    with c_right:
        csv_data = filtered_enrolments.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download CSV Dataset",
            data=csv_data,
            file_name="StudySmart_Filtered_Enrolments.csv",
            mime="text/csv",
            use_container_width=True
        )

st.write("")
st.caption(
    "Study Smart Tuition Centre • Management Portal"
)
