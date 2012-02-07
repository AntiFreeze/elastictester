import os, sys
import simplejson as json
import pyes

class elasticsearch():

    def __init__(self, url, basedir=None):
        self._url = url
        if basedir:
            self._basedir = basedir
            self._datadir = self._basedir + '/data'
        else:
            self._basedir = None
            self._datadir = None
        # we only want to set _savedir upon a save
        self._savedir = None

    def __del__(self):
        self.restore_data()

    def start(self):
        pass

    def stop(self):
        pass

    def save_data(self):
        pass

    def restore_data(self):
        if self._savedir:
            pass

    def clear_data(self):
        pass

    def clear_index(self, index):
        pass

    def is_running(self):
        pass

class index():
    def __init__(self, **kwargs):
        pass

class query():
    def __init__(self, **kwargs):
        pass

class resultSet():

    def addResult(self):
        pass

    def resultExists(self, **kwargs):
        pass

class queryDSL():
    def __init__(self, **kwargs):
        pass

def insertPayload(es, index, payloadDir='./payload'):
    pass

def possibleIndices():
    pass

def possibleQueries(query):
    pass

def compareResultSet(needle, haystack, variance=0):
    pass
