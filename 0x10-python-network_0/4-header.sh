#!/bin/bash
# Sends a GET request and sets a header variable
curl -s -X GET -H "X-School-User-Id: 98" $1
