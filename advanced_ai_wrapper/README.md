🧠 AI Intent Parser + Dynamic Crawler

An AI-powered web intelligence system that understands user intent, dynamically crawls websites, and retrieves structured answers — without hardcoded scraping rules.

🚀 How It Works
User Query
   ↓
Intent Classification (LLM)
   ↓
Dynamic Crawl / Link Selection
   ↓
Chunk + Embed
   ↓
Vector Search
   ↓
LLM Answer

Understands natural language queries

Autonomously selects relevant pages

Uses embeddings + FAISS for fast retrieval

Avoids re-crawling with semantic indexing

🔥 Features

Intent-based crawling

Automatic link discovery

Hybrid mode (crawl if missing, otherwise retrieve)

Structured information extraction

Scalable semantic search

📦 Tech Stack

LangChain

Crawl4AI

SentenceTransformers

FAISS

Groq / OpenAI

⚙️ Installation (uv)
uv init
uv add langchain langchain-groq langchain-community \
langchain-text-splitters sentence-transformers faiss-cpu crawl4ai
🧪 Example Queries

“Who are the co-founders?”

“What products do they sell?”

“Give me homepage content.”

No predefined scraping rules required.
