import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Study Smart BI Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>
    html, body, [class*="css"] {font-family: "Inter", "Segoe UI", sans-serif;}
    .stApp {
        background: radial-gradient(circle at top right, rgba(37,99,235,0.07), transparent 28%), linear-gradient(180deg,#f7f9fc 0%,#eef3f8 100%);
        color:#172033;
    }
    .block-container {padding-top:1.4rem;padding-bottom:3rem;max-width:1550px;}
    [data-testid="stSidebar"] {background:linear-gradient(180deg,#0A3A6E 0%,#082F59 58%,#062744 100%);border-right:1px solid rgba(255,255,255,.08);}
    [data-testid="stSidebar"] > div:first-child {padding-top:1rem;}
    [data-testid="stSidebar"] * {color:#F7FBFF;}
    [data-testid="stSidebar"] h1,[data-testid="stSidebar"] h2,[data-testid="stSidebar"] h3 {color:white;font-weight:750;}
    [data-testid="stSidebar"] [data-baseweb="select"] > div {background:rgba(255,255,255,.97);border:1px solid rgba(255,255,255,.20);border-radius:12px;min-height:44px;}
    [data-testid="stSidebar"] [data-baseweb="select"] * {color:#172033 !important;}
    h1 {font-size:2.35rem !important;font-weight:760 !important;letter-spacing:-.035em;color:#172033;margin-bottom:.15rem !important;}
    h2 {font-weight:720 !important;letter-spacing:-.02em;}
    .dashboard-label {display:inline-flex;align-items:center;padding:6px 11px;border-radius:999px;background:#EAF2FF;color:#1D64C8;font-size:11px;font-weight:800;letter-spacing:.14em;margin-bottom:10px;}
    .dashboard-subtitle {color:#718096;font-size:1.02rem;margin-top:-2px;margin-bottom:18px;}
    .section-title {font-size:20px;font-weight:700;margin-top:8px;margin-bottom:8px;}
    [data-testid="stMetric"] {background:linear-gradient(145deg,rgba(255,255,255,.99),rgba(247,250,255,.98));border:1px solid #DFE7F1;padding:19px 21px;border-radius:18px;min-height:136px;box-shadow:0 8px 24px rgba(15,43,77,.06),0 2px 6px rgba(15,43,77,.04);transition:transform .20s ease,box-shadow .20s ease,border-color .20s ease;}
    [data-testid="stMetric"]:hover {transform:translateY(-3px);box-shadow:0 14px 34px rgba(15,43,77,.10),0 4px 10px rgba(15,43,77,.05);border-color:#BFD0E4;}
    [data-testid="stMetricLabel"] {font-size:.88rem;font-weight:650;color:#667085;}
    [data-testid="stMetricValue"] {font-size:1.9rem;font-weight:760;color:#172033;letter-spacing:-.03em;}
    div[data-testid="stPlotlyChart"] {background:rgba(255,255,255,.97);border:1px solid #DFE7F1;border-radius:18px;padding:12px;box-shadow:0 8px 24px rgba(15,43,77,.05);overflow:hidden;}
    [data-testid="stExpander"] {background:rgba(255,255,255,.96);border:1px solid #DFE7F1;border-radius:14px;box-shadow:0 5px 18px rgba(15,43,77,.04);}
    [data-testid="stDataFrame"] {border-radius:12px;overflow:hidden;border:1px solid #E2E8F0;}
    .stDownloadButton > button {background:linear-gradient(135deg,#0D5CC7,#0A3F8F);color:white;border:none;border-radius:12px;padding:.70rem 1.1rem;font-weight:650;box-shadow:0 8px 20px rgba(13,92,199,.18);transition:all .20s ease;}
    .stDownloadButton > button:hover {transform:translateY(-2px);box-shadow:0 12px 28px rgba(13,92,199,.25);}
    hr {border:none;border-top:1px solid #DFE7F1;margin:1.55rem 0;}
    ::-webkit-scrollbar {width:8px;height:8px;}
    ::-webkit-scrollbar-track {background:transparent;}
    ::-webkit-scrollbar-thumb {background:#C5D0DE;border-radius:10px;}
    footer {visibility:hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# LOAD DATA
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
        "online_sessions": pd.read_excel(
            file_path,
            sheet_name="Online Sessions"
        )
    }

    # Date conversion
    data["students"]["RegistrationDate"] = pd.to_datetime(
        data["students"]["RegistrationDate"],
        errors="coerce"
    )

    data["enrolments"]["EnrolmentDate"] = pd.to_datetime(
        data["enrolments"]["EnrolmentDate"],
        errors="coerce"
    )

    data["payments"]["BillingMonth"] = pd.to_datetime(
        data["payments"]["BillingMonth"],
        errors="coerce"
    )

    data["payments"]["PaymentDate"] = pd.to_datetime(
        data["payments"]["PaymentDate"],
        errors="coerce"
    )

    data["attendance"]["SessionDate"] = pd.to_datetime(
        data["attendance"]["SessionDate"],
        errors="coerce"
    )

    data["exam_scores"]["AssessmentDate"] = pd.to_datetime(
        data["exam_scores"]["AssessmentDate"],
        errors="coerce"
    )

    data["marketing"]["StartDate"] = pd.to_datetime(
        data["marketing"]["StartDate"],
        errors="coerce"
    )

    data["marketing"]["EndDate"] = pd.to_datetime(
        data["marketing"]["EndDate"],
        errors="coerce"
    )

    data["online_sessions"]["SessionDate"] = pd.to_datetime(
        data["online_sessions"]["SessionDate"],
        errors="coerce"
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

# =========================================================
# LOOKUP MAPS
# =========================================================

branch_map = dict(
    zip(
        branches["BranchID"],
        branches["BranchName"]
    )
)

course_map = dict(
    zip(
        courses["CourseID"],
        courses["CourseName"]
    )
)

subject_map = dict(
    zip(
        courses["CourseID"],
        courses["Subject"]
    )
)

tutor_map = dict(
    zip(
        tutors["TutorID"],
        tutors["TutorName"]
    )
)

# =========================================================
# MODERN CHART THEME
# =========================================================

def modern_chart(fig, height=380):
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, Segoe UI, sans-serif", color="#475467", size=13),
        title=dict(font=dict(size=17, color="#172033"), x=0.02, xanchor="left"),
        margin=dict(l=25, r=25, t=60, b=30),
        legend=dict(title=None, orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        hoverlabel=dict(bgcolor="white", font_size=13, font_family="Inter")
    )
    try:
        fig.update_xaxes(showgrid=False, zeroline=False, linecolor="#DBE4EE", tickfont=dict(color="#667085"))
        fig.update_yaxes(gridcolor="#EDF2F7", zeroline=False, linecolor="#DBE4EE", tickfont=dict(color="#667085"))
    except Exception:
        pass
    return fig

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    """
    <div style="padding:10px 0 20px 0;">
        <div style="font-size:24px;font-weight:800;letter-spacing:-0.4px;color:white;">🎓 Study Smart</div>
        <div style="font-size:12px;letter-spacing:1.6px;color:#B8CEE6;margin-top:3px;">TUITION CENTRE</div>
    </div>
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown("---")

dashboard_view = st.sidebar.radio(
    "Stakeholder View",
    [
        "Executive Management",
        "Academic Manager",
        "Finance Manager",
        "Branch Manager",
        "Marketing Manager"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Filters")

branch_options = (
    ["All Branches"]
    + sorted(
        branches["BranchName"]
        .dropna()
        .unique()
        .tolist()
    )
)

selected_branch = st.sidebar.selectbox(
    "Branch",
    branch_options
)

subject_options = (
    ["All Subjects"]
    + sorted(
        courses["Subject"]
        .dropna()
        .unique()
        .tolist()
    )
)

selected_subject = st.sidebar.selectbox(
    "Subject",
    subject_options
)

month_options = (
    ["All Months"]
    + sorted(
        payments["BillingMonth"]
        .dropna()
        .dt.strftime("%Y-%m")
        .unique()
        .tolist()
    )
)

selected_month = st.sidebar.selectbox(
    "Month",
    month_options
)

st.sidebar.markdown("---")

st.sidebar.success(
    "All operational data sources connected"
)

st.sidebar.caption(
    "Source: Study Smart Data Warehouse"
)

# =========================================================
# CREATE FILTERED DATA
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

# =========================================================
# BRANCH FILTER
# =========================================================

selected_branch_id = None

if selected_branch != "All Branches":

    selected_branch_id = branches.loc[
        branches["BranchName"] == selected_branch,
        "BranchID"
    ].iloc[0]

    filtered_students = filtered_students[
        filtered_students["BranchID"]
        == selected_branch_id
    ]

    filtered_tutors = filtered_tutors[
        filtered_tutors["BranchID"]
        == selected_branch_id
    ]

    filtered_enrolments = filtered_enrolments[
        filtered_enrolments["BranchID"]
        == selected_branch_id
    ]

    filtered_payments = filtered_payments[
        filtered_payments["BranchID"]
        == selected_branch_id
    ]

    filtered_attendance = filtered_attendance[
        filtered_attendance["BranchID"]
        == selected_branch_id
    ]

    filtered_scores = filtered_scores[
        filtered_scores["BranchID"]
        == selected_branch_id
    ]

    filtered_inventory = filtered_inventory[
        filtered_inventory["BranchID"]
        == selected_branch_id
    ]

    filtered_online = filtered_online[
        filtered_online["BranchID"]
        == selected_branch_id
    ]

# =========================================================
# SUBJECT FILTER
# =========================================================

if selected_subject != "All Subjects":

    selected_course_ids = courses.loc[
        courses["Subject"] == selected_subject,
        "CourseID"
    ].tolist()

    filtered_courses = filtered_courses[
        filtered_courses["CourseID"]
        .isin(selected_course_ids)
    ]

    filtered_enrolments = filtered_enrolments[
        filtered_enrolments["CourseID"]
        .isin(selected_course_ids)
    ]

    filtered_payments = filtered_payments[
        filtered_payments["CourseID"]
        .isin(selected_course_ids)
    ]

    filtered_attendance = filtered_attendance[
        filtered_attendance["CourseID"]
        .isin(selected_course_ids)
    ]

    filtered_scores = filtered_scores[
        filtered_scores["CourseID"]
        .isin(selected_course_ids)
    ]

    filtered_online = filtered_online[
        filtered_online["CourseID"]
        .isin(selected_course_ids)
    ]

# =========================================================
# MONTH FILTER
# =========================================================

if selected_month != "All Months":

    filtered_payments = filtered_payments[
        filtered_payments["BillingMonth"]
        .dt.strftime("%Y-%m")
        == selected_month
    ]

    filtered_attendance = filtered_attendance[
        filtered_attendance["SessionDate"]
        .dt.strftime("%Y-%m")
        == selected_month
    ]

    filtered_enrolments = filtered_enrolments[
        filtered_enrolments["EnrolmentDate"]
        .dt.strftime("%Y-%m")
        == selected_month
    ]

    filtered_online = filtered_online[
        filtered_online["SessionDate"]
        .dt.strftime("%Y-%m")
        == selected_month
    ]

# =========================================================
# SYNC STUDENTS AND TUTORS
# =========================================================

if (
    selected_subject != "All Subjects"
    or selected_month != "All Months"
):

    valid_student_ids = filtered_enrolments[
        "StudentID"
    ].dropna().unique()

    filtered_students = filtered_students[
        filtered_students["StudentID"]
        .isin(valid_student_ids)
    ]

    valid_tutor_ids = filtered_enrolments[
        "TutorID"
    ].dropna().unique()

    filtered_tutors = filtered_tutors[
        filtered_tutors["TutorID"]
        .isin(valid_tutor_ids)
    ]

# =========================================================
# HEADER FUNCTION
# =========================================================

def dashboard_header(title, subtitle):

    st.markdown(
        '<div class="dashboard-label">'
        'BUSINESS INTELLIGENCE'
        '</div>',
        unsafe_allow_html=True
    )

    st.title(title)

    st.markdown(
        f'<div class="dashboard-subtitle">'
        f'{subtitle}'
        f'</div>',
        unsafe_allow_html=True
    )

    st.caption(
        f"Branch: {selected_branch}   |   "
        f"Subject: {selected_subject}   |   "
        f"Month: {selected_month}"
    )

    st.markdown(
        """
        <div style="margin-top:10px;margin-bottom:4px;padding:10px 12px;background:rgba(255,255,255,.72);border:1px solid #E3EAF2;border-radius:12px;color:#667085;font-size:12px;">
            Live analytical view powered by integrated Study Smart operational data.
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# EXECUTIVE MANAGEMENT
# =========================================================

if dashboard_view == "Executive Management":

    dashboard_header(
        "Executive Dashboard",
        "Overview of organisational performance"
    )

    total_students = filtered_students[
        "StudentID"
    ].nunique()

    total_enrolments = filtered_enrolments[
        "EnrolmentID"
    ].nunique()

    attendance_rate = (
        filtered_attendance["Present"].mean() * 100
        if not filtered_attendance.empty
        else 0
    )

    total_revenue = filtered_payments[
        "PaidAmountRM"
    ].sum()

    outstanding_fees = filtered_payments[
        "OutstandingAmountRM"
    ].sum()

    active_tutors = filtered_tutors[
        "TutorID"
    ].nunique()

    # KPI CARDS
    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Total Students",
        f"{total_students:,}"
    )

    c2.metric(
        "Total Enrolments",
        f"{total_enrolments:,}"
    )

    c3.metric(
        "Attendance Rate",
        f"{attendance_rate:.1f}%"
    )

    c4, c5, c6 = st.columns(3)

    c4.metric(
        "Total Revenue",
        f"RM {total_revenue:,.0f}"
    )

    c5.metric(
        "Outstanding Fees",
        f"RM {outstanding_fees:,.0f}"
    )

    c6.metric(
        "Active Tutors",
        f"{active_tutors:,}"
    )

    st.markdown("---")

    # REVENUE TREND
    col1, col2 = st.columns([1.5, 1])

    with col1:

        revenue_trend = payments.copy()

        if selected_branch_id is not None:
            revenue_trend = revenue_trend[
                revenue_trend["BranchID"]
                == selected_branch_id
            ]

        if selected_subject != "All Subjects":
            revenue_trend = revenue_trend[
                revenue_trend["CourseID"]
                .isin(selected_course_ids)
            ]

        revenue_trend["Month"] = (
            revenue_trend["BillingMonth"]
            .dt.strftime("%b")
        )

        revenue_monthly = (
            revenue_trend
            .groupby("Month")["PaidAmountRM"]
            .sum()
            .reindex(
                ["Jan", "Feb", "Mar", "Apr", "May"]
            )
            .fillna(0)
            .reset_index()
        )

        fig_revenue = px.line(
            revenue_monthly,
            x="Month",
            y="PaidAmountRM",
            markers=True,
            title="Revenue Trend"
        )

        fig_revenue.update_layout(
            xaxis_title="",
            yaxis_title="Revenue (RM)",
            hovermode="x unified"
        )

        fig_revenue = modern_chart(fig_revenue)



        st.plotly_chart(
            fig_revenue,
            use_container_width=True
        )

    # ATTENDANCE GAUGE
    with col2:

        fig_attendance = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=attendance_rate,
                number={
                    "suffix": "%"
                },
                title={
                    "text": "Attendance Performance"
                },
                gauge={
                    "axis": {
                        "range": [0, 100]
                    },
                    "bar": {
                        "color": "#2474D2"
                    },
                    "steps": [
                        {
                            "range": [0, 80],
                            "color": "#F1F5F9"
                        },
                        {
                            "range": [80, 90],
                            "color": "#E2E8F0"
                        },
                        {
                            "range": [90, 100],
                            "color": "#DBEAFE"
                        }
                    ]
                }
            )
        )

        fig_attendance.update_layout(
            height=350
        )

        fig_attendance = modern_chart(fig_attendance, height=350)



        st.plotly_chart(
            fig_attendance,
            use_container_width=True
        )

    # BRANCH & COURSE
    col3, col4 = st.columns(2)

    with col3:

        branch_students = (
            enrolments
            .groupby("BranchID")["StudentID"]
            .nunique()
            .reset_index(
                name="Students"
            )
        )

        branch_students["Branch"] = (
            branch_students["BranchID"]
            .map(branch_map)
        )

        fig_branch = px.bar(
            branch_students.sort_values(
                "Students"
            ),
            x="Students",
            y="Branch",
            orientation="h",
            title="Students by Branch"
        )

        fig_branch = modern_chart(fig_branch)



        st.plotly_chart(
            fig_branch,
            use_container_width=True
        )

    with col4:

        course_popularity = (
            filtered_enrolments
            .groupby("CourseID")["StudentID"]
            .nunique()
            .reset_index(
                name="Students"
            )
        )

        course_popularity["Course"] = (
            course_popularity["CourseID"]
            .map(course_map)
        )

        course_popularity = (
            course_popularity
            .sort_values(
                "Students",
                ascending=False
            )
            .head(7)
        )

        fig_course = px.bar(
            course_popularity,
            x="Students",
            y="Course",
            orientation="h",
            title="Course Popularity"
        )

        fig_course.update_layout(
            yaxis={
                "categoryorder": "total ascending"
            }
        )

        fig_course = modern_chart(fig_course)



        st.plotly_chart(
            fig_course,
            use_container_width=True
        )

# =========================================================
# ACADEMIC MANAGER
# =========================================================

elif dashboard_view == "Academic Manager":

    dashboard_header(
        "Academic Manager Dashboard",
        "Academic performance and student engagement"
    )

    avg_score = (
        filtered_scores["Score"].mean()
        if not filtered_scores.empty
        else 0
    )

    attendance_rate = (
        filtered_attendance["Present"].mean() * 100
        if not filtered_attendance.empty
        else 0
    )

    active_courses = filtered_enrolments[
        "CourseID"
    ].nunique()

    active_tutors = filtered_tutors[
        "TutorID"
    ].nunique()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Average Academic Score",
        f"{avg_score:.1f}%"
    )

    c2.metric(
        "Attendance Rate",
        f"{attendance_rate:.1f}%"
    )

    c3.metric(
        "Active Courses",
        f"{active_courses}"
    )

    c4.metric(
        "Active Tutors",
        f"{active_tutors}"
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    # SCORE BY SUBJECT
    with col1:

        subject_scores = (
            filtered_scores
            .copy()
        )

        subject_scores["Subject"] = (
            subject_scores["CourseID"]
            .map(subject_map)
        )

        subject_scores = (
            subject_scores
            .groupby("Subject")["Score"]
            .mean()
            .reset_index()
        )

        fig_scores = px.bar(
            subject_scores,
            x="Subject",
            y="Score",
            title="Academic Performance by Subject",
            text_auto=".1f"
        )

        fig_scores.update_yaxes(
            range=[0, 100]
        )

        fig_scores = modern_chart(fig_scores)



        st.plotly_chart(
            fig_scores,
            use_container_width=True
        )

    # TUTOR PERFORMANCE
    with col2:

        tutor_performance = (
            filtered_scores
            .groupby("TutorID")["Score"]
            .mean()
            .reset_index()
        )

        tutor_performance["Tutor"] = (
            tutor_performance["TutorID"]
            .map(tutor_map)
        )

        tutor_performance = (
            tutor_performance
            .sort_values(
                "Score",
                ascending=False
            )
            .head(10)
        )

        fig_tutor = px.bar(
            tutor_performance.sort_values(
                "Score"
            ),
            x="Score",
            y="Tutor",
            orientation="h",
            title="Tutor Performance"
        )

        fig_tutor.update_xaxes(
            range=[0, 100]
        )

        fig_tutor = modern_chart(fig_tutor)



        st.plotly_chart(
            fig_tutor,
            use_container_width=True
        )

    col3, col4 = st.columns(2)

    # ATTENDANCE TREND
    with col3:

        att_data = attendance.copy()

        if selected_branch_id is not None:
            att_data = att_data[
                att_data["BranchID"]
                == selected_branch_id
            ]

        if selected_subject != "All Subjects":
            att_data = att_data[
                att_data["CourseID"]
                .isin(selected_course_ids)
            ]

        att_data["Month"] = (
            att_data["SessionDate"]
            .dt.strftime("%b")
        )

        attendance_trend = (
            att_data
            .groupby("Month")["Present"]
            .mean()
            .mul(100)
            .reindex(
                ["Jan", "Feb", "Mar", "Apr", "May"]
            )
            .reset_index(
                name="AttendanceRate"
            )
        )

        fig_att = px.line(
            attendance_trend,
            x="Month",
            y="AttendanceRate",
            markers=True,
            title="Attendance Trend"
        )

        fig_att.update_yaxes(
            range=[70, 100],
            ticksuffix="%"
        )

        fig_att = modern_chart(fig_att)



        st.plotly_chart(
            fig_att,
            use_container_width=True
        )

    # PHYSICAL VS ONLINE
    with col4:

        learning_mode = (
            filtered_attendance
            .groupby("Mode")
            .size()
            .reset_index(
                name="Sessions"
            )
        )

        fig_mode = px.pie(
            learning_mode,
            names="Mode",
            values="Sessions",
            hole=0.55,
            title="Learning Mode Distribution"
        )

        fig_mode = modern_chart(fig_mode)



        st.plotly_chart(
            fig_mode,
            use_container_width=True
        )

    # DRILL DOWN
    with st.expander(
        "🔎 Drill Down: Students Requiring Academic Support"
    ):

        low_scores = filtered_scores[
            filtered_scores["Score"] < 60
        ].copy()

        low_scores = low_scores.merge(
            students[
                [
                    "StudentID",
                    "StudentName",
                    "Level"
                ]
            ],
            on="StudentID",
            how="left"
        )

        low_scores["Course"] = (
            low_scores["CourseID"]
            .map(course_map)
        )

        st.dataframe(
            low_scores[
                [
                    "StudentID",
                    "StudentName",
                    "Level",
                    "Course",
                    "Score"
                ]
            ].sort_values(
                "Score"
            ),
            use_container_width=True
        )

# =========================================================
# FINANCE MANAGER
# =========================================================

elif dashboard_view == "Finance Manager":

    dashboard_header(
        "Finance Manager Dashboard",
        "Revenue, fee collection and financial performance"
    )

    net_billed = (
        filtered_payments["BilledAmountRM"].sum()
        -
        filtered_payments["DiscountAmountRM"].sum()
    )

    collected = filtered_payments[
        "PaidAmountRM"
    ].sum()

    outstanding = filtered_payments[
        "OutstandingAmountRM"
    ].sum()

    collection_rate = (
        collected / net_billed * 100
        if net_billed > 0
        else 0
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Net Billed",
        f"RM {net_billed:,.0f}"
    )

    c2.metric(
        "Collected",
        f"RM {collected:,.0f}"
    )

    c3.metric(
        "Outstanding",
        f"RM {outstanding:,.0f}"
    )

    c4.metric(
        "Collection Rate",
        f"{collection_rate:.1f}%"
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        finance_data = payments.copy()

        if selected_branch_id is not None:
            finance_data = finance_data[
                finance_data["BranchID"]
                == selected_branch_id
            ]

        if selected_subject != "All Subjects":
            finance_data = finance_data[
                finance_data["CourseID"]
                .isin(selected_course_ids)
            ]

        finance_data["Month"] = (
            finance_data["BillingMonth"]
            .dt.strftime("%b")
        )

        monthly_finance = (
            finance_data
            .groupby("Month")
            .agg(
                Collected=(
                    "PaidAmountRM",
                    "sum"
                ),
                Outstanding=(
                    "OutstandingAmountRM",
                    "sum"
                )
            )
            .reindex(
                ["Jan", "Feb", "Mar", "Apr", "May"]
            )
            .fillna(0)
            .reset_index()
        )

        fig_finance = px.line(
            monthly_finance,
            x="Month",
            y=[
                "Collected",
                "Outstanding"
            ],
            markers=True,
            title="Collection vs Outstanding Trend"
        )

        fig_finance = modern_chart(fig_finance)



        st.plotly_chart(
            fig_finance,
            use_container_width=True
        )

    with col2:

        payment_status = (
            filtered_payments
            .groupby("PaymentStatus")
            .size()
            .reset_index(
                name="Transactions"
            )
        )

        fig_status = px.pie(
            payment_status,
            names="PaymentStatus",
            values="Transactions",
            hole=0.55,
            title="Payment Status Distribution"
        )

        fig_status = modern_chart(fig_status)



        st.plotly_chart(
            fig_status,
            use_container_width=True
        )

    # FINANCE BY BRANCH
    finance_branch = (
        payments
        .groupby("BranchID")
        .agg(
            Revenue=(
                "PaidAmountRM",
                "sum"
            ),
            Outstanding=(
                "OutstandingAmountRM",
                "sum"
            )
        )
        .reset_index()
    )

    finance_branch["Branch"] = (
        finance_branch["BranchID"]
        .map(branch_map)
    )

    fig_finance_branch = px.bar(
        finance_branch,
        x="Branch",
        y=[
            "Revenue",
            "Outstanding"
        ],
        barmode="group",
        title="Financial Performance by Branch"
    )

    fig_finance_branch = modern_chart(fig_finance_branch)



    st.plotly_chart(
        fig_finance_branch,
        use_container_width=True
    )

    with st.expander(
        "🔎 Drill Down: Outstanding Payments"
    ):

        outstanding_records = (
            filtered_payments[
                filtered_payments[
                    "OutstandingAmountRM"
                ] > 0
            ]
            .merge(
                students[
                    [
                        "StudentID",
                        "StudentName"
                    ]
                ],
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
            ].sort_values(
                "OutstandingAmountRM",
                ascending=False
            ),
            use_container_width=True
        )

# =========================================================
# BRANCH MANAGER
# =========================================================

elif dashboard_view == "Branch Manager":

    dashboard_header(
        "Branch Manager Dashboard",
        "Branch-level operational performance"
    )

    if selected_branch == "All Branches":
        st.info(
            "Select a specific branch from the sidebar "
            "for detailed branch-level analysis."
        )

    branch_students = filtered_students[
        "StudentID"
    ].nunique()

    branch_tutors = filtered_tutors[
        "TutorID"
    ].nunique()

    branch_attendance = (
        filtered_attendance["Present"].mean() * 100
        if not filtered_attendance.empty
        else 0
    )

    branch_revenue = filtered_payments[
        "PaidAmountRM"
    ].sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Students",
        f"{branch_students:,}"
    )

    c2.metric(
        "Tutors",
        f"{branch_tutors:,}"
    )

    c3.metric(
        "Attendance",
        f"{branch_attendance:.1f}%"
    )

    c4.metric(
        "Revenue",
        f"RM {branch_revenue:,.0f}"
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    # COURSE DEMAND
    with col1:

        branch_courses = (
            filtered_enrolments
            .groupby("CourseID")["StudentID"]
            .nunique()
            .reset_index(
                name="Students"
            )
        )

        branch_courses["Course"] = (
            branch_courses["CourseID"]
            .map(course_map)
        )

        branch_courses = (
            branch_courses
            .sort_values(
                "Students",
                ascending=False
            )
            .head(10)
        )

        fig_branch_courses = px.bar(
            branch_courses.sort_values(
                "Students"
            ),
            x="Students",
            y="Course",
            orientation="h",
            title="Course Demand"
        )

        fig_branch_courses = modern_chart(fig_branch_courses)



        st.plotly_chart(
            fig_branch_courses,
            use_container_width=True
        )

    # INVENTORY
    with col2:

        fig_inventory = px.bar(
            filtered_inventory,
            x="ItemCategory",
            y="ClosingQty",
            color="StockStatus",
            title="Inventory Status",
            hover_data=[
                "ReorderLevel"
            ]
        )

        fig_inventory = modern_chart(fig_inventory)



        st.plotly_chart(
            fig_inventory,
            use_container_width=True
        )

    # BRANCH COMPARISON
    branch_comparison = (
        enrolments
        .groupby("BranchID")["StudentID"]
        .nunique()
        .reset_index(
            name="Students"
        )
    )

    branch_comparison["Branch"] = (
        branch_comparison["BranchID"]
        .map(branch_map)
    )

    fig_compare = px.bar(
        branch_comparison,
        x="Branch",
        y="Students",
        title="Student Distribution Across Branches"
    )

    fig_compare = modern_chart(fig_compare)



    st.plotly_chart(
        fig_compare,
        use_container_width=True
    )

# =========================================================
# MARKETING MANAGER
# =========================================================

elif dashboard_view == "Marketing Manager":

    dashboard_header(
        "Marketing Manager Dashboard",
        "Campaign effectiveness and student acquisition"
    )

    total_leads = marketing[
        "Leads"
    ].sum()

    marketing_enrolments = marketing[
        "Enrolments"
    ].sum()

    total_spend = marketing[
        "SpendRM"
    ].sum()

    conversion_rate = (
        marketing_enrolments
        / total_leads
        * 100
        if total_leads > 0
        else 0
    )

    average_cpa = (
        total_spend
        / marketing_enrolments
        if marketing_enrolments > 0
        else 0
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Marketing Leads",
        f"{total_leads:,}"
    )

    c2.metric(
        "Campaign Enrolments",
        f"{marketing_enrolments:,}"
    )

    c3.metric(
        "Conversion Rate",
        f"{conversion_rate:.1f}%"
    )

    c4.metric(
        "Average CPA",
        f"RM {average_cpa:,.0f}"
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    # CAMPAIGN ENROLMENTS
    with col1:

        campaign_data = (
            marketing
            .sort_values(
                "Enrolments",
                ascending=True
            )
        )

        fig_campaign = px.bar(
            campaign_data,
            x="Enrolments",
            y="CampaignName",
            orientation="h",
            color="Channel",
            title="Enrolments by Campaign",
            hover_name="CampaignName",
            hover_data={
                "Channel": True,
                "SpendRM": ":,.0f",
                "ConversionRatePct": ":.1f",
                "CostPerAcquisitionRM": ":,.0f",
                "CampaignName": False
            }
        )

        fig_campaign = modern_chart(fig_campaign)



        st.plotly_chart(
            fig_campaign,
            use_container_width=True
        )

    # SPEND VS ENROLMENT
    with col2:

        fig_spend = px.scatter(
            marketing,
            x="SpendRM",
            y="Enrolments",
            size="Leads",
            color="Channel",
            title="Campaign Spend vs Enrolments",
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

        fig_spend.update_traces(
            marker=dict(
                line=dict(width=1.5, color="rgba(255,255,255,0.85)")
            )
        )

        fig_spend = modern_chart(fig_spend)



        st.plotly_chart(
            fig_spend,
            use_container_width=True
        )

    # ACQUISITION SOURCE
    acquisition = (
        students
        .groupby("AcquisitionSource")
        .size()
        .reset_index(
            name="Students"
        )
        .sort_values(
            "Students",
            ascending=False
        )
    )

    fig_acquisition = px.bar(
        acquisition,
        x="AcquisitionSource",
        y="Students",
        title="Student Acquisition Sources"
    )

    fig_acquisition = modern_chart(fig_acquisition, height=360)



    st.plotly_chart(
        fig_acquisition,
        use_container_width=True
    )

# =========================================================
# DOWNLOAD SECTION
# =========================================================

st.markdown("---")

st.markdown(
    "### Download Filtered Dataset"
)

export_data = filtered_enrolments.copy()

csv_data = export_data.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered Enrolment Data",
    data=csv_data,
    file_name="StudySmart_Filtered_Enrolments.csv",
    mime="text/csv"
)

# =========================================================
# FOOTER
# =========================================================

st.caption(
    "Study Smart Tuition Centre Business Intelligence Dashboard "
    "• Synthetic data for academic demonstration"
)
