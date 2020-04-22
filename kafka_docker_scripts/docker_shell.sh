#!/bin/sh
echo hello
docker exec -it `docker ps |grep kafka|gawk -F" " '{print $1}'` /bin/bash
