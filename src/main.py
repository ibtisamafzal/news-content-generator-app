import streamlit as st
from api.news_fetcher import fetch_news
from api.text_summarizer import summarize_text
from api.image_generator import generate_image

st.title("AI News Content Generator")

query = st.text_input("Enter your news topic:")
if query:
    st.write("Fetching news...")
    news_data = fetch_news(query)

    if "error" in news_data:
        st.error(f"Error fetching news: {news_data['error']}")
    else:
        for article in news_data.get("value", []):
            st.header(article["name"])
            st.write(article["description"])

            st.write("Summarizing article...")
            summary = summarize_text(article["description"])
            st.success(summary)

            st.write("Generating image...")
            image_url = generate_image(article["description"])
            if image_url:
                st.image(image_url)