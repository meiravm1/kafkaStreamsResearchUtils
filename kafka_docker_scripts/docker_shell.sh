#!/bin/sh
echo hello
docker exec -it `docker ps |grep kafka_1|gawk -F" " '{print $1}'` /bin/bash
