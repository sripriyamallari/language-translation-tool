import streamlit as st
import requests

# Page settings
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Language Translation Tool")
st.write("Translate text between different languages")

# Languages
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Marathi": "mr",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Arabic": "ar",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko"
}

# Language selection
col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "From",
        list(languages.keys())
    )

with col2:
    target_language = st.selectbox(
        "To",
        list(languages.keys()),
        index=1
    )

# Text input
text = st.text_area(
    "Enter text",
    placeholder="Type your text here...",
    height=150
)

# Translation function
def translate_text(text, source, target):

    url = "https://libretranslate.com/translate"

    data = {
        "q": text,
        "source": source,
        "target": target,
        "format": "text"
    }

    response = requests.post(
        url,
        data=data,
        timeout=30
    )

    response.raise_for_status()

    result = response.json()

    return result["translatedText"]


# Translate button
if st.button("🔄 Translate", type="primary"):

    if not text.strip():

        st.warning("Please enter some text.")

    elif source_language == target_language:

        st.success("Translation completed!")

        st.text_area(
            "Translated Text",
            text,
            height=150
        )

    else:

        try:

            with st.spinner("Translating..."):

                result = translate_text(
                    text,
                    languages[source_language],
                    languages[target_language]
                )

            st.success("✅ Translation completed!")

            st.text_area(
                "Translated Text",
                result,
                height=150
            )

        except Exception as e:

            st.error("❌ Translation failed.")
            st.info(
                "The free translation server may be temporarily "
                "busy. Please try again."
            )