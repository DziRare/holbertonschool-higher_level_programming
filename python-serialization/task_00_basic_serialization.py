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
