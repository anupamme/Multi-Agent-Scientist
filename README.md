# Multi-Agent-Scientist

Multi-Agent Scientist
The Multi-Agent Scientist is an AI pipeline designed to automate the process of generating scientific research ideas and drafting patent applications. It consists of four interconnected agents that work sequentially to produce novel scientific ideas and corresponding patents based on the latest research literature.

Table of Contents
Overview
Features
Project Structure
Installation
Prerequisites
Steps
Usage
Customization
Agents and Their Functionality
1. Literature Review Agent
2. Scientific Research Agent
3. Patent Search Agent
4. Patent Writing Agent
Dependencies
License
Acknowledgments
Contact
Overview
The Multi-Agent Scientist leverages OpenAI's o1-preview and o1-mini models to process and generate text, and utilizes APIs from arXiv, PubMed, and patent databases. The pipeline includes:

Literature Review Agent: Gathers and summarizes relevant scientific papers.
Scientific Research Agent: Generates new scientific ideas based on the literature review.
Patent Search Agent: Checks the originality of each idea by searching existing patents.
Patent Writing Agent: Drafts patent applications for original ideas.
Features
Automated Literature Review: Fetches and summarizes recent scientific papers on a chosen topic.
Idea Generation: Produces novel scientific research ideas using AI language models.
Patent Originality Check: Searches patent databases to verify the uniqueness of generated ideas.
Automated Patent Drafting: Creates patent application documents for original ideas.
Project Structure
markdown
Copy code
multi_agent_scientist/
├── README.md
├── requirements.txt
├── config.py
├── main.py
├── agents/
│   ├── __init__.py
│   ├── literature_review_agent.py
│   ├── scientific_research_agent.py
│   ├── patent_search_agent.py
│   ├── patent_writing_agent.py
├── utils/
│   ├── __init__.py
│   ├── arxiv_utils.py
│   ├── pubmed_utils.py
│   ├── patent_utils.py
│   ├── summarization_utils.py
│   ├── idea_generation_utils.py
│   ├── patent_writing_utils.py
├── data/
│   ├── papers.json
│   ├── ideas.json
│   ├── patents.json
├── outputs/
│   ├── literature_review.md
│   └── patent_applications/
│       ├── patent_idea_1.md
│       ├── patent_idea_2.md
│       └── ...
Installation
Prerequisites
Python 3.7 or higher
OpenAI account with access to o1-preview or o1-mini models
NCBI Entrez email registration for PubMed API access
API keys for patent databases (if applicable)
Steps
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/multi_agent_scientist.git
cd multi_agent_scientist
Install Required Packages

bash
Copy code
pip install -r requirements.txt
Set Up Configuration

Open config.py and set your API keys and email:

python
Copy code
# config.py

# OpenAI API Key
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'

# Entrez Email (required by NCBI)
ENTREZ_EMAIL = 'your.email@example.com'

# Patent API Credentials
PATENT_API_KEY = 'YOUR_PATENT_API_KEY'  # Replace if applicable

# Model Names
SUMMARIZATION_MODEL = 'o1-mini'      # For summarization
IDEA_GENERATION_MODEL = 'o1-mini'    # For idea generation
PATENT_WRITING_MODEL = 'o1-mini'     # For patent drafting

# Number of Papers and Ideas
NUM_PAPERS = 10
NUM_IDEAS = 10

# Search Query
SEARCH_QUERY = 'Your research topic here'
Usage
Run the main script to execute the entire pipeline:

bash
Copy code
python main.py
The script will sequentially execute the following agents:

Literature Review Agent: Fetches and summarizes scientific papers.
Scientific Research Agent: Generates new scientific ideas.
Patent Search Agent: Checks the originality of each idea.
Patent Writing Agent: Drafts patent applications for original ideas.
Customization
Change the Topic or Search Query

Edit config.py:

python
Copy code
SEARCH_QUERY = 'Your new research topic here'
Adjust Number of Papers and Ideas

python
Copy code
NUM_PAPERS = 10  # Number of papers to fetch
NUM_IDEAS = 10   # Number of ideas to generate
Select Models

python
Copy code
SUMMARIZATION_MODEL = 'o1-mini'      # For summarization
IDEA_GENERATION_MODEL = 'o1-mini'    # For idea generation
PATENT_WRITING_MODEL = 'o1-mini'     # For patent drafting
Agents and Their Functionality
1. Literature Review Agent
Purpose: Collects and summarizes scientific papers relevant to the chosen topic.

Data Sources: arXiv, PubMed
Functionality:
Searches for papers using the specified query.
Summarizes abstracts using OpenAI's language models.
Compiles summaries into a cohesive literature review.
Output: outputs/literature_review.md
2. Scientific Research Agent
Purpose: Generates new scientific ideas based on the literature review.

Input: The literature review from the first agent.
Functionality:
Analyzes the literature review to identify gaps and opportunities.
Generates novel ideas using AI models.
Output: data/ideas.json
3. Patent Search Agent
Purpose: Determines the originality of generated ideas by searching existing patents.

Input: List of generated ideas.
Functionality:
Searches patent databases (e.g., USPTO, EPO) for each idea.
Marks ideas as original ('y') or not ('n').
Output: Updated data/ideas.json with originality status.
4. Patent Writing Agent
Purpose: Drafts patent applications for original ideas.

Input: Original ideas confirmed by the patent search agent.
Functionality:
Drafts patent documents, including abstract, background, summary, and claims.
Uses AI models to generate professional patent text.
Output: Patent documents in outputs/patent_applications/
Dependencies
arxiv: For accessing arXiv papers.
biopython: For interacting with the PubMed API.
openai: For AI language model access.
requests: For HTTP requests.
tqdm: For progress bars.
json: For data handling (built-in).
Install all dependencies using:

bash
Copy code
pip install -r requirements.txt
License
This project is licensed under the MIT License.

Acknowledgments
OpenAI: For providing powerful language models.
arXiv: For access to pre-print scientific papers.
PubMed: For access to biomedical literature.
Patent Offices: For providing patent search APIs.
Contact
For questions or support, please contact [angelovskiandrej5@gmail.com].

Note: This project is intended for educational and research purposes for now. 