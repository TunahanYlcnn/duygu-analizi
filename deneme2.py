from textblob import TextBlob
from googletrans import Translator

translator = Translator()

# Örnek metinler
metinler = [
    "Bu film gerçekten harikaydı. Herkese tavsiye ederim.",
    "Bu deneyim çok kötüydü. Bir daha asla böyle bir şey yaşamak istemem.",
    "Bugün hava çok güzel, dışarı çıkıp biraz yürüyüş yapmayı düşünüyorum.",
    "Bu cihazın performansı gerçekten hayal kırıklığı yaratıyor.",
    "Müşteri hizmetleri oldukça yardımcı oldu, çok memnun kaldım."
]

# Her metin için duygu analizi yapalım
for yazi in metinler:
    # TextBlob nesnesine çevir
    #blob = TextBlob(yazi)

    blob_eng_text = translator.translate(yazi, dest='en').text
    
    blob = TextBlob(blob_eng_text)

    # Polarity ve Subjectivity değerlerini al
    duygu = blob.sentiment.polarity
    oznelik = blob.sentiment.subjectivity
    
    # Duygu analizini sonuçlara göre sınıflandır
    if duygu > 0:
        sonuc = "Olumlu"
    elif duygu < 0:
        sonuc = "Olumsuz"
    else:
        sonuc = "Nötr"
    
    # Sonuçları yazdır
    print(f"Metin: {yazi}")
    print(f"Duygu Polarity: {duygu}, Öznelik: {oznelik}")
    print(f"Sonuç: {sonuc}\n")











