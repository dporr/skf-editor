import subprocess, shlex, time, os


def get_files_output():
    find = subprocess.run("find lab -print -ls", stdout=subprocess.PIPE, shell=True)
    files = find.stdout.decode('utf-8')
    #return {'files': ''+str(result)+'', 'user': str(context['user']), 'cwd':str(context['cwd'])} 
