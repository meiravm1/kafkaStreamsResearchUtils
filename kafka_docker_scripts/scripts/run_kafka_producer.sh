topic=$1
properties=$2
container_id=`docker ps|grep kafka_1|gawk -F" " '{print $1}'`
echo $container_id
docker exec -it $container_id /opt/bitnami/kafka/bin/kafka-console-producer.sh --broker-list=kafka:29092 --topic $topic $2
