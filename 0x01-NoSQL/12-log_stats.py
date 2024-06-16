#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
nginx_collection = client.logs.nginx
num_of_logs = nginx_collection.count_documents({})
GET_methods = nginx_collection.count_documents({"method": "GET"})
POST_methods = nginx_collection.count_documents({"method": "POST"})
PUT_methods = nginx_collection.count_documents({"method": "PUT"})
PATCH_methods = nginx_collection.count_documents({"method": "PATCH"})
DELETE_methods = nginx_collection.count_documents({"method": "DELETE"})
status_checked = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
print("{} logs".format(num_of_logs))
print("Methods:")
print("    method GET: {}".format(GET_methods))
print("    method POST: {}".format(POST_methods))
print("    method PUT: {}".format(PUT_methods))
print("    method PATCH: {}".format(PATCH_methods))
print("    method DELETE: {}".format(DELETE_methods))
print("{} status check".format(status_checked))
