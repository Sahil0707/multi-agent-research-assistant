# 📚 AI-Powered Multi-Agent Research Assistant  

An AI-powered multi-agent system designed to automate research workflows by collaborating AI agents for searching, summarizing, fact-checking, and generating research content.

---

## 📌 Problem Statement  

**Challenge:**  
Modern research processes require manually sourcing, analyzing, and summarizing large volumes of data, which is time-consuming and error-prone.

**Why AI Agents?**  
AI agents can independently handle specialized tasks and work collaboratively, improving speed, accuracy, and reducing cognitive load for human researchers.

**Unique Value of Multi-Agent Collaboration:**  
- **Task Specialization:** Different agents handle different jobs efficiently.  
- **Parallel Processing:** Multiple agents run concurrently.  
- **Cross-Verification:** Fact-checking improves accuracy.

---

## 📌 Project Description  

The project is a Multi-Agent Research Assistant where autonomous AI agents interact to handle user research queries by:

- Retrieving relevant information  
- Summarizing findings  
- Fact-checking content  
- Generating a polished response  

**How It Works:**  
1. **User Query Input**  
2. **Search Agent:** Fetches relevant online data  
3. **Summarizer Agent:** Condenses retrieved data  
4. **Fact-Checker Agent:** Validates important claims  
5. **Content Generator Agent:** Crafts a final structured response  

Agents communicate through a central controller or agent orchestrator.

---

## 📌 Tools, Libraries, and Frameworks  

- **OpenAI API (openai 1.x SDK)**  
- **LangChain**  
- **Streamlit** (for UI)
- **Python 3.11**  

---

## 📌 LLM Selection  

**Primary Model:**  
- `GPT-4o` via OpenAI API  
  _Best for summarization, reasoning, and high-quality generation._

**Free-Tier/Backup Models:**  
- Google Gemini 1.5 Pro (makersuite / google.generativeai SDK)  
- Mistral 7B / Zephyr from Hugging Face  

---

## 🛠 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Sahil0707/multi-agent-research-assistant.git
   cd solar-ai-assistant
2. Create a virtual environment and activate it:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # Mac/Linux
   .venv\Scripts\activate     # Windows
3. Install Dependencies:
   ```sh
   pip install -r requirements.txt
4. Set up your .env file(create a .env file and add your api key):
   ```sh
   OPENAI_API_KEY=your_openai_api_key
5. Run the application
   ```sh
   streamlit run streamlit_app.py

---

## 📌 Repository Structure  

```bash
multi-agent-research-assistant/
├── agents/
│   ├── data_gatherer.py
│   ├── summarizer_agent.py
│   ├── fact_checker_agent.py
│   └── report_maker.py
├── main.py
├── requirements.txt
├── orchestrator.py
├── .env
└── README.md
