# Agentic RAG Homework – LLM Zoomcamp

This repository contains my solution for the Agentic RAG homework from the DataTalksClub LLM Zoomcamp.

## Objective

The goal of this homework is to:

* Build a RAG (Retrieval-Augmented Generation) system using the Zoomcamp lesson pages as the knowledge base.
* Index and search lesson content using MinSearch.
* Measure token usage for RAG queries.
* Apply document chunking to improve retrieval.
* Convert the RAG system into an Agentic RAG workflow using a search tool.

## Files

```text
rag.ipynb    # Homework implementation and experiments
rag.py       # RAG helper functions
```

## Dataset

The lesson pages are downloaded directly from the official LLM Zoomcamp repository using `gitsource`.

Repository:
https://github.com/DataTalksClub/llm-zoomcamp

Commit used:

```text
8c1834d
```

Only markdown files inside the `lessons/` folders are included in the knowledge base.

## Technologies Used

* Python
* OpenAI GPT-5.4-mini
* MinSearch
* GitSource
* ToyAIKit

## Homework Tasks

### Q1 - Load Lesson Pages

Downloaded lesson pages from the repository and counted the total number of documents.

### Q2 - Search

Created a MinSearch index and searched for:

> How does the agentic loop keep calling the model until it stops?

### Q3 - Build RAG

Implemented a Retrieval-Augmented Generation pipeline and measured prompt token usage.

### Q4 - Chunking

Split lesson pages into overlapping chunks using:

```python
chunk_documents(documents, size=2000, step=1000)
```

### Q5 - RAG with Chunking

Re-indexed the chunks and compared token usage with the original implementation.

### Q6 - Agentic RAG

Built an agent with a search tool that can perform multiple searches before generating an answer.

## Learning Outcomes

Through this homework, I learned:

* Document indexing and retrieval
* Building a RAG pipeline from scratch
* Prompt token analysis
* Chunking strategies
* Agentic workflows and tool usage
* Differences between Traditional RAG and Agentic RAG

## Author

Rohith Parimi
