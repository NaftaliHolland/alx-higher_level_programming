#!/bin/bash
# Sends a JSON POST request
curl -X POST -H "Content-Type: application/json" -d "@$2" "$1"
