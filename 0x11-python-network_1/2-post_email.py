#!/usr/bin/python3
""" Sends a POST request to a URL passed """

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Create dictionary with values
    data = dict()
    data["email"] = email

    # Encode and parse the dictionary
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")

    # Make request
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        body = response.read().decode("utf-8")
        print(body)
