import os
import shutil
"""Создаю структуру файлов и папок"""
directory = os.getcwd()
dir_list = ['settings', 'mainapp', 'authapp']
set_list = ['__init__.py', 'dev.py', 'prod.py']
main_list = ['__init__.py', 'models.py', 'views.py', 'base.html', 'index.html']
auth_list = ['__init__.py', 'models.py', 'views.py', 'base.html', 'index.html']
dir_name = 'my_project'
if not os.path.exists(dir_name):
   os.mkdir(dir_name)
for a in dir_list:
   dir_path = os.path.join(dir_name, a)
   if not os.path.exists(dir_path):
      os.makedirs(dir_path)
os.chdir(os.path.join(directory, dir_name, dir_list[0]))
for a in set_list:
    file_1 = open(a, 'w', encoding='utf-8')
    file_1.close()
os.chdir(os.path.join(directory, dir_name, dir_list[1]))
for a in main_list[:3]:
    file_1 = open(a, 'w', encoding='utf-8')
    file_1.close()
if not os.path.exists(os.path.join('templates', 'mainapp')):
    os.makedirs(os.path.join('templates', 'mainapp'))
os.chdir(os.path.join('templates', 'mainapp'))
for a in main_list[3:]:
    file_1 = open(a, 'w', encoding='utf-8')
    file_1.close()
os.chdir(os.path.join(directory, dir_name, dir_list[2]))
for a in auth_list[:3]:
    file_1 = open(a, 'w', encoding='utf-8')
    file_1.close()
if not os.path.exists(os.path.join('templates', 'authapp')):
    os.makedirs(os.path.join('templates', 'authapp'))
os.chdir(os.path.join('templates', 'authapp'))
for a in main_list[3:]:
    file_1 = open(a, 'w', encoding='utf-8')
    file_1.close()
os.chdir(directory)
"""Нахожу и копирую шаблоны в специальную папку"""
for root, dirs, files in os.walk(dir_name):
   for file in files:
       if '.html' in file:
           if not os.path.exists(os.path.join(dir_name, 'templates', root.split('\\')[-1])):
               os.makedirs(os.path.join(dir_name, 'templates', root.split('\\')[-1]))
           os.chdir(root)
           shutil.copy(file, os.path.join(directory, dir_name, 'templates', root.split('\\')[-1]))
           os.chdir(directory)