# # streamlit_app.py
# import streamlit as st
# from utils.parser import extract_text_from_pdf, parse_resume_with_llama3
# from utils.match_logic import calculate_match_score

# st.set_page_config(page_title="AI Resume & Job Matcher", layout="wide")
# st.title("🧠 AI Resume & Job Matcher")
# st.markdown("Upload your resume and a job description to see how well you match!")

# uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type=["pdf"])
# job_description = st.text_area("💼 Paste Job Description", height=250)

# if st.button("🚀 Match Me"):
#     if uploaded_file and job_description:
#         pdf_text = extract_text_from_pdf(uploaded_file)
#         resume_data = parse_resume_with_llama3(pdf_text)

#         if resume_data is None:
#             st.error("❌ Failed to parse resume.")
#         elif "error" in resume_data:
#             st.error("❌ Error in resume data: " + resume_data["error"])
#         else:
#             st.success("✅ Resume parsed successfully!")
#             st.json(resume_data)

#             result = calculate_match_score(resume_data, job_description)
#             st.subheader("🎯 Match Score")
#             st.metric(label="Score", value=f"{result['match_score']}%")
#             st.markdown(
#                 f"<div style='white-space: pre-wrap; background-color: #f9f9f9; padding: 1rem; border-radius: 10px;'>{result['explanation']}</div>",
#                 unsafe_allow_html=True
#             )
#     else:
#         st.warning("⚠️ Please upload a resume and paste a job description.")





##############if need to change



# import streamlit as st
# from utils.parser import extract_text_from_pdf, parse_resume_with_llama3
# from utils.match_logic import calculate_match_score

# # Page Config
# st.set_page_config(page_title="AI Resume & Job Matcher", layout="wide")

# # Header
# st.markdown(
#     """
#     <h1 style='text-align: center;'>🧠 AI Resume & Job Matcher</h1>
#     <p style='text-align: center;'>Upload your resume and a job description to see how well you match!</p>
#     """,
#     unsafe_allow_html=True,
# )

# st.markdown("---")

# # Layout Columns
# col1, col2 = st.columns(2)

# with col1:
#     uploaded_file = st.file_uploader("📄 Upload your Resume (PDF)", type=["pdf"])

# with col2:
#     job_description = st.text_area("💼 Paste Job Description", height=250, placeholder="Paste job description here...")

# # Match Button
# st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
# if st.button("🚀 Match Me", use_container_width=True):
#     if uploaded_file and job_description:
#         with st.spinner("🔍 Analyzing resume and job description..."):
#             pdf_text = extract_text_from_pdf(uploaded_file)
#             resume_data = parse_resume_with_llama3(pdf_text)

#         if resume_data is None:
#             st.error("❌ Failed to parse resume.")
#         elif "error" in resume_data:
#             st.error("❌ Error in resume data: " + resume_data["error"])
#             if "raw_output" in resume_data:
#                 st.text_area("📄 Raw LLM Output", resume_data["raw_output"], height=200)
#         else:
#             st.success("✅ Resume parsed successfully!")
#             with st.expander("📋 Parsed Resume Data"):
#                 st.json(resume_data)

#             result = calculate_match_score(resume_data, job_description)

#             # Show match score
#             st.markdown("---")
#             st.subheader("🎯 Match Result")
#             st.metric(label="Match Score", value=f"{result['match_score']}%")

#             st.markdown(
#                 f"<div style='white-space: pre-wrap; background-color: #f1f3f5; padding: 1rem; border-radius: 10px; border-left: 5px solid #4CAF50;'>{result['explanation']}</div>",
#                 unsafe_allow_html=True,
#             )
#     else:
#         st.warning("⚠️ Please upload a resume and paste a job description.")
# st.markdown("</div>", unsafe_allow_html=True)



######################################last


# import streamlit as st
# from utils.parser import extract_text_from_pdf, parse_resume_with_llama3
# from utils.match_logic import calculate_match_score

# # Page Config
# st.set_page_config(page_title="AI Resume & Job Matcher", layout="wide")

# # Main Title
# st.markdown("""
#     <h1 style='text-align: center;'>🧠 AI Resume & Job Matcher</h1>
#     <p style='text-align: center; font-size: 18px;'>Upload your resume and a job description to see how well you match!</p>
#     <hr>
# """, unsafe_allow_html=True)

# # Layout: Resume Upload and Job Description Side by Side
# col1, col2 = st.columns(2)

# with col1:
#     st.markdown("### 📄 Upload Your Resume")
#     uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# with col2:
#     st.markdown("### 💼 Paste Job Description")
#     job_description = st.text_area("Paste the job description here", height=250, placeholder="e.g., We're seeking an ML Manager with LLM experience...")

# # Match Button
# st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
# match_btn = st.button("🚀 Match Me", use_container_width=True)
# st.markdown("</div>", unsafe_allow_html=True)

# # Processing Logic
# if match_btn:
#     if uploaded_file and job_description:
#         with st.spinner("🔍 Processing..."):
#             pdf_text = extract_text_from_pdf(uploaded_file)
#             resume_data = parse_resume_with_llama3(pdf_text)

#         if resume_data is None:
#             st.error("❌ Failed to parse resume. Please try another file.")
#         elif "error" in resume_data:
#             st.error("❌ Error in resume data: " + resume_data["error"])
#             if "raw_output" in resume_data:
#                 st.text_area("📄 Raw LLM Output", resume_data["raw_output"], height=200)
#         else:
#             st.success("✅ Resume parsed successfully!")

#             with st.expander("📋 View Parsed Resume JSON"):
#                 st.json(resume_data)

#             # Score matching
#             result = calculate_match_score(resume_data, job_description)

#             st.markdown("---")
#             st.markdown("### 🎯 Match Score", unsafe_allow_html=True)
#             st.metric(label="Score", value=f"{result['match_score']}%", delta=None)

#             st.markdown("""
#                 <div style='background-color: #f0f2f6; padding: 1rem; border-radius: 10px; border-left: 5px solid #4CAF50; font-size: 16px;'>
#             """, unsafe_allow_html=True)
#             st.markdown(result['explanation'])
#             st.markdown("</div>", unsafe_allow_html=True)

#     else:
#         st.warning("⚠️ Please upload a resume and paste a job description.")

#############################last1


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

