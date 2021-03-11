#ReJSON - a simple, yet powerful JSON wrapper for Python3.

import json

class manager:
    def __init__(self, jfile=None):
        self.jfile = jfile
        if self.jfile != None:
            self.loadJSON(self.jfile)
        else:
            self.rawJSON = {}
    
    def loadJSON(self, jfile):
        with open(jfile, "r+") as json_file:
            self.rawJSON = json.load(json_file)
    
    def makeKey(self, name, new_value=None):
        self.rawJSON.update({name : new_value})
    
    def makeFromDict(self, dictionary):
        self.rawJSON.update(dictionary)
    
    def changeKey(self, name, new_value):
        self.rawJSON[name] = new_value

    def removeKey(self, key):
        self.rawJSON.pop(key)

    def saveJSON(self, filename=None):
        with open(filename, "w+") as jfile:
            json.dump(self.rawJSON)

    def returnKey(self, key, k_index=None):
        if k_index != None:
            return self.rawJSON[key][k_index]
        else:
            return self.rawJSON[key]