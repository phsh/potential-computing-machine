
FROM viliusl/ubuntu-h2-server

MAINTAINER perhed <phhedman@gmail.com>

RUN mkdir -p /opt/h2-loaddata

ADD data.csv /opt/h2-loaddata/data.csv
ADD test.sql /opt/h2-loaddata/test.sql

RUN java -cp /opt/h2/bin/h2*.jar org.h2.tools.RunScript -url jdbc:h2:/opt/h2-data/yoda -script /opt/h2-loaddata/test.sql

