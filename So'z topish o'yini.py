# Kampyuter bilan so'z topish o'yini

import random
from uzwords import words

def get_word():
    word = random.chooce(words)
    while '-' in word or ' ' in word:
        word = random.chooce(words)
    return word.upper()

def display(user_letters, word):
    display_letters=""
    for letter in word:
        if letter in user_letters:
            display_letters += letter
        else:
            display_letters += '-'
    return display_letters


def play():
    word = get_word()
    word_letters = set(word)
    user_letters = ''
    print(f"Men {len(word)} xonali so'z o'yladim. Topa olasizmi?")
    
    while word_letters:
        print(display(user_letters, word))
        if user_letters:
            print(f"Shu vaqtgacha kiritgan xarflaringiz: {user_letters}")
            
            letter = input("Xarf kiriting: ").upper()
            if letter in user_letters:
                print("Bu xarfni avval kiritgansiz. Boshqa xarf kiriting.")
                continue
            elif letter in user_letters:
                print(f"{letter} xarfi to'g'ri.")
            else:
                print("Bunday xarf yuq")
            user_letters += letter    
    print(f"Tabriklayman! {word} so'zini {len(user_letters)} ta topdingiz")          