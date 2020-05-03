import datetime
import time
from pandas import json_normalize
# pprint library is used to make the output look more pretty
from pprint import pprint
from pymongo import MongoClient
from random import randint
from urllib.parse import quote_plus


inputDate = "20200421"
inputDate = datetime.datetime.strptime(inputDate, '%Y%m%d').timestamp()
pprint(inputDate)

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
user = "dbuser"
password = "pa$$word"
host = "clusterbot-rvkfk.gcp.mongodb.net"
database = "rasabot"
options = "retryWrites=true&w=majority&connectTimeoutMS=300000"
uri = "mongodb+srv://%s:%s@%s/%s?%s" % (quote_plus(user), quote_plus(password), host, database, options)
pprint(uri)

client = MongoClient(uri)
# ("mongodb+srv://dbuser:pa$$word@clusterbot-rvkfk.gcp.mongodb.net/rasabot?retryWrites=true&w=majority"
#    "&connectTimeoutMS=300000")

# Get the database object
db = client.rasabot

# Get the collection object
conversations_coll = db.conversations

# Print total number of conversations
print(conversations_coll.count())

# Retrieve all the conversations in cursor
conversations_cursor = conversations_coll.find({'latest_event_time': {'$gt': inputDate}}).sort("_id", 1).limit(1)

# Retrieve single conversation
single_conversation = conversations_coll.find_one({})
# pprint(single_conversation)

for conversation in conversations_cursor:
    pprint(conversation.keys())
    df = json_normalize(conversation)
    pprint(df)
    pprint(df["latest_event_time"])
    pprint(df["_id"])
    events = json_normalize(conversation['events'])
    pprint(events)
    latest_message = json_normalize(conversation['latest_message'])
    pprint(latest_message)
    intent_ranking = json_normalize(conversation['latest_message'], 'intent_ranking')
    pprint(intent_ranking)
