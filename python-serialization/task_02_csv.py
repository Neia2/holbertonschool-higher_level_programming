import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV file to JSON format and write to 'data.json'.

    :param csv_filename: The CSV file to convert.
    :return: True if successful, False otherwise.
    """
    try:
        data = []
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False
