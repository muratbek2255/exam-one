# list_elements1 = ['Elements', 'starr', 'Finish']
#
#
# #
# #
# def list_elements(str):
#     list_elements1.insert(2, str)
#
# list_elements('hello')
# list_elements(5)
# list_elements('hello')
# print(list_elements1)


def dobav(*args):
    new_info = dict()

    for i, item in enumerate(args, start=1):
        new_info[item] = i

    return new_info


print(dobav('x', 5, 'John'))



def func(items):
    even_number =[]
    squared_numbers =[]

    for item in items:
        if item % 2 == 0:
            even_number.append(item)
        squared_numbers.append(pow(item, 2))

    return even_number, squared_numbers


a, b = func((1, 2, 3, 4, 5))
print(a)
print(b)




