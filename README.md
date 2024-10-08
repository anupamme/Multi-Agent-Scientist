# Multi-Agent-Scientist

Multi-Agent Scientist
The Multi-Agent Scientist is an AI pipeline designed to automate the process of generating scientific research ideas and drafting patent applications. It consists of four interconnected agents that work sequentially to produce novel scientific ideas and corresponding patents based on the latest research literature.

# Table of Contents
1. Overview
2. Features
3. Project Structure
4. Installation
5. Prerequisites
6. Steps
7. Usage
8. Customization

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

# Installation
## Prerequisites
Python 3.7 or higher
OpenAI account with access to o1-preview or o1-mini models
NCBI Entrez email registration for PubMed API access
API keys for patent databases (if applicable)


# Agents and Their Functionality
## 1. Literature Review Agent
Purpose: Collects and summarizes scientific papers relevant to the chosen topic.

Data Sources: arXiv, PubMed
Functionality:
Searches for papers using the specified query.
Summarizes abstracts using OpenAI's language models.
Compiles summaries into a cohesive literature review.
Output: outputs/literature_review.md

## 2. Scientific Research Agent
Purpose: Generates new scientific ideas based on the literature review.

Input: The literature review from the first agent.
Functionality:
Analyzes the literature review to identify gaps and opportunities.
Generates novel ideas using AI models.
Output: data/ideas.json

## 3. Patent Search Agent
Purpose: Determines the originality of generated ideas by searching existing patents.

Input: List of generated ideas.
Functionality:
Searches patent databases (e.g., USPTO, EPO) for each idea.
Marks ideas as original ('y') or not ('n').
Output: Updated data/ideas.json with originality status.

## 4. Patent Writing Agent
Purpose: Drafts patent applications for original ideas.

Acknowledgments
OpenAI: For providing powerful language models.
arXiv: For access to pre-print scientific papers.
PubMed: For access to biomedical literature.
Patent Offices: For providing patent search APIs.
Contact
For questions or support, please contact [angelovskiandrej5@gmail.com].

Note: This project is intended for educational and research purposes for now. 