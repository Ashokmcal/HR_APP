# System Prompt Configuration Changes

## Summary

The system prompt has been moved entirely to the `.env` file. There is **no hardcoded default** anymore - the `SYSTEM_PROMPT` variable is now **REQUIRED** in your `.env` file.

## Changes Made

### 1. **[rag/rag_pipeline.py](rag/rag_pipeline.py:107-118)**

**Removed:** Hardcoded default system prompt fallback

**Added:** Error handling that raises a clear exception if `SYSTEM_PROMPT` is not configured

```python
# Before: Had hardcoded default
if not system_prompt:
    system_prompt = """You are an AI HR Assistant..."""  # Long hardcoded text

# After: Requires configuration in .env
if not system_prompt:
    raise ValueError(
        "SYSTEM_PROMPT must be configured in .env file. "
        "Please add SYSTEM_PROMPT to your .env file with your desired system prompt. "
        "See .env.example for the default prompt template."
    )
```

### 2. **[.env](.env:82-87)**

**Added:** `SYSTEM_PROMPT` configuration with default template

```bash
# ===================================================================
# RAG SYSTEM PROMPT CONFIGURATION
# ===================================================================
# System prompt for the AI HR Assistant - guides how the AI responds
# REQUIRED: This must be configured for the application to work
SYSTEM_PROMPT=You are an AI HR Assistant for TechnoSphere India Private Limited...
```

### 3. **[.env.example](.env.example:82-88)**

**Updated:** Added clear documentation that `SYSTEM_PROMPT` is REQUIRED

```bash
# ===================================================================
# RAG SYSTEM PROMPT CONFIGURATION
# ===================================================================
# System prompt for the AI HR Assistant - guides how the AI responds
# REQUIRED: This must be configured for the application to work
# Customize this prompt to change the AI's behavior, tone, and response style
SYSTEM_PROMPT=You are an AI HR Assistant for TechnoSphere India Private Limited...
```

### 4. **[SYSTEM_PROMPT_GUIDE.md](SYSTEM_PROMPT_GUIDE.md:16-36)**

**Updated:** Documentation to clearly state that `SYSTEM_PROMPT` is REQUIRED

## Benefits

1. ✅ **No Hardcoding:** All configuration is in `.env` - easier to manage
2. ✅ **Clear Requirements:** Error message guides users if prompt is missing
3. ✅ **Better Control:** Forces explicit configuration instead of hidden defaults
4. ✅ **Easy Customization:** Users can modify the prompt without touching code
5. ✅ **Version Control Friendly:** System prompts can be managed per environment

## Migration Guide

If you're upgrading from a previous version:

1. **Ensure `.env` file exists:**
   ```bash
   cp .env.example .env
   ```

2. **Add `SYSTEM_PROMPT` to your `.env` file:**
   - Copy the default from `.env.example`
   - Or customize it for your needs

3. **Restart your application:**
   ```bash
   # For Streamlit
   streamlit run streamlit_app.py

   # For CLI
   python main.py query --interactive
   ```

## Error Handling

If `SYSTEM_PROMPT` is not configured, you'll see this error:

```
ValueError: SYSTEM_PROMPT must be configured in .env file.
Please add SYSTEM_PROMPT to your .env file with your desired system prompt.
See .env.example for the default prompt template.
```

**Solution:** Add `SYSTEM_PROMPT` to your `.env` file with your desired prompt.

## Testing

To verify your configuration:

```bash
python test_system_prompt.py
```

This will:
- Check if `SYSTEM_PROMPT` is set in environment
- Display the prompt that will be used
- Provide recommendations

## Default Prompt Template

The default template in `.env.example`:

```
You are an AI HR Assistant for TechnoSphere India Private Limited. Your role is to provide accurate, helpful, and professional answers to employee questions about company HR policies and procedures. Guidelines: Base your answers ONLY on the provided context from company policy documents. Be clear, concise, and professional in your responses. If the context doesn't contain enough information to answer the question, say so honestly. Use a friendly but professional tone appropriate for workplace communication. When citing policies, be specific about policy names if mentioned in the context. If asked about topics not covered in the policies, politely indicate that you can only answer questions about company HR policies. Format your answers in a well-structured, easy-to-read manner. For numerical information (like leave days, benefits), be precise and accurate.
```

## Customization Examples

See [SYSTEM_PROMPT_GUIDE.md](SYSTEM_PROMPT_GUIDE.md) for detailed customization examples including:
- Formal tone
- Friendly tone
- Multilingual support
- Compliance-focused
- Detailed with citations

## Files Modified

1. [rag/rag_pipeline.py](rag/rag_pipeline.py) - Removed hardcoded default, added error handling
2. [.env](.env) - Added SYSTEM_PROMPT configuration
3. [.env.example](.env.example) - Added SYSTEM_PROMPT with clear documentation
4. [SYSTEM_PROMPT_GUIDE.md](SYSTEM_PROMPT_GUIDE.md) - Updated to reflect required configuration

## Support

For questions:
1. Check [SYSTEM_PROMPT_GUIDE.md](SYSTEM_PROMPT_GUIDE.md) for customization help
2. Run `python test_system_prompt.py` to verify configuration
3. See [README.md](README.md) for general configuration help
