from bs4 import BeautifulSoup

from prayer_time_app.utils.decorators import driver_decorator
# TODO: remove datetime_utils functions
from prayer_time_app.utils.datetime_utils import *


@driver_decorator
def extract_prayer_times(driver):
    """
    Extracts prayer times from the HTML content of a webpage.

    Parameters:
    - driver: Selenium WebDriver - the WebDriver used to navigate the webpage.

    Returns:
    - times: list - a list containing the extracted prayer times, or None if the 'prayers' div is not found.
    """
    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")
    # Save the HTML content to a file
    with open(
        "/Users/yazidhadni/Desktop/info_projects/prayer_time_app/html/mawaqit.html", "w"
    ) as f:
        f.write(str(soup))
    # Find the 'prayers' div
    prayers_div = soup.find("div", class_="prayers")
    if prayers_div:
        # Find all div elements with class 'time' inside the 'prayers' div
        time_divs = prayers_div.find_all("div", class_="time")
        # Extract times from the 'time' divs
        times = [div.find("div").text for div in time_divs]
        return times
    else:
        print("\033[91mError: 'prayers' div not found.\033[0m")
        return None


def main():
    times = extract_prayer_times()
    print(times)
    dt_times = str_to_datetime(times)
    print(dt_times)
    delta_ = delta(dt_times)
    print(delta_)
    # print(seconds_to_hh_mm(delta_))


if __name__ == "__main__":
    main()

####################################################################
# def get_data(mosque_id):
#     response = requests.get("https://mawaqit.net/en/" + mosque_id)
#     try:
#         response.raise_for_status()
#     except Exception as exception:
#         print("Exception raised - %s" % exception)
#         return None

#     soup = bs4.BeautifulSoup(response.text, "html.parser")
#     with open("./mawaqit.html", "w") as f:
#         f.write(str(soup))
#     dom = etree.HTML(str(soup))
#     return dom


# def extract_varConfData(script_tag):
#     matches = re.search(r"var confData = ({.*?});", script_tag)
#     if matches:
#         confData_str = matches.group(1)
#         try:
#             confData_dict = json.loads(confData_str)

#             # Extract the "times" list
#             times_list = confData_dict.get("times", [])
#             calendar = confData_dict.get("calendar", [])
#             return times_list, calendar
#         except json.JSONDecodeError as e:
#             print(f"Error decoding JSON: {e}")
#     else:
#         raise ValueError("var confData not found in the script.")


# DOM = get_data(mosque_id="grande-mosquee-de-paris")


# def get_prayer_times():
#     script_tag = DOM.xpath("/html/body/script[1]")[0].text
#     times_list, calendar = extract_varConfData(script_tag)
#     now = datetime.datetime.now()
#     now_values = {
#         "year": now.year,
#         "month": now.month,
#         "day": now.day,
#         "hour": now.hour,
#         "minute": now.minute,
#     }
#     month = now_values["month"]
#     day = str(now_values["day"])
#     prayer_schedule = calendar[month - 1][day]
#     now_time = datetime.datetime.strptime(f"{now.hour}:{now.minute}", "%H:%M")
#     if now_time > datetime.datetime.strptime(prayer_schedule[5], "%H:%M"):
#         try:
#             prayer_schedule = calendar[month-1][day+1]
#         except KeyError:
#             prayer_schedule = calendar[month][1]
#         except IndexError:
#             prayer_schedule = calendar[1][1]
#     prayers = {
#         "time_info": now_values,
#         "fajr": prayer_schedule[0],
#         "dhuhr": prayer_schedule[2],
#         "asr": prayer_schedule[3],
#         "maghrib": prayer_schedule[4],
#         "isha": prayer_schedule[5],
#     }
#     return prayers
