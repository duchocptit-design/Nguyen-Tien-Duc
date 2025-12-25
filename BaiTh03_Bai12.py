from collections import Counter
text=input("Nhap 1 chuoi:").replace(" ","")
total=Counter(text)
print(dict(total))