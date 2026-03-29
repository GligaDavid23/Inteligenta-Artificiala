def genereaza_factura(nume_client, **kwargs):
    print(f"Factura pentru: {nume_client}")
    total = 0

    for produs, pret in kwargs.items():
        print(f"- {produs}: {pret} RON")
        total += pret

    print(f"Total: {total} RON")
    return total


def main():
    nume_client = input("Nume client: ").strip()
    nr_produse = int(input("Numar produse: "))
    produse = {}

    for i in range(1, nr_produse + 1):
        nume_produs = input(f"Nume produs {i}: ").strip()
        pret_produs = float(input(f"Pret pentru {nume_produs}: "))
        produse[nume_produs] = pret_produs

    genereaza_factura(nume_client, **produse)


main()
