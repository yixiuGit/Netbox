import pynetbox
import operator
import json

class newObjects:
    def create_from_file(self):
        with open('output.json') as json_file:
            data = json.load(json_file)

    def create_new_request(self, api_attr, filter_data, input_data):
        vlanCheck = netboxGet.get_netbox_info.check_existing_request(self, api_attr, filter_data)
        if vlanCheck:
            print("vlan exist")
            pass
        else:
            operator.attrgetter(api_attr)(self.nb).create(input_data)
            print(f'vlan {input_data} created')
# with open('output.json') as json_file:
#     data = json.load(json_file)
#
# nb = pynetbox.api("http://127.0.0.1:8000", "ac0045b34d40b36b57c8987512b05f5ba0a27817")
#
# api_attr = 'ipam.prefixes'
# # print(len(v))
# operator.attrgetter(api_attr)(nb).create(data)

# api_attr = "ipam.prefixes"
#                     nb = pynetbox.api("http://127.0.0.1:8000", "ac0045b34d40b36b57c8987512b05f5ba0a27817")
# # # input_data= {"prefix": "10.0.1.0/28"}
#                     operator.attrgetter(api_attr)(nb).create(input_data)