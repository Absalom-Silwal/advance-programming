""" Understanding an Advanced Python builtin function """
from itertools import zip_longest

def sensors_readings():
    sensor_ids = ['s1', 's2', 's3', 's4']
    temperature_readings = [27.1, 24.2, 20.5, 17.0]
    return sensor_ids,temperature_readings

def unequal_readings():
    sensor_ids = ['s1', 's2', 's3', 's4']
    temperatures = [27.1, 24.2, 20.5]
    return sensor_ids,temperatures

def create_readings_report(sensors_Ids,tempratures):
    """
    combines sensors_Ids and tempratures using zip and return a dictionary
    """
    combined_data = zip(sensors_Ids,tempratures)
    print("\n")
    print(combined_data)
    return dict(combined_data)


def show_tempratures_report(data,title):
    """ displays sensor id with it's corresponding temperature readings"""
    print(title)
    for id,temperature in data.items():
        print(f"{id} : {temperature}C")

def showcase_zip_behaviour():
    sensor_ids,temperatures = unequal_readings()
    report = create_readings_report(
    sensor_ids,temperatures
    )
    title = f"============================== Showing Zip Behaviour ======================="
    show_tempratures_report(report,title)

    """ s4 is removed from the combined data. This is because zip stops when shortest iterable reaches its end."""

def showcase_zip_longest_behaviour():
    sensor_id,temperatures = unequal_readings()
    report = dict(zip_longest(sensor_id,temperatures))
    show_tempratures_report(report,"============================== Showcasing Zip longest Behaviour ===================================")


def main_zip():
    try:
        sensor_ids,temperature_readings = sensors_readings()
        report  = create_readings_report(sensor_ids,temperature_readings)

        title =f'========== Temperature Reading Report ======================='
        show_tempratures_report(report,title)

        showcase_zip_behaviour()
    except Exception as e:
        print(f"An error has occured: {e}")


def main_zip_longest():
    try:
        sensor_ids,temperature_readings = sensors_readings()
        report = dict(zip_longest(sensor_ids,temperature_readings))
        show_tempratures_report(report,"=========================== Itertools Zip Longets =========================")
        showcase_zip_longest_behaviour()
    except Exception as e:
        print(f"An error has occured: {e}")

if __name__ == "__main__":
    main_zip()
    main_zip_longest()
