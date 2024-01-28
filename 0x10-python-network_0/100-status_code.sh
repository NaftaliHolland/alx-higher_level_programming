#!/bin/bash
# Sends a request and displays only the status code
curl -s -I $1 | head -n 1 | awk '{print $2}'
