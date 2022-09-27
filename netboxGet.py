import pynetbox
import operator
import json


# allprefixes = operator.attrgetter(api_attr)(nb).filter(**dic_filter)
# # allprefixes = operator.attrgetter(api_attr)(nb).filter(**{obj_filter: filter_data, obj_filter1: filter_data1 })
# print(list(allprefixes))

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
            # with open ('output.json', 'w') as outfile:
            #     json.dump(prefix_dic, outfile)
        else:
            print("object does not exist")
        # return  list(return_object)



#
# if __name__ == '__main__':
#     api_attr = "ipam.prefixes"
#     obj_filter = "prefix"
#     filter_data = ["10.0.0.0/28"]
#     obj_filter1 = "status"
#     filter_data1 = "container"
#     nb = pynetbox.api("http://127.0.0.1:8000", "ac0045b34d40b36b57c8987512b05f5ba0a27817")
#     # dic_filter = {obj_filter: filter_data, obj_filter1: filter_data1}
#     dic_filter = {obj_filter: filter_data}
#     dic_filter = [{obj_filter: filter_data, obj_filter1: filter_data1}, {obj_filter: ["10.0.0.0/28"], obj_filter1: 'active'}]



    ### for single enquiry
    ### This is for try to search for 1 object, all the search query is in 1 dictionary, the more searching criteria you have
    ### the more percise return you will have .
    ### It may return more than 1 object if your search query is too broad.
    ### For example, you may have multiple ip prefixes they have same ip and mask, but different status
    # response = get_netbox_info.single_object_check(api_attr,dic_filter)
            # print(list(response))
            # if len(list(response)) > 1:
            #     print('2')
            #     for obj in list(response):
            #         print(obj)
            #         print(dict(obj)['status'])
            # elif len(response) == 1:
            #     print('1')
            #     print(dict(list(response)[0])['status'])
            # else:
            #     print("object does not exist")



    #multiple
    # obj_notexist, obj_exist = get_netbox_info.multi_objects_check(api_attr, dic_filter)
    # print(obj_notexist)
    # print(obj_exist)
    # for obj in list(obj_exist):
    #     print(dict(list(obj)[0])['status'])