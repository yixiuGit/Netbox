import pynetbox
import operator
import json
from netboxGet import check_for_delete_request

nb = pynetbox.api("http://127.0.0.1:8000", "ac0045b34d40b36b57c8987512b05f5ba0a27817")

def delete_request(api_attr, filter_data):
    objExistList, objNotExistList=check_for_delete_request(api_attr, filter_data)
    print(objExistList)
    print(objNotExistList)
    if objNotExistList:
        print(f"The object(s) {objNotExistList} do NOT exist."
              f"We cannot proceed with this request")
    else:
        output = operator.attrgetter(api_attr)(nb).delete(objExistList)
    # output=operator.attrgetter(api_attr)(nb).update(filter_data)
    print(output)

api_attr = "ipam.prefixes"
filter_data=[{ "prefix": "10.0.4.0/28","vlan":{"vid":200}},{"prefix":"10.0.3.0/28", "vlan":{"vid":400}}]
# # ,"prefix": "10.0.4.0/28",
delete_request(api_attr,filter_data)
