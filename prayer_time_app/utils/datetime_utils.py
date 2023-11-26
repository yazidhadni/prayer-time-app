from typing import Dict, List
import datetime as dt


def str_to_datetime(times: Dict[str, str]) -> Dict[str, dt.datetime]:
    """
    Convert a list of strings representing times in 'HH:MM' format to a list of datetime objects.

    Parameters:
    - times (List[str]): A list of strings representing times in 'HH:MM' format.

    Returns:
    - List[datetime]: A list of datetime objects corresponding to the input times.
    """
    dt_times = {}  # Dict to store converted datetime objects
    current_datetime = dt.datetime.now()  # Get the current date and time
    for prayer, time in times.items():
        # Parse the time string into a datetime object, ignoring the date components
        dt_time = dt.datetime.strptime(time, "%H:%M")
        # Set the year, month, and day components to the current date
        dt_time = dt_time.replace(
            year=current_datetime.year,
            month=current_datetime.month,
            day=current_datetime.day,
        )
        dt_times[prayer] = dt_time
    return dt_times


def delta_prayers(dt_times: Dict[str, dt.datetime]) -> dt.timedelta:
    # TODO: Après Isha : lorsque qu'on a 29/11 et qu'il est 23:00
    # et que la prochaine priere est le fajr du 24/11
    current_time = dt.datetime.now()
    delta_fajr = dt_times['fajr'] - current_time
    delta_dhuhr = dt_times['dhuhr'] - current_time
    delta_asr = dt_times['asr'] - current_time
    delta_maghrib = dt_times['maghrib'] - current_time
    delta_isha = dt_times['isha'] - current_time
    deltas = [delta_fajr, delta_dhuhr, delta_asr, delta_maghrib, delta_isha]
    for delta in deltas:
        if delta > dt.timedelta(0):
            return delta
    return dt.timedelta(0)


def seconds_to_hh_mm(delta_time: dt.timedelta) -> str:
    # TODO: maybe change output type
    """
    Convert a timedelta representing a duration in seconds to a formatted string 'HH:MM'.

    Parameters:
    - delta_time (timedelta): A timedelta object representing a duration in seconds.

    Returns:
    - str: A string in 'HH:MM' format representing the duration.
    """
    # Calculate hours and minutes
    hours, remainder = divmod(delta_time.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    # Format as "hour:minute"
    formatted_time = "{:02}:{:02}".format(int(hours), int(minutes))

    return formatted_time
