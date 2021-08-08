import os
from hashlib import md5

paths = {}

ignore_list = ['.git','.vscode']
def get_files_output(path="."):
    nodes = {}
    path = os.path.realpath(path)
    for node in os.listdir(path):
         if(node in ignore_list): continue
         full_path = os.path.join(path,node)
         hashed = md5(str(node).encode("utf-8")).hexdigest()
         paths[hashed] = full_path
         nodes[hashed] = {'name':node, 'type':'file','child':[]}
         if(os.path.isdir(full_path)):
             nodes[hashed]['type'] = 'dir'
             nodes[hashed]['child'].append(get_files_output(full_path))
    return {'files': nodes}