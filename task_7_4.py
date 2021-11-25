import os
dict = {}
dict_sorted = {}
directory = os.getcwd()
for root, dirs, files in os.walk(directory):
    for file in files:
        if 0 <= os.stat(os.path.join(root, file)).st_size <= 10:
            dict.setdefault(10, 0)
            dict[10] += 1
        for i in range(15):
            if os.path.isfile(os.path.join(root, file)):
                num = 10 ** i
                if num < os.stat(os.path.join(root, file)).st_size <= 10 * num:
                    dict.setdefault(10 * num, 0)
                    dict[10 * num] += 1
for i in sorted(dict.keys()):
    dict_sorted.setdefault(i, dict[i])
print(dict_sorted)