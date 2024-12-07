from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization", model="t5-small")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']