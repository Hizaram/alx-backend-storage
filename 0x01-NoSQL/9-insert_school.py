#!/usr/bin/env python3
"""Script that inserts a new document into a collection"""


def insert_school(mongo_collection, **kwargs):
    """Function that inserts a new document based on the kwargs
    Args: mongo_collection (obj): Pymongo collection Object
          **kwargs: keyword argument for data insertion
    Returns: the new _id
    """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
