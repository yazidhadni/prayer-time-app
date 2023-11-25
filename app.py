#!/Users/yazidhadni/Desktop/info_projects/prayer_sync/venv/bin/python

import rumps

# import datetime as dt
# from collections import OrderedDict

from prayer_time_app.scraper import extract_prayer_times


class PrayerTime(rumps.App):
    def __init__(
        self, name, title=None, icon=None, template=None, menu=None, quit_button="Quit"
    ):
        super().__init__("PrayerTime")
        self.title = "🕋"
        # self.quit_button = 'Quit'
        self.prayers = extract_prayer_times()
        self.menu = [
            rumps.MenuItem(f"fajr {self.prayers[0]}"),
            rumps.MenuItem(f"dhuhr {self.prayers[1]}"),
            rumps.MenuItem(f"asr {self.prayers[2]}"),
            rumps.MenuItem(f"maghrib {self.prayers[3]}"),
            rumps.MenuItem(f"isha {self.prayers[4]}"),
        ]


if __name__ == "__main__":
    PrayerTime("Prayer").run()
