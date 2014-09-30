
How to run
docker run  --name couch_one -p 11210:11210 -p 8091:8091 -p 8092:8092 -e CLUSTER_INIT_USER=Administrator -e CLUSTER_INIT_PASSWORD=password -d perhed/couchbase

then 
./populate-couchbase.sh
# Generates a lot of errors, but reruning seems to work better.
