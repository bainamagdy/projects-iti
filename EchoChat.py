import streamlit as st

st.set_page_config(page_title="Prompt Echo App", page_icon="💬", layout="centered")

st.markdown(
    """
    <style>
    .main {
        background-color: #f5f6fa;
    }
    .stTextInput > div > div > input {سفea
        background-color: #fff;
        border-radius: 8px;
        border: 1px solid #d1d5db;
        padding: 10px;
        font-size: 1.1rem;
    }
    .result-card {
        background: #fff;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
        padding: 24px 20px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 style='text-align: center; color: #2d3748;'>Prompt Echo App</h1>", unsafe_allow_html=True)

prompt = st.text_input("Enter your prompt:", key="prompt_input")

if prompt:
    st.markdown(
        f"<div class='result-card'><b>You entered:</b><br>{prompt}</div>",
        unsafe_allow_html=True,
    )