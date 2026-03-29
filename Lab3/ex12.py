num_patrate = {x: x * x for x in range(1, 11)}

text = "programare"
litere_aparitii = {ch: text.count(ch) for ch in set(text)}

divizori = {n: [d for d in range(1, n + 1) if n % d == 0] for n in range(1, 11)}

print(num_patrate)
print(litere_aparitii)
print(divizori)
