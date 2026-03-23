# ok = 0
# while ok == 0:
#     nota = int(input("Nota examen: "))
#     if 0 <= nota <= 10:
#         ok = 1
#     else:
#         print("Nota invalida! Introdu alta nota: ")
# if 0 < nota < 5:
#     print("Reexaminare")
# elif 5 <= nota <= 6:
#     print("Suficient")
# elif 7 <= nota <= 8:
#     print("Bine")
# else:
#     print("Excelent")

note_valide = list(range(1,11))
nota = int(input("Nota examen: "))

while nota not in note_valide:
    print("Nota invalida! Introdu alta nota: ")

if nota in list(range(1,5)): print("Reexaminare")
elif nota in list(range(5,7)): print("Suficient")
elif nota in list(range(7,9)): print("Bine")
else: print("Excelent")
