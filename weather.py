import csv
from datetime import datetime


DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """

    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts an ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    #datetime is library of functions. one of the functions in this library is called fromisoformat
    casted_date = datetime.fromisoformat(iso_string)

    year = casted_date.strftime("%Y")
    month = casted_date.strftime("%B")
    day = casted_date.strftime("%d")
    weekday = casted_date.strftime("%A")
    
    formatted_date = weekday, day, month, year
    #this formatted date will present itself in a tuple. A tuple means that each would be a mini list. 
    #so we want to convert the tuple into a string. 

    string_date = ' '.join(formatted_date) 
    #we can convert the tuple into a string using str.join(tuple) function.
    # str = '' - start off with an empty list
    #.join = join

    return string_date

     #okay



def convert_f_to_c(temp_in_farenheit):
    temp_in_celcius = (float(temp_in_farenheit) - 32) * (5/9)
    # print(temp_in_celcius)

    rounded_celcius_temp = float(round(temp_in_celcius,1))
    # print(rounded_celcius_temp)

    return rounded_celcius_temp
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
     #okay
 


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    # total_data = (sum(weather_data)) #this doesn't work because you can't cast a float into a list
    
    # we can do this with a for loop:
    # total_data = 0 #start of with 1
    # for data in weather_data:
    #     total_data = total_data + float(data) #tell the data to be looped to add all the items in the data.
    #     #this will allow us to specifically tell the items in this weather data list to cast it as a float.  

    #or we can a short hand for loop. 
    # result = [int(item) item in range] : this will convert every item to an interger

    #another method
    #count = 0, for numbers in weather_data: count += float(numbers)

    converted_weather_data = [float(data) for data in weather_data]
    total_data = sum(converted_weather_data)
    mean = total_data/len(converted_weather_data)

    return mean
    
    #okay

def load_data_from_csv(csv_file):
    
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    list = []
    with open(csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for line in reader:
            if line:
                list.append([line[0], float(line[1]), float(line[2])])

    return list

    #okay

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers. 
    Returns:
        The minium value and it's position in the list.
    """
    if len(weather_data) >= 1: #or you can write greater than 0
        min_data = weather_data[0] #lets start off by finding the 1st number in a list
        min_data_index = 0

        for data in range(len(weather_data)): #using range(len()) function, we make the 'data' = the index in the list
            if weather_data[data] <= min_data: #meaning less than or equal to for repeated values in the list. 
                min_data = weather_data[data]
                min_data_index = data

        return float(min_data), min_data_index

    else:
        return ()

    #what does the enumerate function?
    #tuple is a mini list with two or three things. we use paranthesis. 

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if len(weather_data) > 0:
        max_value = weather_data[0]
        value_index = 0

        for x in range(len(weather_data)):
            if  weather_data[x] >= max_value:
                max_value = weather_data[x]
                value_index = x

        return float(max_value), value_index

    else:
        return()

#okay

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    ###the amount of lists is how many days of data the overview will be for e.g. 5 lists = 5 day overview

    total_days = len(weather_data)

    ###finding the minimum temperature

    #creating a list of min and max temperatures from the data so that we can use the function
    min_temp_list = []
    max_temp_list = []
    for data in weather_data:
        min_temp_list.append(convert_f_to_c(data[1]))
        max_temp_list.append(convert_f_to_c(data[2]))

    #created a variable for the identified min temperature
    min_temp = find_min(min_temp_list)[0]

    #used the second index from the mintemp function to find which sublist it is from. 
    min_temp_index =find_min(min_temp_list)[1]

    #formatted with celcius and degree symbol
    overall_min = format_temperature(min_temp)
    #convert iso string for overall min temp 
    min_date = convert_date(weather_data[min_temp_index][0])

    #average of low temperatures
    avg_low = calculate_mean(min_temp_list)
    rounded_avg_low = round(avg_low,1)
    formatted_avg_low = format_temperature(rounded_avg_low)

    ###finding the maximum temperature
    max_temp = find_max(max_temp_list)[0]
    max_temp_index = find_max(max_temp_list)[1] 
    max_date = convert_date(weather_data[max_temp_index][0])


    overall_max = format_temperature(max_temp)

    ###average of max temperatures
    avg_max = calculate_mean(max_temp_list)
    rounded_avg_max = round(avg_max,1)
    formatted_avg_max = format_temperature(rounded_avg_max)

    #using placeholders to format the summary
    summary = """{} Day Overview
  The lowest temperature will be {}, and will occur on {}.
  The highest temperature will be {}, and will occur on {}.
  The average low this week is {}.
  The average high this week is {}.\n"""

    #\n means a new line. 
    return summary.format(total_days, overall_min, min_date, overall_max, max_date, formatted_avg_low, formatted_avg_max)
 
def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summary_str = ''

    for line in weather_data:  
        title = convert_date(line[0])
        daily_min = format_temperature(convert_f_to_c(line[1]))
        daily_max = format_temperature(convert_f_to_c(line[2]))

        summary_str = """---- {} ----
  Minimum Temperature: {}
  Maximum Temperature: {}\n
"""
        daily_summary_str += summary_str.format(title, daily_min, daily_max)

    return daily_summary_str