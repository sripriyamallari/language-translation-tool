import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌐"
)

st.title("🌐 Language Translation Tool")
st.write("Translate text between different languages.")

languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Arabic": "ar",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko"
}

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

text = st.text_area(
    "📝 Enter Text",
    placeholder="Type your text here...",
    height=150
)

if st.button("🔄 Translate", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some text.")

    elif source == target:
        st.subheader("✅ Translated Text")
        st.text_area("Result", text, height=150)

    else:
        try:
            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.subheader("✅ Translated Text")
            st.text_area("Result", translated, height=150)

        except Exception as e:
            st.error("Translation failed. Please try again.")
