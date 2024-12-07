from transformers import pipeline

def summarize_text(text, tone="neutral"):
    summarizer = pipeline("summarization", model="t5-small")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)

    # Adjust tone if necessary
    if tone == "humorous":
        return f"Here’s a fun take: {summary[0]['summary_text']}"
    elif tone == "professional":
        return f"Professionally speaking: {summary[0]['summary_text']}"
    else:
        return summary[0]['summary_text']