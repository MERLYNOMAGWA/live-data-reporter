import requests
from datetime import datetime
import turtle

def get_iss_location():
   try:
      response = requests.get("http://api.open-notify.org/iss-now.json")
      response.raise_for_status()
      data = response.json()
      
      position = data.get("iss_position", {})
      latitude = position.get("latitude", "unknown")
      longitude = position.get("longitude", "unknown")
      
      with open("data/iss_data.txt", "a") as file:
         file.write(f"\n\nISS Location as of {datetime.now()}:\n")
         file.write(f"Latitude: {latitude}, Longitude: {longitude}\n")
      
      log_action("ISS position fetched", True)
      track_iss_on_map(latitude, longitude)
      print(f"Current ISS Location -> Latitude: {latitude}, Longitude: {longitude}")
 
   except Exception as e:
      log_action(f"Failed to fetch ISS location: {e}", False)
      print("Could not get ISS position.")
      
def track_iss_on_map(latitude, longitude):
   try:
      print("🛰️  Starting map display...")
      print(f"Placing ISS at latitude={latitude}, longitude={longitude}")
      screen = turtle.Screen()
      screen.title("ISS Tracker")
      screen.setup(width= 720, height= 360 )
      screen.bgpic("images/map.gif")
      screen.setworldcoordinates(-180, -90, 180, 90)
      screen.bgcolor("black") 

      iss = turtle.Turtle()
      try:
         screen.register_shape("images/iss.gif")
         iss.shape("images/iss.gif")
      except Exception as e:
         print("Could not load 'iss.gif'. Using default turtle shape.")
         iss.shape("turtle") 

      iss.penup()
      try:
         iss.goto(float(longitude), float(latitude))
      except ValueError:
         print(" Invalid latitude/longitude format — skipping map placement.")
         log_action("Invalid ISS coordinates", False)

      screen.mainloop()
   except Exception as e:
      print("Could not display ISS on map.")
      log_action(f"Failed to display ISS map: {e}", False)
      
def log_action(message, success):
   with open("logs.txt", "a") as log_file:
      status = "SUCCESS" if success else "FAILURE"
      log_file.write(f"{datetime.now()} - {status}: {message}\n")
