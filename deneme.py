from textblob import TextBlob
import pandas as pd

metin = ["benim adım Tunahan Yalçın",
         "keman çalmak ve spor yapmayı severim",
         "bu ürün çok kötü"]

from googletrans import Translator
from textblob import TextBlob

translator = Translator()

metin= ["benim adım Tunahan Yalçın.",
        "keman çalmayı ve spor yapmayı severim.",
        "bu ürün çok kötü."]

for yazi in metin:
    blob1 = TextBlob(yazi)
    # TextBlob'u string olarak alıp googletrans ile çevir
    blob_eng_text = translator.translate(str(blob1), dest='en').text
    
    # Çevirilen metni tekrar TextBlob nesnesine çevir
    blob_eng = TextBlob(blob_eng_text)
    
    # Duygu analizini yap ve sonuçları yazdır
    print(f"Metin: {blob_eng}")
    print(f"Sentiment: {blob_eng.sentiment}")