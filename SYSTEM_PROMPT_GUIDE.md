# System Prompt Configuration Guide

## Overview

The HR Assistant now supports configurable system prompts that guide how the AI responds to employee questions. This allows you to customize the AI's behavior, tone, and response guidelines without modifying code.

## How It Works

The system prompt is sent to the LLM (Language Model) before every user question. It acts as "instructions" that tell the AI:
- What role it should play
- How to format responses
- What guidelines to follow
- What tone to use
- How to handle edge cases

## Configuration

### Using Environment Variables (Required)

**IMPORTANT:** The `SYSTEM_PROMPT` variable is **REQUIRED** in your `.env` file. The application will not work without it.

1. Open your `.env` file (copy from `.env.example` if you don't have one)

2. Ensure the `SYSTEM_PROMPT` variable is set:

```bash
SYSTEM_PROMPT=You are an AI HR Assistant for TechnoSphere India Private Limited...
```

3. Customize the prompt to your needs (see examples below)

4. Restart your application for changes to take effect

### Default System Prompt Template

The `.env.example` file includes this default template that you can customize:

```
You are an AI HR Assistant for TechnoSphere India Private Limited. Your role is to provide accurate, helpful, and professional answers to employee questions about company HR policies and procedures.

Guidelines:
- Base your answers ONLY on the provided context from company policy documents
- Be clear, concise, and professional in your responses
- If the context doesn't contain enough information to answer the question, say so honestly
- Use a friendly but professional tone appropriate for workplace communication
- When citing policies, be specific about policy names if mentioned in the context
- If asked about topics not covered in the policies, politely indicate that you can only answer questions about company HR policies
- Format your answers in a well-structured, easy-to-read manner
- For numerical information (like leave days, benefits), be precise and accurate
```

## Customization Examples

### Example 1: More Formal Tone

```bash
SYSTEM_PROMPT=You are an official HR Policy Advisor for TechnoSphere India Private Limited. Provide precise, formal answers based strictly on company policy documents. Always maintain a professional and authoritative tone. If information is not in the provided context, state this clearly and direct employees to contact HR directly.
```

### Example 2: Friendly and Conversational

```bash
SYSTEM_PROMPT=Hi! I'm your friendly HR Assistant at TechnoSphere India. I'm here to help you understand our company policies in a clear and approachable way. I'll answer your questions based on our official policy documents, using simple language and examples where helpful. If I don't have the information you need, I'll let you know and suggest who to contact for help!
```

### Example 3: Multilingual Support

```bash
SYSTEM_PROMPT=You are a multilingual HR Assistant for TechnoSphere India Private Limited. Respond in the language used by the employee (English, Hindi, etc.). Provide accurate information from company policy documents. Be professional, clear, and culturally sensitive in all responses.
```

### Example 4: Compliance-Focused

```bash
SYSTEM_PROMPT=You are a Compliance-Focused HR Assistant for TechnoSphere India Private Limited. Your primary goal is to ensure employees understand policies correctly to maintain regulatory compliance. Always cite specific policy names and sections. If any question relates to legal matters, advise the employee to consult with the Legal/HR department. Never make assumptions or provide advice outside the written policies.
```

### Example 5: Detailed with Citations

```bash
SYSTEM_PROMPT=You are an HR Policy Expert for TechnoSphere India Private Limited. When answering questions:
1. Always cite the specific policy document name
2. Quote relevant sections when possible
3. Explain complex policies in simple terms
4. Provide examples to illustrate policy applications
5. If multiple policies are relevant, explain each one
6. For numerical data (days, amounts), always be precise
7. If the policy has exceptions or special cases, mention them
8. Maintain a helpful and professional tone throughout
```

## Best Practices

### ✅ Do's

- **Be specific** about the AI's role and responsibilities
- **Include guidelines** for handling uncertain situations
- **Specify the tone** you want (formal, friendly, professional, etc.)
- **Mention context boundaries** (e.g., "only from policy documents")
- **Include formatting instructions** if you want structured responses
- **Test your prompt** with various questions to ensure it works as expected

### ❌ Don'ts

- **Don't make it too long** - Keep it focused and concise (under 500 words)
- **Don't include contradictory instructions** - Be clear and consistent
- **Don't use special characters** that might break environment variable parsing
- **Don't include sensitive information** in the prompt itself
- **Don't make assumptions** about what the AI "should know" - be explicit

## Tips for Writing Effective System Prompts

1. **Start with Role Definition**: Clearly state what the AI is (e.g., "You are an HR Assistant...")

2. **Add Behavioral Guidelines**: List specific do's and don'ts
   - "Always cite sources"
   - "Never make assumptions"
   - "If unsure, say so"

3. **Specify Response Format**: How should answers be structured?
   - "Use bullet points for lists"
   - "Start with a direct answer, then provide details"
   - "Keep responses under 200 words"

4. **Define Boundaries**: What should the AI NOT do?
   - "Only answer questions about HR policies"
   - "Don't provide legal advice"
   - "Don't make policy interpretations"

5. **Set the Tone**: What personality should the AI have?
   - "Maintain a professional but friendly tone"
   - "Be empathetic when discussing sensitive topics"
   - "Use simple, clear language"

## Testing Your System Prompt

After configuring a new system prompt:

1. **Test with simple questions**:
   - "What is the leave policy?"
   - "How many vacation days do I get?"

2. **Test edge cases**:
   - Questions outside policy scope
   - Ambiguous questions
   - Questions requiring multiple policies

3. **Verify tone and format**:
   - Check if responses match your desired style
   - Ensure formatting is consistent
   - Confirm citations are included (if requested)

4. **Iterate and refine**:
   - Adjust the prompt based on actual responses
   - Add specific guidelines for common issues
   - Remove unnecessary instructions

## Environment Variable Format

Since the system prompt is stored in an environment variable, keep these formatting tips in mind:

```bash
# Single line (recommended for .env files)
SYSTEM_PROMPT=You are an AI assistant. Guideline 1: Be helpful. Guideline 2: Be accurate.

# For multi-line prompts, use \n or keep it on one line
# Most .env parsers handle long single-line values well
```

## Troubleshooting

**Problem**: System prompt doesn't seem to be applied
- **Solution**: Ensure `.env` file is in the project root directory
- **Solution**: Restart your application after changing `.env`
- **Solution**: Check that `SYSTEM_PROMPT` variable name is correct (case-sensitive)

**Problem**: Responses are not following the prompt guidelines
- **Solution**: Make your instructions more explicit and specific
- **Solution**: Test with different phrasings of the same instruction
- **Solution**: Ensure the LLM model you're using supports system prompts well

**Problem**: Prompt is too long
- **Solution**: Focus on the most important 5-7 guidelines
- **Solution**: Remove redundant instructions
- **Solution**: Use clear, concise language

## Code References

The system prompt feature is implemented in:
- Configuration: [config_loader.py](utils/config_loader.py:88-90)
- RAG Pipeline: [rag_pipeline.py](rag/rag_pipeline.py:107-124)
- Environment Template: [.env.example](.env.example:82-87)

## Support

For questions or issues with system prompt configuration:
1. Review this guide
2. Check the [README.md](README.md) for general configuration help
3. Test with the default prompt first to ensure basic functionality
4. Refer to the code references above for implementation details
