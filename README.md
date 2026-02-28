# AI Wrapper

A Python project that provides AI-powered wrappers using Groq's LLM and various web crawling/embedding capabilities. The project includes two modules: a basic chat wrapper and an intermediate wrapper with web crawling and semantic search functionality.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Linux](#linux)
  - [Windows](#windows)
- [Configuration](#configuration)
- [Modules](#modules)
  - [Basic Wrapper](#basic-wrapper)
  - [Intermediate Wrapper](#intermediate-wrapper)
- [Running the Programs](#running-the-programs)
  - [Linux](#linux-1)
  - [Windows](#windows-1)
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

| Requirement | Version | Notes |
|-------------|---------|-------|
| **Python** | 3.9+ (recommended 3.11) | Required |
| **pip** | Latest | Required |
| **Groq API Key** | - | Required for LLM |

### Verify Python Installation

**Linux:**
```bash
python3 --version
pip3 --version
```

**Windows:**
```cmd
python --version
pip --version
```

---

## Installation

### Linux

#### 1. Navigate to Project Directory

```bash
cd "AI Wrapper"
```

#### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

#### 3. Activate Virtual Environment

```bash
source venv/bin/activate
```

#### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 5. Install Crawl4AI Browser

```bash
crawl4ai-setup
```

> **Note**: This command downloads and sets up browser binaries for web crawling. May take a few minutes.

---

### Windows

#### 1. Navigate to Project Directory

```cmd
cd "AI Wrapper"
```

Or using PowerShell:
```powershell
Set-Location "AI Wrapper"
```

#### 2. Create Virtual Environment

```cmd
python -m venv venv
```

#### 3. Activate Virtual Environment

```cmd
venv\Scripts\activate
```

Or using PowerShell:
```powershell
.\venv\Scripts\Activate
```

#### 4. Install Dependencies

```cmd
pip install -r requirements.txt
```

#### 5. Install Crawl4AI Browser

```cmd
crawl4ai-setup
```

> **Note**: This command downloads and sets up browser binaries for web crawling. May take a few minutes.

---

## Configuration

### Setting Up Environment Variables

Create a `.env` file in the project root with your Groq API key.

**Linux:**
```bash
touch .env
```

**Windows:**
```cmd
type nul > .env
```

Add the following content:

```env
GROQ_API_KEY=your_groq_api_key_here
```

#### Getting a Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in to your account
3. Navigate to API Keys
4. Create a new API key
5. Copy the key to your `.env` file

---

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

---

## Running the Programs

### Linux

#### Running Basic Wrapper

```bash
python3 basic_wrapper.py
```

#### Running Intermediate Wrapper

```bash
python3 intermediate_wrapper.py
```

Interactive mode:
```
Enter E to exit: C
Enter your Prompt: What products does Saflora offer?
# AI will crawl the website and provide context-aware response
```

---

### Windows

#### Running Basic Wrapper

```cmd
python basic_wrapper.py
```

Or:
```powershell
python3 basic_wrapper.py
```

#### Running Intermediate Wrapper

```cmd
python intermediate_wrapper.py
```

Or:
```powershell
python3 intermediate_wrapper.py
```

Interactive mode:
```
Enter E to exit: C
Enter your Prompt: What products does Saflora offer?
# AI will crawl the website and provide context-aware response
```

---

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | Yes | API key for Groq LLM |
| `USER_AGENT` | Optional | User agent for web crawling (default: Mozilla/5.0) |

---

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

---

## Troubleshooting

### Import Errors

Ensure all dependencies are installed:

**Linux:**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

**Windows:**
```cmd
venv\Scripts\activate
pip install -r requirements.txt
```

### Crawl4AI Browser Not Found

Run the setup command:

**Linux & Windows:**
```bash
crawl4ai-setup
```

### API Key Issues

Verify your `.env` file:

**Linux:**
```bash
cat .env
```

**Windows:**
```cmd
type .env
```

### Virtual Environment Activation Issues

**Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```cmd
venv\Scripts\activate
```

If PowerShell blocks execution, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Version Conflicts

Create a fresh virtual environment:

**Linux:**
```bash
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows:**
```cmd
rmdir /s /q venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Memory Issues with sentence-transformers

The default model `all-MiniLM-L6-v2` is lightweight. If you still have memory issues, consider:
- Closing other applications
- Using a machine with more RAM
- Processing in smaller batches

---

## License

MIT License

## Support

For issues and questions, please check the project repository.
