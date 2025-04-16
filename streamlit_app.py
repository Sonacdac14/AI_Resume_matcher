import streamlit as st
from utils.parser import extract_text_from_pdf, parse_resume_with_llama3
from utils.match_logic import calculate_match_score

st.set_page_config(page_title="AI Resume Matcher", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #e0f7fa, #ffffff);
        color: #00363a;
    }

    .main-container {
        background-color: #ffffff;
        padding: 2rem 3rem;
        border-radius: 15px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
        margin-top: 2rem;
    }

    .stButton > button {
        background-color: #00796b;
        color: white;
        padding: 0.75rem 1.5rem;
        font-size: 16px;
        border-radius: 10px;
        border: none;
        transition: background-color 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #004d40;
    }

    .title-text {
        font-size: 42px;
        font-weight: 800;
        color: #004d40;
        text-align: center;
        margin-bottom: 1rem;
    }

    .sub-text {
        font-size: 18px;
        text-align: center;
        margin-bottom: 2rem;
    }

    .score-box {
        background-color: #e0f2f1;
        color: #004d40;
        padding: 1rem;
        font-size: 32px;
        font-weight: bold;
        border-radius: 12px;
        text-align: center;
        margin-top: 1rem;
    }

    .explanation-box {
        background-color: #fafafa;
        border-left: 4px solid #00796b;
        padding: 1rem;
        border-radius: 10px;
        font-size: 16px;
        margin-top: 1rem;
        white-space: pre-wrap;
    }
    </style>
""", unsafe_allow_html=True)

# Main container
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.markdown("<div class='title-text'>🧠 AI Resume & Job Matcher</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-text'>Upload your resume and a job description to see how well you match!</div>", unsafe_allow_html=True)

# Upload and Input
uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type=["pdf"])
job_description = st.text_area("💼 Paste Job Description", height=250)

# Processing
if st.button("🚀 Match Me"):
    if uploaded_file and job_description:
        pdf_text = extract_text_from_pdf(uploaded_file)
        resume_data = parse_resume_with_llama3(pdf_text)

        if resume_data is None:
            st.error("❌ Failed to parse resume.")
        elif "error" in resume_data:
            st.error("❌ Error in resume data: " + resume_data["error"])
        else:
            st.success("✅ Resume parsed successfully!")
            st.subheader("📋 Extracted Resume Info")
            st.json(resume_data)

            result = calculate_match_score(resume_data, job_description)

            st.markdown("### 🎯 Match Score")
            st.markdown(f"<div class='score-box'>{result['match_score']}%</div>", unsafe_allow_html=True)

            st.markdown("### 🔍 Explanation")
            st.markdown(f"<div class='explanation-box'>{result['explanation']}</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please upload a resume and paste a job description.")

st.markdown("</div>", unsafe_allow_html=True)

