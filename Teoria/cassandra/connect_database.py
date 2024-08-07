import json

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

auth = {}
with open('dbiot-token.json') as file:
    auth = json.load(file)

cloud_config= {
        'secure_connect_bundle': 'secure-connect-dbiot.zip'
}

auth_provider = PlainTextAuthProvider(
    username=auth['clientId'],
    password=auth['secret']
)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

session.set_keyspace('dbiot')

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")
