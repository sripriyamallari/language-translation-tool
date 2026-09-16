import streamlit as st
import requests
from gtts import gTTS
import tempfile


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


st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="wide"
)


st.title("🌍 AI Language Translator")
st.subheader("Translate text instantly between multiple languages")


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


if st.button("🔄 Translate", type="primary"):

    if not text_input.strip():
        st.warning("Please enter some text.")

    elif source_language == target_language:
        translated_text = text_input

        st.success("Translation completed!")

        st.text_area(
            "✨ Translated Text",
            translated_text,
            height=180
        )

    else:
        try:
            url = "https://translate.googleapis.com/translate_a/single"

            params = {
                "client": "gtx",
                "sl": languages[source_language],
                "tl": languages[target_language],
                "dt": "t",
                "q": text_input
            }

            response = requests.get(
                url,
                params=params,
                timeout=15
            )

            response.raise_for_status()

            data = response.json()

            translated_text = ""

            for item in data[0]:
                if item[0]:
                    translated_text += item[0]

            if not translated_text:
                raise Exception("No translation was returned.")

            st.success("Translation completed!")

            st.text_area(
                "✨ Translated Text",
                translated_text,
                height=180
            )

            # Text-to-Speech
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

        except Exception as e:
            st.error("Translation error: " + str(e))


st.markdown("---")

st.caption(
    "AI Language Translation Tool | Built with Python, "
    "Streamlit & Google Translate"
)