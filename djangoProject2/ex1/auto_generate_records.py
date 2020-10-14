#!/usr/bin/python
import sys
import random
import string
from pymongo import MongoClient

if len(sys.argv)!= 2:
	print('Please Enter one Argument')
	exit()

countR = int(sys.argv[1]) 

#cluster =MongoClient("mongodb+srv://myuser:admin@cluster0.cadj2.mongodb.net/api?retryWrites=true&w=majority")
#db = cluster['api']
#collection = db["router"]
connection = MongoClient('localhost',27017)
database = connection['api']
collection = database['ex3_routerapi']


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def rand_mac():
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        )



for i in range(countR):
    Sapid    = get_random_string(18)
    hostname = get_random_string(14)
    Loopback = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    MacAddress  = rand_mac()
    routerData = {'sapid':Sapid, 'hostname':hostname, 'loopback':Loopback,'macip':MacAddress,'is_delete':0}
    print(routerData)
    collection.insert_one(routerData)