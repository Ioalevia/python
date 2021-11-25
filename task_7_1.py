import os
dir_list = ['settings', 'mainapp', 'adminapp', 'authapp']
dir_name = 'my_project'
for i in dir_list:
   dir_path = os.path.join(dir_name, i)
   if not os.path.exists(dir_path):
      os.makedirs(dir_path)