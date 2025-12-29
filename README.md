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

## 🧩 Project Architecture

phishdetect_ai/
│
├── app.py # Streamlit UI (main entry point)
│
├── ai/
│ ├── model_loader.py # Loads BERT model & tokenizer
│ └── ai_classifier.py # AI-based phishing prediction
│
├── rules/
│ └── heuristics.py # Rule-based phishing signals
│
├── email_client/
│ └── imap_fetcher.py # Fetch emails using IMAP
│
├── utils/ # Helper utilities
│
├── requirements.txt
└── README.md


