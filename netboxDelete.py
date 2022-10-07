import pynetbox
import operator
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
        print(output)
