import pynetbox
import operator
import json

class get_netbox_info:

    def __init__(self, netbox_ip, netbox_token):
        self.netbox_ip = netbox_ip
        self.token = netbox_token
        self.nb = pynetbox.api(self.netbox_ip, self.token)

    def multi_objects_check(api_attr, filter_data):
        obj_notexist = []
        obj_exist = []
        nb = pynetbox.api("http://127.0.0.1:8000", "ac0045b34d40b36b57c8987512b05f5ba0a27817")
        for obj in filter_data:
            return_object = operator.attrgetter(api_attr)(nb).filter(**obj)
            if return_object is None:
                obj_notexist.append(return_object)
            else:
                print(dict(list(return_object)[0]))
                obj_exist.append(return_object)
        return obj_notexist, obj_exist


    def single_object_check(api_attr, filter_data):
        nb = pynetbox.api("http://127.0.0.1:8000", "ac0045b34d40b36b57c8987512b05f5ba0a27817")
        return_object = operator.attrgetter(api_attr)(nb).filter(**filter_data)

        if len(list(return_object)) > 1:
            #if use return_object here, it will return an empty list/dict, not sure why
            for obj in list(operator.attrgetter(api_attr)(nb).filter(**filter_data)):
                print(obj)
                print(dict(obj))
        elif len(return_object) == 1:
            # print(dict(list(operator.attrgetter(api_attr)(nb).filter(**filter_data))[0]))
            # This is for testing to get a json file for object creation
            prefix_dic = dict(list(operator.attrgetter(api_attr)(nb).filter(**filter_data))[0])
            # prefix_dic.pop('id')
            # del prefix_dic['url']
            # del prefix_dic['created']
            # del prefix_dic['last_updated']
            # del prefix_dic['children']
            # del prefix_dic['_depth']
            print(prefix_dic)

        else:
            print("object does not exist")

