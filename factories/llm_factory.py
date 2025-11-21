"""LLM Factory implementation."""
import os
from typing import Any, Dict
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from .base_factory import BaseFactory
from utils.config_types import LLMType

class LLMFactory(BaseFactory):
    """Factory for creating LLM instances."""

    def create(self, config: Dict[str, Any]) -> Any:
        """
        Create an LLM instance based on configuration.

        Args:
            config: LLM configuration dictionary

        Returns:
            LLM instance

        Raises:
            ValueError: If unsupported LLM type is specified
        """
        llm_type = config.get('type', '').lower()

        if llm_type == LLMType.OPENAI:
            return self._create_openai_llm(config)
        elif llm_type == LLMType.ANTHROPIC:
            return self._create_anthropic_llm(config)
        else:
            raise ValueError(f"Unsupported LLM type: {llm_type}")

    def _create_openai_llm(self, config: Dict[str, Any]) -> ChatOpenAI:
        """
        Create an OpenAI LLM instance.

        Args:
            config: OpenAI configuration

        Returns:
            ChatOpenAI instance
        """
        return ChatOpenAI(
            model=config.get('model_name'),
            temperature=config.get('temperature'),
            max_tokens=config.get('max_tokens')
        )

    def _create_anthropic_llm(self, config: Dict[str, Any]) -> ChatAnthropic:
        """
        Create an Anthropic LLM instance.

        Args:
            config: Anthropic configuration

        Returns:
            ChatAnthropic instance
        """
        return ChatAnthropic(
            model=config.get('model_name'),
            temperature=config.get('temperature'),
            max_tokens=config.get('max_tokens')
        )