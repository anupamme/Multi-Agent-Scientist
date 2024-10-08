# utils/pubmed_utils.py

from Bio import Entrez
from config import ENTREZ_EMAIL
from tqdm import tqdm

Entrez.email = ENTREZ_EMAIL

def fetch_pubmed_papers(query, max_results=5):
    handle = Entrez.esearch(db='pubmed', term=query, retmax=max_results)
    record = Entrez.read(handle)
    id_list = record['IdList']
    return parse_pubmed_records(id_list)

def parse_pubmed_records(id_list):
    papers = []
    ids = ','.join(id_list)
    handle = Entrez.efetch(db='pubmed', id=ids, rettype='abstract', retmode='xml')
    records = Entrez.read(handle)

    for article in tqdm(records['PubmedArticle'], desc='Fetching PubMed papers'):
        # Extract title
        title = article['MedlineCitation']['Article']['ArticleTitle']
        # Extract authors
        authors = []
        try:
            for author in article['MedlineCitation']['Article']['AuthorList']:
                name = f"{author.get('ForeName', '')} {author.get('LastName', '')}".strip()
                if name:
                    authors.append(name)
        except:
            pass
        # Extract abstract
        abstract = ''
        try:
            abstract_texts = article['MedlineCitation']['Article']['Abstract']['AbstractText']
            if isinstance(abstract_texts, list):
                abstract = ' '.join(abstract_texts)
            else:
                abstract = abstract_texts
        except:
            pass
        # Extract DOI and URL
        doi = ''
        try:
            elocation_ids = article['MedlineCitation']['Article'].get('ELocationID', [])
            for elocation in elocation_ids:
                if elocation.attributes.get('EIdType') == 'doi':
                    doi = str(elocation)
                    break
        except:
            pass
        url = f"https://doi.org/{doi}" if doi else ''
        papers.append({
            'title': title,
            'authors': authors,
            'abstract': abstract.replace('\n', ' '),
            'url': url
        })
    return papers
