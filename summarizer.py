import os
import openai
from dotenv import load_dotenv

class PaperSummarizer:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def get_summary(self, text):
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarizes research papers.",
                },
                {
                    "role": "user",
                    "content": f"Summarize the following research paper: {text}",
                }
            ]
        )
        summary = response.choices[0]['message']['content'].strip()
        return summary

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set it in the .env file")

    text = input("Enter the text you want to summarize: ")
    summarizer = PaperSummarizer(api_key)
    summary = summarizer.get_summary(text)
    print(summary)