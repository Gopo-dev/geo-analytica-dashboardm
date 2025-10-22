
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Geo-Analytica", layout="wide")
st.title("🌍 Geo-Analytica | Unified Data Intelligence Dashboard")

# Sidebar
st.sidebar.title("Navigation")
tab = st.sidebar.radio("Select Dashboard", ["Political", "Corporate", "Social Media"])

# Load sample data
mentions = pd.read_csv("data/mentions.csv")
sentiment = pd.read_csv("data/sentiment_data.csv")

# Tabs Logic
if tab == "Political":
    st.header("🗳️ Political Intelligence")
    col1, col2, col3 = st.columns(3)
    col1.metric("Mentions", "8,523")
    col2.metric("Positive Sentiment", "63%")
    col3.metric("Top Candidate", "Candidate A")
    st.bar_chart(mentions.set_index("Candidate"))
    fig = px.line(sentiment, x="Date", y=["Positive", "Neutral", "Negative"], title="Sentiment Over Time")
    st.plotly_chart(fig, use_container_width=True)

elif tab == "Corporate":
    st.header("📊 Corporate Marketing Analytics")
    st.subheader("Campaign Ad Spend vs Conversions")
    st.write("Coming soon...")

elif tab == "Social Media":
    st.header("📱 Social Media Monitoring")
    st.subheader("Trending Hashtags & Influencer Impact")
    st.write("Coming soon...")
