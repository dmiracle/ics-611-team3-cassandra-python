from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os

cloud_config = {"secure_connect_bundle": os.getenv("SECURE_CONNECT_PATH")}
auth_provider = PlainTextAuthProvider(
    os.getenv("DATASTAX_CLIENT_ID"), os.getenv("DATASTAX_CLIENT_SECRET")
)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
try:
    session = cluster.connect("team3")
except Exception as e:
    print(e)

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")
