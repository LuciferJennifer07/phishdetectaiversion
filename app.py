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

# ------------------ Info Section ------------------
with st.expander("ℹ️ How it Works"):
    st.markdown("""
    - Uses **BERT-tiny** model fine-tuned for spam detection.  
    - Combines AI output (probability) + keyword-based **heuristics**.  
    - Emails scoring above 0.7 are flagged as **Phishing**.  
    - Lower scores are treated as **Legit**.  
    - Works offline after model download.  
    - Use **App Passwords** for Gmail for better security.
    """)
    st.markdown("Developed by Yuvraj Tyagi.")


st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background: linear-gradient(90deg, #0f2027, #203a43, #2c5364);
            color: white;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
            font-family: 'Segoe UI', sans-serif;
            z-index: 9999;
        }
        .footer a {
            color: #00c3ff;
            text-decoration: none;
            font-weight: 600;
        }
        .footer a:hover {
            color: #ffffff;
            text-decoration: underline;
        }
    </style>

    <div class="footer">
        🧠 <b>PhishDetect </b> | 
        Built with <b>BERT NLP + Streamlit</b> | 
        Developed by <a href="https://github.com/LuciferJennifer07" target="_blank">Yuvraj Tyagi</a> |
        <a href="https://in.linkedin.com/in/yuvraj-tyagi-486a0b306" target="_blank">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
)
