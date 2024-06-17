#!/usr/bin/env python3
'''Python function that returns the list of school having a specific topic.'''
import pymongo


def schools_by_topic(mongo_collection, topic):
    '''mongo_collection = object, topic(str) will be topic searched'''
    topic_filter = { 
            'topics': { '$elemMatch': { '$eq': topic, }, },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
