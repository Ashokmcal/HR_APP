#!/usr/bin/env python3
"""
Configuration Management Script for HR_APP
Helps users easily switch between different AI providers and configurations
"""

import os
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1].lower()
    
    if command == "list":
        list_current_config()
    elif command == "openai":
        configure_openai()
    elif command == "claude":
        configure_claude()
    elif command == "free":
        configure_free_setup()
    elif command == "help":
        print_help()
    else:
        print(f"Unknown command: {command}")
        print_help()

def print_help():
    print("""
🔧 HR_APP Configuration Manager

Usage: python config_manager.py <command>

Commands:
  list      - Show current configuration
  openai    - Configure for OpenAI models
  claude    - Configure for Claude/Anthropic models  
  free      - Configure for free/local models
  help      - Show this help message

Examples:
  python config_manager.py list
  python config_manager.py claude
  python config_manager.py free
""")

def list_current_config():
    print("📋 Current Configuration:")
    print("=" * 50)
    
    configs = [
        ("LLM Provider", "LLM_TYPE"),
        ("LLM Model", "LLM_MODEL_NAME"), 
        ("LLM Temperature", "LLM_TEMPERATURE"),
        ("Max Tokens", "LLM_MAX_TOKENS"),
        ("Embedding Provider", "EMBEDDING_TYPE"),
        ("Embedding Model", "EMBEDDING_MODEL_NAME"),
        ("Vector Store", "VECTORSTORE_TYPE"),
        ("Chunk Size", "DOCUMENT_CHUNK_SIZE"),
        ("Top K Results", "RETRIEVAL_TOP_K"),
    ]
    
    for name, env_var in configs:
        value = os.getenv(env_var, "Not set")
        print(f"{name:20}: {value}")

def configure_openai():
    print("🚀 Configuring for OpenAI...")
    
    updates = {
        "LLM_TYPE": "openai",
        "LLM_MODEL_NAME": "gpt-4o-mini",
        "EMBEDDING_TYPE": "openai", 
        "EMBEDDING_MODEL_NAME": "text-embedding-3-small"
    }
    
    update_env_file(updates)
    print("✅ Configured for OpenAI! Make sure OPENAI_API_KEY is set in .env")

def configure_claude():
    print("🤖 Configuring for Claude/Anthropic...")
    
    updates = {
        "LLM_TYPE": "anthropic",
        "LLM_MODEL_NAME": "claude-haiku-4-5-20251001", 
        "EMBEDDING_TYPE": "huggingface",
        "EMBEDDING_MODEL_NAME": "sentence-transformers/all-MiniLM-L6-v2"
    }
    
    update_env_file(updates)
    print("✅ Configured for Claude! Make sure ANTHROPIC_API_KEY is set in .env")

def configure_free_setup():
    print("🆓 Configuring for free/local models...")
    
    updates = {
        "LLM_TYPE": "huggingface",
        "LLM_MODEL_NAME": "microsoft/DialoGPT-medium",
        "EMBEDDING_TYPE": "huggingface", 
        "EMBEDDING_MODEL_NAME": "sentence-transformers/all-MiniLM-L6-v2"
    }
    
    update_env_file(updates)
    print("✅ Configured for free models! No API keys required.")

def update_env_file(updates):
    env_path = Path(".env")
    
    if not env_path.exists():
        print("❌ .env file not found! Please copy .env.example to .env first.")
        return
    
    # Read current .env content
    with open(env_path, 'r') as f:
        lines = f.readlines()
    
    # Update specific lines
    updated_lines = []
    for line in lines:
        if '=' in line and not line.strip().startswith('#'):
            key = line.split('=')[0].strip()
            if key in updates:
                updated_lines.append(f"{key}={updates[key]}\n")
                continue
        updated_lines.append(line)
    
    # Write back to .env
    with open(env_path, 'w') as f:
        f.writelines(updated_lines)
    
    print(f"Updated {len(updates)} configuration values in .env")

if __name__ == "__main__":
    main()