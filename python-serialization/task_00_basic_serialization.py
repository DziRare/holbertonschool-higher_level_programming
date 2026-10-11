#!/usr/bin/env python3
import pickle

"""This module is for serialization and deserialization"""


def serialize_and_save_to_file(data, filename):
    """Code to serialize and save data to the specified file"""
    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """Code to load and deserialize data from the specified file"""
    with open(filename, "rb") as file:
        return pickle.load(file)


if __name__ == "__main__":
    # Sample data to be serialized
    data_to_serialize = {"name": "John Doe", "age": 30, "city": "New York"}

    # Serialize the data to JSON and save it to a file
    serialize_and_save_to_file(data_to_serialize, "data.json")

    # Output: The data has been serialized and saved to 'data.json'
    print("Data serialized and saved to 'data.json'.")

    # Load and deserialize data from 'data.json'
    deserialized_data = load_and_deserialize("data.json")

    # Output: The deserialized data
    print("Deserialized Data:")
    print(deserialized_data)
