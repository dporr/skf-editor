import subprocess, shlex, time, os
context = {
    "user":os.getenv("USER"),
    "cwd": os.getenv("PWD")
}

def chdir(cmd):
    new_dir = HOME_DIR =  os.getenv("HOME")
    if len(cmd) > 1:
        new_dir = cmd[1].replace("~", HOME_DIR)
    os.chdir(new_dir)
    context['cwd'] = os.getcwd()

def get_terminal_output(cmd):
    named_tuple = time.localtime() # get struct_time
    current_time = time.strftime("%H:%M:%S", named_tuple)
    output_cmd = ""
    try:
        cmd = shlex.split(cmd)
        if cmd[0] == 'cd':
            chdir(cmd)
        else:
            result = subprocess.run(" ".join(cmd), stdout=subprocess.PIPE, shell=True)
            output_cmd = result.stdout.decode('utf-8')
    except Exception:
        output_cmd = "Error running command"
    result = '<div class="commandLine"><div class="user">&nbsp;&nbsp;' + str(context['user'])+' &nbsp;</div>'+\
             '<div class="cwd">&nbsp;' +str(context['cwd']) + '&nbsp;</div> &nbsp;&nbsp;&nbsp; ' +\
             '<br>'+\
             '<div class="promptVLine"></div><div class="promptHLine">─<div class="promptArrow">▶</div></div> ' +str(" ".join(cmd))+ '</div></div><br> ' +str(output_cmd)
    return {'output': ''+str(result)+'', 'user': str(context['user']), 'cwd':str(context['cwd'])} 
