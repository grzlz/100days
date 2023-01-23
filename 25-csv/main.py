#Open the weather_data.csv User .readlines() to create a list named data that contains the values from the .csv file
with open("./weather_data.csv") as file:
 data = file.readlines()

print(data)