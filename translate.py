# read "source.txt" and export translated file.

from googletrans import Translator

translator = Translator()

with open('source.txt', 'r', encoding='utf-8') as r:
    content = r.readlines()


def translate(text_list, dest):

    for line in text_list:
        trnaslated = translator.translate(line.strip(), src='en', dest='ko')

        with open('translated.txt', 'a', encoding='utf-8') as f:
            f.write(trnaslated.text)


translate(content)


# text1 = "subscribe my channel"

# text2 = "suscríbete a mi canal"

# text3 = "kanalıma abone ol"

# t = translator.translate(text1, src='en', dest='es')
# print("Translate English to ESP : ",
#       t.text, type(t.text))

# print("Translate En to Korean : ",
#       translator.translate(text1, src='en', dest='ko'))
