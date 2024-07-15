import streamlit as st
from transcript import get_transcript
from transformers import pipeline
# ---------------------------------------------------------------------------- 
st.header("Video Summarizer �")
full_yt = st.text_input("Enter video link", "")
if st.button("Get Summary"):
    video_id = full_yt.split("=")[1]
    get_transcript(video_id)
    with open("ms_kitco.txt", "r") as f:
        tx = f.read()
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    x3 = summarizer(tx[:2000], max_length=2300)
    res = x3[0]["summary_text"]
    st.write(res)
