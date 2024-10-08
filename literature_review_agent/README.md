# Literature Review Agent

This project implements a Literature Review Agent that fetches scientific papers on a specified topic, summarizes them using OpenAI's `o1-preview` or `o1-mini` models, and generates a cohesive literature review document.

## **Features**

- Fetches papers from **arXiv** and **PubMed** based on a search query.
- Summarizes abstracts using OpenAI's `o1` models.
- Compiles summaries into a structured Markdown document.
- Configurable number of papers and search query.

## **Code Structure**
    README.md: Instructions and information about the project.
    requirements.txt: List of required Python packages.
    config.py: Configuration file containing API keys and settings.
    main.py: The main script to run the Literature Review Agent.
    utils/: Directory containing utility modules for different functionalities.
    arxiv_utils.py: Functions for interacting with the arXiv API.
    pubmed_utils.py: Functions for interacting with the PubMed API.
    summarization_utils.py: Functions for summarizing text using OpenAI's o1 models.
    data/: Directory for storing fetched paper data.
    papers.json: JSON file containing details of the fetched papers.
    outputs/: Directory for storing the output literature review document.
    literature_review.md: The final literature review markdown file.

## **Prerequisites**

- Python 3.7 or higher
- OpenAI account with access to `o1-preview` or `o1-mini` models.
- NCBI Entrez email registration.
