# Calculate the sum of all even number from 1 to 100 including 100

acumulator = 0
for i in range(2, 101, 2):
    acumulator += i

print(acumulator)