import os, json
import streamlit as st
from PIL import Image
from rag.rag_pipeline import RAGPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="TechnoSphere HR App", layout="wide", initial_sidebar_state="collapsed")

load_dotenv()

# Custom CSS for clean, minimal styling
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Clean header */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem 2rem;
        margin: -1rem -1rem 1rem -1rem;
        border-radius: 0 0 10px 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    /* Clean button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        border-radius: 8px;
        color: white;
        font-weight: 500;
        padding: 0.5rem 1.5rem;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }

    /* Clean message styling */
    .user-message {
        background-color: #e8f2ff;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        border-left: 4px solid #667eea;
    }

    .assistant-message {
        background-color: #f8f9fa;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        border-left: 4px solid #764ba2;
    }

    /* Style the chat input */
    .stChatInput {
        border-top: 2px solid #667eea;
    }

    /* Remove extra spacing */
    .element-container {
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'return_sources' not in st.session_state:
    st.session_state.return_sources = True

# Header with logo
logo_path = os.getenv('APP_LOGO_PATH', 'utils/logo/technospehere_logo.png')

try:
    import base64
    from io import BytesIO

    logo = Image.open(logo_path)
    buffered = BytesIO()
    logo.save(buffered, format="PNG")
    logo_base64 = base64.b64encode(buffered.getvalue()).decode()

    st.markdown(f'''
    <div class="main-header">
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <div style="display: flex; align-items: center; gap: 20px;">
                <img src="data:image/png;base64,{logo_base64}"
                     style="height: 60px; width: auto; border-radius: 6px;"
                     alt="Logo">
                <div>
                    <h1 style="color: white; font-size: 1.8rem; font-weight: 600; margin: 0;">
                        HR Assistant
                    </h1>
                    <p style="color: rgba(255,255,255,0.9); font-size: 0.9rem; margin: 0;">
                        AI-Powered HR Policy Assistant
                    </p>
                </div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
except Exception:
    st.markdown('''
    <div class="main-header">
        <h1 style="color: white; font-size: 1.8rem; font-weight: 600; margin: 0;">
            HR Assistant
        </h1>
        <p style="color: rgba(255,255,255,0.9); font-size: 0.9rem; margin: 0;">
            AI-Powered HR Policy Assistant
        </p>
    </div>
    ''', unsafe_allow_html=True)

# Top right - New Conversation button (only show if there's history)
if st.session_state.chat_history:
    col1, col2 = st.columns([5, 1])
    with col2:
        if st.button("🔄 New Chat", key="new_chat_top", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

# Sidebar for settings (collapsed by default)
with st.sidebar:
    st.title("⚙️ Settings")
    st.session_state.return_sources = st.checkbox(
        "Show source documents",
        value=st.session_state.return_sources,
        help="Display source documents with answers"
    )

    st.markdown("---")
    st.markdown("### 📊 Statistics")
    st.metric("Questions Asked", len(st.session_state.chat_history))
    st.metric("Documents Indexed", "20")

    if st.session_state.chat_history:
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

# Display conversation history
if st.session_state.chat_history:
    st.markdown("## 💬 Conversation")

    for i, (question, answer) in enumerate(st.session_state.chat_history):
        # User question - plain markdown
        st.markdown(f"**You:** {question}")

        # Assistant answer - plain markdown
        st.markdown("**Assistant:**")
        st.markdown(answer)

        # Separator between conversations
        st.markdown("---")
else:
    # Welcome message when no conversation
    st.markdown("""
    <div style="text-align: center; padding: 3rem 1rem;">
        <h2 style="color: #667eea; font-weight: 600;">👋 Welcome!</h2>
        <p style="color: #666; font-size: 1.1rem; margin-top: 1rem;">
            Ask me anything about TechnoSphere's HR policies and procedures.
        </p>
        <p style="color: #999; font-size: 0.9rem; margin-top: 0.5rem;">
            I have access to 20 HR policy documents and can help with questions about leave, benefits, remote work, and more.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Chat input at bottom (Streamlit's native fixed-bottom input)
if st.session_state.chat_history:
    placeholder = "Ask a follow-up question..."
else:
    placeholder = "Ask me about HR policies, leave, benefits, remote work..."

query = st.chat_input(placeholder=placeholder)

# Process the question
if query and query.strip():
    with st.spinner("🔍 Searching HR documents..."):
        try:
            pipeline = RAGPipeline()
            pipeline.load_vectorstore()
            result = pipeline.query(query)

            # Add to chat history
            st.session_state.chat_history.append((query, result['answer']))

            # Rerun to show updated conversation
            st.rerun()

        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("💡 Tip: Make sure documents are indexed and API keys are configured in .env file")
