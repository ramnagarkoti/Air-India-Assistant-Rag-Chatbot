# ✈️ Air-India-Assistant-RAG-Chatbot

A **Retrieval-Augmented Generation (RAG) based AI Assistant** that answers questions about **Air India General Booking Policies** using a PDF knowledge base.

This project combines **LLMs + Vector Search (Pinecone)** to deliver accurate, context-aware responses from official policy documents.

---

## 🚀 Features

* 📄 PDF-based knowledge retrieval (Air India policies)
* 🔍 Semantic search using **OpenAI Embeddings**
* 🧠 Context-aware responses using **Groq LLM (LLaMA 3)**
* ⚡ Fast retrieval with **Pinecone Vector Database**
* 💬 Interactive UI built with **Streamlit**
* 🎯 Strict answer control (short, precise, context-only)

---

## 🧠 Architecture

```
User Query
    ↓
Streamlit UI (Frontend)
    ↓
RAG Pipeline (Backend)
    ↓
Retriever (Pinecone)
    ↓
LLM (Groq - LLaMA 3)
    ↓
Final Answer
```

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM:** Groq (LLaMA 3.1)
* **Embeddings:** OpenAI Embeddings
* **Vector DB:** Pinecone
* **Framework:** LangChain

---

## 📂 Project Structure

```
Air-India-Assistant-Rag-Chatbot/
│
├── app.py                      # Streamlit UI
├── main.py                     # RAG pipeline
├── air-india-general-booking-policies.pdf
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Air-India-Assistant-Rag-Chatbot.git
cd Air-India-Assistant-Rag-Chatbot
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
GROQ_API_KEY=your_groq_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 💡 Example Questions

* What is the minimum threshold value for issuing a single ADM in away or foreign markets?
* What is the minimum threshold value for issuing a single ADM in the Indian market?
* What happens to ADMs that are below the minimum threshold value?
* What happens if the airline cancels a flight?

---

## 🎯 Key Highlights

* Built a **real-world RAG system** using airline policy documents
* Implemented **semantic search + LLM reasoning pipeline**
* Designed **strict prompting** to avoid hallucinations
* Developed a **clean and interactive chatbot UI**

---

## 📜 License

This project is for educational purposes.

---

## 👨‍💻 Author

**Ram**
Aspiring AI Engineer

---

⭐ If you found this project useful, consider giving it a star!

<img width="1847" height="973" alt="image" src="https://github.com/user-attachments/assets/8c339c85-6ce1-4456-a7db-782455a78726" />

