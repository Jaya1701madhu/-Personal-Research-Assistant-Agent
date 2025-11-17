import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
client=Groq(api_key=os.getenv("Groq_API_KEY"))
def summarize_text(text):
    prompt=f"summarize this research paper in bullet points:\n\n{text}\n\nSummary"
    resopnse=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":prompt}]
    )
    return resopnse.choices[0].message.content