import openai
import os
from dotenv import load_dotenv
from arxivScraper import ArxivScraper

class PaperBotCLI:
    def __init__(self):
        self.load_api_key()
        self.display_banner()

    def load_api_key(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            self.setup_api_key()

    def setup_api_key(self):
        api_key = input("Enter your OpenAI API key: ")
        with open(".env", "w") as f:
            f.write(f"OPENAI_API_KEY={api_key}")
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")

    def display_banner(self):
        with open("banner.txt", "r") as banner:
            print(banner.read())

    def get_proper_paper_name(self, paper):
        client = openai.OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that returns the correct name of the research paper with the author names.",
                },
                {
                    "role": "user",
                    "content": f"What is the proper name of the following research paper: {paper}?",
                }
            ]
        )
        return response["choices"][0]["message"]["content"].strip()

    def download_research_paper(self):
        user_response = input("Do you have a particular research paper you want to download? (y/N): ")
        if user_response.lower() == "y":
            paper = input("Enter the name of the paper: ")
            research_article = self.get_proper_paper_name(paper)
            print(f"Trying to download using arxivScraper: {research_article}")
            
            scraper = ArxivScraper(research_article)
            html_content = scraper.search_articles()
            if html_content:
                scraper.download_pdf(html_content)
            else:
                print("No research paper found on arxiv.")
        else:
            print("No paper entered. Exiting.")

    def run(self):
        self.download_research_paper()

if __name__ == "__main__":
    bot = PaperBotCLI()
    bot.run()
