import subprocess, shlex, time


def get_terminal_output(cmd):
    named_tuple = time.localtime() # get struct_time
    current_time = time.strftime("%H:%M:%S", named_tuple)
    try:
        result = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE)
        output_cmd = result.stdout.decode('utf-8')
    except Exception:
        output_cmd = "Error running command"
    path = subprocess.run('pwd', stdout=subprocess.PIPE)
    output_pwd = path.stdout.decode('utf-8')
    result = '<div class="commandLine"><div class="user">&nbsp;&nbsp; app &nbsp;</div>'+\
             '<div class="cwd">&nbsp;' +str(output_pwd)+ '&nbsp;</div> : ' +str(current_time)+ \
             '<br>'+\
             '<div class="promptVLine"></div><div class="promptHLine">─<div class="promptArrow">▶</div></div> ' +str(cmd)+ '</div></div><br> ' +str(output_cmd)
    return {'output': ''+str(result)+'', 'user': 'app', 'cwd':''+str(output_pwd)+''} 
