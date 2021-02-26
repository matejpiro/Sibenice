def oddelovnik():
    print("-"*20)

# získej písmeno a vrať ho kapitálkama
def ziskej_pismeno():
    user_guess = input("Hádej po jednom písmenu. Zadej písmeno:")
    return user_guess.upper()

# funkce která vezme písmeno, projede list a pokud najde shodu, vloží ono písmeno do "view_listu" na správné místo (dle indexu)
def prepis_pismeno(list_to_iterate,hadane_pismeno,my_list):
    for index,letter in enumerate(list_to_iterate):
        if hadane_pismeno == letter:
            my_list.insert(index,hadane_pismeno)
            del my_list[index+1]
    return my_list

def main():
    import random
    # náhodně vygeneruj slovo z listu
    list_of_possibilities = ["KRAVA","TULEN","LVOUN","PSTROS","GEPARD","GAZELA","STONOZKA","SOVA","PIZMON","PAPOUSEK","KOCKA","ZELVA","VOLAVKA",
                             "ANTILOPA","ANAKONDA","KRTEK","CHVOSTOSKOK","VELBLOUD","BARAKUDA","OVCE","VLK","PTAKOPYSK","HOVNIVAL"]
    word_to_guess = random.choice(list_of_possibilities)
    list_of_letters = list(word_to_guess)

    # hoď do hádacího listu tolik znaků "_", kolik má písmen slovo, které hádáš
    view_list = []
    for letter in list_of_letters:  # "letter" je zašeděný a nemělo by být
        view_list.append("_")
    print("Hádané slovo je nějaké zvíře. Obsahuje", len(view_list), "písmen. Máte", len(view_list) +5, "pokusů. Hrajeme bez diakritiky.") # počet pokusů je délka slova + 5

    pocitadlo_pokusu = []
    while len(pocitadlo_pokusu) < len(view_list)+6:
        prepis_pismeno(list_of_letters, ziskej_pismeno(),view_list)
        pocitadlo_pokusu.append("X")
        for letter in view_list:        # hezčí zobrazovadlo (nestiskne se list)
            print(letter," ",end="")
        print("\n","Zbývá: ",len(view_list) - len(pocitadlo_pokusu) +5, "pokus")
        if list_of_letters == view_list:
            print("SPRÁVNĚ!",word_to_guess,"! VYHRÁL JSI!")
            break
        elif len(pocitadlo_pokusu) > len(view_list)+4:
            print("PROHRÁL SI SALÁTE!")
            print("Hledané slovo bylo: ",word_to_guess)
            break
        oddelovnik()

if __name__ == "__main__":
    main()




