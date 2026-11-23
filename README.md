# FinSight AI

An AI-powered financial research platform that combines Retrieval-Augmented Generation (RAG), Google Gemini, and real-time market data to help users analyze stocks, financial reports, and market trends.

---

## Features

- AI-powered Stock Analysis
- Financial Report Analyzer (PDF)
- AI Financial Assistant (RAG + Gemini)
- Real-time Stock Price Charts
- Latest Financial News & Sentiment
- Watchlist Management
- Portfolio Dashboard
- Dark/Light Theme Support

---

## Tech Stack

- Python
- Streamlit
- Google Gemini 2.5 Flash
- LangChain
- ChromaDB
- GoogleGenerativeAIEmbeddings
- PyPDF2
- yfinance
- NewsAPI
- Plotly
- Pandas

---

## Project Structure

```
FinSightAI/
│
├── app.py
├── requirements.txt
├── assets/
├── backend/
├── data/
├── utils/
├── views/
├── chroma_db/
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/BhoomikaGarg22/FinSightAI
cd FinSightAI
```

### Create Virtual Environment

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
python -m pip install extra-streamlit-components
```

---

### Configure Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=*YOUR_SECRET_KEY*
GOOGLE_API_KEY=*YOUR_SECRET_KEY*
```

---

### Run the Application

```bash
streamlit run app.py
```

Open

```
http://localhost:8501
```

---

## Usage

1. Open the Dashboard.
2. Select a company to analyze.
3. Upload a financial report.
4. Click **Analyze Report**.
5. Ask questions in the AI Chat.
6. View News & Sentiment.
7. Manage your Watchlist.
8. Download report summaries.

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Streamlit | Frontend UI |
| Gemini 2.5 Flash | Large Language Model |
| LangChain | RAG Pipeline |
| ChromaDB | Vector Database |
| Google Embeddings | Embedding Generation |
| PyPDF2 | PDF Processing |
| yfinance | Stock Data |
| NewsAPI | Financial News |
| Plotly | Charts |

---

## Future Enhancements

- OCR for scanned PDFs
- Portfolio analytics
- Multilingual support
- Cloud deployment
- Hybrid Retrieval

---

## Team

- Bhoomika Garg (Team Leader)
- Aditi Rana
- Kritika Rana
- Kimish

---

## License

This project is developed for academic purposes as part of the Summer Internship Project (SIP).

