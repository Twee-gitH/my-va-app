import streamlit as st
import os

# 1. Page Setup
st.set_page_config(
    page_title="Twee Shin Tan | Professional VA", 
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
    st.title("Twee Shin Tan")
    st.subheader("Program Developer & Specialized Virtual Assistant")
    st.write("📍 Tagum, Davao Region, Philippines")
    st.write("---")
    
    # Updated description with "Reliability" and "Common Sense" traits
    st.write("""
    A tech-savvy and highly reliable professional bridging the gap between **Program Development** and high-level **Virtual Assistance**. Known for strong operational common sense and a 
    proactive approach to problem-solving, ensuring tasks are handled with minimal supervision. 
    Specializes in delivering structured administrative support tailored for the 
    **Medical and Legal** sectors, combining technical precision with a commitment 
    to data integrity and professional documentation.
    """)

# 3. Expertise / Skills Section
st.header("Professional Expertise")
c1, c2, c3 = st.columns(3)

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
    st.markdown("### 💡 Core Strengths") # Changed from Technical to show your traits
    st.write("""
    - **Proactive Problem Solving:** Intuitive "common sense" approach to daily obstacles.
    - **Reliability:** Consistent delivery on deadlines and high-stakes tasks.
    - **Technical Logic:** Python scripting and workflow automation.
    - **Data Integrity:** Extreme attention to detail in legal/medical files.
    """)

# 4. Contact & Links Section
st.divider()
st.header("Get In Touch")
st.write("📧 **Email:** tweeshingarciatan@gmail.com")
st.write("🔗 **GitHub Portfolio:** [github.com/Twee-gitH](https://github.com/Twee-gitH)")

# Footer
st.write("##")
st.caption("© 2026 Twee Shin Tan | Professional Virtual Assistant Portfolio")
