import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import re
from io import StringIO

# Set page configuration
st.set_page_config(
    page_title="Data Analysis Assistant",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful colors and styling
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    .stApp {
        background: linear-gradient(135deg, #f0f2f6 0%, #d4d8e0 100%);
    }
    .css-1d391kg {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #7d56f3;
    }
    .stButton>button {
        border-radius: 10px;
        background-color: #7d56f3;
        color: white;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #6639e6;
        box-shadow: 0 4px 8px rgba(125, 86, 243, 0.3);
    }
    .user-message {
        background-color: #e3edff;
        color: #1a3c6e;
        border-radius: 15px;
        padding: 12px 18px;
        margin: 8px 0;
        align-self: flex-end;
        max-width: 80%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        border-left: 4px solid #7d56f3;
    }
    .assistant-message {
        background-color: #1a3c6e;
        color: #ffffff;
        border-radius: 15px;
        padding: 12px 18px;
        margin: 8px 0;
        align-self: flex-start;
        max-width: 80%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.15);
        border-right: 4px solid #7d56f3;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        padding: 10px;
    }
    h1 {
        color: #1a3c6e;
        font-weight: 800;
    }
    h2, h3 {
        color: #2e4e7e;
        font-weight: 600;
    }
    .sidebar .stButton>button {
        width: 100%;
        background-color: #1a3c6e;
    }
    .sidebar .stButton>button:hover {
        background-color: #0f325e;
    }
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
    }
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb {
        background: #7d56f3;
        border-radius: 10px;
    }
    /* Code block styling */
    code {
        background-color: #2e4e7e !important;
        color: #fff !important;
        padding: 4px 8px !important;
        border-radius: 5px !important;
    }
    /* Success/error message styling */
    .stSuccess {
        background-color: #d7f7e6 !important;
        color: #0c6e47 !important;
        border: 1px solid #0c6e47 !important;
    }
    .stError {
        background-color: #ffe6e6 !important;
        color: #c62828 !important;
        border: 1px solid #c62828 !important;
    }
    /* File uploader styling */
    .stFileUploader label {
        background-color: #1a3c6e !important;
        color: white !important;
    }
    /* Highlight key metrics */
    .metric-card {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        margin-bottom: 12px;
        border-left: 4px solid #7d56f3;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #1a3c6e;
    }
    .metric-label {
        font-size: 14px;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your Data Analysis Assistant. Upload a CSV file or use sample data, and I'll help you analyze it. What would you like to know?"}
    ]

if 'df' not in st.session_state:
    st.session_state.df = None

if 'df_name' not in st.session_state:
    st.session_state.df_name = None

# Helper functions for data analysis
def analyze_command(command, df):
    """Process natural language commands for data analysis"""
    command = command.lower()
    response = ""
    fig = None
    
    # Show basic info
    if any(x in command for x in ["describe", "summary", "statistics", "info"]):
        response = f"Here's a summary of your data:\n\n{df.describe().to_string()}\n\n"
        response += f"Dataset has {df.shape[0]} rows and {df.shape[1]} columns."
        
    # Show columns
    elif any(x in command for x in ["columns", "features", "variables"]):
        response = f"Your dataset contains the following columns:\n\n{', '.join(df.columns)}"
    
    # Show missing values
    elif any(x in command for x in ["missing", "null", "na", "empty"]):
        response = "Missing values in each column:\n\n"
        missing = df.isnull().sum()
        response += missing.to_string()
        
    # Create scatter plot
    elif "scatter" in command:
        cols = extract_columns(command, df.columns)
        if len(cols) >= 2:
            fig = px.scatter(df, x=cols[0], y=cols[1], title=f"{cols[0]} vs {cols[1]}")
            response = f"Created scatter plot of {cols[0]} vs {cols[1]}"
        else:
            response = "Please specify which columns to use for the scatter plot."
    
    # Create histogram
    elif "histogram" in command or "distribution" in command:
        cols = extract_columns(command, df.columns)
        if cols:
            fig = px.histogram(df, x=cols[0], nbins=20, title=f"Distribution of {cols[0]}")
            response = f"Created histogram for {cols[0]}"
        else:
            response = "Please specify which column to use for the histogram."
    
    # Create bar chart
    elif "bar" in command:
        cols = extract_columns(command, df.columns)
        if len(cols) >= 2:
            fig = px.bar(df, x=cols[0], y=cols[1], title=f"{cols[1]} by {cols[0]}")
            response = f"Created bar chart of {cols[1]} by {cols[0]}"
        else:
            response = "Please specify which columns to use for the bar chart."
    
    # Correlation analysis
    elif "correlation" in command or "corr" in command:
        numeric_df = df.select_dtypes(include=[np.number])
        if not numeric_df.empty:
            corr = numeric_df.corr()
            fig = px.imshow(corr, 
                          color_continuous_scale='RdBu_r',
                          title='Correlation Matrix')
            response = "Generated correlation matrix for numeric columns."
        else:
            response = "No numeric columns available for correlation analysis."
    
    # Calculate aggregate statistics
    elif any(x in command for x in ["mean", "average", "sum", "max", "min", "count"]):
        agg_funcs = {
            "mean": "mean", "average": "mean", "sum": "sum", 
            "max": "max", "min": "min", "count": "count"
        }
        
        for func_name, func in agg_funcs.items():
            if func_name in command:
                cols = extract_columns(command, df.columns)
                if cols:
                    result = getattr(df[cols], func)()
                    response = f"{func_name.capitalize()} of {', '.join(cols)}:\n\n{result.to_string()}"
                else:
                    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
                    result = getattr(df[numeric_cols], func)()
                    response = f"{func_name.capitalize()} of numeric columns:\n\n{result.to_string()}"
                break
    
    # Filter data
    elif any(x in command for x in ["filter", "where", "query"]):
        # This is a simplified filter implementation - would need more complex NLP for production
        response = "Filtering functionality is available. Please specify column and condition."
        
    # Show sample data
    elif any(x in command for x in ["sample", "show", "display", "head", "preview"]):
        count = 5  # Default
        match = re.search(r'(\d+)', command)
        if match:
            count = min(int(match.group(1)), 20)  # Limit to 20 rows
        response = f"Here's a sample of {count} rows from your data:\n\n"
        return response, df.head(count)
        
    else:
        response = "I'm not sure how to process that command. Try asking for statistics, columns, correlations, or to create plots."
    
    return response, fig

def extract_columns(command, available_columns):
    """Extract column names from the command"""
    columns = []
    for col in available_columns:
        if col.lower() in command.lower():
            columns.append(col)
    return columns

# Sidebar
with st.sidebar:
    st.title("🤖 Data Analysis Assistant")
    st.markdown("---")
    
    # File upload
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state.df = df
            st.session_state.df_name = uploaded_file.name
            st.success(f"Successfully loaded {uploaded_file.name}")
        except Exception as e:
            st.error(f"Error loading file: {e}")
    
    # Sample data option
    if st.button("Use Sample Data"):
        # Create sample data
        np.random.seed(42)
        data = {
            'Age': np.random.normal(35, 10, 100).astype(int),
            'Income': np.random.normal(50000, 15000, 100).astype(int),
            'Spending': np.random.normal(30000, 10000, 100).astype(int),
            'Satisfaction': np.random.choice(['Low', 'Medium', 'High'], 100),
            'Region': np.random.choice(['North', 'South', 'East', 'West'], 100)
        }
        df = pd.DataFrame(data)
        st.session_state.df = df
        st.session_state.df_name = "sample_data.csv"
        st.success("Sample data loaded!")
    
    # Display dataset info if loaded
    if st.session_state.df is not None:
        st.markdown("---")
        st.subheader("Dataset Information")
        st.write(f"**Name:** {st.session_state.df_name}")
        st.write(f"**Size:** {st.session_state.df.shape[0]} rows, {st.session_state.df.shape[1]} columns")
        st.write("**Column Types:**")
        for col, dtype in st.session_state.df.dtypes.items():
            st.write(f"- {col}: {dtype}")
    
    st.markdown("---")
    st.markdown("### Example Questions")
    st.markdown("- Show me a summary of the data")
    st.markdown("- Create a histogram of Age")
    st.markdown("- What's the correlation between columns?")
    st.markdown("- Show me a sample of 10 rows")

# Main chat interface
st.title("💬 Data Analysis Chat")

# Display chat messages
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="assistant-message">{message["content"]}</div>', unsafe_allow_html=True)
        # If the message contains a figure, try to display it
        if "figure" in message:
            fig = message["figure"]
            st.plotly_chart(fig, use_container_width=True)
        # If the message contains a dataframe, display it
        if "dataframe" in message:
            st.dataframe(message["dataframe"])
st.markdown('</div>', unsafe_allow_html=True)

# Input for user message
user_input = st.text_input("Type your analysis request here:", key="user_input")

# Process user input
if user_input:
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Check if data is loaded
    if st.session_state.df is None:
        response = "Please upload a CSV file or use sample data first."
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        # Process the command
        response, result = analyze_command(user_input, st.session_state.df)
        
        # Add assistant response to chat
        message = {"role": "assistant", "content": response}
        
        # If result is a figure, add it to the message
        if isinstance(result, (plt.Figure)):
            message["figure"] = result
        # If result is a dataframe, add it to the message
        elif isinstance(result, pd.DataFrame):
            message["dataframe"] = result
            
        st.session_state.messages.append(message)
    
    # Rerun to update the chat interface
    st.rerun()
