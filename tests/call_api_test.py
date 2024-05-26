import datetime
import requests

# Get the current year and month
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month

url = f"http://api.aladhan.com/v1/calendarByCity/{current_year}/{current_month}"

# Define the parameters
params = {
    "city": "Paris",
    "country": "France",
    "method": 2,
    "month": datetime.datetime.now().month,
    "year": datetime.datetime.now().year,
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()["data"]

        # Get the current date
        today = datetime.datetime.now().strftime("%d-%m-%Y")

        # Find the data for the current date
        for day_data in data:
            if day_data["date"]["gregorian"]["date"] == today:
                # Print the date and times of prayers
                # print(f"Date: {day_data['date']['readable']}")
                timings = day_data["timings"]
                for prayer, time in timings.items():
                    print(f"{prayer}: {time}")
                break
        else:
            print("No data found for today's date.")
    else:
        print(f"Error: {response.status_code}")

except requests.RequestException as e:
    print(f"HTTP Request failed: {e}")
except ValueError as e:
    print(f"Error parsing JSON: {e}")
