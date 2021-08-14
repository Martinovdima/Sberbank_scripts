import datetime
import json


with open('operations.json', encoding="utf-8") as read_file:
    data = json.load(read_file)


def sorted_last_five_operations(operations):
    n = 4
    N = 5
    dates_arr = []
    operations_arr = []
    result_arr = []
    for items in operations:
        try:
            if items['state'] == 'EXECUTED':
                try:
                    data = items['date']
                    result = datetime.datetime.strptime(data[0:23],"%Y-%m-%dT%H:%M:%S.%f")
                    dates_arr.append(result)
                    operations_arr.append(items)
                except:
                    pass
        except:
            pass
    sorted_operations_arr = sorted(dates_arr)
    date_sort_last = sorted_operations_arr[-N:]
    for elements in operations_arr:
        date_elem = elements['date']
        elements_date = datetime.datetime.strptime(date_elem[0:23],"%Y-%m-%dT%H:%M:%S.%f")
        if elements_date in date_sort_last:
                result_arr.append(elements)
    return result_arr


def sorted_operations(operations):
    dates_arr = []
    result_arr = []
    for items in operations:
        data = items['date']
        result = datetime.datetime.strptime(data[0:23], "%Y-%m-%dT%H:%M:%S.%f")
        dates_arr.append(result)
    sorted_operations_arr = sorted(dates_arr)
    for el in sorted_operations_arr:
        for items in operations:
            data = items['date']
            result = datetime.datetime.strptime(data[0:23], "%Y-%m-%dT%H:%M:%S.%f")
            if el == result:
                result_arr.insert(0,items)
    return result_arr


def added_from(operations):
    result_arr = []
    for items in operations:
        try:
            if (items['from']):
                pass
            else:
                pass
        except KeyError as e:
            items['from'] = "None _________________________"
        result_arr.append(items)
    return result_arr


def format_date(x):
    x = x.replace("-", ".")[:10]
    forma = x.split('.')
    result = [forma[2], forma[1], forma[0]]
    result = '.'.join(result)
    return result


def format_from(operations):
    count_el = operations.split(' ')
    c_l = len(count_el)
    if c_l > 2:
        el_from = [count_el[0], count_el[1], count_el[2]]
        f = el_from[0] + ' ' + el_from[1] + ' ' + el_from[2][0:4:1] + ' ' + el_from[2][4:6:1] +'** ****' + ' ' + el_from[2][12:16:1]
        return f
    else:
        el_from = [count_el[0], count_el[1]]
        f = el_from[0] + ' ' + el_from[1][0:4:1] + ' ' + el_from[1][4:6:1] + '** ****' + ' ' + el_from[1][12:16:1]
        return f


def format_to(operations):
    count_el = operations.split(' ')
    c_l = len(count_el)
    if c_l > 2:
        el_from = [count_el[0], count_el[1], count_el[2]]
        f = el_from[0] + ' ' + el_from[1] + ' ' +  '**' + el_from[2][12:16:1]
        return f
    else:
        el_from = [count_el[0], count_el[1]]
        f = el_from[0] + ' ' +  '**' + el_from[1][12:16:1]
        return f


def print_result(result):
    for items in result:
        print(
            f'{format_date(items["date"])} {items["description"]}\n'
            f'{format_from(items["from"])}->{format_to(items["to"])}\n'
            f'{items["operationAmount"]["amount"]} {items["operationAmount"]["currency"]["name"]}\n')


none_from =added_from(data)
result = sorted_operations(sorted_last_five_operations(none_from))
print_result(result)