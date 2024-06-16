#!/usr/bin/env python3
""" defines a function that changes all topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school document based on the name """
    for school in mongo_collection.find({"name": name}):
        school.update({"topics": topics})
