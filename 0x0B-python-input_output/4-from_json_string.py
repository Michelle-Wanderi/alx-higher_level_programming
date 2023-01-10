 #!/usr/bin/python3


"""
           Returns an object represented by a json string
   """
import json
   
         
def from_json_string(my_str):
  
  """
          Args : my_str - the json string to be converted to an object
          
          Returns : an object parsed for the json string
 """
  return json.loads(my_str)
