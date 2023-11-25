import datetime as dt

from scraper import extract_prayer_times


if __name__ == "__main__":
    times = extract_prayer_times()
    print(times)


##########################################################################
# def convert_dict_str_values_to_datetime(
#     original_dict: dict, format: str = "%H:%M"
# ) -> dict:
#     """
#     Converts string values representing time in the specified format to datetime objects.

#     Args:
#         original_dict (dict): A dictionary containing key-value pairs, where string values
#                               in the format '%H:%M' represent time.
#         format (str): The format of the time string. Defaults to '%H:%M'.

#     Returns:
#         dict: A new dictionary with the same keys as the input, but with string values
#               representing time converted to datetime objects.

#     Example:
#         original_dict = {'start_time': '08:30', 'end_time': '12:45'}
#         modified_dict = convert_str_values_to_datetime(original_dict)
#     """
#     # Create a copy of the original dictionary to avoid modifying it directly
#     modified_dict = original_dict.copy()

#     # Iterate through key-value pairs in the dictionary
#     for key, value in modified_dict.items():
#         # Check if the value is a string
#         if isinstance(value, str):
#             # Convert string to datetime object using the specified format
#             modified_dict[key] = dt.datetime.strptime(value, format)

#     return modified_dict

# def get_timestamp(dictionary: dict) -> str:
#     year = dictionary['year']
#     month = dictionary['month']
#     day = dictionary['day']
#     hour = dictionary['hour']
#     minute = dictionary['minute']
#     return f"{year}-{month}-{day} {hour}:{minute}"

# def replace_element_date(original_datetime: dt.datetime, element_to_replace: str) -> dt.datetime:
#     replace_dict = {
#         "year": original_datetime.year,
#         "month": original_datetime.month,
#         "day": original_datetime.day,
#         "hour": original_datetime.hour,
#         "minute": original_datetime.minute
#     }

#     if element_to_replace not in replace_dict:
#         setattr(original_datetime, element_to_replace, )

#     new_value = replace_dict.get(element_to_replace, getattr(original_datetime, element_to_replace))

#     return original_datetime.replace(**{element_to_replace: new_value})

# print(f"{replace_element_date(convert_dict_str_values_to_datetime(get_prayer_times()), 'year')=}")

# def compute_delta(datetime1, datetime2):
#     delta = datetime1 - datetime2
#     return delta
