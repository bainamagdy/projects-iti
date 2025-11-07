import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Model Chat", page_icon="🤖", layout="centered")

st.markdown(
    """
    <style>
    .main { background-color: #f5f6fa; }
    .result-card {
        background: #fff;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
        padding: 24px 20px;
        margin-top: 20px;
        font-size: 1.1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 style='text-align: center; color: #2d3748;'>Chat with AI Model</h1>", unsafe_allow_html=True)

# API keys for each model
api_keys = {
    "ChatGPT (gpt-4o-mini)": "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",
    "Gemma": "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"
}

# Available models
model_map = {
    "ChatGPT (gpt-4o-mini)": "gpt-4o-mini",
    "Gemma": "google/gemma-2-9b-it:free"
}

# Select model
model_name = st.selectbox("Select a model:", list(model_map.keys()))

if "messages" not in st.session_state:
    st.session_state.messages = {key: [] for key in model_map.keys()}

prompt = st.text_area("Type your message here:")

if st.button("Send") and prompt:

    st.session_state.messages[model_name].append({"role": "user", "content": prompt})

    with st.spinner("Sending your message..."):
        try:
            
            if model_name == "Gemma":
                client = OpenAI(api_key=api_keys[model_name], base_url="https://openrouter.ai/api/v1")
            else:
                client = OpenAI(api_key=api_keys[model_name])

            response = client.chat.completions.create(
                model=model_map[model_name],
                messages=st.session_state.messages[model_name]
            )
            reply = response.choices[0].message.content

            st.session_state.messages[model_name].append({"role": "assistant", "content": reply})

        except Exception as e:
            st.error(f"An error occurred: {e}")

for msg in st.session_state.messages[model_name]:
    if msg["role"] == "user":
        st.markdown(f"<div class='result-card'><b>You:</b><br>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='result-card'><b>🤖 Reply:</b><br>{msg['content']}</div>", unsafe_allow_html=True)
