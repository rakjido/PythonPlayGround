
from os import rename, listdir, path 

#dirs = '/Users/titan8/Public/media/Youtube/신사임당-음성/'
dirs = '/Users/titan8/Public/media/Youtube/엑셀러레이터'
files = listdir(dirs)

for name in files:
    new_name = name.replace("?","").replace("!","").replace("|","-").replace(","," ").replace("#","")
    # new_name=name[:7]
    print(new_name)
    rename(path.join(dirs,name), path.join(dirs,new_name))

