#!/bin/bash
#Take a URL and Display all HTTP methode
curl -sI "$1" -X OPETIONS | grep "Allow" | cut -c 8-
