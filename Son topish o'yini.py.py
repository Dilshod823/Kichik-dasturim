# Kompyuter bilan son topish o'yini


print("Keling o'ylagan sonni topish o'ynaymiz!")

import random

def soz_topish_oyini():
    oylangan_son = random.randint(1, 10)  
    taxminlar_soni = 0 
    
    print("Men 1 dan 10 gacha son o'yladim. O'sha sonni topa olasanmi?")

    while True:
        taxmin = int(input("Son kiriting: "))  
        taxminlar_soni += 1  
        
        if taxmin < oylangan_son:
            print("Xato! Men o'ylagan son bundan kattaroq. Yana harakat qiling:")
        elif taxmin > oylangan_son:
            print("Xato! Men o'ylagan son bundan kichikroq. Yana harakat qiling:")
        else:
            print(f"Topdingiz! {oylangan_son} sonini o'ylagan edim. {taxminlar_soni} ta taxmin bilan topdingiz.")
            print("Tabriklayman!")
            break  

# O‘yinni ishga tushirish
soz_topish_oyini()
