#Author: Muammer Altunkan 
#kütüphaneler
print('https://www.instagram.com/muammer_altunkan')
import random
import string
#giriş
print('>>Hello, Welcome to Password Generator.')

#şifre uzunluğunu girme
length = int(input('\n Please enter Password length: '))                      

#Veri
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation


#veriler toplamı
all = lower + upper + num + symbols


temp = random.sample(all,length)

#şifre oluşturma
password = "".join(temp)

#şifre yazdırma
print(password)