comentariu = input("Introdu un comentariu: ").lower()

pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
negative = ["urât", "prost", "groaznic", "dezamăgitor"]

if any(cuv in comentariu for cuv in pozitive):
    print("Comentariu pozitiv!")
elif any(cuv in comentariu for cuv in negative):
    print("Comentariu negativ!")
else:
    print("Comentariu neutru.")
