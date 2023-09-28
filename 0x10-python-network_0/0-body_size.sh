#!/bin/bash
# script that take in URL, sends a request to that URL and display
curl -s "$1" | wc -c
