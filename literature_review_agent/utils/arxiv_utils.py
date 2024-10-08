# utils/arxiv_utils.py

import arxiv
from tqdm import tqdm

def fetch_arxiv_papers(query, max_results=5):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    papers = []
    for result in tqdm(search.results(), total=max_results, desc='Fetching arXiv papers'):
        papers.append({
            'title': result.title,
            'authors': [author.name for author in result.authors],
            'abstract': result.summary.replace('\n', ' '),
            'url': result.entry_id
        })
    return papers
