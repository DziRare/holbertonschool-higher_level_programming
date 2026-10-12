#!/usr/bin/env python3
"""This module is for XML serializing"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize to XML"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value

    with open(filename, "wb") as file:
        file.write(ET.tostring(root))


def deserialize_from_xml(filename):
    """Deserialize from XML"""
    dictionary = {}
    with open(filename) as file:
        xml_tree = ET.parse(file)
        root = xml_tree.getroot()
        for element in root:
            dictionary[element.tag] = element.text
    return dictionary


def main():
    """Main function"""
    sample_dict = {"name": "John", "age": "28", "city": "New York"}

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)


if __name__ == "__main__":
    main()
