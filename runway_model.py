import subprocess
import requests

url = 'wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip'
r = requests.get(url, allow_redirects=True)

open('ngrok-stable-linux-amd64.zip', 'wb').write(r.content)
subprocess.call("ls", shell=True)
