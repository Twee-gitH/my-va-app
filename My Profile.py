import streamlit as st
import os

# 1. Page Setup
st.set_page_config(
    page_title="Twee Shin G. Tan | Professional VA", 
    page_icon="💼", 
    layout="wide"
)

# 2. Header Section
col1, col2 = st.columns([1, 2])

with col1:
    if os.path.exists("profile.jpg"):
        st.image("profile.jpg", width=250)
    else:
        st.info("Upload 'profile.jpg' to GitHub.")

with col2:
    st.title("Twee Shin G. Tan")
    st.subheader("Program Developer & Specialized Virtual Assistant")
    st.write("📍 Tagum, Davao Region, Philippines")
    st.write("---")
    st.write("""
    A tech-savvy and highly reliable professional bridging the gap between **Program Development** and high-level **Virtual Assistance**. Known for strong operational common sense and a 
    proactive approach to problem-solving, ensuring tasks are handled with minimal supervision. 
    Specializes in delivering structured administrative support tailored for the 
    **Medical, Legal, and Real Estate** sectors.
    """)

# 3. Work History Section
st.header("Professional Experience")

# Job 1
with st.container():
    c_left, c_right = st.columns([3, 1])
    with c_left:
        st.markdown("#### **Program Developer / VA Project Lead**")
        st.write("Freelance / Independent Projects")
    with c_right:
        st.write("*2024 - Present*")
    st.write("""
    - Developed custom web-based data management tools using Python and Streamlit.
    - Specialized in automated data extraction (OCR) for legal and medical documentation.
    - Managed end-to-end digital workflows, ensuring 100% data integrity and security.
    """)

# Job 2
with st.container():
    c_left, c_right = st.columns([3, 1])
    with c_left:
        st.markdown("#### **Administrative & Technical Specialist**")
        st.write("General Virtual Assistance")
    with c_right:
        st.write("*Previous Experience*")
    st.write("""
    - Provided high-level administrative support, including scheduling and document formatting.
    - Utilized advanced MS Office features to organize complex databases and reports.
    - Applied proactive "common sense" logic to resolve technical and logistical bottlenecks.
    """)

# 4. Expertise Section
st.divider()
st.header("Specialized Expertise")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 🏥 Medical & Legal")
    st.write("- Medical Terminology\n- HIPAA Awareness\n- Legal Transcription\n- Case Filing")

with c2:
    st.markdown("### 🏠 Real Estate")
    st.write("- Listing Management\n- CRM Lead Tracking\n- Transaction Support\n- CMA Assistance")

with c3:
    st.markdown("### 💻 Technical")
    st.write("- Python Development\n- MS Office Suite\n- GitHub/Cloud Deploy\n- Data Automation")

# 5. Contact Section
st.divider()
st.header("Get In Touch")
st.write("📧 **Email:** tweeshingarciatan@gmail.com")
st.write("🔗 **GitHub Portfolio:** [github.com/Twee-gitH](https://github.com/Twee-gitH)")

# Footer
st.write("##")
st.caption("© 2026 Twee Shin G. Tan | Professional Virtual Assistant Portfolio")
