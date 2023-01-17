#!/usr/bin/env python3
"""Script that changes all topics of a school document based on name"""


def update_topics(mongo_collection, name, topics):
    """Function that changes topics of a school document based on name
    Args: mongo_collection (obj): Pymongo collection object
          name (str): name of the school document
          topics (list of strs): list of topics
    """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )
