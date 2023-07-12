import random
import time


def machine_and_guess(): 
    global hak 
    hak = can  
    sayac = 0
    word_picked = random.choice(word_box)
    print("\n")
    print("Kelime makine tarafından seçildi!")
    chance = int(1/len(word_box) * 100) 
    print(f"Doğru kelimeyi bilme şansınız : {chance}")
    print("\n")
    sure_baslatma()
    while hak > 0:
        your_guess = input("Tahmininiz ===> ").strip().lower().title()
        if your_guess == word_picked:
            print(f"Tebrikler, {sayac+1}. denemede doğru kelimeyi bildiniz!")
            print("\n")
            sure_bitimi()
            sure_hesaplama(gecen_zaman)
            break 
        else:
            print(f"Yanlış, {hak-1} hakkınız kaldı.")
            print("\n")
        sayac += 1
        hak -= 1    
    if hak == 0 :
        print(f"Oyun bitti! Seçilen kelime : {word_picked} ")
        print("\n")
        sure_bitimi()
        sure_hesaplama(gecen_zaman)


def sure_baslatma():
    global start
    start = time.time()


def sure_bitimi():
    global bitis
    global gecen_zaman
    bitis = time.time()
    gecen_zaman = bitis - start


def sure_hesaplama(gecen_zaman):
    gecen_zaman = bitis - start
    mins = int(gecen_zaman) // 60
    hour = int(mins) // 60
    print(f"Geçen süre ==> {int(hour)}sa:{int(mins)}dk:{int(gecen_zaman)}sn")


def hak_belirleme():
    global can
    print("\n")
    print("Kaç hakta bilmek istiyorsun:")
    try:
        can = int(input("====>"))
    except ValueError:
        print("Hak bilgisi doğru girilmedi.(İPUCU: Sayı ile girmeyi dene.)")
        hak_belirleme()


def user_interface():
    global box
    global word_box  
    box = input("Kelimelerini Gir ====> ")
    word_box = box.lower().title().strip().split(" ")
    for i in word_box:
        if i == "":
            print("KELİME YAZAR MISIN LÜTFEN!")
            user_interface()
        elif i.isnumeric() == True :
            print("SAYI DEĞİL KELİME YAZACAKSIN!")
            user_interface()
        elif word_box.count(i) > 1:
            print("Aynı kelimeyi birden fazla yazdınız.")
            user_interface()


def security_check ():
    hak = can 
    for i in word_box:        
        if len(word_box) < hak+1:      #BUG DETECTED: YAZILAN KELİMELERİN BİR FAZLASI KADAR HAK YAZILINCA PROGRAM ÇALIŞIYOR FAKAT DOĞRU HAK BİLGİSİ DOĞRU ŞEKİLDE GİRİNE GENE FAZLA OLARAK ALGILIYOR.
            print("Yazdığınız hak sayısı, yazdığınız kelimelerin sayısından büyük olamaz!")
            hak_belirleme()
        else:
            print(f"Kelimeleriniz : {word_box}")
            machine_and_guess()
            break


txt = "" 
print("\n\n")
print(txt.center(30,"*"))
print("KELİME TAHMİN OYUNUMA HOŞ GELDİNİZ!")
print("KURALLAR BASİT:\nKELİME YAZ\nKAÇ HAKTA BİLMEK İSTEDİĞİNİ YAZ\nVE OYUNUN TADINI ÇIKAR!\n\nOyunu tasarlayan : cemsettin\nDiscord : YawHeHe #5790")
print(txt.center(30,"*"))
print("\n")


user_interface()
hak_belirleme()
security_check()

#use await for proper design 