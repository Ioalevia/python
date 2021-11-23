import itertools
with open('users.csv', 'r', encoding='utf-8') as user:
    user_list = user.read()
    # print(user_list)
    user.close()
with open('hobby.csv', 'r', encoding='utf-8') as hobby:
    hobby_list = hobby.read()
    # print(hobby_list)
    hobby.close()
user_name = user_list.split('\n')
user_hobby = hobby_list.split('\n')
if len(user_name) >= len(user_hobby):
    result = dict(itertools.zip_longest(user_name, user_hobby))
    with open('result_6_3.csv', 'w', encoding='utf-8') as res:
        res.write(str(result))
    print(result)
else:
    exit(1)
