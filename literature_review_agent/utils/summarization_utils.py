# utils/summarization_utils.py

import openai
from config import OPENAI_API_KEY, SUMMARIZATION_MODEL
from tqdm import tqdm

openai.api_key = OPENAI_API_KEY

def summarize_papers(papers):
    for paper in tqdm(papers, desc='Summarizing papers'):
        abstract = paper.get('abstract', '')
        if abstract:
            summary = summarize_text(abstract)
            paper['summary'] = summary
        else:
            paper['summary'] = 'No abstract available.'
    return papers

def summarize_text(text):
    prompt = f"Summarize the following scientific abstract in approximately 200 words:\n\n{text}"
    try:
        response = openai.ChatCompletion.create(
            model=SUMMARIZATION_MODEL,
            messages=[
                {'role': 'system', 'content': 'You are an expert scientific writer.'},
                {'role': 'user', 'content': prompt}
            ],
            max_tokens=500,
            temperature=0.5,
        )
        summary = response['choices'][0]['message']['content']
        return summary.strip()
    except Exception as e:
        print(f"An error occurred during summarization: {e}")
        return "Summary not available due to an error."
