import requests
from datetime import datetime

def get_iss_location():
   """ run anytime to get and save the ISS’s live position"""
   try:
      response = requests.get("http://api.open-notify.org/iss-now.json")
      response.raise_for_status()
      data = response.json()
      
      position = data["iss_position", {}]
      """ looks inside the data dicto and looks for value stored under iss-"""
      latitude = position["latitude", "unknown"]
      """looks for the latitude value in the position dict and prints it as a string"""
      longitude = position["longitude", "unknown"]
      
      with open("data/iss_data.txt", "a") as file:
         file.write(f"\n\nISS Location as of {datetime.now()}:\n")
         file.write(f"Latitude: {latitude}, Longitude: {longitude}\n")
      
      
      log_action("ISS position fetched", True)
      print(f"Current ISS Location -> Latitude: {latitude}, Longitude: {longitude}")
      
   except Exception as e:
      log_action(f"Failed to fetch ISS location: {e}", False)
      print("Could not get ISS position.")
      
def log_action(message, success):
   with open("logs.txt", "a") as log_file:
      status = "SUCCESS" if success else "FAILURE"
      log_file.write(f"{datetime.now()} - {status}: {message}\n")
      