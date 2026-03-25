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
    # Using "Specialist" instead of "Aspiring"
    st.subheader("Program Developer & Multi-Sector Virtual Assistant") 
    st.write("📍 Tagum, Davao Region, Philippines")
    st.write("---")
    st.write("""
    A tech-savvy and highly reliable professional bridging the gap between **Program Development** and 
    specialized **Virtual Assistance**. Known for strong operational common sense and a 
    proactive, self-directed approach to problem-solving. Delivers structured 
    administrative support with a focus on data integrity for the **Medical, Legal, and Real Estate** sectors.
    """)

# 3. Foundational Experience Section
st.header("Foundational Experience")

# Job 1
with st.container():
    c_left, c_right = st.columns([3, 1])
    with c_left:
        st.markdown("#### **Administrative & Technical Support Specialist**")
        st.write("Freelance Projects / Office Support")
    with c_right:
        st.write("*2018 - 2020*")
    st.write("""
    - Managed digital file organization and high-accuracy data entry for various projects.
    - Handled professional document formatting and preparation under specific guidelines.
    - Provided consistent support in maintaining schedules and digital correspondence.
    - Applied practical logic to resolve daily administrative tasks with minimal supervision.
    """)

# Job 2
with st.container():
    c_left, c_right = st.columns([3, 1])
    with c_left:
        st.markdown("#### **Information & Data Clerk**")
        st.write("Entry-Level Professional Support")
    with c_right:
        st.write("*2016 - 2018*")
    st.write("""
    - Performed clerical duties including digital record keeping and systematic filing.
    - Leveraged MS Office tools for reporting, list management, and document organization.
    - Maintained a high level of reliability and attention to detail in all assigned tasks.
    """)

# 4. Specialized Skills Section
st.divider()
st.header("Specialized Skills")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 🏥 Medical & Legal")
    st.write("- Medical Terminology Basics\n- Data Privacy Awareness\n- Document Transcription\n- File Organization")

with c2:
    st.markdown("### 🏠 Real Estate")
    st.write("- Property Listing Support\n- CRM Data Entry\n- Appointment Setting\n- Client List Management")

with c3:
    st.markdown("### 💻 Tech & Traits")
    st.write("- Python Development\n- MS Office Suite\n- Operational Common Sense\n- Quick Adoption of New Systems")

# 5. Contact Section
st.divider()
st.header("Get In Touch")
st.write("📧 **Email:** tweeshingarciatan@gmail.com")
st.write("🔗 **GitHub Portfolio:** [github.com/Twee-gitH](https://github.com/Twee-gitH)")

# Footer
st.write("##")
st.caption("© 2026 Twee Shin G. Tan | Professional Virtual Assistant Portfolio")
