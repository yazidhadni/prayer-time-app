import datetime as dt


class Prayer:
    # TODO: change self.prayers to prayer = a prayer time
    def __init__(self, year, month, day, prayer_time, name):
        self.year = year
        self.month = month
        self.day = day
        self.prayer_time = prayer_time
        self.name = name

    def get_timestamp(self):
        hour = self.prayer_time[:2]
        minute = self.prayer_time[3:]
        return f"{self.year}-{self.month}-{self.day} {hour}:{minute}"


if __name__ == "__main__":
    prayer = Prayer(2023, 11, 19, "06:14", "fajr")
    print(prayer.get_timestamp(prayer))
