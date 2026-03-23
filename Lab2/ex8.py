import time

risc = {"coreea de nord", "siria", "iran"}
suspecte = 0
momente = []

n = int(input("Cate tranzactii? "))
print("\nProcesam tranzactiile...")

for _ in range(n):
    suma_txt, tara_txt = input("Suma + tara: ").split(maxsplit=1)
    suma = float(suma_txt)
    tara = tara_txt.strip().lower()

    acum = time.time()
    momente = [t for t in momente if acum - t <= 60] + [acum]

    if tara in risc:
        verdict = "Frauduloasa (tara cu risc ridicat)"
    elif suma > 10000:
        verdict = "Suspicioasa (suma mare)"
    elif len(momente) > 3:
        verdict = "Suspicioasa (bot activ)"
    else:
        verdict = "Sigura"

    if verdict != "Sigura":
        suspecte += 1

    print(f"Tranzactie: {suma:.0f} RON din {tara_txt} -> {verdict}")

if suspecte >= 3:
    print(f"\n{suspecte} tranzactii suspecte detectate! Cont blocat.")
else:
    print(f"\nDoar {suspecte} tranzactii suspecte. Cont activ.")
