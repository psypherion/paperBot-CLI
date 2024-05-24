import os
import random
from dotenv import load_dotenv
from topics import TopicResearcher
from arxivScraper import ArxivScraper
from summarizer import PaperSummarizer

def cleaner(texts):
    cleaned_texts = []
    for text in texts:
        lines = text.split("\n")
        cleaned_lines = []
        for line in lines:
            period_index = line.find(". ")
            if period_index != -1:
                cleaned_line = line[period_index + 2:].strip()
                cleaned_lines.append(cleaned_line)
            else:
                cleaned_lines.append(line.strip())
        cleaned_texts.append("\n".join(cleaned_lines))
    return cleaned_texts

def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set it in the .env file")

    # Get user input
    interested_topic = input("Enter your interested topic (e.g., Machine Learning): ")
    skill_level = input("Enter your skill level (Beginner/Intermediate/Advanced): ")

    # Initialize TopicResearcher
    researcher = TopicResearcher(api_key)

    # Get topics
    topics = researcher.get_topics(interested_topic, skill_level)
    if not topics:
        print("No topics found.")
        return

    research_papers = []
    for topic in topics:
        print(f"Fetching papers for topic: {topic}")
        papers = researcher.get_research_papers(topic)
        cleaned_papers = cleaner(papers)
        research_papers.extend(cleaned_papers)
    
    if not research_papers:
        print("No research papers found.")
        return

    # Randomly select a paper
    selected_paper = random.choice(research_papers)
    print(f"Selected paper: {selected_paper}")

    # Summarize the paper
    summarizer = PaperSummarizer(api_key)
    summary = summarizer.get_summary(selected_paper)
    print(f"Summary:\n{summary}")

    # Ask user if they want to download the paper
    download = input("Do you want to download the full research paper? (yes/no): ").strip().lower()
    if download == 'yes':
        scraper = ArxivScraper(selected_paper)
        html_content = scraper.search_articles()
        if html_content:
            scraper.download_pdf(html_content)
        else:
            print("Research paper not available on arXiv.")
    else:
        print("Download skipped.")

if __name__ == "__main__":
    main()
