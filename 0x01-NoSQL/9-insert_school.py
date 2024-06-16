#!/usr/bin/env python3
""" defines a function that inserts a new document in a collection
based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs """
    the_document = mongo_collection.insert_one(kwargs)
    return the_document.inserted_id
