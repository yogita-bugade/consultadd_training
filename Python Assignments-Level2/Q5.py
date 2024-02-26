'''You are developing a program that analyzes weather data. Write
a Python function that takes a list of temperature readings for a
specific location and determines the average temperature, highest
temperature, and lowest temperature.
Input: temperature_readings = [25, 28, 21, 24, 27]
Output:
Average Temperature: 25.0
Highest Temperature: 28
Lowest Temperature: 21'''
def analyze_weather_data(temperature_readings):
    if not temperature_readings:
        return None

    avg_temperature = sum(temperature_readings) / len(temperature_readings)
    max_temperature = max(temperature_readings)
    min_temperature = min(temperature_readings)

    return avg_temperature, max_temperature, min_temperature

temperature_readings = [25, 28, 21, 24, 27]
result = analyze_weather_data(temperature_readings)

if result:
    avg_temp, max_temp, min_temp = result
    print("Average Temperature:",avg_temp)
    print("Highest Temperature:",max_temp)
    print("Lowest Temperature:",min_temp)
else:
    print("No temperature readings provided.")
