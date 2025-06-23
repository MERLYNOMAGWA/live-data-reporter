from astronauts import get_astronauts
from iss_tracker import get_iss_location
from news import get_news

def main():
   while True:
      print("\n=== Live Data Reporter ===")
      print("1. View astronauts in space")
      print("2. Track ISS location")
      print("3. View top 3 U.S. business news headlines")
      print("4. Exit")

      try:
         choice = input("Choose an option: ")
         if choice == "1":
            get_astronauts()
         elif choice == "2":
            get_iss_location()
         elif choice == "3":
            get_news()
         elif choice == "4":
            print("Goodbye! 👋")
            break
         else:
            print("Invalid input. Please enter a number from 1 to 4.")
            
      except Exception as e:
         print("An error occurred while processing your request.")
         print(f"Details: {e}")

if __name__ == "__main__":
   main()