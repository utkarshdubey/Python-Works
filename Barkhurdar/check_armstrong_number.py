num = int(input("Enter a number: "))  
sm = 0  
temp = num  
order = len(str(num))
while temp > 0:  
   digit = temp % 10  
   sm += digit ** order  
   temp //= 10  
  
if num == sm:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")  