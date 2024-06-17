#!/usr/bin/env python3
""" defines a function that returns all students sorted by average score
"""


def top_students(mongo_collection):
  """ returns all students sorted by average score """
  pipeline = [
        { "$unwind": "$topics" },
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        { "$sort" : {"averageScore": -1}}
    ]
  return [student for student in mongo_collection.aggregate(pipeline)]