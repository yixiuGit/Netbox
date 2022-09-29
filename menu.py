from pathlib import Path
import json
from netboxGet import multi_objects_check, single_object_check,check_existing_request
from netboxCreate import create_new_request
from netboxUpdate import update_request
from netboxDelete import delete_request


file = Path('.').glob('menu.json')
for i in file:
    with open(i) as temfile:
        data = json.load(temfile)


def menu(data, field):
    print('')
    input_result = None
    index = 1
    # for item in data:
    if type(data) is dict:   # the filter_process method will call this with dictionary as input,convert it to make it consistant
        data=list(data.keys())
    for item in data:
        print(f"{index}.{item}")
        index += 1

    input_result = int(input(f"\n\rSelect a {field}: "))
    return data[input_result-1]


def get_attr(data):
    rootList = list(data.keys())
    return rootList



pathDic = {}
filterDic = {}
filter_list = []

def filter_process(data, primay_attr, second_attr, continue_processing):

    global filter_list
    global filterDic
    while continue_processing == 'yes' or continue_processing == 'y':
        continue_processing = input("\n\rAdd data to filter? (y)es to continue, (n)o to finish or (r)eset to clear data and start again: ").lower().strip()

        if continue_processing == 'yes' or continue_processing == 'y':
            #menu.json nested for 3 levels, this is to get the bottom level of key if exist
            filter_attr = menu(data[primay_attr][second_attr], "filter_attr")
            if type(data[primay_attr][second_attr][filter_attr]) is dict:
                third_attr = menu(get_attr(data[primay_attr][second_attr][filter_attr]), "filter_attr")
            else:
                third_attr = ""
            filterData = input(f"\n\rPlease enter your data: ")

            if len(filter_list) == 0:
                if third_attr != '':
                    filterDic.update({filter_attr:{third_attr:filterData}})
                else:
                    filterDic.update({filter_attr:filterData})
                filter_list.append(filterDic)
            else:
                temp_filter = filter_list[len(filter_list)-1]
                if filter_attr not in list(temp_filter.keys()) and third_attr != "":
                    temp_filter.update({filter_attr:{third_attr:filterData}})
                elif filter_attr not in list(temp_filter.keys()) and third_attr == "":
                    temp_filter.update({filter_attr:filterData})
                elif type(temp_filter[filter_attr]) is dict:
                    if filter_attr in list(temp_filter.keys()) and third_attr != "" and third_attr not in list(temp_filter[filter_attr].keys()):
                        temp_filter[filter_attr][third_attr]=filterData
                    elif filter_attr in list(temp_filter.keys()) and third_attr in list(temp_filter[filter_attr].keys()):
                        new_dic = {filter_attr:{third_attr:filterData}}
                        filter_list.append(new_dic)
                elif type(temp_filter[filter_attr]) is not dict:
                    if filter_attr in list(temp_filter.keys()) and third_attr != "" and third_attr not in list(temp_filter.keys()):
                        temp_filter[filter_attr][third_attr]=filterData
                    elif filter_attr in list(temp_filter.keys()) and third_attr == "":
                        new_dic = {filter_attr:filterData}
                        filter_list.append(new_dic)
                elif filter_attr in list(temp_filter.keys()) and third_attr == "":
                    new_dic = {filter_attr: filterData}
                    filter_list.append(new_dic)

            return filter_process(data, primay_attr, second_attr, "yes")
        elif continue_processing == 'no' or continue_processing == 'n':
            return filter_list
        elif continue_processing == 'reset' or continue_processing == 'r':
            filter_list = []
            filterDic.clear()
            return filter_process(data, primay_attr, second_attr, "yes")
    else:
        return filter_list


request_option = int(input("\n\rPlease select which action you want to take"
                           "\n\r1. Create"
                           "\n\r2. Retrieve"
                           "\n\r3. Update"
                           "\n\r4. Delete"
                           "\n\rPlease enter your selection here: "))

primay_attr = menu(get_attr(data),"main_attr")
print(primay_attr)

second_attr = menu(get_attr(data[primay_attr]), "second_attr")
print(second_attr)


filter_outcome = filter_process(data, primay_attr, second_attr,"yes")
print(filter_outcome)

api_attr = f"{primay_attr}.{second_attr}"

if request_option==1:
    create_new_request(api_attr, filter_outcome)
elif request_option ==2:
    if len(filter_outcome) == 1:
        single_object_check(api_attr, filter_outcome[0])
    else:
        multi_objects_check(api_attr, filter_outcome)
elif request_option==3:
    update_request(api_attr, filter_outcome)
elif request_option==4:
    delete_request(api_attr, filter_outcome)




