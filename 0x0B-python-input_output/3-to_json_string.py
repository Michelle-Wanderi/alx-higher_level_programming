#!/usr/bin/python3

"""Returns the JSON representation of an object(string)"""
import json

def to_json_string(my_obj):

	"""
	Args:
		 my_obj - the object to be converted to JSON
	
	Returns:
		The json representation of my_obj

	"""
return json.dumps(my_obj)
