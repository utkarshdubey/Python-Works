import random
text = [1, 2]
text_length = len(text)

while (text_length < 25):
	random_number = str(int(random.randint(0, 50)))
	text += random_number
	print(text_length)

print('Bethhe length ye hai -> ' + str(text_length))
print(text)

print('The length of the text ' + str(text_length))

# text_sum = 0
# for i in range(0,50):
# 	text_sum += int(text[i])
# print(text_sum)