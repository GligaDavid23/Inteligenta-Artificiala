from random import randint, sample

print("Bine ai venit la Loteria Python!\nAlege 6 numere între 1 și 49.")

numere_in = []
numere_valide = list(range(1,50))

numere_extrase = sample(range(1,50), 6)

while len(numere_in) < 6:
    numar = int(input(f"Numarul {len(numere_in)+1}:"))
    if numar not in list(range(1,50)):
        print("Numarul nu este valid, alege altul: ")
        continue
    if numar in numere_in:
        print("Numarul exista deja, introdu altul: ")
        continue
    numere_in.append(numar)

numere_ghicite = [numar for numar in numere_in if numar in numere_extrase]

print(f"Numere extrase: {numere_extrase}")
print(f"Ai ghicit {len(numere_ghicite)} numere!")

if 0 == len(numere_ghicite):
    print("Nu ai castigat nimic!")
elif 1 <= len(numere_ghicite) <= 3:
    print("Felicitări! Ai câștigat un premiu mic!")
elif 3 <= len(numere_ghicite) <= 5:
    print("Felicitări! Ai câștigat un premiu mare!")
else:
    print("Felicitări! Ai câștigat un premiu imens!")