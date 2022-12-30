# Calculate the highest score from a list

input_string = input("Enter student's height separated by a space:\n")

input_list = input_string.split()

input_list = [int(i) for i in input_list]

max_value = 0

for i in input_list:
    if i >= max_value:
        max_value = i

print(max_value)