#!/usr/bin/python3

"""
	Returns an object represented by a json string
"""
	
def from_json_string(my_str):

"""
	Args : my_str - the json string to be converted to an object
	
	Returns : an object parsed for the json string
"""
return json.dumps(my_str)
