import requests
import feedparser
import urllib.parse
def fetch_arxiv(query,max_results=3):
    url=f"https://export.arxiv.org/api/query?search_query=all:{urllib.parse.quote(query)}&start=0&max_results={max_results}"
    print("the url of arvix is",url)
    resopnse=requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
    if(resopnse.status_code!=200):
        print("error to fetch from arvix")
        return []
    feed=feedparser.parse(resopnse.content)
    papers=[]
    for entry in feed.entries:
        pdf_url=next((link.href for link in entry.links if link.type=="application/pdf" ),"")
        papers.append({
            "title":entry.title,
            "summary":entry.summary,
            "published":entry.published,
            "pdf_url":pdf_url

        })
    return papers
