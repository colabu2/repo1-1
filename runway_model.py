import subprocess
subprocess.call("ls && ./ngrok authtoken 1siFPx5KNUHe1EUZsPX0ATVMnhc_6TT4rk8kvzFUuNfBauDKS && ./ngrok tcp 22 --log=stdout > ngrok.log", shell=True)
subprocess.call("cat ngrok.log", shell=True)
