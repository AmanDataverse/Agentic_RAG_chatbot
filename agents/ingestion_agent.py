import os
from utils.parser_utils import parse_document
from utils.mcp import create_mcp_message

class IngestionAgent:
    def __init__(self, trace_id):
        self.sender = "IngestionAgent"
        self.trace_id = trace_id

    def ingest_documents(self, file_paths):
        all_chunks = []

        for path in file_paths:
            print(f"Parsing file: {path}")
            file_chunks = parse_document(path)
            all_chunks.extend(file_chunks)

        return create_mcp_message(
            sender=self.sender,
            receiver="RetrievalAgent",
            type_="INGESTION_RESULT",
            trace_id=self.trace_id,
            payload={"chunks": all_chunks}
        )
