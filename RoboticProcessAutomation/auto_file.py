from os import listdir, makedirs, unlink
from os.path import isdir, splitext, exists
from shutil import copyfile, copytree, rmtree
from datetime import date

original_dir = '/Users/titan7/git/PythonPlayGround/RoboticProcessAutomation'

output_dir ='/Users/titan7/git/PythonPlayGround/RoboticProcessAutomation'

# file list in the folder
file_list = listdir(original_dir)

# print(file_list)

# for f_name in file_list:
#     print(f_name)


today = date.today()
# print(type(today.strftime("%Y-%m-%d")))

target_dir = output_dir + "/" + today.strftime("%Y-%m-%d")
# print(target_dir)

# make directory
if not isdir(target_dir):
    makedirs(target_dir)

# copy files
for f_name in file_list:
    # print(splitext(f_name)[1])
    if splitext(f_name)[1] == ".py":
        # print('true')
        copyfile(original_dir + "/" + f_name, target_dir + "/" +  f_name)
        print(original_dir + "/" + f_name + "==>" + target_dir + "/" +  f_name)

# copy folders
if not exists('/Users/titan7/git/PythonPlayGround/RoboticProcessAutomation/temp'):
    copytree(target_dir, '/Users/titan7/git/PythonPlayGround/RoboticProcessAutomation/temp' )

# delete files
# if exists('/Users/titan7/git/PythonPlayGround/RoboticProcessAutomation/temp'):
#     unlink('/Users/titan7/git/PythonPlayGround/RoboticProcessAutomation/temp/auto_file.py')

# delete folders
if exists('/Users/titan7/git/PythonPlayGround/RoboticProcessAutomation/temp'):
    rmtree('/Users/titan7/git/PythonPlayGround/RoboticProcessAutomation/temp' )
