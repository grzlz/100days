# Calculate the average student height from a list of heights 

input_string = input("Enter student's height separated by a space:\n")

input_list = input_string.split()

input_list = [int(i) for i in input_list]

heights_sum = 0
n = 0

for i in input_list:
    heights_sum += i
    n += 1
    print(i, heights_sum, n)

print(heights_sum/n)