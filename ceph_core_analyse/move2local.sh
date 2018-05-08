#!/bin/bash

DES_HOST="127.0.0.1"
DES_PATH="/usr/share/nginx/html"
echo "hello"



ssh ${DES_HOST} "rm -f ${DES_PATH}/index.html"
ssh ${DES_HOST} "rm -f ${DES_PATH}/code/*"

scp ./index.html ${DES_HOST}:${DES_PATH}/
scp ./src/* ${DES_HOST}:${DES_PATH}/code/
scp ./png/* ${DES_HOST}:${DES_PATH}/code/
