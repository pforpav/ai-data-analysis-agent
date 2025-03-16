import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(
    page_title="My Basic Streamlit App",
    page_icon="🚀",
    layout="wide"
)

# Header
st.title("My Basic Streamlit App")
st.markdown("### Welcome to my first Streamlit application!")
st.write("This app demonstrates the basic features of Streamlit.")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Explorer", "Chart Generator", "About"])

# Home page
if page == "Home":
    st.header("Home")
    st.write("This is a simple Streamlit application that showcases some basic features.")
    
    # Some basic widgets
    st.subheader("Interactive Widgets")
    
    name = st.text_input("What's your name?", "")
    if name:
        st.write(f"Hello, {name}! 👋")
    
    age = st.slider("Your age", 0, 100, 25)
    st.write(f"You selected age: {age}")
    
    if st.button("Click me!"):
        st.balloons()
        st.write("🎉 Thanks for clicking!")

# Data Explorer page
elif page == "Data Explorer":
    st.header("Data Explorer")
    st.write("Upload a CSV file or use sample data to explore.")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    # Sample data checkbox
    use_sample = st.checkbox("Use sample data instead")
    
    # Process data
    if uploaded_file is not None:
        # Load user data
        try:
            df = pd.read_csv(uploaded_file)
            st.success("File uploaded successfully!")
        except Exception as e:
            st.error(f"Error: {e}")
            df = None
    elif use_sample:
        # Create sample data
        st.info("Using sample data")
        df = pd.DataFrame({
            'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 34, 29, 42],
            'City': ['New York', 'Paris', 'Berlin', 'London'],
            'Salary': [90000, 85000, 72000, 93000]
        })
    else:
        df = None
        st.info("Please upload a file or use sample data.")
    
    # Display data if available
    if df is not None:
        st.subheader("Data Preview")
        st.dataframe(df)
        
        st.subheader("Column Information")
        st.write(f"Number of rows: {df.shape[0]}")
        st.write(f"Number of columns: {df.shape[1]}")
        
        st.subheader("Summary Statistics")
        st.write(df.describe())

# Chart Generator page
elif page == "Chart Generator":
    st.header("Chart Generator")
    st.write("Generate simple charts with random data.")
    
    # Chart settings
    chart_type = st.selectbox("Select chart type", ["Line", "Bar", "Scatter", "Histogram"])
    
    # Generate random data
    data_size = st.slider("Data points", 5, 100, 20)
    random_seed = st.number_input("Random seed", 0, 1000, 42)
    
    np.random.seed(random_seed)
    
    x = np.arange(data_size)
    y = np.random.randn(data_size).cumsum()
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if chart_type == "Line":
        ax.plot(x, y, marker='o')
        st.write("### Line Chart")
        
    elif chart_type == "Bar":
        ax.bar(x, y)
        st.write("### Bar Chart")
        
    elif chart_type == "Scatter":
        ax.scatter(x, y, alpha=0.7)
        st.write("### Scatter Plot")
        
    elif chart_type == "Histogram":
        ax.hist(y, bins=10, alpha=0.7)
        st.write("### Histogram")
    
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.grid(True, alpha=0.3)
    
    # Show the chart
    st.pyplot(fig)
    
    # Download option
    st.download_button(
        label="Download data as CSV",
        data=pd.DataFrame({'x': x, 'y': y}).to_csv(index=False),
        file_name='chart_data.csv',
        mime='text/csv',
    )

# About page
elif page == "About":
    st.header("About")
    st.write("This is a basic Streamlit app created as a demonstration.")
    st.write("Streamlit makes it easy to create interactive web applications with Python.")
    
    st.subheader("Features used in this app:")
    features = [
        "Text and markdown",
        "Buttons and interactive widgets",
        "Sidebar navigation",
        "File uploading",
        "DataFrame display",
        "Charts and visualizations",
        "Download functionality"
    ]
    
    for feature in features:
        st.write(f"- {feature}")
    
    st.info("Created as a learning resource.")

# Footer
st.markdown("---")
st.markdown("© 2025 My Basic Streamlit App")
