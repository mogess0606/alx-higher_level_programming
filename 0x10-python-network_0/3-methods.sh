#!/bin/bash
#Take a URL and Display all HTTP methode
curl -sL "$1" -X OPETIONS | grep "Allow" | cut -c 8-
