import streamlit as st
import sys
import os
import uuid

# Setup project root path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent

# Inject custom CSS for styling
st.markdown("""
    <style>
        .chat-message {
            padding: 1rem;
            margin-bottom: 1rem;
            border-radius: 10px;
        }
        .chat-message.user {
            background-color: #e0f7fa;
            color: #006064;
        }
        .chat-message.assistant {
            background-color: #ede7f6;
            color: #4a148c;
        }
        .st-expander {
            background-color: #f3f3f3;
            border: 1px solid #ccc;
            border-radius: 8px;
        }
        html, body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(to bottom right, #f3f4f7, #ffffff);
        }
        .stFileUploader {
            border: 2px dashed #8e24aa;
            background-color: #fafafa;
            padding: 1rem;
            border-radius: 10px;
        }
        h1 {
            color: #4a148c;
            font-size: 2.5rem;
        }
        .css-1aumxhk {
            max-width: 60rem;
            margin: auto;
        }
    </style>
""", unsafe_allow_html=True)

# Page configuration
st.set_page_config(page_title="Agentic RAG Chatbot", layout="wide")
st.title("🧠 Agentic RAG Chatbot")

UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "retriever" not in st.session_state:
    st.session_state.retriever = None
if "trace_id" not in st.session_state:
    st.session_state.trace_id = str(uuid.uuid4())

# Upload files
uploaded_files = st.file_uploader("📁 Upload documents", type=["pdf", "docx", "pptx", "csv", "txt", "md"], accept_multiple_files=True)

if uploaded_files:
    with st.spinner("🔍 Processing files..."):
        saved_paths = []
        for file in uploaded_files:
            path = os.path.join(UPLOAD_DIR, file.name)
            with open(path, "wb") as f:
                f.write(file.getbuffer())
            saved_paths.append(path)

        ingestor = IngestionAgent(st.session_state.trace_id)
        chunks = ingestor.ingest_documents(saved_paths)["payload"]["chunks"]

        retriever = RetrievalAgent(st.session_state.trace_id)
        retriever.index_documents(chunks)

        st.session_state.retriever = retriever
        st.success("✅ Files processed and indexed!")

st.divider()

# Chat input
query = st.chat_input("💬 Ask a question based on your documents")

if query and st.session_state.retriever:
    with st.chat_message("user"):
        st.markdown(query)

    with st.spinner("🧠 Thinking..."):
        top_chunks = st.session_state.retriever.retrieve(query)["payload"]["retrieved_context"]
        llm = LLMResponseAgent(st.session_state.trace_id)
        response = llm.generate_response(top_chunks, query)
        answer = response["payload"]["answer"]
        sources = response["payload"].get("sources", [])

        st.session_state.chat_history.append((query, answer, sources))

    with st.chat_message("assistant"):
        st.markdown(answer)
        if sources:
            if isinstance(sources, str):
                sources = [sources]
            with st.expander("🔍 Source Chunks"):
                for i, chunk in enumerate(sources, 1):
                    st.markdown(f"**Chunk {i}:** {chunk}")

# Display chat history
for user_q, bot_a, sources in st.session_state.chat_history[:-1]:
    with st.chat_message("user"):
        st.markdown(user_q)
    with st.chat_message("assistant"):
        st.markdown(bot_a)
        if sources:
            if isinstance(sources, str):
                sources = [sources]
            with st.expander("🔍 Source Chunks"):
                for i, chunk in enumerate(sources, 1):
                    st.markdown(f"**Chunk {i}:** {chunk}")
