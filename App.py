import streamlit as st
from main import main
import pandas as pd

# Set wide mode layout
st.set_page_config(page_title="ForHumans Data Drill", layout="wide")

# Initialize session state variables
if 'order' not in st.session_state:
    st.session_state['order'] = None
if 'return' not in st.session_state:
    st.session_state['return'] = None
if 'processed_data' not in st.session_state:
    st.session_state['processed_data'] = None


# Function to convert uploaded file to DataFrame
def convert_to_dataframe(uploaded_file):
    if uploaded_file.name.endswith('.csv'):
        return pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        return pd.read_excel(uploaded_file)
    else:
        st.error("Unsupported file format!")
        return None


# Heading
st.title("ForHumans Data Drill")

# Use columns to create a side-by-side layout
left_column, right_column = st.columns(2)

# Left column for controls and messages
with left_column:
    st.subheader("File Upload")

    # File uploader for the Orders file
    uploaded_file1 = st.file_uploader("Step 1: Upload Orders file (.csv or .xlsx)",
                                      type=['csv', 'xlsx'], key='uploader1')
    if uploaded_file1 is not None:
        df_orders = convert_to_dataframe(uploaded_file1)
        if df_orders is not None:
            st.session_state['order'] = df_orders
            st.success("Orders file uploaded and converted successfully!")

    # File uploader for the Return file
    uploaded_file2 = st.file_uploader("Step 2: Upload Return file (.csv or .xlsx)",
                                      type=['csv', 'xlsx'], key='uploader2')
    if uploaded_file2 is not None:
        df_returns = convert_to_dataframe(uploaded_file2)
        if df_returns is not None:
            st.session_state['return'] = df_returns
            st.success("Return file uploaded and converted successfully!")

    # Drill Data button
    if st.button("Drill Data"):
        if st.session_state['order'] is not None and st.session_state['return'] is not None:
            kpis = main(st.session_state['order'], st.session_state['return'])
            if not kpis.empty:
                st.session_state['processed_data'] = kpis
                st.success("Data processed successfully!")
            else:
                st.error("Processing is not successful!")
        else:
            st.error("Please upload both files before drilling data.")

# Right column for displaying the processed file and download link
with right_column:
    st.subheader("Processed KPI's:")
    if st.session_state['processed_data'] is not None:
        st.dataframe(st.session_state['processed_data'])  # Display the processed data

        # Generate a CSV download link
        csv = st.session_state['processed_data'].to_csv(index=False).encode('utf-8')
        st.download_button(label="Download Processed KPI's",
                           data=csv,
                           file_name="processed_data.csv",
                           mime="text/csv")
