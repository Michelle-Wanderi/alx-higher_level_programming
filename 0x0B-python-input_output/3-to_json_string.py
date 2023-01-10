#!/usr/bin/python3

"""
	Returns the JSON representation of an object(string)
"""

def to_json_string(my_obj):
	"""
		Args: my_obj - the string to be converted to JSON
	"""
json_string = json.dumps(my_obj)
print(json_string)
print(type(json_string))
