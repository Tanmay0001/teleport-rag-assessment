## Semantic RAG & Vector Search Benchmark
## Context Aware Retrieval Engine (RAG + Vector Search) 

This project implements a lightweight Retrieval Augmented Generation (RAG) system to compare two retrieval strategies:

## Strategy A: Raw embedding based semantic search
## Strategy B: Query expanded retrieval using a generative model (mocked)

The goal is to evaluate how query rewriting improves retrieval quality in a vector database setup.

## Problem Statement

Design a local RAG pipeline that:

Ingests raw textual documents
Generates embeddings using a transformer model
Stores embeddings in a vector database
Performs semantic retrieval using similarity search
Compares two retrieval strategies:
Raw query embedding (baseline)
Query expansion + embedding (enhanced)
# System Architecture
## Strategy A — Baseline Retrieval
User Query
   ↓
Embedding Model (Sentence Transformers)
   ↓
Vector Search (FAISS)
   ↓
Top-K Similar Documents
## Strategy B — Query-Enhanced Retrieval
User Query
   ↓
Query Expansion (Mock LLM / Generative Model)
   ↓
Expanded Query
   ↓
Embedding Model
   ↓
Vector Search (FAISS)
   ↓
Top-K Similar Documents
# Tech Stack
Python 3.11
Sentence Transformers (all-MiniLM-L6-v2)
FAISS (Inner Product / Cosine Similarity)
NumPy
Pytest (testing)
Mock Vertex AI SDK (for query expansion simulation)
# Dataset

A small curated corpus of 8 technical paragraphs covering:

Auto scaling & load balancing
Distributed systems
RAG architecture
Vector databases (FAISS)
Query expansion techniques
Cloud migration to Vertex AI

# Location:

src/dataset.py
## Core Design Decisions
1. Embedding Model

I use:

# sentence transformers/all-MiniLM-L6-v2
As its:
1. Lightweight
Fast inference
Strong semantic representation
Industry standard for RAG prototypes
2. Similarity Metric

I use Cosine Similarity (via FAISS Inner Product)

Why Cosine Similarity?
Measures directional similarity (semantic meaning)
Works best with L2-normalized embeddings
Standard in transformer-based retrieval systems
3. Vector Database Choice

We use FAISS (IndexFlatIP)

Why FAISS?
High-performance similarity search
In-memory vector indexing
Suitable for small-to-medium scale retrieval systems
4. Query Expansion Strategy

I simulate a generative model using a mock Vertex AI SDK.

Purpose:
Expand short queries into richer semantic descriptions
Improve recall by increasing embedding context coverage
# Evaluation Strategy

We compare both approaches across multiple queries:

Metrics:
Top-K retrieval results
Overlap between strategies
Average similarity scores
Relevance improvement via query expansion
Example Query

## "How does the system handle peak load?"

Strategy A (Raw Query)
Direct embedding of original query
Retrieves general infrastructure-related chunks
Strategy B (Expanded Query)
Query rewritten to include:
autoscaling
load balancing
traffic spikes
Retrieves more relevant and higher-scoring chunks
# Observation

Query expansion consistently improves retrieval quality by:

Increasing semantic coverage
Reducing vocabulary mismatch
Improving recall of relevant documents
# Production Migration (Vertex AI)

In production, this system can be migrated to:

Embeddings:
Vertex AI Text Embedding Model (textembedding-gecko)
Vector DB:
Vertex AI Vector Search (Matching Engine)
Architecture:
Store embeddings in GCS
Build managed ANN index
Deploy real time endpoint for retrieval
## Running the Project
Install dependencies
pip install -r requirements.txt
Run benchmark
python main.py

Outputs:

Console comparison (Strategy A vs B)
JSON report in outputs/
Run tests
pytest
## Project Structure-------dir:
src/
  dataset.py              # Technical corpus
  embedder.py            # Sentence transformer embeddings
  vector_store.py        # FAISS / similarity search
  retrieval_engine.py    # RAG orchestration
  benchmarker.py         # Evaluation logic
  mocks/
    vertexai_mock.py     # Mock LLM for query expansion

tests/
  test_retrieval.py
  test_mock.py

main.py                  # Entry point
outputs/                 # Benchmark results
# Example Output Insight
Query	Strategy A	Strategy B
Peak load handling	Moderate relevance	High relevance (autoscaling context)
DB optimization	Partial match	Strong match (pooling + concurrency)

 # Summary

This project demonstrates:

End to end RAG pipeline design
Vector-based semantic retrieval
Query expansion impact on retrieval quality
Benchmark-driven evaluation of retrieval strategies
Production-ready thinking with Vertex AI migration path
 Final Note

This implementation focuses on:

Clean architecture
Reproducible evaluation
Realworld RAG design patterns
Production scalability considerations
