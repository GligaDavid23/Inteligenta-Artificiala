alegeri = {1: "piatra", 2: "hartie", 3: "foarfeca"}

while True:
    p1 = int(input("Jucatorul 1, alege (1-piatra, 2-hartie, 3-foarfeca): "))
    p2 = int(input("Jucatorul 2, alege (1-piatra, 2-hartie, 3-foarfeca): "))

    if p1 not in alegeri or p2 not in alegeri:
        print("Alegere invalida. Folositi doar 1, 2 sau 3.")
    elif p1 == p2:
        print("Egalitate!")
    elif (p1 == 1 and p2 == 3) or (p1 == 3 and p2 == 2) or (p1 == 2 and p2 == 1):
        print(f"Jucatorul 1 castiga! ({alegeri[p1]} bate {alegeri[p2]})")
    else:
        print(f"Jucatorul 2 castiga! ({alegeri[p2]} bate {alegeri[p1]})")

    din_nou = input("Vreti sa jucati din nou? (da/nu): ").strip().lower()
    if din_nou != "da":
        print("Joc incheiat.")
        break
