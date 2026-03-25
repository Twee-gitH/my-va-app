import streamlit as st
import os

# 1. Page Setup
st.set_page_config(
    page_title="Twee Shin G. Tan | Professional VA", 
    page_icon="💼", 
    layout="wide"
)

# 2. Header Section (Photo & Title)
col1, col2 = st.columns([1, 2])

with col1:
    if os.path.exists("profile.jpg"):
        st.image("profile.jpg", width=250)
    else:
        st.info("Upload 'profile.jpg' to GitHub to show your photo here.")

with col2:
    st.title("Twee Shin G. Tan")
    st.subheader("Program Developer & Specialized Virtual Assistant")
    st.write("📍 Tagum, Davao Region, Philippines")
    st.write("---")
    
    # Description updated to include Real Estate
    st.write("""
    A tech-savvy and highly reliable professional bridging the gap between **Program Development** and high-level **Virtual Assistance**. Known for strong operational common sense and a 
    proactive approach to problem-solving, ensuring tasks are handled with minimal supervision. 
    Specializes in delivering structured administrative support tailored for the 
    **Medical, Legal, and Real Estate** sectors, combining technical precision 
    with a commitment to data integrity and professional documentation.
    """)

# 3. Expertise / Skills Section (Now 4 Columns for better layout)
st.header("Professional Expertise")
c1, c2 = st.columns(2)
c3, c4 = st.columns(2)

with c1:
    st.markdown("### 🏥 Medical VA")
    st.write("""
    - Medical Terminology Accuracy
    - Patient Data Management
    - HIPAA Compliance Awareness
    - Strategic Appointment Scheduling
    """)

with c2:
    st.markdown("### ⚖️ Legal VA")
    st.write("""
    - Precision Legal Transcription
    - Case Document Formatting
    - Systematic Record Keeping
    - Preliminary Legal Research
    """)

with c3:
    st.markdown("### 🏠 Real Estate VA")
    st.write("""
    - Property Listing Management
    - CRM Data Entry & Lead Tracking
    - Transaction Coordination Support
    - Comparative Market Analysis (CMA) Assistance
    """)

with c4:
    st.markdown("### 💡 Core Strengths")
    st.write("""
    - **Proactive Problem Solving:** Intuitive approach to daily obstacles.
    - **Reliability:** Consistent delivery on high-stakes tasks.
    - **Technical Logic:** Python scripting and workflow automation.
    - **Data Integrity:** Extreme attention to detail across all sectors.
    """)

# 4. Contact & Links Section
st.divider()
st.header("Get In Touch")
st.write("📧 **Email:** tweeshingarciatan@gmail.com")
st.write("🔗 **GitHub Portfolio:** [github.com/Twee-gitH](https://github.com/Twee-gitH)")

# Footer
st.write("##")
st.caption("© 2026 Twee Shin G. Tan | Professional Virtual Assistant Portfolio")
