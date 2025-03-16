import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

# Set page configuration
st.set_page_config(
    page_title="About DataWhisperer",
    page_icon="🧐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header
st.title(":rainbow[**DataWhisperer**]: Your AI Data Analysis Assistant")
st.subheader("Transforming Data into Insights, One Conversation at a Time")
st.write("DataWhisperer is an intuitive, conversation-driven data analysis tool that allows you to explore, visualize, and understand your data through natural language. Simply upload your dataset and start asking questions - no complex query language or coding required.")
add_vertical_space(2)

st.markdown("### What Can :rainbow[DataWhisperer] Do?")
st.markdown("- Explore Your Data - Get instant summaries, statistics, and insights about your dataset")
st.markdown("- Create Visualizations - Generate charts and graphs through simple conversations")
st.markdown("- Perform Analysis - Calculate correlations, aggregations, and filter your data effortlessly")
st.markdown("- Answer Questions - Ask about trends, patterns, and relationships within your data")
add_vertical_space(2)

st.markdown("### Getting Started")
st.markdown("1. Upload your CSV file or use our sample dataset")
st.markdown("2. Start chatting with DataWhisperer using natural language")
st.markdown("3. Explore your insights through interactive visualizations and summaries")
add_vertical_space(1)
st.write("Our AI-powered assistant understands data analysis terminology and can help you uncover the stories hidden in your numbers. Whether you're a data professional looking to speed up your workflow or a business user seeking to make data-driven decisions, DataWhisperer makes the process seamless and intuitive. Ready to transform how you interact with your data? Let's begin!")






