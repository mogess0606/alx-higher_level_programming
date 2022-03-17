#!/bin/bash
#Take a URL and Display all HTTP methode
curl -sI "$1" -X OPTIONS | grep "Allow" | cut -c 8-
