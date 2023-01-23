#Open the weather_data.csv User .readlines() to create a list named data that contains the values from the .csv file
# with open("./weather_data.csv") as file:
# data = file.readlines()

# print(data)

# import csv

# with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

# import pandas as pd
# from statistics import mean
# data = pd.read_csv("weather_data.csv")

# Convert temp series to list and find the mean temp

#temp_list = data["temp"].to_list()
#mean_temp = mean(temp_list)

# Get data in columns
#print(data["condition"])
# print(data.condition)

# Get data in rows
# print(data[data["temp"] == data["temp"].max()])

# Convert monday's temperature to farenheit
# Get monday's temperature
# print(data[data.day == "Monday"].temp * 9/5 + 32)

# Create data frame from scratch
# data_dict = {
#    "studens": ["Amy", "James", "Angela"],
#    "scores": [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)
# print(data)
import pandas as pd

data = pd.read_csv("squirrels.csv")

print(data.groupby(["Primary Fur Color"])["Primary Fur Color"].count().to_csv("squirrels_colors.csv"))

