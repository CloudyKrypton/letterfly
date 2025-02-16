import asyncio
from bs4 import BeautifulSoup
import googletrans
from googletrans import Translator

def detect_lang(text):
    translator = Translator()

    async def detect(text):
        return await translator.detect(text)

    return asyncio.run(detect(text)).lang

def translate_html(html, target_lang):
    soup = BeautifulSoup(html, 'html.parser')
    translator = Translator()

    async def translate_text(text):
        return await translator.translate(text, dest=target_lang)
    
    async def process_translation():
        for element in soup.find_all(string=True):
            translated = await translate_text(element)
            element.replace_with(translated.text)
        return str(soup)

    return asyncio.run(process_translation())  # Run the async function

if __name__ == "__main__":
    html = "<p>[Write&nbsp;<strong>your&nbsp;</strong>letter&nbsp;<em>here</em>~]</p><p></p>"
    translated_html = translate_html(html, 'ja')
    print(translated_html)
    print(detect_lang(translated_html))
    print(detect_lang(html))
    langs = googletrans.LANGUAGES
    for key in langs:
        langs[key] = langs[key].split(' ')[0].capitalize()

    reversed_langs = {value: key for key, value in langs.items()}
    print(reversed_langs)
