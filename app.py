import streamlit as st
from ai.ai_classifier import ai_predict
from rules.heuristics import heuristic_score
from email_client.imap_fetcher import fetch_emails

st.set_page_config(page_title="PhishDetect AI", layout="wide")
st.title("🧠 PhishDetect AI — Explainable Phishing Detection")

imap_host = st.sidebar.text_input("IMAP Host", "imap.gmail.com")
email_user = st.sidebar.text_input("Email")
email_pass = st.sidebar.text_input("App Password", type="password")
count = st.sidebar.slider("Emails", 1, 20, 5)

if st.sidebar.button("Fetch & Analyze"):
    emails = fetch_emails(imap_host, email_user, email_pass, count)

    for e in emails:
        text = f"{e['subject']} {e['body']}"
        ai_score = ai_predict(text)
        rule_score = heuristic_score(text)

        final_score = 0.75 * ai_score + 0.25 * rule_score
        label = "🚨 Phishing" if final_score >= 0.7 else "✅ Legit"

        st.subheader(e["subject"])
        st.write(f"From: {e['from']}")
        st.write(f"Result: **{label}**")
        st.progress(final_score)
        st.caption(f"AI={ai_score:.2f} | Heuristic={rule_score:.2f}")
        st.divider()
