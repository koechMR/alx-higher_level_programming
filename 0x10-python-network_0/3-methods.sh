#!/bin/bash
# scrit that takes in a url and display all http methods the server will accept
curl -sI "$1" | grep "ALLOW" | cut -d " " -f 2-
