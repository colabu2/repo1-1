import subprocess
subprocess.call("lscpu && whoami && sudo apt update", shell=True)
