import subprocess
subprocess.call("cat ngrok.log && ps -x && ls", shell=True)
