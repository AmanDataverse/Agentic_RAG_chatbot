import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from utils.mcp import create_mcp_message

class RetrievalAgent:
    def __init__(self, trace_id):
        self.sender = "RetrievalAgent"
        self.trace_id = trace_id
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.documents = []

    def index_documents(self, chunks):
        self.documents = chunks
        embeddings = self.model.encode(chunks, show_progress_bar=True)
        dim = embeddings[0].shape[0]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

        # Save the index and documents for later use
        faiss.write_index(self.index, "db/index.faiss")
        with open("db/docs.pkl", "wb") as f:
            pickle.dump(self.documents, f)

        return create_mcp_message(
            sender=self.sender,
            receiver="LLMResponseAgent",
            type_="INDEXING_DONE",
            trace_id=self.trace_id,
            payload={"status": "success", "num_chunks": len(chunks)}
        )

    def retrieve(self, query, top_k=3):
        if not self.index:
            self.index = faiss.read_index("db/index.faiss")
            with open("db/docs.pkl", "rb") as f:
                self.documents = pickle.load(f)

        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, top_k)
        results = [self.documents[i] for i in indices[0]]

        return create_mcp_message(
            sender=self.sender,
            receiver="LLMResponseAgent",
            type_="RETRIEVAL_RESULT",
            trace_id=self.trace_id,
            payload={"retrieved_context": results, "query": query}
        )
