sayi1 = int(input("Lütfen 1. sayıyı girin:  "))
sayi2 = int(input("Lütfen 2. sayıyı girin:  "))
sayi3 = int(input("lütfen 3. sayıyı girin:  "))
sayi4 = int(input("Lütfen 4. sayıyı girin:  "))
sayi5 = int(input("Lütfen 5. sayıyı girin:  "))
sayi6 = int(input("Lütfen 6. sayıyı girin:  "))
sayi7 = int(input("Lütfen 7. sayıyı girin:  "))
sayi8 = int(input("Lütfen 8. sayıyı girin:  "))


def siralama(n):
  return (n==0)

sayilar = [sayi1 , sayi2 , sayi3 , sayi4 , sayi5 , sayi6 , sayi7 , sayi8]

sayilar.sort(key = siralama)



print (sayilar)