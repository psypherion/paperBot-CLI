import requests
from bs4 import BeautifulSoup

class ArxivScraper:
    def __init__(self, query):
        self.query = query.replace('"', "")
        self.base_url = "https://arxiv.org/search/?"
        self.headers = {'User-Agent': 'Mozilla/5.0'}
    
    def search_articles(self):
        query_encoded = self.query.replace(" ", "+")
        params = {
            "query": query_encoded,
            "searchtype": "all",
            "abstracts": "show",
            "order": "-announced_date_first",
            "size": "50"
        }
        encoded_params = "&".join([f"{k}={v}" for k, v in params.items()])
        full_url = self.base_url + encoded_params
        # print(f"Full URL: {full_url}")

        response = requests.get(full_url, headers=self.headers)

        if response.status_code == 200:
            html_content = response.content
            return html_content
        else:
            print("Failed to find the research article. Status code:", response.status_code)
            return None
    
    def download_pdf(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        pdf_link = soup.find("a", href=lambda href: href and "pdf" in href)

        if pdf_link:
            pdf_url = pdf_link["href"]
            response = requests.get(pdf_url, headers=self.headers)
            if response.status_code == 200:
                with open(f"{self.query}.pdf", "wb") as pdf_file:
                    pdf_file.write(response.content)
                print("PDF downloaded successfully.")
            else:
                print("Failed to download PDF. Status code:", response.status_code)
        else:
            # print("PDF link not found in the HTML content.")
            pass

# Example usage
if __name__ == "__main__":
    query = "An overview of gradient descent optimization algorithms by Sebastian Ruder"
    scraper = ArxivScraper(query)
    html_content = scraper.search_articles()
    if html_content:
        scraper.download_pdf(html_content)
