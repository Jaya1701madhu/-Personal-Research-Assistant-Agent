from src.agent import research_agent
if __name__=="__main__":
    topic=input("enter you search topic")
    report=research_agent(topic)
    for r in report:
        print("\n------------------------------")
        print("Title:",r["title"])
        print("published on",r["published"])
        print("PDF:",r["pdf_url"])
        print("SUMMARY:\n",r["ai_summary"])
        print("\n------------------------------")

