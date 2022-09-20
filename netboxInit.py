import pynetbox
import operator
import netboxGet
import os




class new_netbox_instance:

    def __init__(self, netbox_ip, netbox_token):
        self.netbox_ip = netbox_ip
        self.token = netbox_token
        self.nb = pynetbox.api(self.netbox_ip, self.token)


    def create_new_request(self, api_attr, filter_data, input_data):
        vlanCheck = netboxGet.get_netbox_info.check_existing_request(self, api_attr,  filter_data)
        if vlanCheck:
            print("vlan exist")
            pass
        else :
            operator.attrgetter(api_attr)(self.nb).create(input_data)
            print(f'vlan {input_data} created')
