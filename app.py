import datetime as dt
import requests
import rumps

import helpers

rumps.debug_mode(True)


class PrayerTimesApp(rumps.App):
    def __init__(self):
        super(PrayerTimesApp, self).__init__("Prayer Times")
        self.title = "🕋"
        self.prayers = self.update_prayer_times()
        self.menu = [
            "Refresh",
            f"Fajr: {self.prayers['Fajr']}",
            f"Dhuhr: {self.prayers['Dhuhr']}",
            f"Asr: {self.prayers['Asr']}",
            f"Maghrib: {self.prayers['Maghrib']}",
            f"Isha: {self.prayers['Isha']}",
        ]
        self.quit_button = "Quit"

    @rumps.clicked("Refresh")
    def refresh(self, _):
        try:
            self.update_prayer_times()
            message = "Prayer times have been updated successfully."
        except Exception as e:
            message = f"Failed to update prayer times. Error: {e}"
        helpers.notification(message)

    def update_prayer_times(self):
        url = "http://api.aladhan.com/v1/calendarByCity"
        params = {
            "city": "Paris",
            "country": "France",
            "method": 2,
            "month": dt.datetime.now().month,
            "year": dt.datetime.now().year,
        }
        try:
            response = requests.get(url=url, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors

            data = response.json()["data"]

            # Get the current date
            today = dt.datetime.now().strftime("%d-%m-%Y")

            # Find the data for the current date
            for day_data in data:
                if day_data["date"]["gregorian"]["date"] == today:
                    timings = day_data["timings"]
                    self.prayers = {
                        "Fajr": timings["Fajr"],
                        "Dhuhr": timings["Dhuhr"],
                        "Asr": timings["Asr"],
                        "Maghrib": timings["Maghrib"],
                        "Isha": timings["Isha"],
                    }
                    break
            else:
                self.prayers = "No data for today."

            return self.prayers

        except requests.RequestException as e:
            self.prayers = f"Error fetching data: {e}"
        except ValueError as e:
            self.prayers = f"ValueError: {e}"


if __name__ == "__main__":
    PrayerTimesApp().run()
