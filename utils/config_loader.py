"""Configuration loader utility."""
import os
from typing import Dict, Any


class ConfigLoader:
    """Loads and manages configuration from environment variables."""

    def __init__(self, config_path: str = None):
        """
        Initialize the configuration loader.

        Args:
            config_path: Deprecated - kept for compatibility
        """
        self._config = None

    def load_config(self) -> Dict[str, Any]:
        """
        Load configuration from environment variables.

        Returns:
            Dictionary containing configuration
        """
        self._config = {
            'llm': {
                'type': os.getenv('LLM_TYPE', 'anthropic'),
                'model_name': os.getenv('LLM_MODEL_NAME', 'claude-haiku-4-5-20251001'),
                'temperature': float(os.getenv('LLM_TEMPERATURE', '0.7')),
                'max_tokens': int(os.getenv('LLM_MAX_TOKENS', '500'))
            },
            'embedding': {
                'type': os.getenv('EMBEDDING_TYPE', 'huggingface'),
                'model_name': os.getenv('EMBEDDING_MODEL_NAME', 'sentence-transformers/all-MiniLM-L6-v2')
            },
            'vectorstore': {
                'type': os.getenv('VECTORSTORE_TYPE', 'chroma'),
                'persist_directory': os.getenv('VECTORSTORE_PERSIST_DIRECTORY', './indexes/chroma_db'),
                'collection_name': os.getenv('VECTORSTORE_COLLECTION_NAME', 'rag_documents')
            },
            'document_processing': {
                'chunk_size': int(os.getenv('DOCUMENT_CHUNK_SIZE', '1000')),
                'chunk_overlap': int(os.getenv('DOCUMENT_CHUNK_OVERLAP', '200'))
            },
            'retrieval': {
                'top_k': int(os.getenv('RETRIEVAL_TOP_K', '4')),
                'search_type': os.getenv('RETRIEVAL_SEARCH_TYPE', 'similarity')
            },
            'rag': {
                'system_prompt': os.getenv('SYSTEM_PROMPT', '')
            }
        }

        return self._config

    @property
    def config(self) -> Dict[str, Any]:
        """
        Get the loaded configuration.

        Returns:
            Configuration dictionary
        """
        if self._config is None:
            self.load_config()
        return self._config

    def get_llm_config(self) -> Dict[str, Any]:
        """Get LLM configuration."""
        return self.config.get('llm', {})

    def get_embedding_config(self) -> Dict[str, Any]:
        """Get embedding configuration."""
        return self.config.get('embedding', {})

    def get_vectorstore_config(self) -> Dict[str, Any]:
        """Get vector store configuration."""
        return self.config.get('vectorstore', {})

    def get_document_processing_config(self) -> Dict[str, Any]:
        """Get document processing configuration."""
        return self.config.get('document_processing', {})

    def get_retrieval_config(self) -> Dict[str, Any]:
        """Get retrieval configuration."""
        return self.config.get('retrieval', {})

    def get_rag_config(self) -> Dict[str, Any]:
        """Get RAG configuration including system prompt."""
        return self.config.get('rag', {})