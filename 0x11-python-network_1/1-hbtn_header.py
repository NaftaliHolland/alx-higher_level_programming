#!/usr/bin/python3
""" Sends a request to a url and displays the value of the X-Request-Id """
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(
                sys.argv[1]
            ) as response:
        headers = response.headers
        headers = dict(headers)

        print(headers["X-Request-Id"])
