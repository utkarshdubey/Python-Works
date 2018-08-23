import random

var = []
lt = len(var)
no = int (input("Enter the number of no.s you want in the list"))
for i in range(0, no):
	x = int(input("Enter a number"))
	var.append(x)
i = 0
while i < 10 - lt:
 	rn = random.randint(0,100)
 	var.append(rn)
 	i += 1

print(var)


sum_s = sum(var)
print(sum_s)