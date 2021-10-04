number = 2**15

number_string = str(number)
sum = 0
for item in number_string:

    sum += int(item)
    print(item)

print(sum)
print(number)