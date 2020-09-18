from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb+srv://m001-student:m001-mongodb-basics@cluster0-jxeqq.mongodb.net/test?authSource=admin&replicaSet=Cluster0-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true')
filter={
    'tripduration': {
        '$gt': 2000000
    }
}

result = client['citibike']['trips'].find(
  filter=filter
)
count=0
for i in result:
    count+=1
print(count)
