triangular_list = []

natural_numbers_list = []
number = 0
new_number = 0
iteration = 0

while iteration < 100:
	number +=1
	natural_numbers_list.append(number)
	#triangular_list.append(natural_numbers_list[len(natural_numbers_list)-1]+triangular_list[len(triangular_list)-1])
	for item in natural_numbers_list:
		new_number += item
		#print(new_number)
	#triangular_list.append(new_number+triangular_list[len(triangular_list)-1])
	triangular_list.append(new_number)
	iteration +=1
	new_number = 0

# for item in natural_numbers_list:
# 	print(item)

# for item in triangular_list:
# 	print(item)
