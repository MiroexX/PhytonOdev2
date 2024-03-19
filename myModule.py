from collections import Counter

def harf_mi(str):
    return str.isalpha()

def low(str):
    return str.lower()

def yuzdelik(txt):
    text2 = Counter(txt)
    toplam_harf = sum(text2.values())

    res = {char: {"kac_kere": count, "yuzde": count / toplam_harf * 100} for char, count in text2.items()}
    return res

def my_info():
    name = "Miraç"
    surname = "Taşkıran"
    number = "221220096"
    note = "En Büyük Fener!!!"

    print(f"Öğrenci : {name} {surname} ")
    print(f"No : {number} ")
    print(f"Note : {note} ")
