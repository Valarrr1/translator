#googletrans kütüphanesini ekledim fakat farklı versiyonunu yükledim
from googletrans import Translator

#Kullanmak istediğimiz classımızı çağırdık
translator =Translator()

#girdi alıyoruz buraya istersen kelime istersen cümle yazabilirsin
words=input("Please enter your inputs:")

#translate fonksiyonunu kullanıyoruz
out= translator.translate(words ,dest='en')

print(out.text)