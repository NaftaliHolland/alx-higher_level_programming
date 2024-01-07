#!/usr/bin/bash
# Sends a request to a URL and displays the size of the body of the response
curl -s -w "%{size_download}\n" $1
