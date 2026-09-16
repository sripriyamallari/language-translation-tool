import gradio as gr
import requests


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


def translate_text(text, source, target):

    if not text.strip():
        return "Please enter some text."

    source_code = languages[source]
    target_code = languages[target]

    if source_code == target_code:
        return text

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

        translation = data["responseData"]["translatedText"]

        return translation

    except Exception:
        return "Translation failed. Please try again."


with gr.Blocks(
    title="Language Translation Tool"
) as demo:

    gr.Markdown(
        """
        # 🌐 Language Translation Tool

        Translate text between different languages.
        """
    )

    with gr.Row():

        source = gr.Dropdown(
            choices=list(languages.keys()),
            value="English",
            label="Source Language"
        )

        target = gr.Dropdown(
            choices=list(languages.keys()),
            value="Telugu",
            label="Target Language"
        )

    input_text = gr.Textbox(
        label="📝 Enter Text",
        placeholder="Type your text here...",
        lines=6
    )

    translate_button = gr.Button(
        "🔄 Translate",
        variant="primary"
    )

    output_text = gr.Textbox(
        label="✅ Translated Text",
        lines=6
    )

    translate_button.click(
        fn=translate_text,
        inputs=[input_text, source, target],
        outputs=output_text
    )


if __name__ == "__main__":
    demo.launch()