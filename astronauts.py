import requests 
from datetime import datetime

def get_astronauts():
   try:
      response = requests.get("http://api.open-notify.org/astros.json") 
      response.raise_for_status() 
      data = response.json()
      
      astronauts = data.get ("people", []) 
      with open("data/iss_data.txt", "a") as file:
         file.write(f"\n\nAstronauts in space as of {datetime.now()}:\n")
         for astronaut in astronauts:
            file.write(f"- {astronaut["name"]} on {astronaut["craft"]}\n")
      
      log_action("Astronaut data fetched successfully", True)
      
      print("Astronaut currently in space:")
      for astronaut in astronauts:
         """loops through the lists"""
         print(f"{astronaut["name"]} ({astronaut["craft"]})")
         
   except Exception as e:
      log_action(f"Failed to fetch astronauts: {e}", False)
      print("Error fetching astronaut data.")
      
def log_action(message, success):
   with open("logs.txt", "a") as log_file:
      status = "SUCCESS" if success else "FAILURE"    
      log_file.write(f"{datetime.now()} - {status}: {message}\n")
      