import streamlit as st
import requests

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# -----------------------------------
# Language List
# -----------------------------------
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Marathi": "mr",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Arabic": "ar",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN"
}

# -----------------------------------
# Custom CSS
# -----------------------------------
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 25px;
    }

    .stButton > button {
        width: 100%;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# Title
# -----------------------------------
st.markdown(
    '<div class="main-title">🌍 AI Language Translation Tool</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Translate text between multiple languages easily</div>',
    unsafe_allow_html=True
)

# -----------------------------------
# Language Selection
# -----------------------------------
col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "🌐 From",
        list(languages.keys())
    )

with col2:
    target_language = st.selectbox(
        "🎯 To",
        list(languages.keys()),
        index=1
    )

# -----------------------------------
# Text Input
# -----------------------------------
text = st.text_area(
    "📝 Enter Text",
    placeholder="Type your text here...",
    height=180
)

# -----------------------------------
# Translation Function
# -----------------------------------
def translate_text(text, source, target):

    url = "https://api.mymemory.translated.net/get"

    params = {
        "q": text,
        "langpair": f"{source}|{target}"
    }

    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    result = response.json()

    # Check API response
    if result.get("responseStatus") != 200:
        error_message = result.get(
            "responseDetails",
            "Translation service failed."
        )
        raise Exception(error_message)

    translated_text = result.get("responseData", {}).get(
        "translatedText"
    )

    if not translated_text:
        raise Exception("No translation was returned.")

    return translated_text


# -----------------------------------
# Translate Button
# -----------------------------------
if st.button("🔄 Translate", type="primary"):

    if not text.strip():

        st.warning("⚠️ Please enter some text.")

    elif source_language == target_language:

        st.success("✅ Translation completed!")

        st.text_area(
            "✨ Translated Text",
            text,
            height=180
        )

    else:

        try:

            with st.spinner("🔄 Translating..."):

                translated_text = translate_text(
                    text,
                    languages[source_language],
                    languages[target_language]
                )

            st.success("✅ Translation completed!")

            st.text_area(
                "✨ Translated Text",
                translated_text,
                height=180
            )

        except requests.exceptions.Timeout:

            st.error(
                "❌ Translation service took too long to respond. "
                "Please try again."
            )

        except requests.exceptions.RequestException:

            st.error(
                "❌ Unable to connect to the translation service. "
                "Please try again."
            )

        except Exception as e:

            st.error(
                f"❌ Translation failed: {str(e)}"
            )

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")

st.caption(
    "AI Language Translation Tool | "
    "Built with Python, Streamlit & Translation API"
)