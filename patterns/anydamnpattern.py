o = int(input("Enter the value for loop: "))

for i in range(0, o+1):
	for j in range(0, i):
		print(i, end="")
	for x in range(0, i):
		print(i*"*", "" ,end="")
	print("")

for i in range(o, 0, -1):
	for j in range(i, 0, -1):
		print(i, end="")
	for x in range(0, i):
		print(i*"*", "" ,end="")
	print("")

print("\n")

for i in range(0, o+1):
	for j in range(1, i+1):
		print(j, end="")
	for x in range(1, i+1):
		print(x*"*", "" ,end="")
	print("")

for i in range(o, 0, -1):
	for j in range(1, i+1):
		print(j, end="")
	for x in range(i, 0, -1):
		print(x*"*", "" ,end="")
	print("")