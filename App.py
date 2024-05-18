import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
from main import main, cohorts, sku_update
from DataProcessing.processing import processing_files

# Set wide mode layout
st.set_page_config(page_title="ForHumans Data Drill", layout="wide")


# Function to convert a matplotlib figure to a PIL Image
def fig_to_image(fig):
    """Convert a matplotlib figure to a PIL Image."""
    buf = BytesIO()
    fig.savefig(buf, format='png')  # Adjust format if needed
    buf.seek(0)
    return Image.open(buf)


# Function to convert image to bytes for download
def get_image_bytes(img, format='PNG'):
    buffered = BytesIO()
    img.save(buffered, format=format)
    return buffered.getvalue()


# Function to convert uploaded file to DataFrame
def convert_to_dataframe(uploaded_file):
    try:
        if uploaded_file.name.endswith('.csv'):
            try:
                # Try reading the file with the default delimiter
                df = pd.read_csv(uploaded_file)
                if df.shape[1] == 1:  # Check if all data is in a single column
                    raise ValueError("Single column detected, trying semicolon delimiter.")
                return df
            except Exception as e:
                # st.warning(f"Error reading CSV file with default delimiter: {e}. Trying semicolon delimiter.")
                try:
                    # Reset the buffer's position to the beginning
                    uploaded_file.seek(0)
                    df = pd.read_csv(uploaded_file, delimiter=';')
                    if df.shape[1] == 1:  # Check if all data is in a single column
                        raise ValueError("Single column detected with semicolon delimiter.")
                    return df
                except Exception as e:
                    st.error(f"Error reading CSV file with semicolon delimiter: {e}.")
        elif uploaded_file.name.endswith('.xlsx'):
            return pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
    return None


def clean_dataframe(df):
    # Remove columns that are completely empty
    df_cleaned = df.dropna(axis=1, how='all')
    return df_cleaned


# File upload section
with st.sidebar:
    st.subheader("File Upload")
    uploaded_file1 = st.file_uploader("Step 1: Upload Orders file (.csv or .xlsx)", type=['csv', 'xlsx'], key='uploader1')
    uploaded_file2 = st.file_uploader("Step 2: Upload Return file (.csv or .xlsx)", type=['csv', 'xlsx'], key='uploader2')
    uploaded_file3 = st.file_uploader("Step 3: Upload SKU file (.csv or .xlsx)", type=['csv', 'xlsx'], key='uploader3')

    if st.button("Drill Data"):
        if uploaded_file1 and uploaded_file2 and uploaded_file3:
            orders = convert_to_dataframe(uploaded_file1)
            # print(orders)
            returns = convert_to_dataframe(uploaded_file2)
            # print(returns)
            sku = convert_to_dataframe(uploaded_file3)
            # print(sku)

            if orders is not None and returns is not None and sku is not None:
                orders = clean_dataframe(orders)
                returns = clean_dataframe(returns)
                sku = clean_dataframe(sku)
                print(sku)

                clean_orders, clean_returns, base_return = processing_files(orders, returns)
                df1, df2 = main(clean_orders, clean_returns, base_return)
                df3 = sku_update(clean_orders, clean_returns, sku)
                figures = cohorts(clean_orders)

                # Convert the figures to PIL Images
                st.session_state['df1'], st.session_state['df2'], st.session_state['df3'] = df1, df2, df3
                st.session_state['img1'], st.session_state['img2'], st.session_state['img3'] = fig_to_image(figures['Overall']), fig_to_image(figures['B2B']), fig_to_image(figures['B2C'])
            else:
                st.error("One or more files could not be processed. Please check the file formats and contents.")
        else:
            st.error("Please upload all required files before drilling data.")

# Display DataFrames and images
col1, col2, col3 = st.columns(3)

with col1:
    if 'df1' in st.session_state and st.session_state['df1'] is not None:
        st.dataframe(st.session_state['df1'])
        st.download_button("Download DataFrame 1", st.session_state['df1'].to_csv(index=False), "df1.csv", "text/csv")
    if 'img1' in st.session_state and st.session_state['img1'] is not None:
        st.image(st.session_state['img1'], caption='Overall Cohort')
        img_bytes = get_image_bytes(st.session_state['img1'])
        st.download_button("Download Image 1", img_bytes, "cohort_overall.png", "image/png")

with col2:
    if 'df2' in st.session_state and st.session_state['df2'] is not None:
        st.dataframe(st.session_state['df2'])
        st.download_button("Download DataFrame 2", st.session_state['df2'].to_csv(index=False), "df2.csv", "text/csv")
    if 'img2' in st.session_state and st.session_state['img2'] is not None:
        st.image(st.session_state['img2'], caption='B2B Cohort')
        img_bytes = get_image_bytes(st.session_state['img2'])
        st.download_button("Download Image 2", img_bytes, "cohort_b2b.png", "image/png")

with col3:
    if 'df3' in st.session_state and st.session_state['df3'] is not None:
        st.dataframe(st.session_state['df3'])
        st.download_button("Download DataFrame 3", st.session_state['df3'].to_csv(index=False), "df3.csv", "text/csv")
    if 'img3' in st.session_state and st.session_state['img3'] is not None:
        st.image(st.session_state['img3'], caption='B2C Cohort')
        img_bytes = get_image_bytes(st.session_state['img3'])
        st.download_button("Download Image 3", img_bytes, "cohort_b2c.png", "image/png")
