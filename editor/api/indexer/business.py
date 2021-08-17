import os
from hashlib import md5

paths = {}

ignore_list = ['.git','.vscode', '__pycache__']
def get_files_output(path=""):
    if(not path): path = os.path.join(os.getcwd() , "lab")
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

def open_file(hashed=False, save=False):
    result = {"hash":""}
    full_path = paths.get(hashed, False)
    if(not full_path): return result
    with open(full_path) as f:
        result["hash"] = f.read()
    return result
