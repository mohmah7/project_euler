triangular_list = []

natural_numbers_list = []
list_of_list_division = []

division_list = []
number = 0
new_number = 0
iteration = 0
remainder_division = 0


length_of_division_list = 0

while length_of_division_list < 500:
	number +=1
	natural_numbers_list.append(number)
	#triangular_list.append(natural_numbers_list[len(natural_numbers_list)-1]+triangular_list[len(triangular_list)-1])
	for item in natural_numbers_list:
		new_number += item
		#print(new_number)
	#triangular_list.append(new_number+triangular_list[len(triangular_list)-1])
	triangular_list.append(new_number)
	# for item in natural_numbers_list:
	# 	remainder_division = new_number % item
	# 	if remainder_division == 0:
	# 		division_list.append(item)
	# print(division_list)
	# print(new_number)
	# print(natural_numbers_list)
	# division_list.append(new_number)
	# list_of_list_division.append(division_list)
	# division_list = []
	# remainder_division = 0

	division_number = new_number
	while division_number > 0:
		new_remander_division = new_number % division_number
		if new_remander_division == 0:
			division_list.append(division_number)
		# new_remander_division = new_number % division_number
		division_number -= 1 

	print(division_list)
	print(new_number)
	length_of_division_list = len(division_list)
	print(length_of_division_list)
	division_list =[]





	iteration +=1
	new_number = 0

# for item in list_of_list_division:
# 	print(item)

# for item in natural_numbers_list:
# 	print(item)

# for item in triangular_list:
# 	print(item)
