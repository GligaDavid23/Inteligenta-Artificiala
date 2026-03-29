preturi = [100, None, 250, 80, None, 60]

preturi_valide = list(filter(lambda x: x is not None, preturi))
preturi_reduse = list(map(lambda x: x * 0.9, preturi_valide))

print(preturi_reduse)
