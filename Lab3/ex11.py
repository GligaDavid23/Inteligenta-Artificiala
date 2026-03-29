nr_pare = {x for x in range(2, 21, 2)}

text = "Ana are mere si pere"
litere_distincte = {ch for ch in text if ch != " "}

cuvinte = text.split()
cuvinte_5_litere = {c for c in cuvinte if len(c) >= 5}

print(nr_pare)
print(litere_distincte)
print(cuvinte_5_litere)
