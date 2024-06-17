#!/usr/bin/env python3
'''Python func that changes all topics of a school doc based on the name.'''
import pymongo


def update_topics(mongo_collection, name, topics):
    '''name(string) will be updated, topic will be the list of topic.'''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
