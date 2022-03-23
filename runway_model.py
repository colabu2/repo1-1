import subprocess
subprocess.call("cat ngrok.log && ps -x", shell=True)
