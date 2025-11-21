# Quick Start Guide

## 5-Minute Setup

### 1. Install Dependencies

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### 2. Set Up Configuration

```bash
# Copy example configuration
cp .env.example .env

# Edit .env file with your settings and API keys
# All configuration is now in environment variables
```

### 3. Index Your First Document

```bash
# Index a PDF
python main.py index path/to/your/document.pdf
```

### 4. Start Querying

```bash
# Interactive mode
python main.py query --interactive

# Or single query
python main.py query --question "What is this document about?"
```

## Example Session

```bash
# Terminal 1: Index documents
$ python main.py index ./documents/research_paper.pdf
Loading documents from: ./documents/research_paper.pdf
Loaded 15 document(s)
Splitting documents into chunks...
Created 45 chunks
Creating vector store and indexing documents...
Indexing complete!

# Terminal 2: Query documents
$ python main.py query --interactive

=== RAG Interactive Query Mode ===
Type 'exit' or 'quit' to exit

Question: What are the main findings?

Searching and generating answer...

Answer: The research paper presents three main findings: 
1) The proposed method improves accuracy by 15%
2) Processing time is reduced by 40%
3) The approach generalizes well across different datasets

Question: exit

Goodbye!
```

## Running Tests

```bash
# Run all tests
pytest

# With coverage report
pytest --cov=src --cov-report=html tests/

# Run specific test
pytest tests/test_factories.py -v
```

## Common Commands

```bash
# Index single file
python main.py index document.pdf

# Index directory
python main.py index ./documents/

# Query with sources
python main.py query --interactive --show-sources

# Use custom config
python main.py --config my_config.yaml index document.pdf
```

## Configuration Tips

Edit `.env` file for:

- **Better accuracy**: Set `RETRIEVAL_TOP_K=6`
- **Faster responses**: Use `LLM_MODEL_NAME=claude-haiku-4-5-20251001`
- **Larger documents**: Set `DOCUMENT_CHUNK_SIZE=1500`
- **More context**: Set `DOCUMENT_CHUNK_OVERLAP=300`

## Troubleshooting

**Problem**: "OpenAI API key not found"
**Solution**: Check `.env` file exists and contains valid API key

**Problem**: "Vector store not initialized"
**Solution**: Run `index` command before `query`

**Problem**: "File not found"
**Solution**: Use absolute paths or check current directory

**Problem**: Empty or irrelevant answers
**Solution**: 
- Increase `top_k` in config
- Check if documents are properly indexed
- Verify chunk size is appropriate for your documents

## Next Steps

1. Read the full [README.md](README.md) for detailed documentation
2. Explore the [Configuration Guide](#configuration) 
3. Check out the [Examples](#examples) directory
4. Learn about [Extending the Application](README.md#extending-the-application)