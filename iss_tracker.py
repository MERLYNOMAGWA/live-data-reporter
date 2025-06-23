import requests
from datetime import datetime
import turtle

def get_iss_location():
   try:
      response = requests.get("http://api.open-notify.org/iss-now.json")
      response.raise_for_status()
      data = response.json()
      
      position = data["iss_position", {}]
      latitude = position["latitude", "unknown"]
      longitude = position["longitude", "unknown"]
      
      with open("data/iss_data.txt", "a") as file:
         file.write(f"\n\nISS Location as of {datetime.now()}:\n")
         file.write(f"Latitude: {latitude}, Longitude: {longitude}\n")
      
      
      log_action("ISS position fetched", True)
      print(f"Current ISS Location -> Latitude: {latitude}, Longitude: {longitude}")
      
   except Exception as e:
      log_action(f"Failed to fetch ISS location: {e}", False)
      print("Could not get ISS position.")
      
def track_iss_on_map(latitude, longitude):
   try:
      screen = turtle.Screen()
      screen.title("ISS Tracker")
      screen.setup(width= 250, height= 250 )
      screen.bgpic("images/map.gif")
      screen.setworldcoordinates(-180, -90, 180, 90)

      iss = turtle.Turtle()
      screen.register_shape("images/iss.gif")
      iss.shape("images/iss.gif")
      iss.penup()
      iss.goto(float(longitude), float(latitude))

      screen.mainloop()
   except Exception as e:
      print("Could not display ISS on map.")
      log_action(f"Failed to display ISS map: {e}", False)
      
def log_action(message, success):
   with open("logs.txt", "a") as log_file:
      status = "SUCCESS" if success else "FAILURE"
      log_file.write(f"{datetime.now()} - {status}: {message}\n")
