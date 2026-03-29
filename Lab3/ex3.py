import random


def normalize_data(data):
    if not data:
        return []

    minim = min(data)
    maxim = max(data)

    if minim == maxim:
        return [0.0 for d in data]

    return [(x - minim) / (maxim - minim) for x in data]


def main():
    data = [random.randint(1, 100) for no in range(5)]
    normalized_data = normalize_data(data)

    print("Data:", data)
    print("Normalized data:", normalized_data)


main()
