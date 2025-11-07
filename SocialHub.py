import streamlit as st

st.set_page_config(page_title="SocialHub", page_icon="🌐", layout="centered")

st.markdown("""
<style>
    .main { background-color: #f5f6fa; }
    .title { 
        color: #2d3748; 
        margin-bottom: 2rem;
    }
    .subtitle {
        color: #718096;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title' style='text-align: center;'>🌐 SocialHub</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle' style='text-align: center;'>Your Gateway to Social Media</p>", unsafe_allow_html=True)

social_links = {
    "Facebook": "https://facebook.com",
    "Twitter": "https://twitter.com",
    "Instagram": "https://instagram.com",
    "LinkedIn": "https://linkedin.com",
}

option = st.selectbox("Select a social media platform:", [""] + list(social_links.keys()))

if option != "":
    url = social_links[option]
    st.markdown(f"<meta http-equiv='refresh' content='0; url={url}'>", unsafe_allow_html=True)
