library = {}
library2 = {}
def thesaurus(*name):
    list = []
    name_list=[*name]
    name_list.sort()
    # print(name_list)
    a = ord('А')
    for name1 in name_list:
        if a == ord(name1[:1]):
            # print(name1[:1])
            list.append(name1)
            # print(list)
        elif a != ord(name1[:1]):
            a = ord(name1[:1])
            # print(name1[:1])
            list.clear()
            list.append(name1)
            # print(list)
        library.setdefault(name1[:1], list[:])
        library2.update(library)
        library.clear()
    print(library2)
thesaurus("Иван", "Мария", "Петр", "Илья", "Яна")