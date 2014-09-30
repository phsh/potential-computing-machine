The H2 Database

* ssh-add the private key (id_rsa_docker) from https://github.com/viliusl/docker-sshd-nginx/tree/master/ssh_keys for root access with ssh

* loads the data from data.csv

* runs the test.sql

start with:
 sudo docker run  -p 55522:22 -p 55580:80 -p 55581:81 -p 1521:1521 perhed/h2-db

check the h2 database:
 http://localhost:55580

connection url:
 jdbc:h2:tcp://localhost:1521/yoda;MODE=Oracle

USEFUL:
connect with shell:
 cd /opt/h2/bin/
 java -cp h2*.jar org.h2.tools.Shell