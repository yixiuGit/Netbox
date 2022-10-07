import pynetbox
import operator


nb = pynetbox.api("http://127.0.0.1:8000", "ac0045b34d40b36b57c8987512b05f5ba0a27817")
def multi_objects_check(api_attr, filter_data):
    obj_notexist = []
    obj_exist = []
    for obj in filter_data:
        return_object = operator.attrgetter(api_attr)(nb).filter(**obj)
        if return_object is None:
            obj_notexist.append(return_object)
        else:
            obj_exist.append(return_object)
    for new_obj in obj_exist:
        print(dict(list(new_obj)[0]))
    return obj_notexist, obj_exist


def single_object_check(api_attr, filter_data):

    return_object = operator.attrgetter(api_attr)(nb).filter(**filter_data)

    #When initially write the script, it returned multiple items in the return_object
    #if the filter_data contains multiple subset, for example 10.0.0.0/10 contains 10.0.4.0/28
    #but cannot replicate it anymore, thus this if command does not look useful
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

def check_existing_request(api_attr, filter_data):
    objExistList = []
    objNotExistList = []
    for obj in filter_data:
        return_object = operator.attrgetter(api_attr)(nb).filter(**obj)
        if return_object:
            objExistList.append(obj)
        else:
            objNotExistList.append(obj)
    return objExistList, objNotExistList


#For updating object, need to check if objects were already exist.
#If object already exist, collect "id" information and add to the update filter.
def check_for_update_request(api_attr, filter_data):
    objExistList = []
    objNotExistList = []
    for obj in filter_data:
        return_object = operator.attrgetter(api_attr)(nb).filter(**obj)
        if return_object:
            obj['id']=dict(list(return_object)[0])['id']
            objExistList.append(obj)
        else:
            objNotExistList.append(obj)
    return objExistList, objNotExistList

def check_for_delete_request(api_attr, filter_data):
    objExistList = []
    objNotExistList = []
    for obj in filter_data:
        return_object = operator.attrgetter(api_attr)(nb).filter(**obj)
        if return_object:
            objExistList.append(dict(list(return_object)[0])['id'])
        else:
            objNotExistList.append(obj)
    return objExistList, objNotExistList