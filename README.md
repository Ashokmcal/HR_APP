# HR Application (RAG)

A modular Retrieval Augmented Generation (RAG) application built with LangChain 0.3 and Python 3.13. This application allows you to index PDF documents and query them using natural language with OpenAI's language models.

## Features

- **Modular Architecture**: Factory pattern implementation for easy extensibility
- **Configurable**: YAML-based configuration for all components
- **PDF Support**: Load and process PDF documents
- **Persistent Vector Store**: ChromaDB for efficient document storage and retrieval
- **CLI Interface**: Simple command-line interface for indexing and querying
- **Comprehensive Testing**: Unit tests for all major components

## Architecture

```
rag-application/
├── config/
│   └── config.yaml              # Main configuration file
├── src/
│   ├── factories/               # Factory pattern implementations
│   │   ├── llm_factory.py
│   │   ├── embedding_factory.py
│   │   └── vectorstore_factory.py
│   ├── components/              # Core components
│   │   ├── document_loader.py
│   │   ├── text_splitter.py
│   │   └── retriever.py
│   ├── rag/
│   │   └── rag_pipeline.py      # Main RAG pipeline
│   └── utils/
│       └── config_loader.py     # Configuration loader
├── tests/                       # Unit tests
└── main.py                      # CLI entry point
```

## Installation

### Prerequisites

- Python 3.13+
- OpenAI API key

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd rag-application
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and configure all application settings including API keys
```

5. Configure the application:
```bash
# Edit config/config.yaml with your preferred settings
```

## Configuration

The application is configured via environment variables in the `.env` file. All configuration has been moved from code to environment variables for better security and flexibility. Key configuration options:

### LLM Configuration
```bash
# In .env file
LLM_TYPE=anthropic
LLM_MODEL_NAME=claude-haiku-4-5-20251001
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=500
```

### Embedding Configuration
```bash
# In .env file
EMBEDDING_TYPE=huggingface
EMBEDDING_MODEL_NAME=sentence-transformers/all-MiniLM-L6-v2
```

### Vector Store Configuration
```bash
# In .env file
VECTORSTORE_TYPE=chroma
VECTORSTORE_PERSIST_DIRECTORY=./indexes/chroma_db
VECTORSTORE_COLLECTION_NAME=rag_documents
```

### Document Processing
```bash
# In .env file
DOCUMENT_CHUNK_SIZE=1000
DOCUMENT_CHUNK_OVERLAP=200
```

### Retrieval Configuration
```bash
# In .env file
RETRIEVAL_TOP_K=4
RETRIEVAL_SEARCH_TYPE=similarity
```

### System Prompt Configuration
```bash
# In .env file
# Customize how the AI assistant responds to queries
SYSTEM_PROMPT=You are an AI HR Assistant for TechnoSphere India Private Limited...
```

See [SYSTEM_PROMPT_GUIDE.md](SYSTEM_PROMPT_GUIDE.md) for detailed customization options and examples.

## Usage

### Indexing Documents

Index a single PDF file:
```bash
python main.py index /path/to/document.pdf
```

Index all PDFs in a directory:
```bash
python main.py index /path/to/documents/
```

### Querying Documents

Interactive mode (recommended):
```bash
python main.py query --interactive
```

Single query:
```bash
python main.py query --question "What is this document about?"
```

Show source documents:
```bash
python main.py query --interactive --show-sources
```

### Custom Configuration

Use a different configuration file:
```bash
python main.py --config custom_config.yaml index document.pdf
```

## Testing

Run all tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=src tests/
```

Run specific test file:
```bash
pytest tests/test_factories.py
```

## Factory Pattern

The application uses the Factory Pattern for creating instances of:

1. **LLM Factory**: Creates language model instances (OpenAI)
2. **Embedding Factory**: Creates embedding model instances (OpenAI)
3. **Vector Store Factory**: Creates vector store instances (Chroma)

To add support for new providers, simply:
1. Extend the appropriate factory class
2. Add configuration in `config.yaml`
3. Implement the provider-specific creation method

Example:
```python
def _create_anthropic_llm(self, config: Dict[str, Any]) -> Any:
    return ChatAnthropic(
        model=config.get('model_name', 'claude-sonnet-4-20250514'),
        temperature=config.get('temperature', 0.7)
    )
```

## Components

### Document Loader
Handles loading PDF documents from files or directories.

### Text Splitter
Splits documents into chunks for efficient processing and retrieval.

### Retriever
Retrieves relevant document chunks based on similarity search.

### RAG Pipeline
Orchestrates the entire RAG workflow:
1. Document loading
2. Text splitting
3. Vector store creation/loading
4. Query processing
5. Answer generation

## Project Structure Details

```
src/
├── factories/           # Factory pattern implementations
│   ├── base_factory.py  # Abstract base class for factories
│   ├── llm_factory.py   # LLM instance creation
│   ├── embedding_factory.py  # Embedding model creation
│   └── vectorstore_factory.py  # Vector store creation
│
├── components/          # Modular components
│   ├── document_loader.py  # PDF loading
│   ├── text_splitter.py    # Text chunking
│   └── retriever.py        # Document retrieval
│
├── rag/                 # Main RAG logic
│   └── rag_pipeline.py  # Pipeline orchestration
│
└── utils/               # Utility functions
    └── config_loader.py # YAML configuration loading
```

## Extending the Application

### Adding a New LLM Provider

1. Update `src/factories/llm_factory.py`:
```python
def create(self, config: Dict[str, Any]) -> Any:
    llm_type = config.get('type', '').lower()
    
    if llm_type == 'openai':
        return self._create_openai_llm(config)
    elif llm_type == 'anthropic':  # New provider
        return self._create_anthropic_llm(config)
    else:
        raise ValueError(f"Unsupported LLM type: {llm_type}")
```

2. Update `config/config.yaml`:
```yaml
llm:
  type: "anthropic"
  model_name: "claude-sonnet-4-20250514"
```

### Adding a New Vector Store

Follow the same pattern in `src/factories/vectorstore_factory.py`.

## Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your OpenAI API key is set in `.env`
2. **File Not Found**: Check that PDF paths are correct
3. **Memory Issues**: Reduce `chunk_size` or `top_k` in config
4. **Empty Results**: Ensure documents are indexed before querying

## Performance Tips

1. **Chunk Size**: Larger chunks (1000-2000) for comprehensive context, smaller (500-1000) for precise retrieval
2. **Overlap**: 10-20% of chunk size for better context continuity
3. **Top K**: 3-5 documents for most queries, increase for complex questions
4. **Temperature**: Lower (0.3-0.5) for factual answers, higher (0.7-0.9) for creative responses

## License

MIT License

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request

## Support

For issues and questions, please open an issue on GitHub.