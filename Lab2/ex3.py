from random import randint

rand_int = randint(0,50)
ct = 0

while True:
    guess = int(input("Ghicește numărul (1-50): "))
    ct += 1
    if rand_int < guess:
        print("Numărul este mai mic!")
    elif rand_int > guess:
        print("Numărul este mai mare!")
    else:
        print(f"Felicitări! Ai ghicit numarul in {ct} incercari! ")
        break