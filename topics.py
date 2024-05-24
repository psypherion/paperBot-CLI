import os
import openai
from dotenv import load_dotenv

class TopicResearcher:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.client = openai.OpenAI(api_key=api_key)
    
    def get_topics(self, interested_topic, skill_level):
        prompt = f"Give important topics for {interested_topic} with {skill_level} level for which research papers are available on arXiv."
        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{prompt}",
                }
            ],
            model="gpt-3.5-turbo",
        )

        topics = []
        if response and response.choices:
            for choice in response.choices:
                topics.append(choice.message.content.strip())
        return topics

    def get_research_papers(self, topic):
        prompt = f"Give most important research paper article name and the name of the authors for {topic} only if available on arXiv."
        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{prompt}",
                }
            ],
            model="gpt-3.5-turbo",
        )
        research_papers = []
        if response and response.choices:
            for choice in response.choices:
                research_papers.append(choice.message.content.strip())
        return research_papers

# Example usage
if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    researcher = TopicResearcher(api_key)
    topics = researcher.get_topics("Machine Learning", "Beginner")
    for topic in topics:
        papers = researcher.get_research_papers(topic)
        print(f"Topic: {topic}")
        for paper in papers:
            print(f" - {paper}")
