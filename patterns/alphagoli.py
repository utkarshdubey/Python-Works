import string
n = int(input("Enter the number: "))

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    for i in range(size - 1, 0, -1):
        row = ["-"] * (size * 2 - 1)
        for j in range(0, size - i):
            row[size - 1 - j] = alphabet[j + i]
            row[size - 1 + j] = alphabet[j + i]
        print("-".join(row))

    for i in range(0, size):
        row = ["-"] * (size * 2 - 1)
        for j in range(0, size - i):
            row[size - 1 - j] = alphabet[j + i]
            row[size - 1 + j] = alphabet[j + i]
        print("-".join(row))
print(print_rangoli(n))
