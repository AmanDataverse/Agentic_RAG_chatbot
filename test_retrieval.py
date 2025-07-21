from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent

# Ingest document
files = ["data/cle_assignment1.pdf"]
ingestor = IngestionAgent(trace_id="demo-456")
ingest_response = ingestor.ingest_documents(files)

chunks = ingest_response["payload"]["chunks"]

# Index with RetrievalAgent
retriever = RetrievalAgent(trace_id="demo-456")
index_response = retriever.index_documents(chunks)
print(index_response)

# Retrieve top chunks for a sample query
query = "What are the advantages of ADR?"
retrieval_response = retriever.retrieve(query)
print("\nTop Results:")
for chunk in retrieval_response["payload"]["retrieved_context"]:
    print("-", chunk[:200], "...")
