nr_pare = list(range(0,101,2))

cubes = [n**3 for n in range(1,11)]

commons = [n for n in nr_pare if n in cubes]

print(nr_pare)
print(cubes)
print(commons)