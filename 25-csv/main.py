#Open the weather_data.csv User .readlines() to create a list named data that contains the values from the .csv file
# with open("./weather_data.csv") as file:
# data = file.readlines()

# print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)