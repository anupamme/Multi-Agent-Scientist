# main.py

import os
from utils.arxiv_utils import fetch_arxiv_papers
from utils.pubmed_utils import fetch_pubmed_papers
from utils.summarization_utils import summarize_papers
from config import NUM_PAPERS, SEARCH_QUERY, OUTPUT_FILE
from tqdm import tqdm
import json

def main():
    # Ensure necessary directories exist
    os.makedirs('data', exist_ok=True)
    os.makedirs('outputs', exist_ok=True)

    print("Fetching papers from arXiv...")
    arxiv_papers = fetch_arxiv_papers(SEARCH_QUERY, max_results=NUM_PAPERS//2)

    print("Fetching papers from PubMed...")
    pubmed_papers = fetch_pubmed_papers(SEARCH_QUERY, max_results=NUM_PAPERS//2)

    # Combine papers
    papers = arxiv_papers + pubmed_papers
    papers = papers[:NUM_PAPERS]  # Ensure we have exactly NUM_PAPERS

    # Save raw paper data
    with open('data/papers.json', 'w', encoding='utf-8') as f:
        json.dump(papers, f, ensure_ascii=False, indent=4)

    print("Summarizing papers...")
    papers = summarize_papers(papers)

    # Generate literature review document
    document = create_literature_review(papers, SEARCH_QUERY)

    # Save document
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(document)

    print(f"Literature review saved to '{OUTPUT_FILE}'.")

def create_literature_review(papers, topic):
    document = ''
    # Introduction
    document += f"# Literature Review on {topic}\n\n"
    document += "This document summarizes recent advancements based on 10 selected scientific papers.\n\n"
    # Paper Summaries
    for idx, paper in enumerate(papers, 1):
        document += f"## Paper {idx}: {paper['title']}\n"
        document += f"**Authors**: {', '.join(paper['authors'])}\n"
        if paper['url']:
            document += f"**URL**: {paper['url']}\n"
        document += f"\n### Summary\n{paper['summary']}\n\n"
    # Conclusion
    document += "## Conclusion\n"
    document += "This literature review highlights the significant progress in the field and identifies areas for future research.\n"
    return document

if __name__ == '__main__':
    main()
