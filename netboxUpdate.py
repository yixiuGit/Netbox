import pynetbox
import operator
from netboxGet import check_for_update_request

nb = pynetbox.api("http://127.0.0.1:8000", "ac0045b34d40b36b57c8987512b05f5ba0a27817")

def update_request(api_attr, filter_data):
    objExistList, objNotExistList=check_for_update_request(api_attr, filter_data)
    if objNotExistList:
        print(f"The object(s) {objNotExistList} do NOT exist."
              f"We cannot proceed with this request")
    else:
        output = operator.attrgetter(api_attr)(nb).update(objExistList)
    # output=operator.attrgetter(api_attr)(nb).update(filter_data)
    print(output)


