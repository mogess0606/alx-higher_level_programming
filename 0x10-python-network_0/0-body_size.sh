#!/bin/bash
curl -sI "$1" | grep 'Content-length:' | cut -c 17-

