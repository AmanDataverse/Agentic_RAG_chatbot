from utils.mcp import create_mcp_message
import requests
import os
from dotenv import load_dotenv

load_dotenv()
class LLMResponseAgent:
    def __init__(self, trace_id):
        self.trace_id = trace_id
        self.api_key = os.getenv("GROQ_API_KEY")

    def generate_response(self, top_chunks, query):
        context = "\n".join(top_chunks)
        prompt = f"Answer the following question based on the provided context.\n\nContext:\n{context}\n\nQuestion:\n{query}\n\nAnswer:"

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-8b-8192",  # Double check this
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.5,
                "max_tokens": 1024
            }
        )

        try:
            result = response.json()

            # Debug: print entire response
            print("🔍 Raw Response from Groq:", result)

            if "choices" in result:
                answer = result["choices"][0]["message"]["content"]
            else:
                answer = "⚠️ Error: Groq API returned no answer. Check your API key, model name, or rate limits."
        except Exception as e:
            answer = f"❌ Exception occurred while calling Groq API: {str(e)}"

        return {
    "payload": {
        "answer": answer,
        "sources": context  # ✅ should be a list of strings
    }
}


