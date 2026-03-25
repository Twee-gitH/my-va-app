import streamlit as st
import json
import os

# Web Interface Setup
st.set_page_config(page_title="VA Profile Database", page_icon="💼")
st.title("📋 VA Professional Database")

FILENAME = "profiles_db.json"

# Load Data
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        try:
            data = json.load(f)
        except:
            data = []
else:
    data = []

# Sidebar: Add New Profile
with st.sidebar:
    st.header("Add New Entry")
    name = st.text_input("Full Name")
    role = st.selectbox("Role", ["Medical VA", "Legal VA", "General VA"])
    skills = st.text_area("Skills")
    
    if st.button("Save to Database"):
        if name:
            new_entry = {"Name": name, "Role": role, "Skills": skills}
            data.append(new_entry)
            with open(FILENAME, "w") as f:
                json.dump(data, f)
            st.success(f"Saved {name}!")
        else:
            st.error("Please enter a name.")

# Main Screen: Display Data
st.write("### Current Registered Profiles")
if data:
    st.table(data)
else:
    st.info("No profiles found. Use the sidebar to add one!")
    
