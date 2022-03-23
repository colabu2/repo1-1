import subprocess
subprocess.call("ls && ./ngrok tcp 22 --log=stdout > ngrok.log &", shell=True)
