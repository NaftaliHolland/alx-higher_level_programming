#!/usr/bin/python3
""" This module has a script that adds arguments to a python list"""
import sys


load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

json_list = []
json_list = load_from_json_file("add_item.json")

json_list += sys.argv[1:]

save_to_json_file(json_list, "add_item.json")
