from agents.ingestion_agent import IngestionAgent

files = ["data/cle_assignment1.pdf"]  # Use the exact name of your PDF file here
agent = IngestionAgent(trace_id="test-123")
response = agent.ingest_documents(files)

print("TYPE:", response["type"])        
print("CHUNKS:", response["payload"]["chunks"][:3])  # Print first 3 chunks only
