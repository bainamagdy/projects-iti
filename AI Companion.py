import streamlit as st
from openai import OpenAI

# Page config with custom theme
st.set_page_config(page_title="SmartChat AI", page_icon="🤖", layout="centered")

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f5f6fa;
        padding: 2rem;
    }
    .stTextInput > div > div > input {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        font-size: 1.1rem;
    }
    .chat-message {
        background: white;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .user-message {
        border-left: 5px solid #2e7af7;
    }
    .ai-message {
        border-left: 5px solid #10b981;
    }
</style>
""", unsafe_allow_html=True)

# App title
st.markdown("<h1 style='text-align: center; color: #1f2937;'>🤖 SmartChat AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6b7280;'>Your intelligent conversation partner</p>", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    css_class = "user-message" if message["role"] == "user" else "ai-message"
    st.markdown(f"""
        <div class='chat-message {css_class}'>
            <b>{'You' if message["role"] == "user" else '🤖 AI'}:</b><br>
            {message["content"]}
        </div>
    """, unsafe_allow_html=True)

prompt = st.text_input("Enter your prompt:")


if prompt:
    try:
      
        client = OpenAI(
            api_key="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"
        )

        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

        ai_reply = response.choices[0].message.content
        st.success("AI Response:")
        st.write(ai_reply)

    except Exception as e:
        st.error(f"Error: {e}")
