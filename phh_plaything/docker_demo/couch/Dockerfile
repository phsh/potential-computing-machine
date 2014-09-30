#Building Couchbase and populate it
# sudo docker build -t perhed/couch-db .

FROM jamesdbloom/couchbase
#FROM viliusl/ubuntu-sshd-nginx:latest


MAINTAINER perhed <phhedman@gmail.com>

RUN mkdir -p /opt/couchbase-loaddata

ADD loaddata.json /opt/couchbase-loaddata/loaddata.json

ADD populate-couchbase.sh /populate-couchbase.sh

#RUN ["/populate-couchbase.sh"]

#CMD curl -X POST -u $CLUSTER_INIT_USER:$CLUSTER_INIT_PASSWORD -d name=jawa-sample -d authType=none -d proxyPort=11220 -d replicaNumber=0 -d ramQuotaMB=101 http://localhost:8091/pools/defau1t/buckets