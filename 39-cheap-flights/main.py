#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

dm = DataManager()
fs = FlightSearch()

sheet_data = dm.get_data()
# fs.get_code(sheet_data)
# dm.upload_data(sheet_data)
fs.get_prices(sheet_data)