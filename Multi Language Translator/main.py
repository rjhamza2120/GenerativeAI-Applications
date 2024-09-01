from transformers import MarianMTModel, MarianTokenizer
import sentencepiece  
import gradio as gr

def translate_text(text, source_lang='en', target_lang='fr'):
    # Prepare the text for translation
    model_name = f'Helsinki-NLP/opus-mt-{source_lang}-{target_lang}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Tokenize the input text and translate
    tokenized_text = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated_tokens = model.generate(**tokenized_text)
    translated_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)

    return translated_text[0]

# Update the translation_app function to use translate_text
def translation_app(text, source_language, target_language):
    translated_text = translate_text(text, source_language, target_language)
    return translated_text

iface = gr.Interface(
    fn=translation_app,
    inputs=[
        gr.Textbox(label="Input Text"),
        gr.Dropdown(choices=['en', 'fr', 'de', 'es'], label="Source Language"),
        gr.Dropdown(choices=['en', 'fr', 'de', 'es'], label="Target Language")
    ],
    outputs=gr.Textbox(label="Translated Text"),  # Ensure the output is a gr.Textbox
    title="AI-Powered Translation Service"
)

iface.launch()
