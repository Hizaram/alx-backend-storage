#!/usr/bin/env python3
"""Script that lists all documents in a MongoDB collection `school`
"""


def list_all(mongo_collection):
    """Function that lists all documents in a MongoDB collection `school`
    Args: mongo_collection: pymongo collection Object
    Returns: List of all documents in the collection 
             otherwise empty list
    """
    docs = mongo_collection.find()
    return [i for i in docs]
