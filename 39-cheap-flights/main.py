#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager

dm = DataManager()
sheet_data = dm.get_data()
print(sheet_data)