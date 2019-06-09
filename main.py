import json
import sys
from pyquery import PyQuery as pq
from patrollers.taaze import TaazePatroller
from patrollers.iread import IReadPatroller
from patrollers.books import BooksPatroller
from patrollers.cite import CitePatroller
from patrollers.kingstone import KingStonePatroller

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "__jsonencode__"):
            return obj.__jsonencode__()
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

def json_encode(object):
    return json.dumps(object, cls=JSONEncoder)

patrollers = [TaazePatroller(), IReadPatroller(), CitePatroller(), BooksPatroller(), KingStonePatroller()]
data = {}
for patroller in patrollers:
    data[patroller.name] = patroller.generate()

if len(sys.argv) >= 2:
    demo = open(sys.argv[1], "w")
    demo.write(json_encode(data))
else:
    print(sys.argv)
    print(json_encode(data))