from transformers import AutoTokenizer, AutoModelForSequenceClassification
import streamlit as st

MODEL_NAME = "mrm8488/bert-tiny-finetuned-sms-spam-detection"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    id2label = model.config.id2label
    return tokenizer, model, id2label
