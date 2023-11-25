from typing import Any, List
import datetime as dt


def str_to_datetime(times: List[str]) -> List[dt.datetime]:
    """
    Convert a list of strings representing times in 'HH:MM' format to a list of datetime objects.

    Parameters:
    - times (List[str]): A list of strings representing times in 'HH:MM' format.

    Returns:
    - List[datetime]: A list of datetime objects corresponding to the input times.
    """
    dt_times = []  # List to store converted datetime objects
    current_datetime = dt.datetime.now()  # Get the current date and time
    for time in times:
        # Parse the time string into a datetime object, ignoring the date components
        dt_time = dt.datetime.strptime(time, "%H:%M")
        # Set the year, month, and day components to the current date
        dt_time = dt_time.replace(
            year=current_datetime.year,
            month=current_datetime.month,
            day=current_datetime.day,
        )
        dt_times.append(dt_time)
    return dt_times


def delta(dt_times: List[dt.datetime]):
    # TODO: faire tous les cas possibles notamment lorsque qu'on a 29/11 et qu'il est 23:00
    # et que la prochaine priere est le fajr du 24/11
    current_time = dt.datetime.now()
    delta = current_time - dt_times[0]
    if delta < dt.timedelta(0):
        negative = "c'est négatif"
        return negative
    return delta


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
