from pathlib import Path
import json
from netboxGet import multi_objects_check, single_object_check
import pynetbox

file = Path('.').glob('menu.json')
for i in file:
    with open(i) as temfile:
        data = json.load(temfile)
        print(data)

def menu(data, field):
    print('')
    input_result = None
    index = 1
    for item in data:
        print(f"{index}.{item}")
        index += 1

    input_result = int(input(f"\n\rSelect a {field}: "))
    return data[input_result-1]


def main_attr(data):
    rootList = []
    for k in data.keys():
        rootList.append(k)
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
            filter_attr = menu(data[primay_attr][second_attr], "filter_attr")
            filterData = input(f"\n\rPlease enter your data: ")

            if len(filter_list) == 0:
                filterDic.update({filter_attr:filterData})
                filter_list.append(filterDic)
            else:
                temp_filter = filter_list[len(filter_list)-1]
                if filter_attr not in list(temp_filter.keys()):
                    temp_filter.update({filter_attr:filterData})
                else:
                    new_dic = {filter_attr:filterData}
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

primay_attr = menu(main_attr(data),"main_attr")
print(primay_attr)

second_attr = menu(main_attr(data[primay_attr]), "second_attr")
print(second_attr)


filter_outcome = filter_process(data, primay_attr, second_attr,"yes")
print(filter_outcome)




api_attr = f"{primay_attr}.{second_attr}"
if len(filter_outcome) == 1:
    single_object_check(api_attr, filter_outcome[0])
else:
    multi_objects_check(api_attr, filter_outcome)