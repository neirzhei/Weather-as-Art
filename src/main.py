import data_processor
import art_generator
import os
from PIL import Image

def display_banner():
    print("\n" + "=" * 60)
    print("   WEATHER ART GENERATOR")
    print("   Turn weather data into generative art")
    print("=" * 60)

def validate_input(prompt, min_val, max_val):
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'q':
            return 'q'
        try:
            value = int(user_input)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Value must be between {min_val} and {max_val}. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    display_banner()
    csv_path = "data/Temp_and_rain.csv"
    df = data_processor.load_data(csv_path)
    if df is None:
        return

    min_year, max_year = data_processor.get_available_years(df)
    if min_year is None:
        min_year, max_year = 1901, 2023

    print(f"\nData available from {min_year} to {max_year}")

    while True:
        print("\nEnter 'q' at any prompt to quit")
        month = validate_input("Enter month (1-12): ", 1, 12)
        if month == 'q':
            break
        year = validate_input(f"Enter year ({min_year}-{max_year}): ", min_year, max_year)
        if year == 'q':
            break

        temp, rain = data_processor.get_weather_data(df, month, year)
        if temp is not None and rain is not None:
            print(f"Average Temperature: {temp:.2f}°C, Average Rainfall: {rain:.2f}mm")
            image_path = art_generator.generate_art(temp, rain)
            if image_path:
                try:
                    Image.open(image_path).show()
                    print(f"Artwork saved as {image_path}")
                except Exception:
                    print(f"View the saved image at: {os.path.abspath(image_path)}")
            else:
                print("Failed to generate artwork.")
        else:
            print("No data found for the given month and year.")
    
if __name__ == "__main__":
    main()
