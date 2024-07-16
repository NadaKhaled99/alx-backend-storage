#!/usr/bin/env python3
'''Change topic of a collection's document based on the name.
'''


def update_topics(mongo_collection, name, topics):
    '''Change topic of a collection's document based on the name.
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
