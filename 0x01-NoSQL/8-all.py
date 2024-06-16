#!/usr/bin/env python3
""" defines a function that lists all documents in shool collection """


def list_all(mongo_collection):
    """ lists all documents in a collection """
    return [doc for doc in mongo_collection.find()]
