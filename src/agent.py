from utils.arxiv_fetcher import fetch_arxiv
from models.groq_llm import summarize_text
def research_agent(query):
    papers=fetch_arxiv(query)
    print("DEBUG: Papers fetched:", papers)
    finalreport=[]
    for paper in papers:
        summary=summarize_text(paper["summary"])
        report_section={
            "title":paper["title"],
            "published":paper["published"],
            "pdf_url":paper["pdf_url"],
            "ai_summary":summary

        }
        finalreport.append(report_section)
    return finalreport