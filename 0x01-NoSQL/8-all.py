#!/usr/bin/env python3
'''List all document in Python
'''


def list_all(mongo_collection):
    '''List all document in a collection.
    '''
    return mongo_collection.find()
