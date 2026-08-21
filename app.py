import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Study Smart BI",
    page_icon="🍀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# DESIGN SYSTEM
# =========================================================

st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: "Inter", "Segoe UI", sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top right, rgba(59,130,246,0.07), transparent 28%),
            linear-gradient(180deg, #F7F9FC 0%, #EEF3F8 100%);
        color: #172033;
    }

    .block-container {
        padding-top: 1.15rem;
        padding-bottom: 2.4rem;
        max-width: 1540px;
    }

    /* ---------------- SIDEBAR ---------------- */

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0B2F59 0%, #092A4B 60%, #07233D 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 0.55rem;
    }

    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        gap: 0.35rem !important;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: #F8FBFF !important;
    }

    .brand-wrap {
        padding: 5px 2px 12px 2px;
    }

    .brand-title {
        font-size: 24px;
        font-weight: 800;
        letter-spacing: -0.45px;
        color: white;
    }

    .brand-subtitle {
        margin-top: 5px;
        font-size: 11px;
        letter-spacing: 1.9px;
        font-weight: 750;
        color: #ACC5DF;
    }

    .side-section {
        margin-top: 13px;
        margin-bottom: 8px;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 1.65px;
        color: #AFC6DF;
    }

    [data-testid="stSidebar"] hr {
        margin: 0.75rem 0 !important;
        border-color: rgba(255,255,255,0.09) !important;
    }

    /* Radio navigation */
    [data-testid="stSidebar"] [data-testid="stRadio"] > label {
        display: none !important;
    }

    [data-testid="stSidebar"] [role="radiogroup"] {
        gap: 0.12rem !important;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label {
        padding: 0.42rem 0.48rem !important;
        border-radius: 10px !important;
        transition: all 0.16s ease !important;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label:hover {
        background: rgba(255,255,255,0.08) !important;
        transform: translateX(2px);
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] span,
    [data-testid="stSidebar"] [data-testid="stRadio"] p {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        font-weight: 600 !important;
        opacity: 1 !important;
    }

    /* Selectboxes */
    [data-testid="stSidebar"] [data-testid="stSelectbox"] {
        margin-bottom: 0.18rem !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        min-height: 42px !important;
        border-radius: 10px !important;
        background: #FFFFFF !important;
        border: 1px solid #D7E1EC !important;
        box-shadow: none !important;
        transition: all 0.15s ease !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] span,
    [data-testid="stSidebar"] [data-baseweb="select"] input,
    [data-testid="stSidebar"] [data-baseweb="select"] div {
        color: #172033 !important;
        -webkit-text-fill-color: #172033 !important;
        opacity: 1 !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] svg {
        fill: #667085 !important;
        color: #667085 !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] > div:hover {
        border-color: #94B4D4 !important;
        transform: translateY(-1px);
    }

    [data-testid="stSidebar"] [data-baseweb="select"] > div:focus-within {
        border-color: #3B82F6 !important;
        box-shadow: 0 0 0 2px rgba(59,130,246,0.12) !important;
    }

    div[role="listbox"] {
        background: white !important;
        border: 1px solid #D9E3EE !important;
        border-radius: 10px !important;
        box-shadow: 0 14px 30px rgba(15,43,77,0.16) !important;
    }

    div[role="option"], li[role="option"] {
        background: white !important;
        color: #172033 !important;
        -webkit-text-fill-color: #172033 !important;
    }

    div[role="option"]:hover, li[role="option"]:hover {
        background: #EEF5FD !important;
    }

    [data-testid="stSidebar"] .stButton > button {
        width: 100%;
        min-height: 38px;
        border-radius: 10px;
        color: #FFFFFF;
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.16);
        font-weight: 650;
        transition: all 0.16s ease;
    }

    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(255,255,255,0.13);
        border-color: rgba(255,255,255,0.28);
        transform: translateY(-1px);
    }
/* ---------------- HOME ---------------- */

    .hero {
        padding: 28px 30px;
        border-radius: 22px;
        background:
            linear-gradient(135deg, rgba(11,47,89,0.98), rgba(20,83,145,0.94));
        box-shadow: 0 16px 40px rgba(11,47,89,0.16);
        margin-bottom: 18px;
    }

    .hero-kicker {
        color: #BCD8F3;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 1.7px;
        margin-bottom: 8px;
    }

    .hero-title {
        color: #FFFFFF;
        font-size: 34px;
        font-weight: 800;
        letter-spacing: -0.8px;
        margin: 0;
    }

    .hero-sub {
        color: #D5E6F6;
        font-size: 15px;
        margin-top: 9px;
        max-width: 720px;
        line-height: 1.55;
    }

    .home-section-title {
        margin-top: 18px;
        margin-bottom: 8px;
        color: #172033;
        font-size: 20px;
        font-weight: 750;
    }

    .role-card {
        background: rgba(255,255,255,0.98);
        border: 1px solid #DFE7F1;
        border-radius: 16px;
        padding: 18px 18px 16px 18px;
        min-height: 150px;
        box-shadow: 0 7px 20px rgba(15,43,77,0.045);
        transition: all 0.18s ease;
    }

    .role-card:hover {
        transform: translateY(-3px);
        border-color: #C6D6E7;
        box-shadow: 0 14px 28px rgba(15,43,77,0.08);
    }

    .role-icon {
        font-size: 24px;
        margin-bottom: 8px;
    }

    .role-title {
        color: #172033;
        font-size: 16px;
        font-weight: 750;
        margin-bottom: 4px;
    }

    .role-desc {
        color: #667085;
        font-size: 12px;
        line-height: 1.45;
    }

    /* ---------------- MAIN DASHBOARD ---------------- */

    h1 {
        font-size: 2.18rem !important;
        font-weight: 780 !important;
        letter-spacing: -0.04em;
        color: #172033;
        margin-bottom: 0.1rem !important;
    }

    .dashboard-label {
        display: inline-flex;
        padding: 6px 10px;
        border-radius: 999px;
        background: #EAF2FF;
        color: #1D64C8;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 0.14em;
        margin-bottom: 8px;
    }

    .dashboard-subtitle {
        color: #718096;
        font-size: 0.99rem;
        margin-top: -2px;
        margin-bottom: 13px;
    }

    .context-bar {
        margin-top: 6px;
        margin-bottom: 14px;
        padding: 9px 12px;
        border-radius: 11px;
        background: rgba(255,255,255,0.75);
        border: 1px solid #E1E8F0;
        color: #667085;
        font-size: 12px;
    }

    [data-testid="stMetric"] {
        min-height: 124px;
        padding: 18px 20px;
        border-radius: 16px;
        background: linear-gradient(145deg, #FFFFFF, #F8FBFF);
        border: 1px solid #DFE7F1;
        box-shadow:
            0 8px 22px rgba(15,43,77,0.05),
            0 2px 6px rgba(15,43,77,0.03);
        transition: all 0.18s ease;
    }

    [data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        border-color: #C2D3E5;
        box-shadow: 0 14px 30px rgba(15,43,77,0.09);
    }

    [data-testid="stMetricLabel"] {
        font-size: 0.86rem;
        font-weight: 650;
        color: #667085;
    }

    [data-testid="stMetricValue"] {
        font-size: 1.84rem;
        font-weight: 760;
        letter-spacing: -0.03em;
        color: #172033;
    }

    div[data-testid="stPlotlyChart"] {
        padding: 10px;
        border-radius: 16px;
        background: rgba(255,255,255,0.98);
        border: 1px solid #DFE7F1;
        box-shadow: 0 7px 20px rgba(15,43,77,0.045);
        overflow: hidden;
        transition: all 0.18s ease;
    }

    div[data-testid="stPlotlyChart"]:hover {
        border-color: #C9D8E7;
        box-shadow: 0 12px 28px rgba(15,43,77,0.08);
    }

    [data-testid="stExpander"] {
        background: rgba(255,255,255,0.97);
        border: 1px solid #DFE7F1;
        border-radius: 12px;
    }

    [data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #E2E8F0;
    }

    .stDownloadButton > button {
        background: linear-gradient(135deg, #0D5CC7, #0A3F8F);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.68rem 1rem;
        font-weight: 650;
        box-shadow: 0 8px 18px rgba(13,92,199,0.16);
    }

    hr {
        border: none;
        border-top: 1px solid #DFE7F1;
        margin: 1rem 0;
    }


    /* ===== SIDEBAR ACTIONS & SYSTEM ===== */
    [data-testid="stSidebar"] .stButton > button {
        min-height: 36px !important;
        padding: 0.45rem 0.75rem !important;
        font-size: 0.82rem !important;
        border-radius: 9px !important;
        background: rgba(255,255,255,0.07) !important;
        color: #F8FBFF !important;
        border: 1px solid rgba(255,255,255,0.14) !important;
        box-shadow: none !important;
    }

    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(255,255,255,0.12) !important;
        border-color: rgba(255,255,255,0.24) !important;
        transform: translateY(-1px);
    }

    .system-card {
        margin-top: 0.65rem;
        padding: 0.75rem 0.8rem;
        border-radius: 12px;
        background: rgba(255,255,255,0.055);
        border: 1px solid rgba(255,255,255,0.10);
    }

    .system-label {
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 1.4px;
        color: #9EBAD6;
        margin-bottom: 7px;
    }

    .system-status-row {
        display: flex;
        align-items: center;
        gap: 7px;
        margin-bottom: 7px;
    }

    .status-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #35D07F;
        box-shadow: 0 0 0 4px rgba(53,208,127,0.10);
        display: inline-block;
    }

    .system-status-text {
        color: #E9FFF3;
        font-size: 12px;
        font-weight: 700;
    }

    .system-name {
        color: #FFFFFF;
        font-size: 12px;
        font-weight: 700;
        margin-top: 2px;
    }

    .system-meta {
        color: #AFC6DF;
        font-size: 11px;
        margin-top: 2px;
    }

    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        padding-bottom: 0.8rem !important;
    }

    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# DATA
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
# HELPERS
# =========================================================

def modern_chart(fig, height=370):
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="Inter, Segoe UI, sans-serif",
            color="#475467",
            size=12
        ),
        title=dict(
            font=dict(size=16, color="#172033"),
            x=0.02,
            xanchor="left"
        ),
        margin=dict(l=20, r=20, t=58, b=28),
        legend=dict(
            title=None,
            orientation="h",
            yanchor="bottom",
            y=1.04,
            xanchor="right",
            x=1,
            font=dict(size=10)
        ),
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Inter"
        )
    )

    try:
        fig.update_xaxes(
            showgrid=False,
            zeroline=False,
            linecolor="#D9E3EE",
            tickfont=dict(color="#667085")
        )
        fig.update_yaxes(
            gridcolor="#EDF2F7",
            zeroline=False,
            linecolor="#D9E3EE",
            tickfont=dict(color="#667085")
        )
    except Exception:
        pass

    return fig


def dashboard_header(title, subtitle):
    st.markdown(
        '<div class="dashboard-label">STUDY SMART TUITION CENTRE</div>',
        unsafe_allow_html=True
    )
    st.title(title)
    st.markdown(
        f'<div class="dashboard-subtitle">{subtitle}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class="context-bar">
            <strong>Branch:</strong> {selected_branch}
            &nbsp;&nbsp;•&nbsp;&nbsp;
            <strong>Subject:</strong> {selected_subject}
            &nbsp;&nbsp;•&nbsp;&nbsp;
            <strong>Month:</strong> {selected_month}
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

st.sidebar.markdown(
    """
    <div class="brand-wrap">
        <div class="brand-title">🎓 Study Smart</div>
        <div class="brand-subtitle">MANAGEMENT PORTAL</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '<div class="side-section">MENU</div>',
    unsafe_allow_html=True
)

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

# Filters are useful on dashboards, not home
if st.session_state.page != "Home":
    st.sidebar.markdown(
        '<div class="side-section">FILTERS</div>',
        unsafe_allow_html=True
    )

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

    st.sidebar.markdown(
        '<div class="side-section">ACTIONS</div>',
        unsafe_allow_html=True
    )

    if st.sidebar.button("↻ Reset Filters", use_container_width=True):
        st.session_state.branch_filter = "All Branches"
        st.session_state.subject_filter = "All Subjects"
        st.session_state.month_filter = "All Months"
        st.rerun()

    st.sidebar.markdown(
        """
        <div class="system-card">
            <div class="system-label">SYSTEM</div>
            <div class="system-status-row">
                <span class="status-dot"></span>
                <span class="system-status-text">Connected</span>
            </div>
            <div class="system-name">Study Smart BI v2.0</div>
            <div class="system-meta">Data Warehouse</div>
        </div>
        """,
        unsafe_allow_html=True
    )

else:
    selected_branch = "All Branches"
    selected_subject = "All Subjects"
    selected_month = "All Months"

# =========================================================
# FILTER DATA
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

    filtered_students = filtered_students[
        filtered_students["BranchID"] == selected_branch_id
    ]
    filtered_tutors = filtered_tutors[
        filtered_tutors["BranchID"] == selected_branch_id
    ]
    filtered_enrolments = filtered_enrolments[
        filtered_enrolments["BranchID"] == selected_branch_id
    ]
    filtered_payments = filtered_payments[
        filtered_payments["BranchID"] == selected_branch_id
    ]
    filtered_attendance = filtered_attendance[
        filtered_attendance["BranchID"] == selected_branch_id
    ]
    filtered_scores = filtered_scores[
        filtered_scores["BranchID"] == selected_branch_id
    ]
    filtered_inventory = filtered_inventory[
        filtered_inventory["BranchID"] == selected_branch_id
    ]
    filtered_online = filtered_online[
        filtered_online["BranchID"] == selected_branch_id
    ]

if selected_subject != "All Subjects":
    selected_course_ids = courses.loc[
        courses["Subject"] == selected_subject,
        "CourseID"
    ].tolist()

    filtered_courses = filtered_courses[
        filtered_courses["CourseID"].isin(selected_course_ids)
    ]
    filtered_enrolments = filtered_enrolments[
        filtered_enrolments["CourseID"].isin(selected_course_ids)
    ]
    filtered_payments = filtered_payments[
        filtered_payments["CourseID"].isin(selected_course_ids)
    ]
    filtered_attendance = filtered_attendance[
        filtered_attendance["CourseID"].isin(selected_course_ids)
    ]
    filtered_scores = filtered_scores[
        filtered_scores["CourseID"].isin(selected_course_ids)
    ]
    filtered_online = filtered_online[
        filtered_online["CourseID"].isin(selected_course_ids)
    ]

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

    filtered_students = filtered_students[
        filtered_students["StudentID"].isin(valid_student_ids)
    ]
    filtered_tutors = filtered_tutors[
        filtered_tutors["TutorID"].isin(valid_tutor_ids)
    ]

# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    st.markdown(
        """
        <div class="hero">
            <div class="hero-kicker">STUDY SMART TUITION CENTRE</div>
            <div class="hero-title">Empowering Students. Inspiring Excellence.</div>
            <div class="hero-sub">
                Delivering quality tuition programmes through experienced educators,
                structured learning and continuous student development across our branches.
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

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Students", f"{total_students_home:,}")
    c2.metric("Total Revenue", f"RM {total_revenue_home:,.0f}")
    c3.metric("Attendance Rate", f"{attendance_home:.1f}%")

    c4, c5, c6 = st.columns(3)
    c4.metric("Branches", f"{total_branches_home}")
    c5.metric("Active Tutors", f"{total_tutors_home}")
    c6.metric("Courses", f"{total_courses_home}")

    st.markdown(
        '<div class="home-section-title">Stakeholder Dashboards</div>',
        unsafe_allow_html=True
    )
    st.caption(
        "Select the dashboard most relevant to your management responsibilities."
    )

    r1c1, r1c2, r1c3 = st.columns(3)

    with r1c1:
        st.markdown(
            """
            <div class="role-card">
                <div class="role-icon">👔</div>
                <div class="role-title">Executive Management</div>
                <div class="role-desc">
                    Organisation-wide KPIs, revenue, attendance, branch performance
                    and course demand.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Open Executive Dashboard →", use_container_width=True):
            set_page("Executive Management")

    with r1c2:
        st.markdown(
            """
            <div class="role-card">
                <div class="role-icon">🎓</div>
                <div class="role-title">Academic Manager</div>
                <div class="role-desc">
                    Academic results, attendance, tutor effectiveness,
                    learning modes and student support.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Open Academic Dashboard →", use_container_width=True):
            set_page("Academic Manager")

    with r1c3:
        st.markdown(
            """
            <div class="role-card">
                <div class="role-icon">💰</div>
                <div class="role-title">Finance Manager</div>
                <div class="role-desc">
                    Revenue, fee collection, outstanding balances
                    and branch-level financial performance.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Open Finance Dashboard →", use_container_width=True):
            set_page("Finance Manager")

    r2c1, r2c2, r2c3 = st.columns(3)

    with r2c1:
        st.markdown(
            """
            <div class="role-card">
                <div class="role-icon">🏢</div>
                <div class="role-title">Branch Manager</div>
                <div class="role-desc">
                    Branch operations, course demand, tutor capacity,
                    revenue and inventory status.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Open Branch Dashboard →", use_container_width=True):
            set_page("Branch Manager")

    with r2c2:
        st.markdown(
            """
            <div class="role-card">
                <div class="role-icon">📈</div>
                <div class="role-title">Marketing Manager</div>
                <div class="role-desc">
                    Campaign effectiveness, acquisition channels,
                    conversion rate and acquisition cost.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Open Marketing Dashboard →", use_container_width=True):
            set_page("Marketing Manager")

    with r2c3:
        st.markdown(
            """
            <div class="role-card">
                <div class="role-icon">🗄️</div>
                <div class="role-title">Integrated Data Warehouse</div>
                <div class="role-desc">
                    Curated operational data supporting role-based BI analysis
                    across all five management views.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.button(
            "Data Sources Connected ✓",
            disabled=True,
            use_container_width=True
        )

# =========================================================
# EXECUTIVE MANAGEMENT
# =========================================================

elif st.session_state.page == "Executive Management":

    dashboard_header(
        "Executive Management Dashboard",
        "Organisation-wide performance and strategic management overview"
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

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Students", f"{total_students:,}")
    c2.metric("Total Enrolments", f"{total_enrolments:,}")
    c3.metric("Attendance Rate", f"{attendance_rate:.1f}%")

    c4, c5, c6 = st.columns(3)
    c4.metric("Total Revenue", f"RM {total_revenue:,.0f}")
    c5.metric("Outstanding Fees", f"RM {outstanding_fees:,.0f}")
    c6.metric("Active Tutors", f"{active_tutors:,}")

    st.markdown("---")

    col1, col2 = st.columns([1.5, 1])

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

        fig = px.line(
            revenue_monthly,
            x="Month",
            y="PaidAmountRM",
            markers=True,
            title="Revenue Performance"
        )
        fig.update_layout(
            xaxis_title="",
            yaxis_title="Revenue (RM)",
            hovermode="x unified"
        )
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=attendance_rate,
                number={"suffix": "%"},
                title={"text": "Attendance Performance"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "#2474D2"},
                    "steps": [
                        {"range": [0, 80], "color": "#F1F5F9"},
                        {"range": [80, 90], "color": "#E2E8F0"},
                        {"range": [90, 100], "color": "#DBEAFE"}
                    ]
                }
            )
        )
        fig = modern_chart(fig, height=370)
        st.plotly_chart(fig, use_container_width=True)

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
            title="Branch Performance Comparison"
        )
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True)

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
            title="Course Popularity"
        )
        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True)

# =========================================================
# ACADEMIC MANAGER
# =========================================================

elif st.session_state.page == "Academic Manager":

    dashboard_header(
        "Academic Manager Dashboard",
        "Academic performance, tutor effectiveness and student engagement"
    )

    avg_score = filtered_scores["Score"].mean() if not filtered_scores.empty else 0
    attendance_rate = (
        filtered_attendance["Present"].mean() * 100
        if not filtered_attendance.empty else 0
    )
    active_courses = filtered_enrolments["CourseID"].nunique()
    active_tutors = filtered_tutors["TutorID"].nunique()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Average Academic Score", f"{avg_score:.1f}%")
    c2.metric("Attendance Rate", f"{attendance_rate:.1f}%")
    c3.metric("Active Courses", f"{active_courses}")
    c4.metric("Active Tutors", f"{active_tutors}")

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
            title="Academic Performance by Subject"
        )
        fig.update_yaxes(range=[0, 100])
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True)

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
            text="Score"
        )
        fig.update_xaxes(range=[0, 100])
        fig.update_traces(texttemplate="%{text:.1f}", textposition="outside")
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True)

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
            title="Attendance Trend"
        )
        fig.update_yaxes(range=[70, 100], ticksuffix="%")
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        learning_mode = (
            filtered_attendance.groupby("Mode")
            .size()
            .reset_index(name="Sessions")
        )

        fig = px.pie(
            learning_mode,
            names="Mode",
            values="Sessions",
            hole=0.55,
            title="Learning Mode Distribution"
        )
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True)

    with st.expander("🔎 Drill Down: Students Requiring Academic Support"):
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
# FINANCE MANAGER
# =========================================================

elif st.session_state.page == "Finance Manager":

    dashboard_header(
        "Finance Manager Dashboard",
        "Revenue, fee collection and financial performance"
    )

    net_billed = (
        filtered_payments["BilledAmountRM"].sum()
        - filtered_payments["DiscountAmountRM"].sum()
    )
    collected = filtered_payments["PaidAmountRM"].sum()
    outstanding = filtered_payments["OutstandingAmountRM"].sum()
    collection_rate = collected / net_billed * 100 if net_billed > 0 else 0

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Net Billed", f"RM {net_billed:,.0f}")
    c2.metric("Collected", f"RM {collected:,.0f}")
    c3.metric("Outstanding", f"RM {outstanding:,.0f}")
    c4.metric("Collection Rate", f"{collection_rate:.1f}%")

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

        fig = px.line(
            monthly_finance,
            x="Month",
            y=["Collected", "Outstanding"],
            markers=True,
            title="Collection vs Outstanding Trend"
        )
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        payment_status = (
            filtered_payments.groupby("PaymentStatus")
            .size()
            .reset_index(name="Transactions")
        )

        fig = px.pie(
            payment_status,
            names="PaymentStatus",
            values="Transactions",
            hole=0.55,
            title="Payment Status Distribution"
        )
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True)

    finance_branch = (
        payments.groupby("BranchID")
        .agg(
            Revenue=("PaidAmountRM", "sum"),
            Outstanding=("OutstandingAmountRM", "sum")
        )
        .reset_index()
    )
    finance_branch["Branch"] = finance_branch["BranchID"].map(branch_map)

    fig = px.bar(
        finance_branch,
        x="Branch",
        y=["Revenue", "Outstanding"],
        barmode="group",
        title="Financial Performance by Branch"
    )
    fig = modern_chart(fig, height=410)
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("🔎 Drill Down: Outstanding Payments"):
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
# BRANCH MANAGER
# =========================================================

elif st.session_state.page == "Branch Manager":

    dashboard_header(
        "Branch Manager Dashboard",
        "Branch-level operational performance and resource monitoring"
    )

    if selected_branch == "All Branches":
        st.info(
            "Select a specific branch from the sidebar for detailed branch-level analysis."
        )

    branch_students = filtered_students["StudentID"].nunique()
    branch_tutors = filtered_tutors["TutorID"].nunique()
    branch_attendance = (
        filtered_attendance["Present"].mean() * 100
        if not filtered_attendance.empty else 0
    )
    branch_revenue = filtered_payments["PaidAmountRM"].sum()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Students", f"{branch_students:,}")
    c2.metric("Tutors", f"{branch_tutors:,}")
    c3.metric("Attendance", f"{branch_attendance:.1f}%")
    c4.metric("Revenue", f"RM {branch_revenue:,.0f}")

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
            title="Course Demand"
        )
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.bar(
            filtered_inventory,
            x="ItemCategory",
            y="ClosingQty",
            color="StockStatus",
            title="Inventory Status",
            hover_data=["ReorderLevel"]
        )
        fig = modern_chart(fig)
        st.plotly_chart(fig, use_container_width=True)

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
        title="Student Distribution Across Branches"
    )
    fig = modern_chart(fig, height=390)
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# MARKETING MANAGER
# =========================================================

elif st.session_state.page == "Marketing Manager":

    dashboard_header(
        "Marketing Manager Dashboard",
        "Campaign effectiveness, acquisition efficiency and student growth"
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

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Marketing Leads", f"{total_leads:,}")
    c2.metric("Campaign Enrolments", f"{marketing_enrolments:,}")
    c3.metric("Conversion Rate", f"{conversion_rate:.1f}%")
    c4.metric("Average CPA", f"RM {average_cpa:,.0f}")

    st.markdown("---")

    col1, col2 = st.columns([1.05, 0.95])

    with col1:
        st.markdown("#### Enrolments by Campaign")
        st.caption("Campaigns ranked by student enrolment outcomes.")

        campaign_data = marketing.sort_values("Enrolments", ascending=True)

        fig = px.bar(
            campaign_data,
            x="Enrolments",
            y="CampaignName",
            orientation="h",
            color="Channel",
            hover_name="CampaignName",
            hover_data={
                "Channel": True,
                "SpendRM": ":,.0f",
                "ConversionRatePct": ":.1f",
                "CostPerAcquisitionRM": ":,.0f",
                "CampaignName": False
            }
        )
        fig.update_layout(
            showlegend=False,
            height=405,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=10, r=12, t=12, b=20),
            xaxis_title="Enrolments",
            yaxis_title="",
            font=dict(family="Inter, Segoe UI, sans-serif", color="#475467", size=12)
        )
        fig.update_xaxes(showgrid=True, gridcolor="#EDF2F7", zeroline=False)
        fig.update_yaxes(showgrid=False, categoryorder="total ascending")
        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )

    with col2:
        st.markdown("#### Campaign Spend vs Enrolments")
        st.caption("Evaluate whether higher campaign spending produces stronger enrolment.")

        fig = px.scatter(
            marketing,
            x="SpendRM",
            y="Enrolments",
            size="Leads",
            color="Channel",
            hover_name="CampaignName",
            hover_data={
                "SpendRM": ":,.0f",
                "Enrolments": True,
                "Leads": True,
                "ConversionRatePct": ":.1f",
                "CostPerAcquisitionRM": ":,.0f",
                "Channel": True
            }
        )
        fig.update_traces(
            marker=dict(
                line=dict(width=1.4, color="rgba(255,255,255,0.90)"),
                opacity=0.88
            )
        )
        fig.update_layout(
            showlegend=False,
            height=405,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=10, r=12, t=12, b=20),
            xaxis_title="Spend (RM)",
            yaxis_title="Enrolments",
            font=dict(family="Inter, Segoe UI, sans-serif", color="#475467", size=12)
        )
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=True, gridcolor="#EDF2F7", zeroline=False)
        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )

    st.markdown("#### Student Acquisition Sources")
    st.caption("Primary channels through which students discovered Study Smart.")

    acquisition = (
        students.groupby("AcquisitionSource")
        .size()
        .reset_index(name="Students")
        .sort_values("Students", ascending=False)
    )

    fig = px.bar(
        acquisition,
        x="AcquisitionSource",
        y="Students"
    )
    fig.update_layout(
        showlegend=False,
        height=350,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=12, t=12, b=20),
        xaxis_title="Acquisition Source",
        yaxis_title="Students",
        font=dict(family="Inter, Segoe UI, sans-serif", color="#475467", size=12)
    )
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor="#EDF2F7", zeroline=False)
    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

# =========================================================
# DOWNLOAD + FOOTER
# =========================================================

if st.session_state.page != "Home":
    st.markdown("---")
    st.markdown("### Download Filtered Data")

    csv_data = filtered_enrolments.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Filtered Enrolment Data",
        data=csv_data,
        file_name="StudySmart_Filtered_Enrolments.csv",
        mime="text/csv"
    )

st.caption(
    "Study Smart Tuition Centre • Management Portal "
    "• Synthetic data for academic demonstration"
)
