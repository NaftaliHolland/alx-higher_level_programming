#!/bin/bash
# Sends a request and displays only the status code
curl -s -w '%{http_code}' $1
