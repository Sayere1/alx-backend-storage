#!/usr/bin/env python3
'''Python func that inserts a new doc in a collection based on kwargs'''
import pymongo


def insert_school(mongo_collection, **kwargs):
    '''mongo_collection will be the pymongo collection object Ret d new _id'''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
