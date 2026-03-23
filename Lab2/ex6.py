from random import randint

evenimente_stanga = ["Ai intalnit un lup.", "Ai gasit un rau ascuns.", "Ai auzit un cantec misterios.", "Ai descoperit o poiana fermecata."]
evenimente_dreapta = ["Ai gasit o comoara mica.", "Ai intalnit o zana.", "Ai vazut urme de dragon.", "Ai descoperit o pestera luminata."]
obiecte = ["cheie veche", "harta magica", "potiune", "moneda de aur", "sabie mica"]
inventar = []

print("Aventura in padurea magica")
print("Comenzi: stanga, dreapta, inventar, iesire")

while True:
    directie = input("\nAlege directia: ").strip().lower()

    if directie == "iesire":
        break

    if directie == "inventar":
        if len(inventar) == 0:
            print("Inventar gol.")
        else:
            print("Inventar:", ", ".join(inventar))
        continue

    if directie == "stanga":
        index_eveniment = randint(0, len(evenimente_stanga) - 1)
        eveniment = evenimente_stanga[index_eveniment]
    elif directie == "dreapta":
        index_eveniment = randint(0, len(evenimente_dreapta) - 1)
        eveniment = evenimente_dreapta[index_eveniment]
    else:
        print("Comanda invalida.")
        continue

    index_obiect = randint(0, len(obiecte) - 1)
    obiect = obiecte[index_obiect]

    print("Eveniment:", eveniment)
    print("Obiect gasit:", obiect)

    if obiect not in inventar:
        inventar.append(obiect)
    else:
        print("Obiectul era deja in inventar.")

print("\nInventarul final:")
if len(inventar) == 0:
    print("Inventar gol.")
else:
    print(", ".join(inventar))
