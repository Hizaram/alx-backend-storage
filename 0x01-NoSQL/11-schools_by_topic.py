#!/usr/bin/env python3
"""Script that returns a list of schools having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Function that returns a list of schools having a specific topic
    Args: mongo_collection (obj): Pymongo collection object
          topic (str): specific topic to search for
    Returns: List of schools having specific topic
    """
    return mongo_collection.find({"topics": topic})
