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
    # Check if you uploaded a photo named 'profile.jpg' to GitHub
    if os.path.exists("profile.jpg"):
        st.image("profile.jpg", width=250)
    else:
        st.info("Upload 'profile.jpg' to GitHub to show your photo here.")

with col2:
    st.title("Twee Shin Tan")
    st.subheader("Program Developer & Specialized Virtual Assistant")
    st.write("📍 Tagum, Davao Region, Philippines")
    st.write("---")
    st.write("""
    I am a tech-savvy professional combining **Program Development** expertise with 
    high-level **Virtual Assistance**. I specialize in providing structured administrative 
    support for the **Medical and Legal** sectors, ensuring data accuracy and 
    professional documentation.
    """)

# 3. Expertise / Skills Section
st.header("Professional Expertise")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 🏥 Medical VA")
    st.write("""
    - Medical Terminology
    - Patient Data Management
    - HIPAA Compliance Awareness
    - Appointment Scheduling
    """)

with c2:
    st.markdown("### ⚖️ Legal VA")
    st.write("""
    - Legal Transcription
    - Case Document Formatting
    - Filing & Record Keeping
    - Research Assistance
    """)

with c3:
    st.markdown("### 💻 Technical")
    st.write("""
    - Python Programming
    - MS Office (Word, Excel)
    - GitHub & Cloud Deploy
    - Data Extraction/OCR
    """)

# 4. Contact Section
st.divider()
st.header("Get In Touch")
st.write("📧 **Email:** tweeshingarciatan@gmail.com")
st.write("🔗 **GitHub:** [github.com/Twee-gitH](https://github.com/Twee-gitH)")

# 5. Signature Section (Bottom Right)
st.write("##")
sig_col1, sig_col2 = st.columns([3, 1])

with sig_col2:
    st.write("Respectfully,")
    # Check if you uploaded 'signature.png' to GitHub
    if os.path.exists("signature.png"):
        st.image("signature.png", width=180)
    else:
        st.write("*(Signature)*")
    st.markdown("### **Twee Shin Tan**")
    st.write("Professional VA / Developer")
    
