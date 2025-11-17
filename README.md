Personal Research Assistant Agent

This is a small project where I built a simple Research Assistant using Python.
The idea is straightforward: you enter a topic, and the script fetches related papers from arXiv and generates short summaries using the Groq LLaMA model.

I made this project as part of the OneData ML Engineer Assignment – Option 1.

## What the Project Does

Asks the user for a research topic
Searches arXiv for papers related to that topic
Collects the title, abstract, PDF link, and published date
Uses the Groq API to generate a short summary
Displays everything in a clean and readable format
Nothing complicated — just a simple workflow from fetching → summarizing → displaying.

## Project Structure

AI_RESEARCH_AGENT/
│
├── main.py
├── src/
│ └── agent.py
├── utils/
│ └── arxiv_fetcher.py
├── models/
│ └── groq_llm.py
└── venv/

## How to Run

1. Install the required packages:
   pip install -r requirements.txt

2. Create a .env file in the project folder and add your Groq API key
   GROQ_API_KEY=your_api_key_here

3. Run the program:
   python src/main.py

4. Enter a topic when prompted, for example:
   machine learning in agriculture

## Example Output

Title: Deep Learning Models for Crop Prediction
Published: 2023-08-12
PDF: https://arxiv.org/pdf/xxxx.xxxxx

Summary:

- Discusses using deep learning for crop yield prediction
- Compares different model performances
- Shows improvements over traditional methods
