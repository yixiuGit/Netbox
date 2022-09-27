from pathlib import Path
import json
from netboxGet import get_netbox_info
import pynetbox

file = Path('.').glob('menu.json')
for i in file:
    # print(i)
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

secondKeyList = []
secondList = []
pathDic = {}
filterDic = {}
filter_list = []
# temp_filter = {}
def filter_process(data, primay_attr, second_attr, continue_processing):

    # continue_processing = 'yes'
    global filter_list
    # global temp_filter
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
            # print(filterDic.keys())
    #         if filter_attr in list(filterDic.keys()) and filter_selector==1:
    #             filter_processing = input('\n\rThe same filter attribute already exist, it against the rule of creating single filter object. You can select option 2 which is for multiple filter objects.'
    #                                       '\n\rEnter (n)o to complete build this filter object, (r)eset to go back to previous menu: ').lower().strip()
    #             if filter_processing not in ('no', 'n', 'reset', 'r'):
    #                 print("\n\rPlease enter either 'r' or 'n'")
    #             elif filter_processing == 'no' or filter_processing == 'n':
    #                 return filterDic
    #             elif filter_processing == 'reset' or filter_processing == 'r':
    #                 return filter_process(data, primay_attr, second_attr, filter_selector, "yes")
    #         elif filter_attr not in list(filterDic.keys()) and filter_selector==1:
    #             filterDic[filter_attr] = filterData
    #             return filter_process(data, primay_attr, second_attr, filter_selector, "yes")
    #         elif filter_attr in list(filterDic.keys()) and filter_selector==2:
    #             filter_list.append(filterDic)
    #             temp_filter.update({filter_attr: filterData})
    #             # temp_filter[filter_attr] = filterData
    #             filterDic = temp_filter.copy()
    #             filter_list.append(temp_filter)
    #
    #             print(filter_list)
    #             return filter_process(data, primay_attr, second_attr, filter_selector, "yes")
    #         elif filter_attr not in list(filterDic.keys()) and filter_selector==2:
    #             filterDic.update({filter_attr: filterData})
    #             print(filterDic)
    #             # filter_list.append(filterDic)
    #             print(filter_list)
    #             return filter_process(data, primay_attr, second_attr, filter_selector, "yes")
    #     elif continue_processing == 'reset' or continue_processing == 'r':
    #         filterDic.clear()
    #         return filter_process(data, primay_attr, second_attr,filter_selector, 'yes')
    # if filter_selector == 1:
    #     return filterDic
    # elif filter_selector == 2:
    #     return filter_list

# filter_selector = int(
#     input("\n\rPlease select below options to create filter object."
#           "\n\rEnter 1 to create single filter object, enter 2 to create multiple filter objects: ").strip())

primay_attr = menu(main_attr(data),"main_attr")
print(primay_attr)

second_attr = menu(main_attr(data[primay_attr]), "second_attr")
print(second_attr)


filter_outcome = filter_process(data, primay_attr, second_attr,"yes")
print(filter_outcome)



# nb = pynetbox.api("http://127.0.0.1:8000", "ac0045b34d40b36b57c8987512b05f5ba0a27817")
api_attr = f"{primay_attr}.{second_attr}"
if len(filter_outcome) == 1:
    get_netbox_info.single_object_check(api_attr, filter_outcome[0])
else:
    get_netbox_info.multi_objects_check(api_attr, filter_outcome)