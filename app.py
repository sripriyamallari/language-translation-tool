import streamlit as st
import requests

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌐"
)

st.title("🌐 Language Translation Tool")
st.write("Translate text between different languages")

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
    "Chinese": "zh",
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
    placeholder="Type your text here..."
)

if st.button("🔄 Translate"):

    if not text.strip():
        st.warning("Please enter some text.")

    else:
        source_code = languages[source]
        target_code = languages[target]

        if source_code == target_code:
            translated = text

        else:
            try:
                url = "https://api.mymemory.translated.net/get"

                params = {
                    "q": text,
                    "langpair": f"{source_code}|{target_code}"
                }

                response = requests.get(
                    url,
                    params=params,
                    timeout=15
                )

                data = response.json()

                translated = data["responseData"]["translatedText"]

            except Exception:
                translated = "Translation failed. Please try again."

        st.subheader("✅ Translated Text")
        st.text_area(
            "Translated Text",
            translated,
            height=150
        )
        