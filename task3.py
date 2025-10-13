import myfunctions
import test_data

with open('result.txt', 'w') as f:
    for i, lst in enumerate([test_data.list1, test_data.list2, test_data.list3], 1):
        smallest, second = myfunctions.find_two_smallest(lst)
        line = f"List {i}: 2 smaillest: {smallest}, {second}\n"
        f.write(line)
        print(line.strip())