a = int(input("Enter the number of rows you want: "))
for i in range(0, a+1):
    for j in range(0, i):
        print("* ", end="")
    print()