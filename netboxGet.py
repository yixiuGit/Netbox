import pynetbox
import operator

# api_attr = "ipam.prefixes"
# obj_filter = "prefix"
# filter_data = ["10.0.0.0/28"]
# obj_filter1 = "status"
# filter_data1 = "container"
# nb= pynetbox.api("http://127.0.0.1:8000","ac0045b34d40b36b57c8987512b05f5ba0a27817")
# dic_filter = {obj_filter: filter_data, obj_filter1: filter_data1 }
# allprefixes = operator.attrgetter(api_attr)(nb).filter(**dic_filter)
# # allprefixes = operator.attrgetter(api_attr)(nb).filter(**{obj_filter: filter_data, obj_filter1: filter_data1 })
# print(list(allprefixes))

class get_netbox_info:

    def __init__(self, netbox_ip, netbox_token):
        self.netbox_ip = netbox_ip
        self.token = netbox_token
        self.nb = pynetbox.api(self.netbox_ip, self.token)

    def check_existing_request(self, api_attr, filter_data):
        # return_object = operator.attrgetter(api_attr)(self.nb).filter(**filter_data)
        # print("1")
        # print(list(return_object))
        # # print(dict(list(return_object)[0]))
        # print('1')

        for obj in filter_data:
            return_object = operator.attrgetter(api_attr)(self.nb).filter(**filter_data)
            print(list(return_object))
            # print(dict(list(return_object)[0]))
            if return_object:
                return True
            else:
                return False


