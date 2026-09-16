import streamlit as st
import requests
from gtts import gTTS
import tempfile

# -----------------------------
# Language list
# -----------------------------
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Marathi": "mr",
    "Bengali": "bn",
    "Gujarati": "gu",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Korean": "ko",
    "Arabic": "ar"
}

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# Styling
# -----------------------------
st.markdown("""
<style>
.stButton > button {
    width: 100%;
    border-radius: 10px;
    font-size: 18px;
    font-weight: bold;
}

textarea {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.title("🌍 AI Language Translator")
st.subheader("Translate text instantly between multiple languages")

# -----------------------------
# Input
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    text_input = st.text_area(
        "📝 Enter Text",
        placeholder="Type your text here...",
        height=180
    )

    source_language = st.selectbox(
        "🌐 Source Language",
        list(languages.keys()),
        index=0
    )

with col2:
    target_language = st.selectbox(
        "🎯 Target Language",
        list(languages.keys()),
        index=1
    )

# -----------------------------
# Translation function
# -----------------------------
def translate_text(text, source, target):
    api_key = st.secrets["GOOGLE_TRANSLATE_API_KEY"]

    url = "https://translation.googleapis.com/language/translate/v2"

    params = {
        "key": api_key
    }

    data = {
        "q": text,
        "source": source,
        "target": target,
        "format": "text"
    }

    response = requests.post(
        url,
        params=params,
        json=data,
        timeout=30
    )

    response.raise_for_status()

    result = response.json()

    return result["data"]["translations"][0]["translatedText"]


# -----------------------------
# Translate button
# -----------------------------
if st.button("🔄 Translate", type="primary"):

    if not text_input.strip():

        st.warning("⚠️ Please enter some text.")

    elif source_language == target_language:

        translated_text = text_input

        st.success("✅ Translation completed!")

        st.text_area(
            "✨ Translated Text",
            translated_text,
            height=180
        )

    else:

        try:

            with st.spinner("Translating..."):

                translated_text = translate_text(
                    text_input,
                    languages[source_language],
                    languages[target_language]
                )

            st.success("✅ Translation completed!")

            st.text_area(
                "✨ Translated Text",
                translated_text,
                height=180
            )

            # -----------------------------
            # Text-to-Speech
            # -----------------------------
            try:

                tts = gTTS(
                    text=translated_text,
                    lang=languages[target_language]
                )

                audio_file = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".mp3"
                )

                tts.save(audio_file.name)

                st.audio(audio_file.name)

            except Exception:
                st.info("🔊 Audio is not available for this language.")

        except requests.exceptions.HTTPError as e:

            st.error(
                "❌ Translation API error. "
                "Please check your Google Cloud API key and API setup."
            )

        except Exception as e:

            st.error(
                "❌ Translation error: " + str(e)
            )


# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption(
    "AI Language Translation Tool | "
    "Built with Python, Streamlit & Google Cloud Translation"
)
    
        