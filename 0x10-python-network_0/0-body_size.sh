#!/bin/bash 
# Displays the size of the body of the response of a URL request.
curl -s "$1" | wc -c
