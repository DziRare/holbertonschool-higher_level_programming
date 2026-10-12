#!/usr/bin/env python3
import json
import csv

"""This module is for converting csv to json"""


def convert_csv_to_json(csv_filename):
    """This function is for converting csv to json"""

    with open(csv_filename) as csv_file:
        dict_list = list(csv.DictReader(csv_file))
        with open("data.json", "w") as file:
            json.dump(dict_list, file)


if __name__ == "__main__":
    csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")
