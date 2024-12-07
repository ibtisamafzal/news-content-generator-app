import streamlit as st
from api.news_fetcher import fetch_news
from api.text_summarizer import summarize_text
from api.image_generator import generate_image

st.title("AI News Content Generator")

# Input form
def user_input():
    with st.form("input_form"):
        prompt = st.text_input("Enter your news topic:")
        tone = st.selectbox("Select the tone:", ["neutral", "humorous", "professional"], index=0)
        platform = st.selectbox("Select the platform:", ["Instagram", "Facebook", "LinkedIn"], index=0)
        submitted = st.form_submit_button("Generate Content")
        return prompt, tone, platform, submitted

query, tone, platform, submitted = user_input()
if submitted and query:
    st.write("Fetching news...")
    news_data = fetch_news(query)

    if "error" in news_data:
        st.error(f"Error fetching news: {news_data['error']}")
    else:
        article = news_data.get("value", [])[0]  # Get the first article
        st.header(article["name"])
        st.write(article["description"])

        st.write("Summarizing article...")
        summary = summarize_text(article["description"], tone=tone)
        st.success(summary)

        st.write("Generating image...")
        try:
            image = generate_image(summary)
            st.image(image, caption="Generated Image")
        except Exception as e:
            st.error(f"Error generating image: {e}")