# AI Wrapper

A Python project that provides AI-powered wrappers using Groq's LLM and various web crawling/embedding capabilities. The project includes two modules: a basic chat wrapper and an intermediate wrapper with web crawling and semantic search functionality.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Modules](#modules)
  - [Basic Wrapper](#basic-wrapper)
  - [Intermediate Wrapper](#intermediate-wrapper)
- [Running the Programs](#running-the-programs)
- [Environment Variables](#environment-variables)
- [Package Versions](#package-versions)
- [Troubleshooting](#troubleshooting)

## Overview

This project provides two AI wrapper modules:

1. **Basic Wrapper** (`basic_wrapper.py`): A simple chatbot using Groq's Llama model, specialized in philosophy and psychology domains.

2. **Intermediate Wrapper** (`intermediate_wrapper.py`): An advanced wrapper that combines:
   - Web crawling with Crawl4AI
   - Semantic search using sentence embeddings
   - Cosine similarity for content matching
   - Context-aware AI responses about Saflora

## Project Structure

```
AI Wrapper/
├── basic_wrapper.py          # Basic chat wrapper module
├── intermediate_wrapper.py   # Advanced wrapper with web crawling
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (API keys)
└── README.md                 # This documentation
```

## Prerequisites

- **Python**: 3.9 or higher (recommended: 3.11)
- **pip**: Latest version recommended
- **Groq API Key**: Required for LLM functionality

## Installation

### 1. Clone the Repository

```bash
cd "AI Wrapper"
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Crawl4AI Browser (Required for intermediate_wrapper.py)

```bash
crawl4ai-setup
```

> **Note**: This command downloads and sets up the browser binaries required for web crawling. It may take a few minutes depending on your internet connection.

## Configuration

### Setting Up Environment Variables

The project requires a `.env` file with the following variables:

```env
GROQ_API_KEY=your_groq_api_key_here
```

#### Getting a Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in to your account
3. Navigate to API Keys
4. Create a new API key
5. Copy the key to your `.env` file

### Creating the .env File

Create a `.env` file in the project root:

```bash
touch .env
```

Add your API key:

```env
GROQ_API_KEY=gsk_your_api_key_here
```

## Modules

### Basic Wrapper

**File**: `basic_wrapper.py`

A simple chatbot using Groq's Llama 3.1 8B Instant model with conversation history support.

**Features**:
- Philosophy and psychology domain specialist
- Conversation history tracking
- Customizable streaming support

**Class**: `ChatGroqWrapper`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `stream` | `bool` | `False` | Enable streaming responses |

**Methods**:

- `ask(prompt: str) -> str`: Send a prompt and get AI response

**Usage Example**:

```python
from basic_wrapper import ChatGroqWrapper

# Initialize the wrapper
wrapper = ChatGroqWrapper(stream=False)

# Ask a question
response = wrapper.ask("Explain the concept of free will in philosophy")
print(response)
```

**Running Directly**:

```bash
python basic_wrapper.py
```

---

### Intermediate Wrapper

**File**: `intermediate_wrapper.py`

An advanced wrapper that crawls websites, creates vector embeddings, and uses semantic similarity to find relevant content before generating AI responses.

**Features**:
- Web crawling with Crawl4AI
- Semantic search using sentence embeddings
- Cosine similarity for content matching
- Context-aware responses for Saflora website

**Classes**:

| Class | Description |
|-------|-------------|
| `VectorEncoder` | Creates embeddings using sentence-transformers |
| `Parser` | Parses HTML and extracts links |
| `Crawler` | Async web crawler using Crawl4AI |
| `Splitter` | Splits text into chunks for processing |
| `SafloraWrapper` | AI wrapper specialized for Saflora |

**Usage Example**:

```python
import asyncio
from intermediate_wrapper import Crawler, Parser, VectorEncoder, SafloraWrapper

async def main():
    # Crawl a website
    crawler = Crawler()
    result = await crawler.crawl("https://www.saflora.com.np")
    
    # Parse links
    parser = Parser()
    links = parser.parse_links(result.html)
    
    # Create embeddings and find similar content
    encoder = VectorEncoder()
    # ... (similarity calculation)
    
    # Get AI response with context
    wrapper = SafloraWrapper()
    response = wrapper.ask("Your question", context="relevant context")
    print(response)

asyncio.run(main())
```

**Running Directly**:

```bash
python intermediate_wrapper.py
```

The interactive mode accepts:
- `C` - Continue to ask a question
- `E` - Exit the program

## Running the Programs

### Running Basic Wrapper

```bash
python basic_wrapper.py
```

Expected output:
```
# AI will respond with an answer about philosophy/psychology
```

### Running Intermediate Wrapper

```bash
python intermediate_wrapper.py
```

Interactive mode:
```
Enter E to exit: C
Enter your Prompt: What products does Saflora offer?
# AI will crawl the website and provide context-aware response
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | Yes | API key for Groq LLM |
| `USER_AGENT` | Optional | User agent for web crawling (default: Mozilla/5.0) |

## Package Versions

The following versions are tested and compatible with this project:

| Package | Version | Description |
|---------|---------|-------------|
| `langchain-groq` | 1.1.2 | Groq integration for LangChain |
| `langchain-core` | 1.2.15 | LangChain core abstractions |
| `langchain-community` | 0.2.16 | Third-party LangChain integrations |
| `langchain-text-splitters` | 0.3.9 | Text splitting utilities |
| `beautifulsoup4` | 4.14.3 | HTML/XML parsing |
| `python-dotenv` | 1.0.1 | Environment variable loading |
| `crawl4ai` | 0.7.6 | Web crawler for LLM |
| `sentence-transformers` | 5.2.3 | Sentence embedding models |
| `scikit-learn` | 1.6.1 | Machine learning library |
| `numpy` | 2.2.3 | Numerical computing |
| `groq` | 0.14.0 | Groq API client |
| `lxml` | 5.3.0 | XML/HTML processing |

## Troubleshooting

### Import Errors

If you encounter import errors, ensure all dependencies are installed:

```bash
pip install -r requirements.txt
```

### Crawl4AI Browser Not Found

If you get browser-related errors:

```bash
crawl4ai-setup
```

### API Key Issues

Make sure your `.env` file contains the correct `GROQ_API_KEY`:

```bash
cat .env
```

### Version Conflicts

If you experience version conflicts, create a fresh virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Memory Issues with sentence-transformers

If you run into memory issues, you can use a lighter model or process in batches. The default model `all-MiniLM-L6-v2` is already lightweight.

## License

MIT License

## Support

For issues and questions, please check the project repository.
