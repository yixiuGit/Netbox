import pynetbox
import operator
import json

with open('output.json') as json_file:
    data = json.load(json_file)

nb = pynetbox.api("http://127.0.0.1:8000", "ac0045b34d40b36b57c8987512b05f5ba0a27817")

api_attr = 'ipam.prefixes'
# print(len(v))
operator.attrgetter(api_attr)(nb).create(data)

# api_attr = "ipam.prefixes"
#                     nb = pynetbox.api("http://127.0.0.1:8000", "ac0045b34d40b36b57c8987512b05f5ba0a27817")
# # # input_data= {"prefix": "10.0.1.0/28"}
#                     operator.attrgetter(api_attr)(nb).create(input_data)