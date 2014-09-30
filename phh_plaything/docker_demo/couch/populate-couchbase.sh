#!/bin/bash

#Creates the jawa-sample bucket.
curl -X POST -u Administrator:password -d name=jawa-sample -d authType=none -d proxyPort=11220 -d replicaNumber=0 -d ramQuotaMB=101 http://localhost:8091/pools/default/buckets
# can't use 'wait $(<"$pid_file")' as process not child of shell

COUCHBASE=Couchbase-Java-Client/Couchbase-Java-Client-1.4.4
javac -cp $COUCHBASE/couchbase-client-1.4.4.jar:$COUCHBASE/spymemcached-2.11.4.jar $COUCHBASE/LoadData.java

java -cp $COUCHBASE:$COUCHBASE/couchbase-client-1.4.4.jar:$COUCHBASE/spymemcached-2.11.4.jar:$COUCHBASE/jettison-1.1.jar:$COUCHBASE/netty-3.5.5.Final.jar:$COUCHBASE/commons-codec-1.5.jar:$COUCHBASE/httpcore-4.3.jar:$COUCHBASE/httpcore-nio-4.3.jar LoadData

#curl http://localhost:8092/jawa-sample