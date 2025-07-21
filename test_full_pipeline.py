from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent

# Ingest document
files = ["data/cle_assignment1.pdf"]
trace_id = "full-001"
ingestor = IngestionAgent(trace_id)
chunks = ingestor.ingest_documents(files)["payload"]["chunks"]

# Index + retrieve
retriever = RetrievalAgent(trace_id)
retriever.index_documents(chunks)
query = "What are the advantages of ADR?"
top_chunks = retriever.retrieve(query)["payload"]["retrieved_context"]

# Generate LLM answer
llm = LLMResponseAgent(trace_id)
response = llm.generate_response(top_chunks, query)

print("💬 Answer:\n", response["payload"]["answer"])
