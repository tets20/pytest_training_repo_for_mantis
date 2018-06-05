
from sys import maxsize


class Project:

    def __init__(self, name=None, discription = None):
        self.name = name
        self.discription = discription

    def __repr__(self):
        return "%s:%s" % (self.name, self.discription)


    def __eq__(self, other):
        return (self.name is None or other.name is None or self.name == other.name), self.discription == other.discription


    def id_or_max(self):
        if self.name:
            return int(self.name)
        else:
            return maxsize