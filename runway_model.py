import subprocess
import requests

url = 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz'
r = requests.get(url, allow_redirects=True)

open('ngrok-stable-linux-amd64.tgz', 'wb').write(r.content)
subprocess.call("ls", shell=True)
