"""
Simple test script to verify system prompt configuration is working.
Run this after configuring your SYSTEM_PROMPT in .env file.
"""
import os
from dotenv import load_dotenv
from utils.config_loader import ConfigLoader

def test_system_prompt_loading():
    """Test that system prompt is loaded correctly from environment."""
    print("=" * 70)
    print("SYSTEM PROMPT CONFIGURATION TEST")
    print("=" * 70)

    # Load environment variables
    load_dotenv()

    # Check if SYSTEM_PROMPT is set in environment
    env_prompt = os.getenv('SYSTEM_PROMPT', '')

    print("\n1. Environment Variable Check:")
    print("-" * 70)
    if env_prompt:
        print("✓ SYSTEM_PROMPT found in environment variables")
        print(f"\nLength: {len(env_prompt)} characters")
        print(f"\nFirst 200 characters:")
        print(env_prompt[:200] + "..." if len(env_prompt) > 200 else env_prompt)
    else:
        print("⚠ SYSTEM_PROMPT not set in .env file")
        print("  The application will use the default system prompt")

    # Test ConfigLoader
    print("\n\n2. ConfigLoader Test:")
    print("-" * 70)
    config_loader = ConfigLoader()
    config_loader.load_config()

    rag_config = config_loader.get_rag_config()
    loaded_prompt = rag_config.get('system_prompt', '')

    if loaded_prompt:
        print("✓ System prompt loaded successfully via ConfigLoader")
        print(f"\nLength: {len(loaded_prompt)} characters")
        print(f"\nFirst 200 characters:")
        print(loaded_prompt[:200] + "..." if len(loaded_prompt) > 200 else loaded_prompt)

        # Verify they match
        if loaded_prompt == env_prompt:
            print("\n✓ ConfigLoader matches environment variable")
        else:
            print("\n✗ WARNING: ConfigLoader output doesn't match environment variable")
    else:
        print("⚠ No system prompt in ConfigLoader")
        print("  The RAG pipeline will use the default prompt")

    # Show what will be used
    print("\n\n3. Effective System Prompt:")
    print("-" * 70)
    if loaded_prompt:
        print("The following custom system prompt will be used:")
        print("\n" + loaded_prompt)
    else:
        print("The default system prompt will be used:")
        default_prompt = """You are an AI HR Assistant for TechnoSphere India Private Limited. Your role is to provide accurate, helpful, and professional answers to employee questions about company HR policies and procedures.

Guidelines:
- Base your answers ONLY on the provided context from company policy documents
- Be clear, concise, and professional in your responses
- If the context doesn't contain enough information to answer the question, say so honestly
- Use a friendly but professional tone appropriate for workplace communication
- When citing policies, be specific about policy names if mentioned in the context
- If asked about topics not covered in the policies, politely indicate that you can only answer questions about company HR policies
- Format your answers in a well-structured, easy-to-read manner
- For numerical information (like leave days, benefits), be precise and accurate"""
        print("\n" + default_prompt)

    print("\n" + "=" * 70)
    print("TEST COMPLETE")
    print("=" * 70)

    # Recommendations
    print("\n📝 RECOMMENDATIONS:")
    if not loaded_prompt:
        print("   • To use a custom system prompt, add SYSTEM_PROMPT to your .env file")
        print("   • See SYSTEM_PROMPT_GUIDE.md for examples and best practices")
    else:
        print("   ✓ Custom system prompt configured successfully")
        print("   • Test it by running a query: python main.py query --interactive")
        print("   • Monitor responses to ensure they match your expectations")
        print("   • Adjust the prompt in .env as needed and restart the application")

if __name__ == "__main__":
    test_system_prompt_loading()
