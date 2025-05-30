from config.openai_client import chat_with_openai

def summarize_content(content):
    messages = [
        {"role": "system", "content": "You are an expert AI summarizer."},
        {"role": "user", "content": f"Summarize the following content:\n{content}"}
    ]
    summary = chat_with_openai(messages)
    return summary
