a = int(input("Please enter the number of times you want to print the pattern: "))

for i in range(1, a + 1):
    for j in range(i, 0, -1):
        print(j, end=""),
    print("")