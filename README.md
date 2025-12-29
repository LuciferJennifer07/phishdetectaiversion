# 🧠 PhishDetect AI (Phish Guard v2)

PhishDetect AI (also referred to as **Phish Guard v2**) is an AI-powered cybersecurity tool designed to detect phishing emails using a **Transformer-based NLP model (BERT)** combined with **rule-based heuristics**.  
The project is built as a **real-world, hackathon-ready cybersecurity product**, not just a demo or keyword-based script.

---

## 🚀 Features

- 🔐 **Secure Email Fetching (IMAP)**
  - Connects to Gmail and other IMAP-supported email providers
  - Uses **App Passwords** for secure authentication

- 🤖 **AI-Powered Phishing Detection**
  - Uses a **BERT-based transformer model**
  - Understands **context and intent**, not just keywords
  - Can detect **new and unseen phishing words**

- 🧠 **Hybrid Detection Engine**
  - AI (semantic understanding) + rule-based heuristics
  - More accurate and robust than keyword-only systems

- 📊 **Explainable Output**
  - Shows phishing confidence score
  - Displays AI score + heuristic score

- 🖥️ **Clean Streamlit Dashboard**
  - Modern UI for easy demo and analysis

- 🏗️ **Clean & Modular Architecture**
  - Separate folders for AI, rules, email fetching, and UI

---

## ▶️ Setup & Run Instructions

### Create & Activate Virtual Environment (Recommended)

#### Windows
```bash
python -m venv venv
venv\Scripts\activate

**
Install Dependencies**
pip install -r requirements.txt

Run the Application
python -m streamlit run app.py


