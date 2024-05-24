# PaperBot-CLI

Welcome to PaperBot-CLI! This project provides tools to help you find, summarize, and download research papers from arXiv.org based on your topics of interest.

## Repository Overview
This repository contains the following Python scripts:

1. arxivScraper.py: A tool to search for and download research papers from arXiv.org.
2. summarizer.py: A tool to summarize research papers using OpenAI's GPT-3.5-turbo model.
3. topics.py: A tool to fetch important research topics and papers based on user interest and skill level using OpenAI's GPT-3.5-turbo model.
4. main.py: The main script that integrates the functionalities of the above tools.

## Setting Up

### 1. Clone the Repository
```bash
git clone https://github.com/ky13troj/paperbot-CLI.git
cd paperbot-CLI
```

### 2. Create Your own .env file
Create a .env file in the root directory of the repository and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_openai_api_key
```

## Usage
```bash
python main.py
```
This script will:

- Ask for your topic of interest (e.g., Machine Learning) and your skill level (Beginner/Intermediate/Advanced).
- Fetch relevant research topics and papers from arXiv.org.
- Process and clean the fetched papers.
- Summarize a randomly selected paper.
- Ask if you want to download the summarized research paper in PDF format.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Contact
For any questions or suggestions, feel free to reach out to me via my social media accounts.

___

Thank you for using PaperBot-CLI! Happy researching!
