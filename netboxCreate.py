import pynetbox
import operator
import json
from netboxGet import single_object_check, multi_objects_check, check_existing_request

nb = pynetbox.api("http://127.0.0.1:8000", "ac0045b34d40b36b57c8987512b05f5ba0a27817")
def create_from_file():
    with open('output.json') as json_file:
        data = json.load(json_file)

def create_new_request(api_attr, filter_data):
    objExistList, objNotExistList = check_existing_request(api_attr, filter_data)
    if objExistList:
        processing_option = input("\n\rThere are some objects already exist"
                                  "\n\r (p)roceed to create objects anyway"
                                  "\n\r (o)nly to create objects not exist"
                                  "\n\r (a)bort to cancel the action: ").lower().strip()

        if processing_option == 'p' or processing_option == 'proceed':
            operator.attrgetter(api_attr)(nb).create(filter_data)
        elif processing_option == 'o' or processing_option == 'only':
            operator.attrgetter(api_attr)(nb).create(objNotExistList)
        elif processing_option == 'a' or processing_option == 'abort':
            return

    else:
        operator.attrgetter(api_attr)(nb).create(filter_data)
        print(f'objects {objNotExistList} created')
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