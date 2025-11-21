"""Embedding Factory implementation."""
from typing import Any, Dict
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from .base_factory import BaseFactory
from utils.config_types import EmbeddingModelType

class EmbeddingFactory(BaseFactory):
    """Factory for creating embedding model instances."""

    def create(self, config: Dict[str, Any]) -> Any:
        """
        Create an embedding model instance based on configuration.

        Args:
            config: Embedding configuration dictionary

        Returns:
            Embedding model instance

        Raises:
            ValueError: If unsupported embedding type is specified
        """
        embedding_type = config.get('type', '').lower()

        if embedding_type == EmbeddingModelType.OPENAI:
            return self._create_openai_embedding(config)
        elif embedding_type == EmbeddingModelType.HUGGINGFACE:
            return self._create_huggingface_embedding(config)
        else:
            raise ValueError(f"Unsupported embedding type: {embedding_type}")

    def _create_openai_embedding(self, config: Dict[str, Any]) -> OpenAIEmbeddings:
        """
        Create an OpenAI embedding instance.

        Args:
            config: OpenAI embedding configuration

        Returns:
            OpenAIEmbeddings instance
        """
        return OpenAIEmbeddings(
            model=config.get('model_name')
        )

    def _create_huggingface_embedding(self, config: Dict[str, Any]) -> HuggingFaceEmbeddings:
        """
        Create a Hugging Face embedding instance.

        Args:
            config: Hugging Face embedding configuration

        Returns:
            HuggingFaceEmbeddings instance
        """
        return HuggingFaceEmbeddings(
            model_name=config.get('model_name')
        )