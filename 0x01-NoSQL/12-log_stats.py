#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    num_of_logs = nginx_collection.count_documents({})
    GET_methods = nginx_collection.count_documents({"method" : "GET"})
    POST_methods = nginx_collection.count_documents({"method" : "POST"})
    PUT_methods = nginx_collection.count_documents({"method" : "PUT"})
    PATCH_methods = nginx_collection.count_documents({"method" : "PATCH"})
    DELETE_methods = nginx_collection.count_documents({"method" : "DELETE"})
    status_checked = nginx_collection.count_documents({"method" : "GET" , "path" : "/status"})
    print(f"{num_of_logs} logs")
    print("Methods:")
    print(f"    method GET: {GET_methods}")
    print(f"    method POST: {POST_methods}")
    print(f"    method PUT: {PUT_methods}")
    print(f"    method PATCH: {PATCH_methods}")
    print(f"    method DELETE: {DELETE_methods}")
    print(f"{status_checked} status check")
