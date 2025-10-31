import streamlit as st
import pandas as pd

st.title("Census Data Analysis")

# Upload file
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    census_data = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    
    st.subheader("🔍 Data Preview")
    st.dataframe(census_data.head())

    # Dropdown to select report
    report_options = ["Select Report", "Education Distribution", "College Dropouts"]
    selected_report = st.selectbox("Choose a report to generate:", report_options)

    if selected_report == "Education Distribution":
        if 'Education' in census_data.columns:
            education_distribution = census_data['Education'].value_counts()
            st.subheader("🎓 Education Distribution")
            st.write(education_distribution)
            st.bar_chart(education_distribution)
        else:
            st.error("❌ 'Education' column not found in this dataset.")

    elif selected_report == "College Dropouts":
        if 'Education' in census_data.columns:
            college_dropouts = census_data[census_data['Education'] == "Somecollegebutnodegree"]
            st.subheader("🎓 College Dropouts (Attended but didn't graduate)")
            st.write(f"Total count: {college_dropouts.shape[0]}")
            st.dataframe(college_dropouts)
        else:
            st.error("❌ 'Education' column not found in this dataset.")
else:
    st.info("👆 Please upload a CSV file to continue.")
