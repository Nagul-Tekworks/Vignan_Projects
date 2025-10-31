import streamlit as st
import pandas as pd

st.title("Census Data Analysis")

# Upload file
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# If file is uploaded
if uploaded_file is not None:
    census_data = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    st.subheader("🔍 Data Preview")
    st.dataframe(census_data.head())

    # Show button to generate report
    if st.button("1. Show Education Distribution"):
        if 'Education' in census_data.columns:
            education_distribution = census_data['Education'].value_counts()

            st.subheader("🎓 Education Distribution")
            st.write(education_distribution)

            # Optional: show chart
            st.bar_chart(education_distribution)
        else:
            st.error("❌ 'Education' column not found in this dataset.")
     # Button to show college dropouts
    if st.button("Show College Dropouts"):
        if 'Education' in census_data.columns:
        # Count people who attended college but didn't graduate
            college_dropouts = census_data[census_data['Education'] == "Somecollegebutnodegree"]
            st.write("### College Dropouts (Attended but didn't graduate)")
            st.write(f"Total count: {college_dropouts.shape[0]}")
            st.dataframe(college_dropouts)  # Optional: show data
        else:
            st.error("No 'Education' column found in dataset!")
else:
    st.info("👆 Please upload a CSV file to continue.")
