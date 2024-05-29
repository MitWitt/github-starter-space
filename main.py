import random

print("Tervetuloa hirsipuupeliin!")
print("Pelin tarkoitus on arvata sana, joka on valittu satunnaisesti.")
print("Pelin sanat ovat hedelmiä suomenkielellä.")
print("---------------------------------------------------------------")

sanapankki = ["appelsiini", "omena", "banaani", "kirsikka", "sitruuna", "päärynä", "granaattiomena", "mango", "ananas"]
randomSana = random.choice(sanapankki)

for x in randomSana:
    print("_", end=" ")

def print_hirsipuu(wrong):
    if wrong == 0:
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 1:
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 2:
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif wrong == 3:
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif wrong == 4:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif wrong == 5:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif wrong == 6:
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")

def printSana(arvatutMerkit):
    laskuri = 0
    oikeatMerkit = 0
    for merkki in randomSana:
        if merkki in arvatutMerkit:
            print(merkki, end=" ")
            oikeatMerkit += 1
        else:
            print("_", end=" ")
        laskuri += 1
    return oikeatMerkit

def printViivat():
    print("\r")
    for merkki in randomSana:
        print("\u203E", end=" ")

sanan_pituus = len(randomSana)
virheiden_maara = 0
nykyiset_arvatut_merkit = []
nykyiset_oikeat_merkit = 0

while virheiden_maara < 6 and nykyiset_oikeat_merkit != sanan_pituus:
    print("\nTähän asti arvattuja merkkejä: ")
    for merkki in nykyiset_arvatut_merkit:
        print(merkki, end=" ")

    arvaus = input("\nArvaa merkki: ").lower()

    if arvaus in nykyiset_arvatut_merkit:
        print("Olet jo arvannut tämän merkin.")
    elif arvaus in randomSana:
        nykyiset_arvatut_merkit.append(arvaus)
        nykyiset_oikeat_merkit = printSana(nykyiset_arvatut_merkit)
        printViivat()
    else:
        virheiden_maara += 1
        nykyiset_arvatut_merkit.append(arvaus)
        print_hirsipuu(virheiden_maara)
        nykyiset_oikeat_merkit = printSana(nykyiset_arvatut_merkit)
        printViivat()

if nykyiset_oikeat_merkit == sanan_pituus:
    print("\nOnnittelut! Arvasit sanan oikein:", randomSana)
else:
    print("\nPeli päättyi. Oikea sana oli:", randomSana)
    print("Kiitos pelaamisesta!")
