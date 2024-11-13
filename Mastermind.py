import os , random

Rouge = "\033[91m\u25A0\033[0m"
Jaune = "\033[93m\u25A0\033[0m"
Bleu = "\033[94m\u25A0\033[0m"
Vert = "\033[92m\u25A0\033[0m"
Blanc = "\033[97m\u25A0\033[0m"
Magenta = "\033[95m\u25A0\033[0m"

pastille_rouge  = "\033[91m\u25CF"
pastille_blanche = "\033[97m\u25CF"


color_list = [Magenta, Blanc, Vert, Bleu, Jaune, Rouge]

colors_to_find = []


for _ in range(4):
    color = random.choice(color_list)
    colors_to_find.append(color)


def print_menu():
    print("""
JEU DU MASTERMIND
Trouvez la bonne combinaison de quatre couleurs secrètes que notre 'IA' aura généré.
A chaque couleur bien positionnée, vous aurez en retour un indicateur rouge.
A chaque couleur présente mais mal positionnée, vous aurez en retour un indicateur blanc.
          
Entrez votre combinaison secrète en utilisant les chiffres des couleurs disponibles.
[1]: \033[93mJaune\033[0m [2]: \033[94mBleu\033[0m [3]: \033[91mRouge\033[0m [4]: \033[92mVert\033[0m [5]: \033[97mBlanc\033[0m [6]: \033[95mMagenta\033[0m
""")

os.system('cls')

print_menu()
print()
nb_try = 1
for _ in range(10):
    print(f"\nTour {nb_try}/10\n")
    integer_verification = ""
    counter = 0
    Question = input('Veuillez saisir vos quatre chiffres pour les couleurs : ')
    for value in Question:
        try:
            value = int(value)
            if 0 < int(value) > 6:
                print("Veuillez saisir une valeur entre 1 et 6")
                break
        except :
            print("Une des valeurs saisie n'est pas correct")
            integer_verification = 1
            break
        
        counter = counter+1



    if counter != 4:
        print("Veuillez saisir 4 chiffres")
        integer_verification = 1
    
    else:
        if integer_verification == 1:
            print(integer_verification)
        else:
            print()

            player_color = []

            for chiffre in Question:
                if int(chiffre) == 1:
                    player_color.append(Jaune)
                elif int(chiffre) == 2:
                    player_color.append(Bleu)
                elif int(chiffre) == 3:
                    player_color.append(Rouge)
                elif int(chiffre) == 4:
                    player_color.append(Vert)
                elif int(chiffre) == 5:
                    player_color.append(Blanc)
                elif int(chiffre) == 6:
                    player_color.append(Magenta)

            for colors in player_color: print(f" {colors} ", end='')
            print(" indicateur : ", end = "")
            win = 0
            red_count = 0
            white_count = 0
            player_copy = player_color[:]
            secret_copy = colors_to_find[:]

            for d in range(4):
                if player_copy[d] == secret_copy[d]:
                    red_count += 1
                    player_copy[d] = None
                    secret_copy[d] = None
                    win += 1

            for e in range(4):
                if player_copy[e] is not None and player_copy[e] in secret_copy:
                    white_count += 1
                    secret_copy[secret_copy.index(player_copy[e])] = None

            print(pastille_rouge * red_count + pastille_blanche * white_count)


            print("\033[0m")
            if win == 4 : 
                print("\033[0m")
                print(f"Bravo vous avez gagné la combinaison était bien : " , end="")
                for f in colors_to_find:
                    print(f" {f} ", end="")
                print(f" | vous avez gagné en {nb_try} essais")
                break
            nb_try = nb_try+1



input("appuyer sur entrée pour fermer la fenetre\n\n")
