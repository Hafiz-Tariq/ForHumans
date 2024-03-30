import streamlit as st
import pandas as pd
import os
from tempfile import NamedTemporaryFile

# Set wide mode layout
st.set_page_config(page_title="ForHumans Data Drill", layout="wide")

# Function to check if the uploaded file is valid
def is_valid_file(uploaded_file):
    if uploaded_file is not None and (uploaded_file.name.endswith('.csv') or uploaded_file.name.endswith('.xlsx')):
        return True
    return False

# Function to save the processed file, placeholder for the user to complete
def process_files(file1, file2):
    # Placeholder for processing logic
    # Replace with actual processing code
    processed_data = pd.DataFrame()  # Dummy dataframe, replace with actual processed data
    return processed_data

# Heading
st.title("ForHumans Data Drill")

# Use columns to create a side-by-side layout
left_column, right_column = st.columns(2)

# Left column for controls and messages
with left_column:
    # st.subheader("Controls")
    # Sidebar for file upload
    st.subheader("File Upload")

    # File uploader for the first file
    file1 = st.file_uploader("Step 1: Upload first file (.csv or .xlsx)", type=['csv', 'xlsx'])
    if is_valid_file(file1):
        st.success("First file uploaded successfully!")

    # File uploader for the second file
    file2 = st.file_uploader("Step 2: Upload second file (.csv or .xlsx)", type=['csv', 'xlsx'])
    if is_valid_file(file2):
        st.success("Second file uploaded successfully!")

    # Drill Data button
    if st.button("Drill Data") and file1 and file2:
        # Placeholder for the logic to process files
        # Here you would call your processing function
        processed_data = process_files(file1, file2)
        st.success("Data processed successfully!")  # Confirmation message

        # Save processed data to a temporary file
        tmp_file = NamedTemporaryFile(delete=False)
        processed_data.to_csv(tmp_file.name, index=False)
        tmp_file.close()

        # Download link for processed data
        st.download_button(label="Download Processed Data",
                           data=tmp_file.name,
                           file_name="processed_data.csv",
                           mime="text/csv",
                           on_click=lambda: os.unlink(tmp_file.name))

# Right column for displaying the processed file
with right_column:
    st.subheader("Processed Data")
    if 'processed_data' in locals():
        st.dataframe(processed_data)  # Display the processed data
